from odoo import api, fields, models, _
import datetime


class InvoiceInherity(models.Model):
    _inherit = "account.invoice"

    members = fields.Many2one(comodel_name="form.registration", string="Company", required=True, )
    reg_payment = fields.Float(string="Registration Payment", related="members.applicable_fee",  required=False, )
    annual_payment = fields.Float(string="Annual Payment", related="members.annual_fee", required=False, )
    partern_id = fields.Many2one(comodel_name="form.registration", string="Partner", required=False, )