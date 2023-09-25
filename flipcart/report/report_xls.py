from odoo import api, fields, models

class CustomerReportXls(models.AbstractModel):
    _name = 'report.amazon.customer_report_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xls_report(self, workbook, data, lines):
        print("lines", lines, data)
        # format1 = workbook.add_format({'font_size':14, 'align':'vcenter', 'bold':True})
        # format2 = workbook.add_format({'font_size':10, 'align':'vcenter'})
        workbook.add_worksheet('customer_report')
        # sheet.write(2,2,'Name', format1)
        # sheet.write(2,3,lines.customer_name, format2)






