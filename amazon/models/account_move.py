from odoo import api, models, fields, _


class AccountMoveInherit(models.Model):
    _inherit = "account.move"

    total_amt = fields.Float(string="Total Amounts")

