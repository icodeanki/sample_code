from odoo import api, fields, models, _


class AmazonOrder(models.Model):
    _name = "amazon.order"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Amazon order"
    _rec_name = 'product_id'

    customer_id = fields.Many2one('amazon.customer', string='Customer')
    order_time = fields.Datetime(string="Order Time")
    order_date = fields.Date(string="Order Date")
    age = fields.Integer(string='Age')
    amazon_ids = fields.One2many('amazon.order.line', 'amazon_id', string="Amazon Records")
    product_id = fields.Many2one('amazon.product', string="Product Name")

    @api.model
    def create(self, vals):
        res = super(AmazonOrder, self).create(vals)
        print('self', self)
        print('vals', vals)
        print('res', res)
        return res

    @api.onchange("customer_id")
    def onchange_customer_id(self):
        self.age = self.customer_id.age


class AmazonOrderLine(models.Model):
    _name = 'amazon.order.line'

    amazon_id = fields.Many2one('amazon.order')
    name = fields.Char(string='Name')
    age = fields.Char(string='Age')

    def set_age(self):
        return {
            'type': 'ir.actions.act_window',
            'name': "Update Age",
            'res_model': 'update.age.wizards',
            'view_mode': 'form',
            'target': 'new',
            # 'context': {'active_id': self.id, 'active_model': 'amazon.order.line',},
            'context': {'default_record_id': self.id}
            # 'views': [[False, 'form']]
        }

