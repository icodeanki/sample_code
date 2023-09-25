from odoo import fields, api, models, _


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    address = fields.Char(string="Address")
    product_id = fields.Many2many('product.template', string="Product")




