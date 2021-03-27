from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class FormRegistration(models.Model):
    _name = "form.registration"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Registration form membership table"

    name = fields.Char(string="Name", required=True)
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
    sector_industry = fields.Many2one(comodel_name="configuration.setting.industry", string="Sector/ Industry",
                                      required=False, )
    membership_cat = fields.Many2one(comodel_name="configuration.setting.category", string="Membership Category",
                                     required=False, )
    applicable_fee = fields.Float(string="Registration Fees", related="membership_cat.registration_fee",
                                  required=False, )
    annual_fee = fields.Float(string="Annual Fees", related="membership_cat.annual_subscription_fee", required=False, )
    street = fields.Char(string="", required=False, )
    street_two = fields.Char(string="", required=False, )
    region = fields.Selection(string="Region",
                              selection=[('arusha', 'Arusha'), ('dar', 'Dar es Salaam'), ('dodoma', 'Dodoma'),
                                         ('geita', 'Geita'),
                                         ('iringa', 'Iringa'), ('kagera', 'Kagera'), ('katavi', 'Katavi'),
                                         ('kigoma', 'Kigoma'),
                                         ('kilimanjaro', 'Kilimanjaro'),
                                         ('lindi', 'Lindi'), ('manyara', 'Manyara'), ('mara', 'Mara'),
                                         ('mbeya', 'Mbeya'), ('morogoro', 'Morogoro'),
                                         ('mtwara', 'Mtwara'), ('mwanza', 'Mwanza'), ('njombe', 'Njombe'),
                                         ('pwani', 'Pwani'),
                                         ('rukwa ', 'Rukwa '), ('ruvuma', 'Ruvuma'),
                                         ('shinyanga', 'Shinyanga'), ('simiyu', 'Simiyu'), ('singida', 'Singida'),
                                         ('songwe', 'Songwe'), ('tabora', 'Tabora'),
                                         ('tanga', 'Tanga')], required=False, )
    # district = fields.Selection(string="District", selection=[('monduli', 'Monduli')], required=False,)
    arusha_districts = fields.Selection(string="District",
                                        selection=[('meru', 'Meru'), ('arusha_city', 'Arusha City'), ('ar', 'Arusha'),
                                                   ('karatu', 'Karatu'), ('longido', 'Longido'), ('monduli', 'Monduli'),
                                                   ('ngorongoro', 'Ngorongoro'), ], required=False, )
    dar_districts = fields.Selection(string="District",
                                     selection=[('ilala', 'Ilala'), ('kinondoni', 'Kinondoni'), ('temeke', 'Temeke'),
                                                ('kigamboni', 'Kigamboni'), ('ubungo', 'Ubungo'), ], required=False, )
    dodoma_districts = fields.Selection(string="District",
                                        selection=[('bahi', 'Bahi'), ('chamwino', 'Chamwino'), ('chemba', 'Chemba'),
                                                   ('dodoma_municipal', 'Dodoma Municipal'), ('kondoa', 'Kondoa'),
                                                   ('kongwa', 'Kongwa'), ('mpwapwa', 'Mpwapwa'), ], required=False, )
    geita_districts = fields.Selection(string="District", selection=[('bukombe', 'Bukombe'), ('chato', 'Chato'),
                                                                     ('geita_town', 'Geita Town Council & Geita'),
                                                                     ('mbogwe', 'Mbogwe'), ("nyang", "Nyang'hwale"), ],
                                       required=False, )
    iringa_districts = fields.Selection(string="District",
                                        selection=[('iringa_disc', 'Iringa'), ('iringa_munic', 'Iringa Municipal'),
                                                   ('kilolo', 'Kilolo'),
                                                   ('mafinga', 'Mafinga'), ('mufindi', 'Mufindi'), ], required=False, )
    kagera_districts = fields.Selection(string="District",
                                        selection=[('biharamulo', 'Biharamulo'), ('bukoba', 'Bukoba'),
                                                   ('bukoba_munic', 'Bukoba Municipal'),
                                                   ('karagwe', 'Karagwe'), ('kyerwa', 'Kyerwa'),
                                                   ('missenyi', 'Missenyi'), ('muleba', 'Muleba'),
                                                   ('ngara', 'Ngara'), ], required=False, )
    katavi_districts = fields.Selection(string="District", selection=[('mlele', 'Mlele'), ('mpanda', 'Mpanda'),
                                                                      ('mpanda_town', 'Mpanda Town'), ],
                                        required=False, )
    kigoma_districts = fields.Selection(string="District",
                                        selection=[('buhigwe', 'Buhigwe'), ('kakonko', 'Kakonko'), ('kasulu', 'Kasulu'),
                                                   ('kasulu_town', 'Kasulu Town'),
                                                   ('kibondo', 'Kibondo'), ('kigoma', 'Kigoma'),
                                                   ('kigoma_munic', 'Kigoma-Ujiji Municipal'), ('uvinza', 'Uvinza'), ],
                                        required=False, )
    kilimanjaro_districts = fields.Selection(string="District", selection=[('hai', 'Hai'), ('moshi', 'Moshi'),
                                                                           ('moshi_monic', 'Moshi Municipal'),
                                                                           ('mwanga', 'Mwanga'),
                                                                           ('rombo', 'Rombo'), ('same', 'Same'),
                                                                           ('siha', 'Siha'), ], required=False, )
    lindi_districts = fields.Selection(string="District", selection=[('kilwa', 'Kilwa'), ('lindi', 'Lindi'),
                                                                     ('lindi_munic', 'Lindi Municipal'),
                                                                     ('liwale', 'Liwale'),
                                                                     ('nachingwea', 'Nachingwea'),
                                                                     ('ruangwa', 'Ruangwa'), ], required=False, )
    manyara_districts = fields.Selection(string="District",
                                         selection=[('babati_town', 'Babati Town'), ('babati', 'Babati'),
                                                    ('hanang', 'Hanang'), ('kiteto', 'Kiteto'),
                                                    ('mbulu', 'Mbulu'), ('simanjiro', 'Simanjiro'), ], required=False, )
    mara_districts = fields.Selection(string="District",
                                      selection=[('bunda', 'Bunda'), ('butiama', 'Butiama'), ('musoma', 'Musoma'),
                                                 ('musoma_munic', 'Musoma Municipal'),
                                                 ('rorya', 'Rorya'), ('serengeti', 'Serengeti'),
                                                 ('tarime', 'Tarime'), ], required=False, )
    mbeya_districts = fields.Selection(string="District",
                                       selection=[('busokelo', 'Busokelo'), ('chunya', 'Chunya'), ('kyela', 'Kyela'),
                                                  ('mbarali', 'Mbarali'), ('mbeya_city', 'Mbeya City'),
                                                  ('mbeya', 'Mbeya'), ('rungwe', 'Rungwe'), ], required=False, )
    morogoro_districts = fields.Selection(string="District", selection=[('gairo', 'Gairo'), ('kilombero', 'Kilombero'),
                                                                        ('kilosa', 'Kilosa'), ('morogoro', 'Morogoro'),
                                                                        ('morogoro_municipal ', 'Morogoro Municipal '),
                                                                        ('mvomero', 'Mvomero'), ('ulanga', 'Ulanga'),
                                                                        ('malinyi', 'Malinyi'),
                                                                        ('ifakara', 'Ifakara'), ], required=False, )
    mtwara_districts = fields.Selection(string="District",
                                        selection=[('masasi', 'Masasi'), ('masasi_town', 'Masasi Town'),
                                                   ('mtwara', 'Mtwara'), ('mtwara_municipal', 'Mtwara Municipal'),
                                                   ('nanyumbu', 'Nanyumbu'), ('newala', 'Newala'),
                                                   ('tandahimba', 'Tandahimba'), ], required=False, )
    mwanza_districts = fields.Selection(string="District",
                                        selection=[('ilemela_municipal', 'Ilemela Municipal'), ('kwimba', 'Kwimba'),
                                                   ('magu', 'Magu'), ('misungwi', 'Misungwi'),
                                                   ('nyamagana_municipal', 'Nyamagana Municipal'),
                                                   ('sengerema', 'Sengerema'), ('ukerewe', 'Ukerewe'), ],
                                        required=False, )
    njombe_districts = fields.Selection(string="District",
                                        selection=[('ludewa', 'Ludewa'), ('makambako_town', 'Makambako Town'),
                                                   ('makete', 'Makete'), ('njombe', 'Njombe'),
                                                   ('njombe_town', 'Njombe Town'), ('wang', "Wanging'ombe"), ],
                                        required=False, )
    pwani_districts = fields.Selection(string="District", selection=[('bagamoyo', 'Bagamoyo'), ('kibaha', 'Kibaha'),
                                                                     ('kibaha_town', 'Kibaha Town'),
                                                                     ('kisarawe', 'Kisarawe'),
                                                                     ('mafia', 'Mafia'), ('mkuranga', 'Mkuranga'),
                                                                     ('rufiji ', 'Rufiji '), ], required=False, )
    rukwa_districts = fields.Selection(string="District", selection=[('kalambo', 'Kalambo'), ('nkasi', 'Nkasi'),
                                                                     ('sumbawanga', 'Sumbawanga'), (
                                                                         'sumbawanga_municipal',
                                                                         'Sumbawanga Municipal'), ],
                                       required=False, )
    ruvuma_districts = fields.Selection(string="District", selection=[('mbinga', 'Mbinga'), ('songea', 'Songea'),
                                                                      ('songea_Municipal', 'Songea Municipal'),
                                                                      ('tunduru', 'Tunduru'),
                                                                      ('namtumbo ', 'Namtumbo '),
                                                                      ('nyasa ', 'Nyasa '), ], required=False, )
    shinyanga_districts = fields.Selection(string="District",
                                           selection=[('kahama_town', 'Kahama Town'), ('kahama', 'Kahama'),
                                                      ('kishapu', 'Kishapu'),
                                                      ('shinyanga_municipal', 'Shinyanga Municipal'),
                                                      ('shinyanga', 'Shinyanga'), ], required=False, )
    simiyu_districts = fields.Selection(string="District", selection=[('bariadi ', 'Bariadi '), ('busega ', 'Busega '),
                                                                      ('itilima', 'Itilima'), ('maswa', 'Maswa'),
                                                                      ('meatu', 'Meatu'), ], required=False, )
    singida_districts = fields.Selection(string="District",
                                         selection=[('ikungi', 'Ikungi'), ('iramba', 'Iramba'), ('manyoni', 'Manyoni'),
                                                    ('mkalama', 'Mkalama'), ('singida', 'Singida'),
                                                    ('singida_municipal', 'Singida Municipal'), ], required=False, )
    songwe_districts = fields.Selection(string="District",
                                        selection=[('ileje', 'Ileje'), ('mbozi', 'Mbozi'), ('momba', 'Momba'),
                                                   ('songwe', 'Songwe'), ], required=False, )
    tabora_districts = fields.Selection(string="District",
                                        selection=[('iogunga', 'Igunga'), ('kaliua', 'Kaliua'), ('nzega', 'Nzega'),
                                                   ('sikonge', 'Sikonge'),
                                                   ('tabora_municipal', 'Tabora Municipal'), ('urambo ', 'Urambo '),
                                                   ('uyui ', 'Uyui '), ], required=False, )
    tanga_districts = fields.Selection(string="District",
                                       selection=[('handeni', 'Handeni'), ('handeni_town', 'Handeni Town'),
                                                  ('kilindi', 'Kilindi'), ('korogwe_town', 'Korogwe Town'),
                                                  ('korogwe', 'Korogwe'), ('lushoto', 'Lushoto'), ('muheza', 'Muheza'),
                                                  ('kkinga', 'Mkinga'), ('pangani ', 'Pangani '),
                                                  ('tanga_city', 'Tanga City'), ], required=False, )
    ward = fields.Char(string="Ward", required=False, )
    website = fields.Char(string="Website", required=False, )
    directors_line_ids = fields.One2many(comodel_name="directors.lines", inverse_name="directors_id",
                                         string="Directors", required=False, )
    business_description_ids = fields.One2many(comodel_name="business.description",
                                               inverse_name="business_description_id", string="Business Description",
                                               required=False, )
    general_contact_lines_ids = fields.One2many(comodel_name="general.contact", inverse_name="general_contact_id",
                                                string="Campany", required=False, )

    @api.depends('arusha_districts', 'region', 'dar_districts')
    def compute_district(self):
        for rec in self:
            if rec.region == 'arusha':
                rec.district = rec.arusha_districts
            else:
                rec.district = rec.dar_districts


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


class GeneralContact(models.Model):
    _name = "general.contact"
    _description = "table to store general contact of hte company"

    name = fields.Char(string="Contact Name", required=True)
    title = fields.Many2one(comodel_name="contact.title", string="Title", required=False, )
    # image_small = fields.Binary(string="Photo",  )
    job_position = fields.Char(string="Job Position", required=False)
    phone = fields.Char(string="Phone", required=False)
    email = fields.Char(string="Email", required=False)
    mobile = fields.Char(string="Mobile", required=False)
    general_contact_id = fields.Many2one(comodel_name="form.registration", string="General Contact", required=False, )


class Payment(models.Model):
    _name = "payment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Record payment table"

    name = fields.Many2one(comodel_name="form.registration", string="Company Name", required=True, )
    reg_fee = fields.Float(string="registration fee", related="name.applicable_fee", required=False, )
    annual_fee = fields.Float(string="annual fee", related="name.annual_fee", required=False, )
    fee_amount = fields.Float(string="Amount", required=True, compute="amount_required")
    amount_paid = fields.Float(string="Amount Paid", required=False, )
    amount_remain = fields.Float(string="Amount Remain", required=False, compute="compute_amount_remain_unpaid")
    pay_year = fields.Integer(string="For Year ", required=True, )
    pay_date = fields.Date(string="Payment Date", required=False, )
    type = fields.Selection(string="Type of Payment", selection=[('annual', 'Annual'),
                                                                 ('reg_fee', 'Registration Fees'), ], required=True, )
    receipt = fields.Binary(string="Attach Receipt", attachment=True, store=True, )
    receipt_file_name = fields.Char('Receipt File Name')
    state = fields.Selection(string="Status", selection=[('unpaid', 'Unpaid'),
                                                         ('partial', 'Partial Paid'),
                                                         ('paid', 'Paid'),
                                                         ], track_visibility='onchange',
                             readonly=True, required=True, copy=False, default='unpaid')
    is_active = fields.Boolean(string="Active", default=False)

    @api.depends('type', 'annual_fee', 'reg_fee')
    def amount_required(self):
        for rec in self:
            if rec.type == 'annual':
                rec.fee_amount = rec.annual_fee
            elif rec.type == 'reg_fee':
                rec.fee_amount = rec.reg_fee

    @api.depends('fee_amount', 'amount_paid')
    def compute_amount_remain_unpaid(self):
        for rec in self:
            rec.amount_remain = rec.fee_amount - rec.amount_paid

    @api.multi
    def button_approve(self):
        for rec in self:
            if rec.amount_paid != rec.fee_amount:
                raise ValidationError(_("Fee amount should be equal to paid amount"))
        self.write({'state': 'paid'})
        return True

    @api.depends('amount_paid', 'fee_amount')
    @api.multi
    def button_partial_paid(self):
        for rec in self:
            if rec.amount_paid == rec.fee_amount:
                raise ValidationError(_("The payment is marked as full paid not partial"))
            elif rec.amount_paid > rec.fee_amount:
                raise ValidationError(_("Amount Paid should be less or equal to fee amount"))
        self.write({'state': 'partial'})
        return True


class ConfigurationSettingCategory(models.Model):
    _name = "configuration.setting.category"
    _description = "configuration setting table category"
    _rec_name = "name"

    name = fields.Char(string="Category name", required=True, )
    registration_fee = fields.Float(string="Registration Fee", required=False, )
    annual_subscription_fee = fields.Float(string="Annual Subscription Fee", required=False, )


class ConfigurationSettingCluster(models.Model):
    _name = "configuration.setting.cluster"
    _description = "configuration setting table cluster "
    _rec_name = "name"

    name = fields.Char(string="Cluster name", required=True, )


class ConfigurationSettingIndustry(models.Model):
    _name = "configuration.setting.industry"
    _description = "configuration setting table cluster "
    _rec_name = "name"

    name = fields.Char(string="Industry Type", required=True, )


class ContactTitle(models.Model):
    _name = "contact.title"
    _description = "contact title table"
    _rec_name = "name"

    name = fields.Char(string="Title", required=True, )
    abbreviation = fields.Char(string="Abbreviation", required=False, )

# class ConfigurationSettingCluster(models.Model):
#     _name = "configuration.setting.cluster"
#     _description = "configuration setting table cluster "
#     _rec_name = "name"

# name = fields.Char(string="Cluster name", required=False, )
