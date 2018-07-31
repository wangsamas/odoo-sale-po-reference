# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = "sale.order"

    po_ref = fields.Char(string='PO Reference', translate=True)

    @api.multi
    def _prepare_invoice(self):
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        invoice_vals['po_ref'] = self.po_ref
        return invoice_vals
	
class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    po_ref = fields.Char(string="PO Reference") 
	
class StockPicking(models.Model):
    _inherit = "stock.picking"

    po_ref = fields.Char(string="PO Reference", related='sale_id.po_ref', readonly=True)
