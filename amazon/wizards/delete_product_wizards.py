from odoo import api, models, fields


class DeleteProduct(models.TransientModel):
    _name = "delete.product.wizards"
    _description = "Delete Product Wizards"

    product_id = fields.Many2one('amazon.product', string='Product ID')