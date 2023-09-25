from odoo import api, models, fields, _

class QualityStatus(models.Model):
    _inherit = 'sale.order'

    button_state = fields.Char("Quality Status", compute="_compute_button_state")

    @api.depends('order_line.is_selected')
    def _compute_button_state(self):
        for record in self:
            checkbox_values = []
            for checkbox in record.order_line:
                if checkbox.is_selected == True:
                    checkbox_values.append(True)
                else:
                    checkbox_values.append(False)

            # checkbox_values = [checkbox.is_selected for checkbox in record.checkbox_ids]
            print('checkbox_values...................', checkbox_values)
            if all(checkbox_values):
                self.button_state = 'Quality Check'
            else:
                self.button_state = 'Not Check'

            # record.button_state = all(checkbox.is_selected for checkbox in record.checkbox_ids)


    def quality_status(self):
        pass

class QualityCheckButton(models.Model):
    _inherit = 'sale.order.line'

    is_selected = fields.Boolean(string="Quality Status", readonly=True, default=False)

    def open_wizards(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Quality Check',
            'res_model': 'sale.order.quality.check.wizards',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_record_id': self.id}
        }


