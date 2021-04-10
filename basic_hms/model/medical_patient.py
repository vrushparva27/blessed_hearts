# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from datetime import date, datetime
from dateutil.relativedelta import relativedelta


class medical_patient(models.Model):
    _name = 'medical.patient'
    _rec_name = 'patient_id'
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin']
    _description = 'Medical patient'

    @api.onchange('patient_id')
    def _onchange_patient(self):
        '''
        The purpose of the method is to define a domain for the available
        purchase orders.
        '''
        address_id = self.patient_id
        self.partner_address_id = address_id

    def print_report(self):
        return self.env.ref('basic_hms.report_print_patient_card').report_action(self)

    @api.depends('date_of_birth')
    def onchange_age(self):
        for rec in self:
            if rec.date_of_birth:
                d1 = rec.date_of_birth
                d2 = datetime.today().date()
                rd = relativedelta(d2, d1)
                rec.age = str(rd.years) + "y" + " " + str(rd.months) + "m" + " " + str(rd.days) + "d"
            else:
                rec.age = "No Date Of Birth!!"

    document_attachment = fields.Binary('Document', attachment=True)
    patient_id = fields.Many2one('res.partner', domain=[('is_patient', '=', True)], string="Patient", required=True)
    name = fields.Char(string='Indoor ID')
    last_name = fields.Char('Last Name')
    date_of_birth = fields.Date(string="Date of Birth")
    sex = fields.Selection([('m', 'Male'), ('f', 'Female')], string="Sex")
    age = fields.Char(compute=onchange_age, string="Patient Age", store=True)
    critical_info = fields.Text(string="Patient Critical Information")
    photo = fields.Binary(string="Picture")
    blood_type = fields.Selection([('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')], string="Blood Type")
    rh = fields.Selection([('-+', '+'), ('--', '-')], string="Rh")
    marital_status = fields.Selection(
        [('s', 'Single'), ('m', 'Married'), ('w', 'Widowed'), ('d', 'Divorced'), ('x', 'Seperated')],
        string='Marital Status')
    deceased = fields.Boolean(string='Deceased')
    date_of_death = fields.Datetime(string="Date of Death")
    cause_of_death = fields.Char(string='Cause of Death')
    receivable = fields.Float(string="Receivable", readonly=True)
    current_insurance_id = fields.Many2one('medical.insurance', string="Insurance")
    partner_address_id = fields.Many2one('res.partner', string="Address", )
    primary_care_physician_id = fields.Many2one('medical.physician', string="Primary Care Doctor")
    patient_status = fields.Char(string="Hospitalization Status", readonly=True)
    patient_disease_ids = fields.One2many('medical.patient.disease', 'patient_id')
    patient_psc_ids = fields.One2many('medical.patient.psc', 'patient_id')
    excercise = fields.Boolean(string='Excercise')
    excercise_minutes_day = fields.Integer(string="Minutes/Day")
    sleep_hours = fields.Integer(string="Hours of sleep")
    sleep_during_daytime = fields.Boolean(string="Sleep at daytime")
    number_of_meals = fields.Integer(string="Meals per day")
    coffee = fields.Boolean('Coffee')
    coffee_cups = fields.Integer(string='Cups Per Day')
    eats_alone = fields.Boolean(string="Eats alone")
    soft_drinks = fields.Boolean(string="Soft drinks(sugar)")
    salt = fields.Boolean(string="Salt")
    diet = fields.Boolean(string=" Currently on a diet ")
    diet_info = fields.Integer(string=' Diet info ')
    general_info = fields.Text(string="Info")
    lifestyle_info = fields.Text('Lifestyle Information')
    smoking = fields.Boolean(string="Smokes")
    smoking_number = fields.Integer(string="Cigarretes a day")
    ex_smoker = fields.Boolean(string="Ex-smoker")
    second_hand_smoker = fields.Boolean(string="Passive smoker")
    age_start_smoking = fields.Integer(string="Age started to smoke")
    age_quit_smoking = fields.Integer(string="Age of quitting")
    drug_usage = fields.Boolean(string='Drug Habits')
    drug_iv = fields.Boolean(string='IV drug user')
    ex_drug_addict = fields.Boolean(string='Ex drug addict')
    age_start_drugs = fields.Integer(string='Age started drugs')
    age_quit_drugs = fields.Integer(string="Age quit drugs")
    alcohol = fields.Boolean(string="Drinks Alcohol")
    ex_alcohol = fields.Boolean(string="Ex alcoholic")
    age_start_drinking = fields.Integer(string="Age started to drink")
    age_quit_drinking = fields.Integer(string="Age quit drinking")
    alcohol_beer_number = fields.Integer(string="Beer / day")
    alcohol_wine_number = fields.Integer(string="Wine / day")
    alcohol_liquor_number = fields.Integer(string="Liquor / day")
    cage_ids = fields.One2many('medical.patient.cage', 'patient_id')
    sex_oral = fields.Selection([('0', 'None'),
                                 ('1', 'Active'),
                                 ('2', 'Passive'),
                                 ('3', 'Both')], string='Oral Sex')
    sex_anal = fields.Selection([('0', 'None'),
                                 ('1', 'Active'),
                                 ('2', 'Passive'),
                                 ('3', 'Both')], string='Anal Sex')
    prostitute = fields.Boolean(string='Prostitute')
    sex_with_prostitutes = fields.Boolean(string=' Sex with prostitutes ')
    sexual_preferences = fields.Selection([
        ('h', 'Heterosexual'),
        ('g', 'Homosexual'),
        ('b', 'Bisexual'),
        ('t', 'Transexual'),
    ], 'Sexual Orientation', sort=False)
    sexual_practices = fields.Selection([
        ('s', 'Safe / Protected sex'),
        ('r', 'Risky / Unprotected sex'),
    ], 'Sexual Practices', sort=False)
    sexual_partners = fields.Selection([
        ('m', 'Monogamous'),
        ('t', 'Polygamous'),
    ], 'Sexual Partners', sort=False)
    sexual_partners_number = fields.Integer('Number of sexual partners')
    first_sexual_encounter = fields.Integer('Age first sexual encounter')
    anticonceptive = fields.Selection([
        ('0', 'None'),
        ('1', 'Pill / Minipill'),
        ('2', 'Male condom'),
        ('3', 'Vasectomy'),
        ('4', 'Female sterilisation'),
        ('5', 'Intra-uterine device'),
        ('6', 'Withdrawal method'),
        ('7', 'Fertility cycle awareness'),
        ('8', 'Contraceptive injection'),
        ('9', 'Skin Patch'),
        ('10', 'Female condom'),
    ], 'Anticonceptive Method', sort=False)
    sexuality_info = fields.Text('Extra Information')
    motorcycle_rider = fields.Boolean('Motorcycle Rider', help="The patient rides motorcycles")
    helmet = fields.Boolean('Uses helmet', help="The patient uses the proper motorcycle helmet")
    traffic_laws = fields.Boolean('Obeys Traffic Laws', help="Check if the patient is a safe driver")
    car_revision = fields.Boolean('Car Revision', help="Maintain the vehicle. Do periodical checks - tires,breaks ...")
    car_seat_belt = fields.Boolean('Seat belt', help="Safety measures when driving : safety belt")
    car_child_safety = fields.Boolean('Car Child Safety',
                                      help="Safety measures when driving : child seats, proper seat belting, not seating on the front seat, ....")
    home_safety = fields.Boolean('Home safety',
                                 help="Keep safety measures for kids in the kitchen, correct storage of chemicals, ...")
    fertile = fields.Boolean('Fertile')
    menarche = fields.Integer('Menarche age')
    menopausal = fields.Boolean('Menopausal')
    menopause = fields.Integer('Menopause age')
    menstrual_history_ids = fields.One2many('medical.patient.menstrual.history', 'patient_id')
    breast_self_examination = fields.Boolean('Breast self-examination')
    mammography = fields.Boolean('Mammography')
    pap_test = fields.Boolean('PAP test')
    last_pap_test = fields.Date('Last PAP test')
    colposcopy = fields.Boolean('Colposcopy')
    mammography_history_ids = fields.One2many('medical.patient.mammography.history', 'patient_id')
    pap_history_ids = fields.One2many('medical.patient.pap.history', 'patient_id')
    colposcopy_history_ids = fields.One2many('medical.patient.colposcopy.history', 'patient_id')
    pregnancies = fields.Integer('Pregnancies')
    premature = fields.Integer('Premature')
    stillbirths = fields.Integer('Stillbirths')
    abortions = fields.Integer('Abortions')
    pregnancy_history_ids = fields.One2many('medical.patient.pregnency', 'patient_id')
    family_history_ids = fields.Many2many('medical.family.disease', string="Family Disease Lines")
    perinatal_ids = fields.Many2many('medical.preinatal')
    ex_alcoholic = fields.Boolean('Ex alcoholic')
    currently_pregnant = fields.Boolean('Currently Pregnant')
    born_alive = fields.Integer('Born Alive')
    gpa = fields.Char('GPA')
    works_at_home = fields.Boolean('Works At Home')
    colposcopy_last = fields.Date('Last colposcopy')
    mammography_last = fields.Date('Last mammography')
    ses = fields.Selection([
        ('None', ''),
        ('0', 'Lower'),
        ('1', 'Lower-middle'),
        ('2', 'Middle'),
        ('3', 'Middle-upper'),
        ('4', 'Higher'),
    ], 'Socioeconomics', help="SES - Socioeconomic Status", sort=False)
    education = fields.Selection([('o', 'None'), ('1', 'Incomplete Primary School'),
                                  ('2', 'Primary School'),
                                  ('3', 'Incomplete Secondary School'),
                                  ('4', 'Secondary School'),
                                  ('5', 'University')], string='Education Level')
    housing = fields.Selection([
        ('None', ''),
        ('0', 'Shanty, deficient sanitary conditions'),
        ('1', 'Small, crowded but with good sanitary conditions'),
        ('2', 'Comfortable and good sanitary conditions'),
        ('3', 'Roomy and excellent sanitary conditions'),
        ('4', 'Luxury and excellent sanitary conditions'),
    ], 'Housing conditions', help="Housing and sanitary living conditions", sort=False)
    works = fields.Boolean('Works')
    hours_outside = fields.Integer('Hours outside home',
                                   help="Number of hours a day the patient spend outside the house")
    hostile_area = fields.Boolean('Hostile Area')
    notes = fields.Text(string="Extra info")
    sewers = fields.Boolean('Sanitary Sewers')
    water = fields.Boolean('Running Water')
    trash = fields.Boolean('Trash recollection')
    electricity = fields.Boolean('Electrical supply')
    gas = fields.Boolean('Gas supply')
    telephone = fields.Boolean('Telephone')
    television = fields.Boolean('Television')
    internet = fields.Boolean('Internet')
    single_parent = fields.Boolean('Single parent family')
    domestic_violence = fields.Boolean('Domestic violence')
    working_children = fields.Boolean('Working children')
    teenage_pregnancy = fields.Boolean('Teenage pregnancy')
    sexual_abuse = fields.Boolean('Sexual abuse')
    drug_addiction = fields.Boolean('Drug addiction')
    school_withdrawal = fields.Boolean('School withdrawal')
    prison_past = fields.Boolean('Has been in prison')
    prison_current = fields.Boolean('Is currently in prison')
    relative_in_prison = fields.Boolean('Relative in prison',
                                        help="Check if someone from the nuclear family - parents sibblings  is or has been in prison")
    fam_apgar_help = fields.Selection([
        ('None', ''),
        ('0', 'None'),
        ('1', 'Moderately'),
        ('2', 'Very much'),
    ], 'Help from family',
        help="Is the patient satisfied with the level of help coming from the family when there is a problem ?",
        sort=False)
    fam_apgar_discussion = fields.Selection([
        ('None', ''),
        ('0', 'None'),
        ('1', 'Moderately'),
        ('2', 'Very much'),
    ], 'Problems discussion',
        help="Is the patient satisfied with the level talking over the problems as family ?", sort=False)
    fam_apgar_decisions = fields.Selection([
        ('None', ''),
        ('0', 'None'),
        ('1', 'Moderately'),
        ('2', 'Very much'),
    ], 'Decision making',
        help="Is the patient satisfied with the level of making important decisions as a group ?", sort=False)
    fam_apgar_timesharing = fields.Selection([
        ('None', ''),
        ('0', 'None'),
        ('1', 'Moderately'),
        ('2', 'Very much'),
    ], 'Time sharing',
        help="Is the patient satisfied with the level of time that they spend together ?", sort=False)
    fam_apgar_affection = fields.Selection([
        ('None', ''),
        ('0', 'None'),
        ('1', 'Moderately'),
        ('2', 'Very much'),
    ], 'Family affection',
        help="Is the patient satisfied with the level of affection coming from the family ?", sort=False)
    fam_apgar_score = fields.Integer('Score',
                                     help="Total Family APGAR 7 - 10 : Functional Family 4 - 6  : Some level of disfunction \n"
                                          "0 - 3  : Severe disfunctional family \n")
    lab_test_ids = fields.One2many('medical.patient.lab.test', 'patient_id')
    fertile = fields.Boolean('Fertile')
    menarche_age = fields.Integer('Menarche age')
    menopausal = fields.Boolean('Menopausal')
    pap_test_last = fields.Date('Last PAP Test')
    colposcopy = fields.Boolean('Colpscopy')
    gravida = fields.Integer('Pregnancies')
    medical_vaccination_ids = fields.One2many('medical.vaccination', 'medical_patient_vaccines_id')
    medical_appointments_ids = fields.One2many('medical.appointment', 'patient_id', string='Appointments')
    lastname = fields.Char('Last Name')
    report_date = fields.Date('Date', default=datetime.today().date())
    medication_ids = fields.One2many('medical.patient.medication1', 'medical_patient_medication_id')
    deaths_2nd_week = fields.Integer('Deceased after 2nd week')
    deaths_1st_week = fields.Integer('Deceased after 1st week')
    full_term = fields.Integer('Full Term')
    ses_notes = fields.Text('Notes')
    address_1 = fields.Char('Address')
    address_2 = fields.Char('Address')
    zip = fields.Char("Zip")
    city = fields.Char('City')
    state_id = fields.Many2one("res.country.state", string='State', ondelete='restrict',
                               domain="[('country_id', '=?', country_id)]",
                               default=lambda s: s.env['res.country.state'].search([('name', '=', 'Gujarat')], limit=1))
    country_id = fields.Many2one('res.country', string='Country', ondelete='restrict',
                                 default=lambda s: s.env['res.country'].search([('name', '=', 'India')], limit=1))
    phone = fields.Char("Phone")
    mobile = fields.Char("Mobile")
    hospitalization_ids = fields.One2many("medical.inpatient.registration", 'patient_id', "Hospitalization")
    document_ids = fields.One2many("medical.patient.documents", 'patient_id', "Documents")
    invoice_ids = fields.One2many("account.move", 'patient_id', string="Invoices",
                                  domain=[('type', '=', 'out_invoice'), ('state', '!=', 'cancel')], store=True)
    invoice_refund_ids = fields.One2many("account.move", 'patient_id', string="Refund Invoices",
                                         domain=[('type', '=', 'out_refund'), ('state', '!=', 'cancel')])
    deposit_ids = fields.One2many("account.payment", 'patient_id', "Deposits",
                                  domain=[('payment_type', '=', 'inbound'),('state', '!=', 'cancelled')])
    deposit_refund_ids = fields.One2many("account.payment", 'patient_id', string="Refund Deposits",
                                         domain=[('payment_type', '=', 'outbound'), ('state', '!=', 'cancelled')])
    invoice_count = fields.Integer(string='Invoice Count', readonly=True)
    deposit_count = fields.Integer(string='Deposit Count', readonly=True)
    impatient_count = fields.Integer(string='Impatient Count', readonly=True)
    documents_count = fields.Integer(string="Document Count")
    deposit_refund_count = fields.Integer(string="Refund Deposit", readonly=True)
    invoice_refund_count = fields.Integer(string="Refund Invoice", readonly=True)
    total_inv_amt = fields.Monetary(string="Total Invoice", compute='_get_invoiced', readonly=True, store=True)
    total_inv_refund_amt = fields.Monetary(string="Total Refund Invoices", readonly=True,
                                           store=True)
    total_deposit_amt = fields.Monetary(string="Total Deposit", readonly=True, store=True)
    total_deposit_refund_amt = fields.Monetary(string="Total Refund Deposits", readonly=True,
                                               store=True)
    company_id = fields.Many2one('res.company', 'Company', required=True, index=True,
                                 default=lambda self: self.env.company)
    currency_id = fields.Many2one('res.currency', string='Currency', required=True, readonly=True,
                                  default=lambda self: self.env.company.currency_id)
    active = fields.Boolean(default=True,
                            help="Set archive to true to hide the maintenance request without deleting it.")

    @api.onchange('patient_id')
    def set_caps(self):
        val = str(self.patient_id.name)
        self.patient_id.name = val.upper()

    @api.depends('invoice_ids', 'invoice_refund_ids',
                 'deposit_ids', 'deposit_refund_ids',
                 'invoice_ids.amount_total', 'invoice_refund_ids.amount_total',
                 'deposit_ids.amount', 'deposit_refund_ids.amount',
                 'document_ids')
    def _get_invoiced(self):
        for rec in self:
            invoices = rec.mapped('invoice_ids')
            refund_invoices = rec.mapped('invoice_refund_ids')
            deposits = rec.mapped('deposit_ids')
            refund_deposits = rec.mapped('deposit_refund_ids')
            impatients = self.env['medical.inpatient.registration'].search(
                [('patient_id', '=', rec.id)])
            rec.invoice_count = len(invoices.ids)
            rec.deposit_count = len(deposits.ids)
            rec.impatient_count = len(impatients.ids)
            rec.documents_count = len(rec.document_ids)
            rec.deposit_refund_count = len(refund_deposits.ids)
            rec.invoice_refund_count = len(refund_invoices.ids)
            rec.total_inv_amt = sum([inv.amount_total for inv in invoices.filtered(lambda so: so.state in ('posted'))])
            rec.total_inv_refund_amt = sum(
                [rinv.amount_total for rinv in refund_invoices.filtered(lambda so: so.state in ('posted'))])
            rec.total_deposit_amt = sum([d.amount for d in deposits.filtered(lambda so: so.state in ('posted'))])
            rec.total_deposit_refund_amt = sum(
                [r.amount for r in refund_deposits.filtered(lambda so: so.state in ('posted'))])

    def write(self, vals):
        res = super(medical_patient, self).write(vals)
        for rec in self:
            rec.partner_address_id.street = rec.address_1
            rec.partner_address_id.street2 = rec.address_2
            rec.partner_address_id.state_id = rec.state_id
            rec.partner_address_id.country_id = rec.country_id
            rec.partner_address_id.phone = rec.phone
            rec.partner_address_id.mobile = rec.mobile
            rec.partner_address_id.zip = rec.zip
        return res

    @api.model
    def create(self, val):
        appointment = self._context.get('appointment_id')
        res_partner_obj = self.env['res.partner']
        if appointment:
            val_1 = {'name': self.env['res.partner'].browse(val['patient_id']).name}
            patient = res_partner_obj.create(val_1)
            val.update({'patient_id': patient.id})
        if val.get('date_of_birth'):
            dt = val.get('date_of_birth')
            d1 = datetime.strptime(str(dt), "%Y-%m-%d").date()
            d2 = datetime.today().date()
            rd = relativedelta(d2, d1)
            age = str(rd.years) + "y" + " " + str(rd.months) + "m" + " " + str(rd.days) + "d"
            val.update({'age': age})

        # patient_id = self.env['ir.sequence'].next_by_code('medical.patient')
        # if patient_id:
        #     val.update({
        #         'name': patient_id,
        #     })
        result = super(medical_patient, self).create(val)
        return result

    def action_refund_deposit(self):
        action = self.env.ref('basic_hms.action_account_payments_payable').read()[0]
        action['domain'] = [('partner_id', '=', self.patient_id.id),
                            ('patient_id', '=', self.id),
                            ('payment_type', '=', 'outbound'),
                            ('state', '!=', 'cancelled')]

        action['context'] = {
            'from_billing_deposit': 1,
            'default_payment_type': 'outbound',
            'default_partner_type': 'supplier',
            'search_default_outbound_filter': 1,
            'res_partner_search_mode': 'supplier',
            'default_partner_id': self.patient_id.id,
            'default_patient_id': self.id,
        }
        return action

    def action_open_deposit(self):
        action = self.env.ref('basic_hms.action_account_deposit').read()[0]
        action['domain'] = [('partner_id', '=', self.patient_id.id),
                            ('patient_id', '=', self.id),
                            ('payment_type', '=', 'inbound'),
                            ('state', '!=', 'cancelled')]

        action['context'] = {
            'from_billing_deposit': 1,
            'default_payment_type': 'inbound',
            'default_partner_type': 'customer',
            'search_default_inbound_filter': 1,
            'res_partner_search_mode': 'customer',
            'default_partner_id': self.patient_id.id,
            'default_patient_id': self.id,
        }
        return action

    def action_refund_billing(self):
        action = self.env.ref('basic_hms.action_move_in_invoice_type').read()[0]
        action['domain'] = [('partner_id', '=', self.patient_id.id),
                            ('type', '=', 'out_refund'),
                            ('state', '!=', 'cancel'),
                            ('patient_id', '=', self.id)]
        action['context'] = {'from_billing_deposit': 1,
                             'default_type': 'out_refund',
                             'default_partner_id': self.patient_id.id,
                             'default_patient_id': self.id}
        return action

    def action_open_billing(self):
        action = self.env.ref('basic_hms.action_move_out_invoice_type').read()[0]
        action['domain'] = [('partner_id', '=', self.patient_id.id),
                            ('type', '=', 'out_invoice'),
                            ('state', '!=', 'cancel'),
                            ('patient_id', '=', self.id)]
        action['context'] = {'from_billing_deposit': 1,
                             'default_type': 'out_invoice',
                             'default_partner_id': self.patient_id.id,
                             'default_patient_id': self.id}
        return action


class PatientDocument(models.Model):
    _name = "medical.patient.documents"
    _description = 'Patient Documents'

    name = fields.Char("Name", required=True)
    patient_id = fields.Many2one("medical.patient", string="Patient")
    document = fields.Binary("Document", attachment=True)
    doc_name = fields.Char("Document Name")
    created_date = fields.Datetime("Created Date", default=fields.Datetime.now, readonly=True)


class IrAttachment(models.Model):
    _inherit = 'ir.attachment'

    @api.model
    def create(self, vals):
        res = super(IrAttachment, self).create(vals)
        if res.res_model == 'medical.patient.documents' and res.res_field == 'document':
            res.public = True
        return res

# vim=expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
