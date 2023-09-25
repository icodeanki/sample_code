from odoo import api, models, fields


class SaleOrderApi(models.TransientModel):
    _name = 'sale.order.api.wizards'

    customer = fields.Many2one('res.partner', string="Customer")
    pricelist = fields.Many2one('product.pricelist', string="Pricelist")
    expiration = fields.Date(string="Expiration")
    quotation = fields.Datetime(string="Quotation Date")
    payment = fields.Many2one('account.payment.term', string="Payment Term")

    product = fields.Many2one('product.template', string="Product")
    desc = fields.Char(string="Description")
    quantity = fields.Integer(string="Quantity")
    unit_price = fields.Float(string="Unit Price")
    tax = fields.Many2many('account.tax', string="Taxes")

    def create_order(self):
        self.env['sale.order'].create({
            'partner_id': self.customer.id,
            'validity_date': self.expiration,
            'pricelist_id': self.pricelist.id,
            'date_order': self.quotation,
            'payment_term_id': self.payment.id,
            'order_line': [(0, 0, {
                'product_id': self.product.id,
                'name': self.product.name,
                'order_partner_id': self.customer.id,
                'product_uom_qty': 2.0,
                'price_unit': self.unit_price,
                # 'tax_id': [],
            })]
        })
        # rec_id.update({
        #     'order_line': [(0, 0, {
        #         'product_template_id': self.product.id,
        #         'name': self.product.name,
        #         'product_uom': 1,
        #         'product_uom_qty': 2.0,
        #         'price_unit': self.unit_price,
        #         'tax_id': [(4, self.tax.id)],
        #     })]
        # })


# class SaleOrder(models.Model):
#     _inherit = 'sale.order'
#
#     @api.model
#     def create(self, vals):
#         print("self", self)
#         print("vals", vals)
#         res = super(SaleOrder, self).create(vals)
#         print("res", res)
#         return res
