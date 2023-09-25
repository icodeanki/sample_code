from odoo import api, models, fields


class CancelOrder(models.TransientModel):
    _name = "cancel.order.wizards"
    _description = "Cancel Order Wizards"

    customer_ids = fields.Many2one('amazon.customer', string='Customer ID', domain=[('gender','=', 'female'),('age','=', 23)])
    # customers_ids = fields.Many2one('amazon.order', string='Customer ID', domain=[('age','>', 20)])