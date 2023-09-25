from odoo import api, fields, models, _


class FlipcartUsers(models.Model):
    _inherit = "flipcart.users"

    email = fields.Char(string="Email")