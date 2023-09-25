from odoo import models


class TaxInvoiceXlsx(models.AbstractModel):
    _name = 'report.amazon.export_invoice_report_xls'
    _inherit = 'report.report_xlsx.abstract'


    def generate_xlsx_report(self, workbook, data, user):
        sheet = workbook.add_worksheet('Customer Records')
        bold = workbook.add_format({'bold': True})
        format_1 = workbook.add_format({'bold': True, 'align': 'center'})
        row = 3
        col = 3
        sheet.set_column('D:E', 15)
        for obj in user:
            row += 1
            sheet.merge_range(row, col, row, col + 1, 'Customer Records', format_1)
            row += 1
            sheet.write(row, col, 'Name', bold)
            sheet.write(row, col + 1, obj.name)
            row += 1
            sheet.write(row, col, 'Gender', bold)
            sheet.write(row, col + 1, obj.gender)
            row += 1
            sheet.write(row, col, 'Contact No', bold)
            sheet.write(row, col + 1, obj.contact)





