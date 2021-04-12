from odoo import api, fields, models, _
import datetime


class EmailInherity(models.Model):
    _inherit = "mail.mass_mailing.contact"

    @api.onchange('name')
    def _onchange_name_id(self):
        categories = []
        for category in self.name:
            categories.append(category.id)
        return {'domain': {'company_name': [('id', 'in', categories)]}}

    name = fields.Many2one(comodel_name="configuration.setting.category", string="Category", required=False, )
    company_name = fields.Many2one(comodel_name="form.registration", string="Company", required=False, )
    contact_name = fields.Many2one(comodel_name="general.contact", string="Member Name", required=False, )
    email = fields.Char(string="Email", related="contact_name.email", required=False)

