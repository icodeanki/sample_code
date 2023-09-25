{
    'name': 'Amazon System',
    'version': '1.0.0',
    'category': 'Retail',
    'author': 'Ankita',
    'summary': 'Retail Management System',
    'description': """Retail Management System.""",
    'depends': ['base', 'mail', 'sale', 'account', 'flipcart','report_xlsx', 'website', 'contacts'],
    'data': [
        'data/sequence_data.xml',
        'security/ir.model.access.csv',
        'security/security_access.xml',
        'wizards/cancel_order_view.xml',
        'wizards/deletel_product_view.xml',
        'wizards/sale_order_api.xml',
        'wizards/update_age.xml',
        'wizards/sale_order_quality_check_wizards.xml',
        # 'wizards/update_quantity.xml',
        'views/customer_view.xml',
        'views/order_view.xml',
        'views/sale_order.xml',
        # 'views/flipcart_users.xml',
        'views/product_view.xml',
        'views/account_move.xml',
        'views/female_customer_view.xml',
        'views/template_customer_data.xml',
        'views/website_form.xml',
        'views/website_customer_list_view.xml',
        'views/website_customer_view.xml',
        'views/sale_order_qualitycheck_button.xml',
        'reports/customer_reports.xml',
        'reports/reports.xml',
        'reports/order_reports.xml',
        'reports/tax_invoice.xml',
        'reports/export_invoice.xml',
        'reports/purchase_order.xml',
        # 'reports/inherit_customer_invoice.xml',

    ],
    'demo': [],
    'sequence': -100,
    'application': True,
    'installable': True,
    'auto_install': False,
    'assets': {},
    'license': 'LGPL-3',
}
