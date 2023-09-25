from odoo import api, fields,models


class AmazonProduct(models.Model):
    _name = 'amazon.product'
    _rec_name = 'prod_name'

    prod_name = fields.Char(string='product name')
    prod_price = fields.Float(string="product price ")
    quantity = fields.Integer(string='quantity')
    amazon_prod_id = fields.One2many('amazon.product.line', 'product_ids', string="Product Records")
    order_count = fields.Integer(string='total order', compute='count_order')

    def name_get(self):
        res = []
        for rec in self:
            res.append((rec.id, '%s (%s)' % (rec.prod_name, rec.prod_price)))
        return res

    def count_order(self):
        order_count = self.env["amazon.order"].search_count([('product_id', '=', self.id)])
        self.order_count = order_count

    def check_status(self):
        for i in range(100):
            print("Done")


class AmazonProductLine(models.Model):
    _name = 'amazon.product.line'

    product_ids = fields.Many2one('amazon.product')
    name = fields.Char(string='Name')
    quantity = fields.Integer(string="Quantity")

    def set_quantity(self):
        return {
            'type': 'ir.actions.act_window',
            'name': "Update quantity",
            'res_model': 'update.quantity.wizards',
            'view_mode': 'form',
            'target': 'new',
            'context': {'active_id': self.id, 'active_model': 'amazon.order.line',},
            #'context': {'default_record_id': self.id}
            # 'views': [[False, 'form']]
        }

