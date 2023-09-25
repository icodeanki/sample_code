from odoo import api, fields, models


class SaleOrderInherited(models.Model):
    _inherit = 'res.partner'


    def name_get(self):
        res = []
        for rec in self:
            res.append((rec.id, '%s (%s)' % (rec.name, rec.email)))
        return res
