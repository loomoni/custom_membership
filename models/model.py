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
    sector_industry = fields.Many2one(comodel_name="configuration.setting.industry", string="Sector/ Industry", required=False, )
    membership_cat = fields.Many2one(comodel_name="configuration.setting.category", string="Membership Category", required=False, )
    applicable_fee = fields.Float(string="Applicable Fees", related="membership_cat.registration_fee", required=False, )
    annual_fee = fields.Float(string="Annual Fees", related="membership_cat.annual_subscription_fee", required=False, )

    directors_line_ids = fields.One2many(comodel_name="directors.lines", inverse_name="directors_id",
                                         string="Directors", required=False, )
    business_description_ids = fields.One2many(comodel_name="business.description",
                                               inverse_name="business_description_id", string="Business Description",
                                               required=False, )


class DirectorsLines(models.Model):
    _name = "directors.lines"
    _description = "directors record table"
    _rec_name = "name"

    name = fields.Char(string="Name", required=False, )
    nationality = fields.Char(string="Nationality", required=False, )
    directors_id = fields.Many2one(comodel_name="form.registration", string="Directors Id", required=False, )


class BusinessDescription(models.Model):
    _name = "business.description"
    _description = "business description table"

    business_description = fields.Text(string="Business Description", required=False, )
    business_description_id = fields.Many2one(comodel_name="form.registration", string="Business Description Id",
                                              required=False, )


class Payment(models.Model):
    _name = "payment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Record payment table"

    name = fields.Many2one(comodel_name="form.registration", string="Name", required=False, )
    fee_amount = fields.Float(string="Amount", related="name.annual_fee", required=True, )
    type = fields.Selection(string="Type", selection=[('annual', 'Annual'), ], required=True, )
    state = fields.Selection(string="Status", selection=[('unpaid', 'Unpaid'),
                                                         ('partial', 'Partial Paid'),
                                                         ('paid', 'Paid'),
                                                         ], track_visibility='onchange',
                             readonly=True, required=True, copy=False, default='unpaid')


    @api.multi
    def button_approve(self):
        self.write({'state': 'paid'})
        return True


class ConfigurationSettingCategory(models.Model):
    _name = "configuration.setting.category"
    _description = "configuration setting table category"
    _rec_name = "name"

    name = fields.Char(string="Category name", required=True, )
    registration_fee = fields.Float(string="Registration Fee",  required=False, )
    annual_subscription_fee = fields.Float(string="Annual Subscription Fee",  required=False, )


class ConfigurationSettingCluster (models.Model):
    _name = "configuration.setting.cluster"
    _description = "configuration setting table cluster "
    _rec_name = "name"

    name = fields.Char(string="Cluster name", required=True,)


class ConfigurationSettingIndustry(models.Model):
    _name = "configuration.setting.industry"
    _description = "configuration setting table cluster "
    _rec_name = "name"

    name = fields.Char(string="Industry Type", required=True, )


# class ConfigurationSettingCluster(models.Model):
#     _name = "configuration.setting.cluster"
#     _description = "configuration setting table cluster "
#     _rec_name = "name"

    # name = fields.Char(string="Cluster name", required=False, )
