from odoo import api, fields, models, _
from datetime import date
from odoo.exceptions import ValidationError

class AmazonCustomer(models.Model):
    _name = "amazon.customer"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Amazon Customer"

    name = fields.Char(string='name', tracking=True, required=True)
    dob = fields.Date(string="DOB")
    ref = fields.Char(string="Reference", readonly=True)
    age = fields.Integer(string='Age', compute='calc_age', store=1, default=25)
    contact = fields.Integer(string="Contact No.", tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string='Gender',
                              default='male')
    active = fields.Boolean(string='Active', default=True)
    order_count = fields.Integer(string='total order', compute='count_order')

    @api.model
    def name_get(self):
        res = []
        for rec in self:
            # res.append((rec.id, '%s (%s)' % (rec.name, rec.ref)))
            res.append((rec.id, '%s - %s' % (rec.name, rec.ref)))
        return res


    def test_recordset(self):
        for rec in self:
            print("ODOO: ORM Recordset operation...................... !!!")
            partners = self.env['amazon.customer'].search([])
            print("Partners using Mapped......", partners.mapped('name'))
            print("Sorted Partners......", partners.sorted('name'))
            print("filtered Partners......", partners.filtered('contact'))
            # partners = self.env['res.partner'].mapped('name')
            # # print("Partners using Mapped......", partners.mapped('name'))
            print("Partners......", partners)
            # print("Partners name......", sorted(self.env['amazon.customer'].search([]).mapped('name')))


    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=10):
        args = list(args or [])
        if name:
            args += ['|', '|', ('name', operator, name), ('ref', operator, name),
                     ('contact', operator, name)]
        return self._search(args, limit=limit)


    @api.constrains('contact')
    def onchange_contact(self):
        if self.contact > 100:
            raise ValidationError("You can not enter 100")

    def count_order(self):
        order_count = self.env["amazon.order"].search_count([('customer_id', '=', self.id)])
        self.order_count = order_count

    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('amazon.customer')
        return super(AmazonCustomer, self).create(vals)

    @api.depends("dob")
    def calc_age(self):
        for i in self:
            today = date.today()
            if i.dob:
                i.age = today.year - i.dob.year
            else:
                i.age = 1

    # create, search, exist, browse, write, copy, unlink, search_count, default_get, name_get, name_search
    def check_status(self):
        # list1 = ['kaju1','barfi','katli','rasogulla']
        # for i in list1:
        #    vals = {
        #        'name': i,
        #        'age': 150,
        #        'gender': 'female'
        #    }
        #    res = self.env['amazon.customer'].create(vals)
        #    print(res.id, res.name)

        # res = self.env['amazon.customer'].search([('gender', '=', 'female')])
        # print(res)

        # res = self.env['amazon.customer'].search_count([('gender', '=', 'female')])
        # print(res)
        # res = self.env['amazon.customer'].search_count([('gender', '=', 'female'),('contact', '>=', 23)])
        # print(res)

        # res = self.env['amazon.customer'].browse(98)
        # if res.exists():
        #     vals = {
        #         'name': 'rrr',
        #         'age': 150,
        #         'gender': 'female'
        #     }
        #     res.write(vals)
        #     print(res.name)
        # else:
        #     print("||||  None ||||")

        res = self.env['amazon.customer'].browse(67)
        if res.exists():
           res.unlink()
           print('||||  Record Deleted  ||||')
        else:
           print('||||  Noooooo  ||||')

    # def action_open_order(self):
    #    print('done')

    def action_open_order(self):
        return {
            "name": "Orders",
            "type": "ir.actions.act_window",
            "res_model": "amazon.order",
            "domain": [("customer_id", "=", self.id)],
            "view_mode": "tree,form",
            "target": "current"
        }

    @api.model
    def default_get(self, fields):
        res = super(AmazonCustomer, self).default_get(fields)
        print("fields---------->", fields)
        print("res---------->", res)
        print("res---------->", res.get('gender'))
        if not res.get('gender'):
            res['gender'] = 'female'
        return res

    def create_order(self):
        vals = {
            'name': self.name,
            'dob': self.dob,
            'age': self.age
        }
        self.env['amazon.customer'].create(vals)

    def search_count(self):
        count = self.env['amazon.customer'].search_count([()])
        # res = self.env['amazon.customer'].search_count([('gender', '=', 'female')])
        print(count)


