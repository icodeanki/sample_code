from odoo import api, models, fields


class UpdateAge(models.TransientModel):
    _name = "update.age.wizards"
    _description = "Update Age Wizards"

    age_id = fields.Integer(string='Age')
    name = fields.Char('Name')
    record_id = fields.Char()

    def update_age(self):
        # record_id = self.env.context.get('active_id')
        # model = self.env.context.get('active_model')
        model = 'amazon.order.line'
        res = self.env[model].search([('id', '=', self.record_id)])
        res.update({
            'age': self.age_id,
            'name': self.name
        })
