# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
import math


class PatientConsultationDetail(models.Model):
    _name = 'patient.consultation.detail'
    _description = 'Patient Consultation Information'

    name = fields.Char(related='partner_id.name', store=True)
    partner_id = fields.Many2one('res.partner', string='Patient')
    birth_date = fields.Date(related='partner_id.birth_date', store=True, string='DOB')
    age = fields.Char(related='partner_id.age', store=True, string='Age')
    age_years = fields.Integer(related='partner_id.age_years', store=True, string='Age Years')
    gender = fields.Selection(related='partner_id.gender', store=True, string='Sex')
    file_number = fields.Char(related='partner_id.file_number', store=True, string='Sequence')
    reference_id = fields.Many2one(related='partner_id.reference_id', store=True, string="Reference")
    occupation_id = fields.Many2one(related='partner_id.occupation_id', store=True, string="Occupation")
    mobile = fields.Char(related='partner_id.mobile', store=True, string='Mobile')
    # first_name = fields.Char(related='partner_id.first_name', store=True)
    # last_name = fields.Char(related='partner_id.last_name', store=True)

    parent_id = fields.Many2one('patient.consultation.detail')
    child_ids = fields.One2many('patient.consultation.detail', 'parent_id')
    is_compelete = fields.Boolean('Complete Consultation')

    @api.multi
    def complete_consultation(self):
        self.is_compelete = 1

    # page-1
    cardiac_history = fields.Text("Cardiac History")
    icu_stay = fields.Text("ICU Stay")

    # page-2
    medical_surgical_history = fields.Text("Medical/Surgical History")
    signs_symptoms = fields.Text("Signs / Symptoms")

    # page3
    nyha_class = fields.Selection([('a', 'Class I'),
                                   ('b', 'Class IIa'),
                                   ('c', 'Class IIb'),
                                   ('d', 'Class IIIa'),
                                   ('e', 'Class IIIb'),
                                   ('f', 'Class IV'),
                                   ('g', 'Not Heart Failure')], string='NYHA Class')

    ccs_angina_class = fields.Selection([('a', 'I'),
                                         ('b', 'II'),
                                         ('c', 'III'),
                                         ('d', 'IV'), ], string="CCS Angina Class")
    # no_hf = fields.Boolean('Not a HF Patient')
    no_of_angina_episodes = fields.Selection([('day', 'Day'),
                                              ('week', 'Week'),
                                              ('month', 'Month'),
                                              ], string="No of Angina Episodes ")
    no_of_sublingual_nitrate_spray = fields.Selection([('day', 'Day'),
                                                       ('week', 'Week'),
                                                       ('month', 'Month'),
                                                       ], string="No of Sublingual Nitrate Spray")
    # spray_time_type = fields.Selection([('week', 'Week'),
    #                                     ('day', 'Day')], string='Spray time type')
    no_of_spray = fields.Integer('No of spray')
    diagnosis = fields.Selection([('cad', 'CAD'),
                                  ('heart_failure', 'Heart Failure'),
                                  ('refractory', 'Refractory'),
                                  ('angina_other', 'Angina Other')], string="Diagnosis")
    other_angina_diagnosis = fields.Char('Oteher angina diagnosis')
    date_of_diagnosis = fields.Date("Date of diagnosis")
    mi = fields.Selection([("yes", "Yes"), ("no", "No")], string="MI")
    date_of_mi = fields.Date('Date of MI')
    cabg_procedure = fields.Selection([("yes", "Yes"), ("no", "No")], string="CABG Procedure")
    ptca_procedure = fields.Selection([("yes", "Yes"), ("no", "No")], string="PTCA")
    madical_management_procedure = fields.Selection([("yes", "Yes"), ("no", "No")], string="Medical Management")
    history_ccf_other = fields.Text('History of CCF/Others')

    # Cardiac Tests & Procedures:
    stress_date = fields.Date('Stress Report Date')
    stress_test = fields.Text("Stress Test")
    echo = fields.Text("Echo")
    stress_echo_thallium_echo = fields.Text("Stress Echo/Thallium Echo")
    cardiac_cath = fields.Text("Cardiac Cath")
    ptca_stent = fields.Text('PTCA/ Stent')
    cabg = fields.Text('CABG')
    other_tests_procedures = fields.Text("Other Tests/ Procedures")

    # CAD Risk Factors
    # Family History of CAD
    father_diabetes_mellitus = fields.Selection([("yes", "Yes"), ("no", "No")], string="Father Diabetes Mellitus")
    mother_diabetes_mellitus = fields.Selection([("yes", "Yes"), ("no", "No")], string="Mother Diabetes Mellitus")
    sibling_diabetes_mellitus = fields.Selection([("yes", "Yes"), ("no", "No")], string="Sibling Diabetes Mellitus")
    father_diabetes_mellitus_age = fields.Integer("Father Diabetes Mellitus Age")
    mother_diabetes_mellitus_age = fields.Integer("Mother Diabetes Mellitus Age")
    sibling_diabetes_mellitus_age = fields.Integer("Sibiling Diabetes Mellitus Age")

    father_hypertension = fields.Selection([("yes", "Yes"), ("no", "No")], string="Father Hypertension")
    mother_hypertension = fields.Selection([("yes", "Yes"), ("no", "No")], string="Mother Hypertension")
    sibling_hypertension = fields.Selection([("yes", "Yes"), ("no", "No")], string="Sibling Hypertension")
    father_hypertension_age = fields.Integer("Father Hypertension Age")
    mother_hypertension_age = fields.Integer("Mother Hypertension Age")
    sibling_hypertension_age = fields.Integer("Sibling Hypertension Age")

    father_colonary_artery_disease = fields.Selection([("yes", "Yes"), ("no", "No")],
                                                      string="Father Colonary Artery Disease")
    mother_colonary_artery_disease = fields.Selection([("yes", "Yes"), ("no", "No")],
                                                      string="Mother Colonary Artery Disease")
    sibling_colonary_artery_disease = fields.Selection([("yes", "Yes"), ("no", "No")],
                                                       string="Sibling Colonary Artery Disease")
    father_colonary_artery_disease_age = fields.Integer("Father Colonary Artery Disease Age")
    mother_colonary_artery_disease_age = fields.Integer("Mother Colonary Artery Disease Age")
    sibling_colonary_artery_disease_age = fields.Integer("Sibling Colonary Artery Disease Age")

    father_stroke = fields.Selection([("yes", "Yes"), ("no", "No")], string="Father Stroke")
    mother_stroke = fields.Selection([("yes", "Yes"), ("no", "No")], string="Mother Stroke")
    sibling_stroke = fields.Selection([("yes", "Yes"), ("no", "No")], string="Sibling Stroke")
    father_stroke_age = fields.Integer("Father Stroke Age")
    mother_stroke_age = fields.Integer("Mother Stroke Age")
    sibling_stroke_age = fields.Integer("Sibling Stroke Age")

    # Smoking / Tobacco
    current_smoking_tabacco = fields.Selection([("yes", "Yes"), ("no", "No")], default='yes',
                                               string='Current Smoking/ Tobacco')
    smoking_tabacco_per_day = fields.Integer('How many per day')
    smoking_tabacco_desire_quit = fields.Selection([("yes", "Yes"), ("no", "No")], string='Desire to quit')
    smoking_tabacco_date_to_quit = fields.Date('Date of quit smoke')
    past_smoking_tabacco = fields.Selection([("yes", "Yes"), ("no", "No")], default='no',
                                            string='Past history Smoking/ Tobacco')
    past_smoking_tabacco_per_day = fields.Integer('How many per day past')
    smoking_tabacco_since_how_long = fields.Integer('Smoking/ Tobacco Since')

    # Blood Pressure
    hypertension = fields.Boolean('Hypertension')
    hypertension_since_how_long = fields.Integer('Hypertension Since how long')
    hypertension_medication = fields.Text('Hypertension Medications')

    # Cholesterol
    cholesterol = fields.Boolean('Cholesterol')
    patient_cholesterol_ids = fields.One2many('patient.cholesterol', 'patient_consultation_id',
                                              string='Patient Cholesterol Records', copy=True)

    # Diabetes
    patient_diabetes = fields.Boolean('Diabetes')
    diabetes_since_how_long = fields.Integer('Diabetes Since how long')
    diabetes_medication = fields.Text('Diabetes Medications')
    patient_diabetes_ids = fields.One2many('patient.diabetes', 'patient_consultation_id',
                                           string='Patiet Diabetes Records')

    # Stress
    feel_stress = fields.Boolean('Under Stress')
    stress_rating = fields.Selection([('1', '1'), ('2', '2'), ('3', '3'),
                                      ('4', '4'), ('5', '5'), ('6', '6'),
                                      ('7', '7'), ('8', '8'), ('9', '9'),
                                      ('10', '10')], string='Stress Rating', default='1')
    stress_family_related = fields.Boolean('Family stress')
    stress_business_related = fields.Boolean('Business stress')
    stress_finance_related = fields.Boolean('Finance stress')
    stress_other = fields.Boolean('Other')
    other_stress = fields.Text('Other stress')

    # Nutrition
    nutration_veg_non_veg = fields.Selection([('veg', 'Veg'), ('non_veg', "Non-Veg")], string="Nutrition")
    cooking_medium = fields.Char("Cooking Medium")
    consumption_oil_ghee = fields.Selection([('low', 'Low'), ('medium', "Medium"), ('high', "High")],
                                            string="Consumption of Oil/ Ghee")

    # Alcohol
    alcohol = fields.Boolean('Alcohol')
    alcohol_consumption = fields.Selection(
        [('regular', 'Regular'), ('occassionally', "Occassionally"), ('very_rare', "Very Rare")],
        string="Alcohol Consumption")
    drinks_per_week = fields.Integer("Drinks per week")

    # Exercise
    exercise = fields.Boolean('Exercise')
    type_of_exercise = fields.Text('Type of exercise')
    how_often_exercise = fields.Integer('How often')
    exercise_duration = fields.Float('Durartion')
    physical_limitation = fields.Text('Physical Limitations')

    # Physical Examination
    height = fields.Float(string="Height", default=1.0)
    height_uom = fields.Many2one(string="Height UoM",
                                 comodel_name="uom.uom",
                                 default=lambda self: self.env.ref('uom.product_uom_cm', False),
                                 # default=lambda s: s.env['res.lang'].default_uom_by_category('Height'),
                                 domain=lambda self: [('id', '=', self.env.ref('uom.product_uom_cm').id)])

    weight = fields.Float(string="Weight", default=1.0)
    weight_uom = fields.Many2one(
        string="Weight UoM",
        comodel_name="uom.uom",
        default=lambda self: self.env.ref('uom.product_uom_kgm', False),
        # default=lambda s: s.env['res.lang'].default_uom_by_category('Weight'),
        domain=lambda self: ['|', ('id', '=', self.env.ref('uom.product_uom_lb').id),
                             ('id', '=', self.env.ref('uom.product_uom_kgm').id),
                             ])

    bmi = fields.Float(string="BMI", compute='_compute_bmi_calculation')
    bmi_status = fields.Selection(string="BMI Status",
                                  selection=[('under_weight', 'Under Weight'),
                                             ('normal_weight', 'Normal weight'),
                                             ('over_weight', 'Overweight'),
                                             ('obesity', 'Obesity')], compute='_compute_bmi_status'
                                  )

    @api.multi
    def _compute_bmi_calculation(self):
        kg = False
        m = False
        for rec in self:
            if rec.weight == 0 or rec.height == 0:
                rec.bmi = 0
            elif rec.weight_uom.id == self.env.ref('uom.product_uom_lb').id:
                kg = (rec.weight * 0.453592)
                m = (rec.height / 100.0)
                rec.bmi = kg / (m * m)
            else:
                m = (rec.height / 100.0)
                rec.bmi = rec.weight / (m * m)

    @api.multi
    def _compute_bmi_status(self):
        for rec in self:
            if round(rec.bmi, 1) < 18.5:
                rec.bmi_status = 'under_weight'
            elif (round(rec.bmi, 1) >= 18.5) & (round(rec.bmi, 1) <= 24.9):
                rec.bmi_status = 'normal_weight'
            elif (round(rec.bmi, 1) >= 25) & (round(rec.bmi, 1) <= 29.9):
                rec.bmi_status = 'over_weight'
            elif round(rec.bmi, 1) >= 30:
                rec.bmi_status = 'obesity'

    # #####
    auscultatory_finding = fields.Char('Auscultatory findings')
    pulse = fields.Float('Pulse')
    carotid_artery_lt = fields.Selection([('1p', '1+'), ('2p', '2+'),
                                          ('3p', '3+'), ('4p', '4+'),
                                          ('5p', '5+')], string='Carotid Artery Left')
    carotid_artery_rt = fields.Selection([('1p', '1+'), ('2p', '2+'),
                                          ('3p', '3+'), ('4p', '4+'),
                                          ('5p', '5+')], string='Carotid Artery Right')

    brachial_artery_lt = fields.Selection([('1p', '1+'), ('2p', '2+'),
                                           ('3p', '3+'), ('4p', '4+'),
                                           ('5p', '5+')], string='Brachial Artery Left')
    brachial_artery_rt = fields.Selection([('1p', '1+'), ('2p', '2+'),
                                           ('3p', '3+'), ('4p', '4+'),
                                           ('5p', '5+')], string='Brachial Artery Right')

    radial_artery_lt = fields.Selection([('1p', '1+'), ('2p', '2+'),
                                         ('3p', '3+'), ('4p', '4+'),
                                         ('5p', '5+')], string='Radial Artery Left')

    radial_artery_rt = fields.Selection([('1p', '1+'), ('2p', '2+'),
                                         ('3p', '3+'), ('4p', '4+'),
                                         ('5p', '5+')], string='Radial Artery Right')

    femoral_artery_lt = fields.Selection([('1p', '1+'), ('2p', '2+'),
                                          ('3p', '3+'), ('4p', '4+'),
                                          ('5p', '5+')], string='Femoral Artery Left')

    femoral_artery_rt = fields.Selection([('1p', '1+'), ('2p', '2+'),
                                          ('3p', '3+'), ('4p', '4+'),
                                          ('5p', '5+')], string='Femoral Artery Right')

    popliteal_artery_lt = fields.Selection([('1p', '1+'), ('2p', '2+'),
                                            ('3p', '3+'), ('4p', '4+'),
                                            ('5p', '5+')], string='Popliteal Artery Left')
    popliteal_artery_rt = fields.Selection([('1p', '1+'), ('2p', '2+'),
                                            ('3p', '3+'), ('4p', '4+'),
                                            ('5p', '5+')], string='Popliteal Artery Right')

    tibial_artery_lt = fields.Selection([('1p', '1+'), ('2p', '2+'),
                                         ('3p', '3+'), ('4p', '4+'),
                                         ('5p', '5+')], string='Tibial Artery Left')
    tibial_artery_rt = fields.Selection([('1p', '1+'), ('2p', '2+'),
                                         ('3p', '3+'), ('4p', '4+'),
                                         ('5p', '5+')], string='Tibial Artery Right')

    dorsalis_pedis_lt = fields.Selection([('1p', '1+'), ('2p', '2+'),
                                          ('3p', '3+'), ('4p', '4+'),
                                          ('5p', '5+')], string='Dorsalis Pedis Left')

    dorsalis_pedis_rt = fields.Selection([('1p', '1+'), ('2p', '2+'),
                                          ('3p', '3+'), ('4p', '4+'),
                                          ('5p', '5+')], string='Dorsalis Pedis Right')

    # Medications
    drug_allergies_side_effects = fields.Boolean('Any drug allergies or side effects')
    drug_allergies_side_effects_name = fields.Char('Name of drug allergies or side effects')
    drug_allergies_side_effects_ids = fields.One2many('patient.drug.allergie', 'patient_consultation_id',
                                                      string='Drug allergies or side effects')
    antiplatelet_agent = fields.Boolean('Antiplatelet Agent')
    ace_i_arb = fields.Boolean('ACE-I or ARB')
    b_blocker = fields.Boolean('B-Blocker')
    statin = fields.Boolean('Statin')

    # Contra-indication checklist
    uncontrolled_ventricular = fields.Selection([("yes", "Yes"), ("no", "No")],
                                                string="Uncontrolled ventricular/superaventricular arrhymias")
    decompensated_heart_failure = fields.Selection([("yes", "Yes"), ("no", "No")],
                                                   string="Decompensated heart failure (raised central venous "
                                                          "pressure >7mmHg or pulmonary oedema)")
    severe_pulmonary_hypertension = fields.Selection([("yes", "Yes"), ("no", "No")],
                                                     string="Severe pulmonary hypertension (Mean pulm. artery "
                                                            "pressure >50mmHg)")
    uncontrolled_systemic_hypertension = fields.Selection([("yes", "Yes"), ("no", "No")],
                                                          string="Uncontrolled systemic hypertension (>180/110mmHg)")
    severe_aortic_insufficiency = fields.Selection([("yes", "Yes"), ("no", "No")],
                                                   string="severe aortic insufficiency")
    severe_lower_extremity_peripheral_vascular_disease = fields.Selection([("yes", "Yes"), ("no", "No")],
                                                                          string="Severe lower extremity peripheral "
                                                                                 "vascular disease with rest "
                                                                                 "claudication or non-healing ulcers")
    aortic_aneurysm = fields.Selection([("yes", "Yes"), ("no", "No")],
                                       string="Aortic aneurysm requiring surgical repair")
    recent_lower_extremity_thrombophlebitis = fields.Selection([("yes", "Yes"), ("no", "No")],
                                                               string='Current or recent (<2 months) lower extremity '
                                                                      'thrombophlebitis')
    lower_extremity_deep_vein_thrombosis = fields.Selection([("yes", "Yes"), ("no", "No")],
                                                            string="Lower extremity deep vein thrombosis")
    bleeding_diathesis_on_warfarin = fields.Selection([("yes", "Yes"), ("no", "No")],
                                                      string="Bleeding diathesis or on warfarin with INR>3.0")
    pragnancy = fields.Selection([("yes", "Yes"), ("no", "No")],
                                 string="Pragnancy")

    # Indications Check list

    # Six Minutes Walk Test
    pre_eecp_date = fields.Date('Pre EECP Date')
    post_eecp_date = fields.Date('Post EECP Date')
    pre_hr = fields.Char('Pre HR')
    post_hr = fields.Char('Post HR')
    pre_bp = fields.Char('Pre BP')
    post_bp = fields.Char('Post BP')
    # # EX.HR
    pre_one_min_ex_hr = fields.Char('Pre 1 Min EX.HR')
    pre_two_min_ex_hr = fields.Char('Pre 2 Min EX.HR')
    pre_three_min_ex_hr = fields.Char('Pre 3 Min EX.HR')
    post_one_min_ex_hr = fields.Char('Post 1 Min EX.HR')
    post_two_min_ex_hr = fields.Char('Post 2 Min EX.HR')
    post_three_min_ex_hr = fields.Char('Post 3 Min EX.HR')
    # # Recovery HR
    pre_one_min_recovery_hr = fields.Char('Pre 1 Min Recovery HR')
    pre_two_min_recovery_hr = fields.Char('Pre 2 Min Recovery HR')
    pre_three_min_recovery_hr = fields.Char('Pre 3 Min Recovery HR')
    post_one_min_recovery_hr = fields.Char('Post 1 Min Recovery HR')
    post_two_min_recovery_hr = fields.Char('Post 2 Min Recovery HR')
    post_three_min_recovery_hr = fields.Char('Post 3 Min Recovery HR')
    # # Recovery BP
    pre_one_min_recovery_bp = fields.Char('Pre 1 Min Recovery BP')
    pre_two_min_recovery_bp = fields.Char('Pre 2 Min Recovery BP')
    pre_three_min_recovery_bp = fields.Char('Pre 3 Min Recovery BP')
    post_one_min_recovery_bp = fields.Char('Post 1 Min Recovery BP')
    post_two_min_recovery_bp = fields.Char('Post 2 Min Recovery BP')
    post_three_min_recovery_bp = fields.Char('Post 3 Min Recovery BP')
    # # Distance
    pre_distance = fields.Float('Pre Distance')
    post_distance = fields.Float('Post Distance')
    # # RPE
    pre_rpe = fields.Float('Pre RPE')
    post_rpe = fields.Float('Post RPE')

    # Treatment Chart
    patient_treatment_chart_ids = fields.One2many('patient.treatment.chart', 'patient_consultation_id',
                                                  string='Patient Treatment Chart')
