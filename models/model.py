from odoo import api, fields, models, _


class FormRegistration(models.Model):
    _name = "form.registration"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Registration form membership table"

    name = fields.Char(string="Name", required=True, )
    certificate = fields.Char(string="Certificate of Incorporation", required=False, )
    year_establishment = fields.Integer(string="Year of Establishment", required=False, )
    business_no = fields.Integer(string="Business License No", required=False, )
    company_status = fields.Selection(string="Company Status",
                                      selection=[('private', 'Private'), ('public', 'Public'), ], required=False, )
    chairperson_name = fields.Char(string="Chairperson Name", required=False, )
    executive_name = fields.Char(string="CEO/Executive Director's Name", required=False, )
    copy_registration_certificate_attachment = fields.Binary(string="Copy of registration certificate", attachment=True,
                                                             store=True, )
    copy_registration_certificate_file_name = fields.Char('Copy registration certificate File Name')
    date_registration = fields.Date(string="Date of Registration", required=False, )


class Payment(models.Model):
    _name = "payment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Record payment table"

    name = fields.Char(string="Name", required=True, )
    fee_amount = fields.Float(string="Amount", required=True, )
    type = fields.Selection(string="Type", selection=[('one', 'One Time'), ('annual', 'Annual'), ], required=True, )
    state = fields.Selection(string="Status", selection=[('draft', 'Draft'),
                                                         ('unpaid', 'Unpaid'),
                                                         ('partial', 'Partial Paid'),
                                                         ('paid', 'Paid'),
                                                         ], track_visibility='onchange',
                             readonly=True, required=True, copy=False, default='draft')

    @api.multi
    def button_approve(self):
        self.write({'state': 'paid'})
        return True
