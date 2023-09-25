from odoo import api, models, fields, _

class SaleOrderQualityCheckWizards(models.Model):
    _name = 'sale.order.quality.check.wizards'

    record_id = fields.Char()

    def quality_check(self):
        print('Button Clicked !!!!')
        model = "sale.order.line"
        print('model', '...'*20, model)
        res = self.env[model].search([('id', '=', self.record_id)])
        print('res', '...'*20, res)
        res.update({'is_selected': True})














