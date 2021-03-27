from odoo import api, fields, models, _


class ResPartenerInherit(models.Model):
    _inherit = 'res.partner'

    # company_type = fields.Selection(selection_remove=[('person', 'Individual')])
