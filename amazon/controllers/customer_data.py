from odoo import http
from odoo.http import request

class CustomerData(http.Controller):
    @http.route('/customer/', type='http', auth='public', website=True)

    def Customer_Data(self, **post):
        cust = request.env['amazon.order'].search([])
        values = {
        'records': cust
        }
        # return "hello Ankita..!!!"
        return request.render('amazon.tmp_customer_data_page', values)