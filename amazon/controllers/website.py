from odoo import http
from odoo.http import request

class CustomerWebsite(http.Controller):

    @http.route('/customer-registration', type='http', auth='public', website=True)
    def customer_webform(self, **post):
        country_id = request.env['res.country'].search([])
        state_id = request.env['res.country.state'].search([])
        auto_fill = {
            'country_id': country_id,
            'state_id': state_id,
        }
        print('EXecution here.......................')
        # gst_num = request.env['res.partner'].sudo().search([()])
        # print('GST_NUM......................', gst_num)
        return http.request.render('amazon.customer_registration_form', auto_fill)

    @http.route('/customer-registration/submit', type='http', auth='public', website=True)
    def create_customer_webform_submit(self, **post):
        print('###############################################', post)
        print('###############################################', post['email'])
        # request.env['res.partner'].create(post)
        return request.render('amazon.submit_registration', {})

    @http.route('/customer-registration/all', type='http', auth='user', website=True)
    def customer_list_view(self, **post):

        cust_id = request.env['res.partner'].search([])
        vals = {
            'cust_ids': cust_id
        }
        print('################################==>', vals)

        return request.render('amazon.customer_list_view_menu', vals)

    @http.route('/customer/<int:customer_id>/', type='http', auth='user', website=True)
    def customer_view(self, customer_id, **post):
        cust_id = request.env['res.partner'].search([('id', '=', customer_id)])
        vals = {
            'cust_ids': cust_id
        }
        print('################################==>', vals)

        return request.render('amazon.customer_view', vals)







