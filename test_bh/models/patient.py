# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from datetime import date, datetime
from dateutil.relativedelta import relativedelta


class MedicalPatient(models.Model):
    _name = 'medical.patient'
    _rec_name = 'name'

    def start_treatment(self):
        return

    @api.onchange('patient_id')
    def _onchange_patient(self):
        '''
        The purpose of the method is to define a domain for the available
        purchase orders.
        '''
        address_id = self.patient_id
        self.partner_address_id = address_id

    @api.depends('date_of_birth')
    def onchange_age(self):
        print("called")
        for rec in self:
            if rec.date_of_birth:
                d1 = rec.date_of_birth
                d2 = datetime.today().date()
                rd = relativedelta(d2, d1)
                rec.age = str(rd.years) + "y" + " " + str(rd.months) + "m" + " " + str(rd.days) + "d"
            else:
                rec.age = "No Date Of Birth!!"

    # demographic Data
    patient_id = fields.Many2one('res.partner', string="Patient", required=True)
    name = fields.Char(string='ID', readonly=True)
    last_name = fields.Char('Last Name')
    date_of_birth = fields.Date(string="Date of Birth", store=True)
    photo = fields.Binary(string="Picture")
    sex = fields.Selection([('m', 'Male'), ('f', 'Female')], string="Sex")
    age = fields.Char(compute=onchange_age, string="Patient Age", store=True)
    marital_status = fields.Selection(
        [('s', 'Single'), ('m', 'Married'), ('w', 'Widowed'), ('d', 'Divorced'), ('x', 'Seperated')],
        string='Marital Status')
    partner_address_id = fields.Many2one('res.partner', string="Address")
    occupation = fields.Char('Occupation')
    mobile = fields.Char("Tel. No.")
    phone = fields.Char("Phone No. 1")
    mobile_1 = fields.Char("Phone No. 2")
    mobile_2 = fields.Char("Phone No. 3")
    referring_doctor = fields.Char('Referring Doctor')
    company_id = fields.Many2one('res.company', 'Company', required=True, index=True,
                                 default=lambda self: self.env.company)
    currency_id = fields.Many2one('res.currency', string='Currency', required=True, readonly=True,
                                  default=lambda self: self.env.company.currency_id)
    address_1 = fields.Char('Address')
    address_2 = fields.Char('Address')
    zip = fields.Char("Zip")
    city = fields.Char('City')
    state_id = fields.Many2one("res.country.state", string='State', ondelete='restrict',
                               domain="[('country_id', '=?', country_id)]",
                               default=lambda s: s.env['res.country.state'].search([('name', '=', 'Gujarat')], limit=1))
    country_id = fields.Many2one('res.country', string='Country', ondelete='restrict',
                                 default=lambda s: s.env['res.country'].search([('name', '=', 'India')], limit=1))
    hight_light = fields.Char('Hight Light')

    # cardiac history
    cardiac_history = fields.Text('Cardiac History')
    icu_stay = fields.Text('ICU Stay : Eventful/Uneventful')
    patient_cholesterol_ids = fields.One2many('patient.cholesterol', 'medical_patient_id', 'Cholesterol')
    patient_diabetes_ids = fields.One2many('patient.diabetes', 'medical_patient_id', 'Diabetes')
    patient_medications_ids = fields.One2many('patient.medications', 'medical_patient_id', 'Medications')
    is_chol_bool = fields.Boolean('Cholesterol')
    is_diabetes_bool = fields.Boolean('Diabetes')

    # Stress
    is_stress = fields.Boolean('Do You Feel Under Stress Often ?')
    source_of_stress = fields.Text('Source of Stress')
    rating_stress = fields.Selection([('1', '1'),
                                      ('2', '2'),
                                      ('3', '3'),
                                      ('4', '4'),
                                      ('5', '5'),
                                      ('6', '6'),
                                      ('7', '7'),
                                      ('8', '8'),
                                      ('9', '9'),
                                      ('10', '10')],
                                     string="Rating of Stress on Scale of 1 to 10")

    # Medical /Surgery History
    diabetes_mellitus = fields.Boolean('Diabetes Mellitus')
    diabetes_type = fields.Selection([('1', 'Type I'),
                                      ('2', 'Type II')],
                                     string='Diabetes Type')

    hin = fields.Boolean('HIN')
    hin_years = fields.Char('Since How Long Years')

    ckd = fields.Boolean('CKD')
    ckd_years = fields.Char('Since How Long Years')

    leg_fracture = fields.Boolean('Leg Fracture')
    fracture_text = fields.Char('Facture Details')

    leg_surgery = fields.Boolean('Leg Surgery')
    surgery_text = fields.Char('Surgery Details')

    # sign and symptoms
    dyspnea = fields.Boolean('Dyspnea')
    nyha_class = fields.Selection([('1', 'I'),
                                   ('2a', 'IIA'),
                                   ('2b', 'IIB'),
                                   ('3', 'III'),
                                   ('4', 'IV')],
                                  string='NYHA Class')
    angina = fields.Boolean('Angina')
    interval_angina = fields.Selection([('day', 'Days'),
                                        ('week', 'Week'),
                                        ('month', 'Month')],
                                       string='NYHA Class')
    no_angina = fields.Selection([('1', '1'),
                                  ('2', '2'),
                                  ('3', '3'),
                                  ('4', '4'),
                                  ('5', '5'),
                                  ('6', '6'),
                                  ('7', '7'),
                                  ('8', '8'),
                                  ('9', '9'),
                                  ('10', '10')],
                                 string="No. of Angina Episodes/Day")

    # nutrition
    veg = fields.Boolean('Veg')
    non_veg = fields.Boolean('Non-Veg:')
    oil_consumption = fields.Selection([('low', 'Low'),
                                        ('medium', 'Medium'),
                                        ('high', 'High')],
                                       string='Oil Consumption')

    ghee_consumption = fields.Selection([('low', 'Low'),
                                         ('medium', 'Medium'),
                                         ('high', 'High')],
                                        string='ghee Consumption')
    # Alcohol
    is_drinking = fields.Boolean("Is Drinking")
    drinks_per_peg = fields.Integer("Pegs per Week")

    # exercise
    is_exercise = fields.Boolean("Doing Exercise")
    exercise_type = fields.Text('Type of Exercise')
    how_ofter_exercise = fields.Text('How Ofter')
    exercise_duration = fields.Text('Duration')
    physical_limitations = fields.Text('Physical Limitations')

    # physical examination
    height = fields.Float("Height / cms")
    weight = fields.Float("Weight / Kg")
    bmi = fields.Float("BMI / kg/ meter square")
    pulse = fields.Float("pulse / bpm")
    blood_pressure = fields.Float("Blood Pressure / mmHg")
    auscultatory_finding = fields.Text('Auscultatory Finding')
    peripheral_pulses = fields.Text('Peripheral Pulses')

    # medications
    antiplatelet_agent = fields.Boolean("Antiplatelet Agent")
    ace_1_or_arb = fields.Boolean("ACE-1 Or ARB")
    beta_blocker = fields.Boolean("B-Blocker")
    statin = fields.Boolean("Statin")
    anti_anginal = fields.Boolean("Anti-Anginal")

    # 6mwt
    target_hr = fields.Char("TARGET HR")
    pre_date = fields.Date(string="Date")
    post_date = fields.Date(string="Date")

    pre_hr = fields.Char("PRE HR")
    post_hr = fields.Char("POST HR")

    pre_bp = fields.Char("PRE BP")
    post_bp = fields.Char("POST BP")

    ex_hr_1_min_pre = fields.Integer("Ex.Hr 1 Min")
    ex_hr_2_min_pre = fields.Integer("Ex.Hr 2 Min")
    ex_hr_3_min_pre = fields.Integer("Ex.Hr 3 Min")

    ex_hr_1_min_post = fields.Integer("Ex.Hr 1 Min")
    ex_hr_2_min_post = fields.Integer("Ex.Hr 2 Min")
    ex_hr_3_min_post = fields.Integer("Ex.Hr 3 Min")

    recovery_hr_1_min_pre = fields.Integer("Recovery.Hr 1 Min")
    recovery_hr_2_min_pre = fields.Integer("Recovery.Hr 2 Min")
    recovery_hr_3_min_pre = fields.Integer("Recovery.Hr 3 Min")

    recovery_hr_1_min_post = fields.Integer("Recovery.Hr 1 Min")
    recovery_hr_2_min_post = fields.Integer("Recovery.Hr 2 Min")
    recovery_hr_3_min_post = fields.Integer("Recovery.Hr 3 Min")

    recovery_bp_1_min_pre = fields.Integer("Recovery.bp 1 Min")
    recovery_bp_2_min_pre = fields.Integer("Recovery.bp 2 Min")
    recovery_bp_3_min_pre = fields.Integer("Recovery.bp 3 Min")

    recovery_bp_1_min_post = fields.Integer("Recovery.bp 1 Min")
    recovery_bp_2_min_post = fields.Integer("Recovery.bp 2 Min")
    recovery_bp_3_min_post = fields.Integer("Recovery.bp 3 Min")

    distance_pre = fields.Integer("Distance")
    distance_post = fields.Integer("Distance")

    rpe_pre = fields.Integer("RPE")
    rpe_post = fields.Integer("RPE")

    # diagnosis
    cad = fields.Char("CAD")
    chf = fields.Char("CHF")
    refractory_angina = fields.Char("Refractory Angina")

    mi = fields.Boolean("MI")
    mi_date = fields.Date(string='Date of MI')

    cabg = fields.Boolean("CABG")
    cabg_date = fields.Date(string='Date of CABG')
    cabg_text = fields.Char("CABG text")

    ptca = fields.Boolean("PTCA")
    ptca_date = fields.Date(string='Date of PTCA')
    ptca_text = fields.Char("PTCA text")

    medical_mx = fields.Boolean("Medical MX")
    medical_mx_text = fields.Char("Medical MX text")

    # cardiac test and procedures
    ecg_ids = fields.One2many('patient.ecg', 'medical_patient_id', 'ECG')
    echo_ids = fields.One2many('patient.echo', 'medical_patient_id', 'Echo')
    stress_echo_ids = fields.One2many('patient.stress_echo', 'medical_patient_id', 'Stress Echo / Thallium Echo')
    angiography_ids = fields.One2many('patient.angiography', 'medical_patient_id', 'Cardiac Cath / Angiography ')
    ptca_stend_ids = fields.One2many('patient.ptca_stent', 'medical_patient_id', 'PTCA / Stent ')
    cabg_ids = fields.One2many('patient.cabg', 'medical_patient_id', 'CABG')
    other_test_ids = fields.One2many('patient.other_tests', 'medical_patient_id', 'Other Tests')
    treatment_chart_ids = fields.One2many('patient.treatment.chart', 'medical_patient_id', 'ECG')

    # Indications Check List

    con_indication_1 = fields.Boolean("Uncontrolled Ventricular/Supraventricular arrhythmias", default=True)
    con_indication_2 = fields.Boolean(
        "Decompensated heart Failure (raised central venous pressure > 7mmHg or Pulmonary oedema)", default=True)
    con_indication_3 = fields.Boolean("Severe Pulmonary hypertension(MRsn pulm. artery pressure > 50mmHg)",
                                      default=True)
    con_indication_4 = fields.Boolean("Uncontrolled systemic hypertension", default=True)
    con_indication_5 = fields.Boolean("Severe aortic insufficiency", default=True)
    con_indication_6 = fields.Boolean(
        "Severe Lower Extremity peripheral vascular diesase with rest claudication or no -healing ulcers", default=True)
    con_indication_7 = fields.Boolean("Aortic aneurysm surgical repair", default=True)
    con_indication_8 = fields.Boolean("Current Or recent  (< 2 months) Lower extremity thyombophlebitis", default=True)
    con_indication_9 = fields.Boolean("Lower extermity deep vein thrombosis", default=True)
    con_indication_10 = fields.Boolean("Bleeding diathesis or on warfarin with INR > 3.0", default=True)
    con_indication_11 = fields.Boolean("Pregnancy", default=True)

    # indication_1 = fields.Boolean("CHROMIC CAD \n"
    #                               "(a). Surgery / PTCA not contemplated \n"
    #                               "1. Patient refused due to.")
    # indication_2 = fields.Boolean("Diffuse Distal Disease")
    # indication_3 = fields.Boolean("Systemic Disorder-High Risk Surgery")
    # indication_4 = fields.Boolean("LV Dysfunction - High Risk CABG; EF < 35%")

    # Final Diagnosis
    final_html = fields.Html(string='Final Diagnosis')

    @api.model
    def create(self, val):
        if val.get('date_of_birth'):
            dt = val.get('date_of_birth')
            d1 = datetime.strptime(str(dt), "%Y-%m-%d").date()
            d2 = datetime.today().date()
            rd = relativedelta(d2, d1)
            age = str(rd.years) + "y" + " " + str(rd.months) + "m" + " " + str(rd.days) + "d"
            val.update({'age': age})

        patient_name = self.env['ir.sequence'].next_by_code('medical.patient')
        print("patient_name", patient_name)
        if patient_name:
            val.update({
                'name': patient_name,
            })
        result = super(MedicalPatient, self).create(val)
        return result

    def write(self, vals):
        res = super(MedicalPatient, self).write(vals)
        for rec in self:
            rec.partner_address_id.image_1920 = rec.photo
            rec.partner_address_id.street = rec.address_1
            rec.partner_address_id.street2 = rec.address_2
            rec.partner_address_id.state_id = rec.state_id
            rec.partner_address_id.country_id = rec.country_id
            rec.partner_address_id.phone = rec.phone
            rec.partner_address_id.mobile = rec.mobile
            rec.partner_address_id.zip = rec.zip
        return res


class PatientCholesterol(models.Model):
    _name = 'patient.cholesterol'
    _rec_name = 'total_chol'

    medical_patient_id = fields.Many2one('medical.patient', string="Patient")

    date = fields.Date(string='Date', default=datetime.now())
    total_chol = fields.Char('Total Cholesterol')
    ldl = fields.Char('LDL')
    hdl = fields.Char('HDL')
    triglycerides = fields.Char('Triglycerides')
    other_tests = fields.Char('Other_tests')
    medications = fields.Char('Medications')


class PatientDiabetes(models.Model):
    _name = 'patient.diabetes'

    medical_patient_id = fields.Many2one('medical.patient', string="Patient")

    date = fields.Date(string='Date', default=datetime.now())
    rbs = fields.Char('RBS')
    fast_blood_suger = fields.Char('Fast Blood Suger')
    ppbs = fields.Char('PPBS')
    hba1c = fields.Char('HBA 1c')
    how_long = fields.Char('Since How Long Years')
    medications = fields.Char('Medications')


class PatientMedications(models.Model):
    _name = 'patient.medications'

    medical_patient_id = fields.Many2one('medical.patient', string="Patient")

    date = fields.Date(string='Date', default=datetime.now())
    name = fields.Char('Name of Medication')
    dose = fields.Char('Dose')
    frequency = fields.Char('Frequency')


class PatientTreatmentChart(models.Model):
    _name = 'patient.treatment.chart'

    medical_patient_id = fields.Many2one('medical.patient', string="Patient")
    sequence = fields.Integer('Sequence')
    date = fields.Date(string='Date', default=datetime.now())
    pre_bp = fields.Char("PRE BP")
    hr = fields.Char("HR")
    time = fields.Char("TIME")
    diagnosis_systolic_aug_ratio = fields.Integer("Diagnosis Systolic Augmentation Ratio")
    post_bp = fields.Char("POST BP")
    post_hr = fields.Char("POST HR")
    weight = fields.Integer("Weight")
    rbs = fields.Integer("RBS")
    complaints = fields.Char("Complaints")
