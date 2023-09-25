from odoo import api, fields, models

class FlipcartUsers(models.Model):
    _name = "flipcart.users"
    _description = "Flipcart Users"

    user_id = fields.Integer(string="User_Id")
    name = fields.Char(string="Name")
    gender = fields.Selection([('male','Male'),('female', 'Female')], string='Gender')
    contact = fields.Integer(string="Contact No")
    active = fields.Boolean(string="Active", default=True)

