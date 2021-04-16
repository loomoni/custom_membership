from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class FormRegistration(models.Model):
    _name = "form.registration"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Registration form membership table"

    name = fields.Char(string="Name", required=True)
    certificate = fields.Char(string="Certificate of Incorporation", required=False, )
    year_establishment = fields.Char(string="Year of Establishment", required=False, )
    membership_number = fields.Char(string="Membership number", required=False, )
    # year_establishment = fields.Selection(string="Year of Establishment",
    #                                       selection=[('2017', '2017'), ('2018', '2018'), ('2019', '2019'),
    #                                                  ('2017', '2017'), ('2018', '2018'), ('2019', '2019'),
    #                                                  ('2017', '2017'), ('2018', '2018'), ('2019', '2019'),
    #                                                  ('2017', '2017'), ('2018', '2018'), ('2019', '2019'),
    #                                                  ('2017', '2017'), ('2018', '2018'), ('2019', '2019'),
    #                                                  ('2017', '2017'), ('2018', '2018'), ('2019', '2019'),
    #                                                  ('2017', '2017'), ('2018', '2018'), ('2019', '2019'),
    #                                                  ('2017', '2017'), ('2018', '2018'), ('2019', '2019'),
    #                                                  ('2017', '2017'), ('2018', '2018'), ('2019', '2019'),
    #                                                  ('2017', '2017'), ('2018', '2018'), ('2019', '2019'),
    #                                                  ('2017', '2017'), ('2018', '2018'), ('1980', '1980'),
    #                                                  ('1990', '1990'), ('1991', '1991'), ('1992', '1992'),
    #                                                  ('1993', '1993'), ('1994', '1994'), ('1995', '1995'),
    #                                                  ('1996', '1996'), ('1997', '1997'), ('1998', '1998'),
    #                                                  ('1999', '1999'), ('2000', '2000'), ('2001', '2001'),
    #                                                  ('2002', '2002'), ('2003', '2003'), ('2004', '2004'),
    #                                                  ('2005', '2005'), ('2006', '2006'), ('2007', '2007'),
    #                                                  ('2008', '2008'), ('2009', '2009'), ('2010', '2010'),
    #                                                  ('2011', '2011'), ('2012', '2012'), ('2013', '2013'),
    #                                                  ('2014', '2014'), ('2015', '2015'), ('2016', '2016'),
    #                                                  ('2017', '2017'), ('2018', '2018'), ('2019', '2019'),
    #                                                  ('2020', '2020'), ('2021', '2021'), ('2022', '2022'),
    #                                                  ('2023', '2023'), ('2024', '2024'), ('2025', '2025'),
    #                                                  ('2026', '2026'), ('2027', '2027'), ('2028', '2028'),
    #                                                  ('2029', '2029'), ('2030', '2030'), ('2031', '2031'),
    #                                                  ('2032', '2032'), ('2033', '2033'), ('2034', '2034'),
    #                                                  ('2035', '2035'), ('2036', '2036'), ('2037', '2037'),
    #                                                  ('2038', '2038'), ('2039', '2039'), ('2040', '2040'),
    #                                                  ('2041', '2041'), ('2042', '2042'), ('2043', '2043'),
    #                                                  ('2044', '2044'), ('2045', '2045'), ('2046', '2046'),
    #                                                  ('2047', '2047'), ('2048', '2048'), ('2049', '2049'),
    #                                                  ('2050', '2050'), ('2051', '2051'), ('2052', '2052'),
    #                                                  ('2053', '2053'), ('2054', '2054'), ('2055', '2055'),
    #                                                  ('2056', '2056'), ('2057', '2057'), ('2058', '2058'),
    #                                                  ('2059', '2059'), ('2060', '2060'), ('2061', '2061'),
    #                                                  ('2062', '2062'), ('2063', '2063'), ('2064', '2064'),
    #                                                  ('2065', '2065'), ('2066', '2066'), ('2067', '2067'),
    #                                                  ('2068', '2068'), ('2069', '2069'), ('2070', '2070'),
    #                                                  ('2071', '2071'), ('2072', '2072'), ('2073', '2073'),
    #                                                  ('2074', '2074'), ('2075', '2075'), ('2076', '2076'),
    #                                                  ('2077', '2077'), ('2078', '2078'), ('2079', '2079'),
    #                                                  ('2080', '2080'), ('2081', '2081'), ('2082', '2082'),
    #                                                  ('2083', '2083'), ('2084', '2084'), ('2085', '2085'),
    #                                                  ('2086', '2086'), ('2087', '2087'), ('2088', '2089'),
    #                                                  ('2090', '2090'), ('2091', '2091'), ('2092', '2092'),
    #                                                  ('2093', '2093'), ('2094', '2094'), ('2095', '2095'),
    #                                                  ('2096', '2096'), ('2097', '2097'), ('2098', '2098'),
    #                                                  ('2099', '2099'), ('3000', '3000'), ],
    #                                       required=False, )

    business_no = fields.Char(string="Business License No", required=False, )
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
    cluster_id = fields.Many2one(comodel_name="configuration.setting.cluster", string="Cluster", required=False, )
    membership_cat = fields.Many2one(comodel_name="configuration.setting.category", string="Category",
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
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "directors record table"
    _rec_name = "name"

    name = fields.Char(string="Name", required=False, )
    nationality = fields.Char(string="Nationality", required=False, )
    directors_id = fields.Many2one(comodel_name="form.registration", string="Directors Id", required=False, )


class BusinessDescription(models.Model):
    _name = "business.description"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "business description table"

    business_description = fields.Text(string="Business Description", required=False, )
    business_description_id = fields.Many2one(comodel_name="form.registration", string="Business Description Id",
                                              required=False, )


class GeneralContact(models.Model):
    _name = "general.contact"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "table to store general contact of hte company"
    _rec_name = "email"

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
    reg_fee = fields.Float(string="registration fee", related="name.applicable_fee", required=False,
                           group_operator=True)
    annual_fee = fields.Float(string="annual fee", related="name.annual_fee", required=False, group_operator=True)
    fee_amount = fields.Float(string="Amount", required=True, compute="amount_required", group_operator=True)
    amount_paid = fields.Float(string="Amount Paid", required=False, compute="amount_paid_compute", group_operator=True)
    amount_remain = fields.Float(string="Amount Remain", required=False, compute="compute_amount_remain_unpaid",
                                 group_operator=True)
    category = fields.Char(string="Category", related="name.membership_cat.name", required=False, )
    cluster = fields.Char(string="Cluster", related="name.cluster_id.name", required=False, )
    pay_year = fields.Selection(string="For Year", selection=[('2017', '2017'), ('2018', '2018'), ('2019', '2019'),
                                                              ('2020', '2020'), ('2021', '2021'), ('2022', '2022'),
                                                              ('2023', '2023'), ('2024', '2024'), ('2025', '2025'),
                                                              ('2026', '2026'), ('2027', '2027'), ('2028', '2028'),
                                                              ('2029', '2029'), ('2030', '2030'), ('2031', '2031'),
                                                              ('2032', '2032'), ('2033', '2033'), ('2034', '2034'),
                                                              ('2035', '2035'), ('2036', '2036'), ('2037', '2037'),
                                                              ('2038', '2038'), ('2039', '2039'), ('2040', '2040'),
                                                              ('2041', '2041'), ('2042', '2042'), ('2043', '2043'),
                                                              ('2044', '2044'), ('2045', '2045'), ('2046', '2046'),
                                                              ('2047', '2047'), ('2048', '2048'), ('2049', '2049'),
                                                              ('2050', '2050'), ('2051', '2051'), ('2052', '2052'),
                                                              ('2053', '2053'), ('2054', '2054'), ('2055', '2055'),
                                                              ('2056', '2056'), ('2057', '2057'), ('2058', '2058'),
                                                              ('2059', '2059'), ('2060', '2060'), ('2061', '2061'),
                                                              ('2062', '2062'), ('2063', '2063'), ('2064', '2064'),
                                                              ('2065', '2065'), ('2066', '2066'), ('2067', '2067'),
                                                              ('2068', '2068'), ('2069', '2069'), ('2070', '2070'),
                                                              ('2071', '2071'), ('2072', '2072'), ('2073', '2073'),
                                                              ('2074', '2074'), ('2075', '2075'), ('2076', '2076'),
                                                              ('2077', '2077'), ('2078', '2078'), ('2079', '2079'),
                                                              ('2080', '2080'), ('2081', '2081'), ('2082', '2082'),
                                                              ('2083', '2083'), ('2084', '2084'), ('2085', '2085'),
                                                              ('2086', '2086'), ('2087', '2087'), ('2088', '2089'),
                                                              ('2090', '2090'), ('2091', '2091'), ('2092', '2092'),
                                                              ('2093', '2093'), ('2094', '2094'), ('2095', '2095'),
                                                              ('2096', '2096'), ('2097', '2097'), ('2098', '2098'),
                                                              ('2099', '2099'), ('3000', '3000'), ],
                                required=False, )
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
    payment_lines_ids = fields.One2many(comodel_name="payment.lines", inverse_name="payment_id", string="Payment Lines",
                                        required=False, )

    @api.depends('payment_lines_ids.amount_payment')
    def amount_paid_compute(self):
        for record in self:
            paid = 0
            for line in record.payment_lines_ids:
                paid += line.amount_payment
            record.amount_paid = paid

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
                raise ValidationError(
                    _("Fee amount should be equal to paid amount, Payment is marked as Partial Payment"))
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


class PaymentsLines(models.Model):
    _name = "payment.lines"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "payments line records table"

    amount_payment = fields.Float(string="Amount Paid", required=False, )
    payment_date = fields.Date(string="Date", required=False, )
    receipt = fields.Binary(string="Receipt", attachment=True, store=True, )
    receipt_file_name = fields.Char('Receipt File Name')
    payment_id = fields.Many2one(comodel_name="payment", string="Payment ID", required=False, )


class ConfigurationSettingCategory(models.Model):
    _name = "configuration.setting.category"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "configuration setting table category"
    _rec_name = "name"

    name = fields.Char(string="Category name", required=True, )
    registration_fee = fields.Float(string="Registration Fee", required=False, )
    annual_subscription_fee = fields.Float(string="Annual Subscription Fee", required=False, )


class ConfigurationSettingCluster(models.Model):
    _name = "configuration.setting.cluster"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "configuration setting table cluster "
    _rec_name = "name"

    name = fields.Char(string="Cluster name", required=True, )


class ConfigurationSettingIndustry(models.Model):
    _name = "configuration.setting.industry"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "configuration setting table cluster "
    _rec_name = "name"

    name = fields.Char(string="Industry Type", required=True, )


class ContactTitle(models.Model):
    _name = "contact.title"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "contact title table"
    _rec_name = "name"

    name = fields.Char(string="Title", required=True, )
    abbreviation = fields.Char(string="Abbreviation", required=False, )


class Engagement(models.Model):
    _name = "engagement"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Engagement recording Table"

    member_field = fields.Many2one(comodel_name="form.registration", string="Member", required=False, )
    engagement_type = fields.Many2one(comodel_name="engagement.type", string="Engagement Type", required=False, )
    description = fields.Text(string="Description", required=False, )
    date = fields.Date(string="Date", required=False, )
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
    location_name = fields.Char(string="Location Name", required=False, )
    state_select = fields.Many2one(comodel_name="status", string="Status", required=False, )
    # Selection(string="Status",
    #                             selection=[('initiated', 'Initiated'), ('ongoing', 'Ongoing'),
    #                                        ('completed', 'Completed'), ], required=False, )
    outcome = fields.Char(string="Outcome", required=False, )
    attachment_copy = fields.Binary(string="Attachment", attachment=True,
                                    store=True, )
    attachment_copy_file_name = fields.Char('Attachment File Name')


class Issue(models.Model):
    _name = "issue"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Issue table"

    name = fields.Char(string="Issue Name", required=True, )
    member_other = fields.Many2one(comodel_name="form.registration", string="Member", required=False, )
    date = fields.Date(string="Date", required=False, )
    status = fields.Many2one(comodel_name="status", string="Status", required=False, )
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
    location_name = fields.Char(string="Location Name", required=False, )
    issue_type_id = fields.Many2one(comodel_name="issue.type", string="Issue Type", required=False, )
    received_by = fields.Char(string="Received by", required=False, )
    issue_summary = fields.Text(string="Issue Summary", required=False, )
    conclusion = fields.Text(string="Conclusion", required=False, )


class Event(models.Model):
    _name = "event"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "event table"

    name = fields.Char(string="Event Name", required=True, )
    date = fields.Date(string="Date", required=False, )
    description = fields.Text(string="Description", required=False, )
    event_them = fields.Many2one(comodel_name="event.theme", string="Event Theme", required=False, )
    event_organizer = fields.Char(string="Event Organizer", required=False, )
    venue = fields.Char(string="Venue", required=False, )
    location_name = fields.Char(string="Location Name", required=False, )
    stakeholder = fields.Char(string="Stakeholder/Participant", required=False, )
    activity_summary = fields.Text(string="Activity Summary", required=False, )
    conclusion = fields.Text(string="Conclusion/Outcome", required=False, )
    attachment_copy = fields.Binary(string="Attachment", attachment=True,
                                    store=True, )
    attachment_copy_file_name = fields.Char('Attachment File Name')
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


class EngagementType(models.Model):
    _name = "engagement.type"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Engagement Type table"
    _rec_name = "name"

    name = fields.Char(string="Engagement Type", required=True, )


class IssueType(models.Model):
    _name = "issue.type"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Issue Type table"

    name = fields.Char(string="Issue Type", required=True, )


class EventTheme(models.Model):
    _name = "event.theme"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Event Theme Table"

    name = fields.Char(string="Event Theme", required=True, )


class Status(models.Model):
    _name = "status"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Status Table"

    name = fields.Char(string="Status", required=True, )
