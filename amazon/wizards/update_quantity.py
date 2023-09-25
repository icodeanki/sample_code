from odoo import api, models, fields


class UpdateQuantity(models.TransientModel):
    _name = "update.quantity.wizards"
    _description = "Update Quantity Wizards"

    quantity = fields.Integer(string="Quantity")

    def update_quantity(self):
        record_id = self.env.context.get('active_id')
        model = self.env.context.get('active_model')
        #model = 'amazon.order.line'
        res = self.env[model].search([('id', '=', record_id)])
        res.update({
            'quantity': self.quantity
        })