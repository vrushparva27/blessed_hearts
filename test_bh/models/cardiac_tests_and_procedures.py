# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from datetime import date, datetime


class PatientEcg(models.Model):
    _name = 'patient.ecg'
    date = fields.Date(string='Date', default=datetime.now())
    medical_patient_id = fields.Many2one('medical.patient', string="Patient")
    documents = fields.Binary('Documents', attachement=True)
    text = fields.Char('Remarks')


class PatientEcho(models.Model):
    _name = 'patient.echo'
    date = fields.Date(string='Date', default=datetime.now())
    medical_patient_id = fields.Many2one('medical.patient', string="Patient")
    documents = fields.Binary('Documents', attachement=True)
    text = fields.Char('Remarks')


class PatientStressEcho(models.Model):
    _name = 'patient.stress_echo'

    date = fields.Date(string='Date', default=datetime.now())
    medical_patient_id = fields.Many2one('medical.patient', string="Patient")
    documents = fields.Binary('Documents', attachement=True)
    text = fields.Char('Remarks')


class PatientAngiography(models.Model):
    _name = 'patient.angiography'
    date = fields.Date(string='Date', default=datetime.now())
    medical_patient_id = fields.Many2one('medical.patient', string="Patient")
    documents = fields.Binary('Documents', attachement=True)
    text = fields.Char('Remarks')


class PatientPtcastent(models.Model):
    _name = 'patient.ptca_stent'

    date = fields.Date(string='Date', default=datetime.now())
    medical_patient_id = fields.Many2one('medical.patient', string="Patient")
    documents = fields.Binary('Documents', attachement=True)
    text = fields.Char('Remarks')


class PatientCabg(models.Model):
    _name = 'patient.cabg'
    medical_patient_id = fields.Many2one('medical.patient', string="Patient")
    documents = fields.Binary('Documents', attachement=True)
    text = fields.Char('Remarks')


class PatientOthertests(models.Model):
    _name = 'patient.other_tests'
    medical_patient_id = fields.Many2one('medical.patient', string="Patient")
    documents = fields.Binary('Documents', attachement=True)
    text = fields.Char('Remarks')


class PatientCholesterol(models.Model):
    _name = 'patient.cholesterol'
    _rec_name = 'total_chol'

    medical_patient_id = fields.Many2one('medical.patient', string="Patient")

    date = fields.Date(string='Date', default=datetime.now())
    total_chol = fields.Char('Total Cholesterol', default=' mg/dl')
    ldl = fields.Char('LDL', default=' mg/dl')
    hdl = fields.Char('HDL', default=' mg/dl')
    triglycerides = fields.Char('Triglycerides', default=' mg/dl')
    vldl = fields.Char('VLDL', default=' mg/dl')
    medications = fields.Char('Medications')


class PatientDiabetes(models.Model):
    _name = 'patient.diabetes'

    medical_patient_id = fields.Many2one('medical.patient', string="Patient")

    date = fields.Date(string='Date', default=datetime.now())
    rbs = fields.Char('RBS')
    fast_blood_suger = fields.Char('Fast Blood Suger')
    ppbs = fields.Char('PPBS')
    hba1c = fields.Char('HBA 1c')


class PatientMedications(models.Model):
    _name = 'patient.medications'

    medical_patient_id = fields.Many2one('medical.patient', string="Patient")

    date = fields.Date(string='Date', default=datetime.now())
    name = fields.Char('Name of Medication')
    dose = fields.Char('Generic name')
    frequency = fields.Char('Frequency')


class PatientTreatmentChart(models.Model):
    _name = 'patient.treatment.chart'

    medical_patient_id = fields.Many2one('medical.patient', string="Patient")
    sequence = fields.Integer('Sequence')
    date = fields.Date(string='Date', default=datetime.now())
    pre_bp = fields.Char("PRE BP")
    hr = fields.Char("HR")
    diagnosis_systolic_aug_ratio = fields.Integer("Diastolic Systolic Augmentation Ratio")
    post_bp = fields.Char("POST BP")
    post_hr = fields.Char("POST HR")
    weight = fields.Integer("Weight")
    rbs = fields.Integer("RBS")
    complaints = fields.Char("Complaints")


class NTProBNP(models.Model):
    _name = 'nt.pro.bnp'

    medical_patient_id = fields.Many2one('medical.patient', string="Patient")
    date = fields.Date(string='Date', default=datetime.now())
    nt_pro_bnp = fields.Char("NT Pro BNP", default='pg/ml')


class CADPT(models.Model):
    _name = 'cad.pt'

    medical_patient_id = fields.Many2one('medical.patient', string="Patient")
    date = fields.Date(string='Date', default=datetime.now())
    cad_pt = fields.Char("PT")


class CADINR(models.Model):
    _name = 'cad.inr'

    medical_patient_id = fields.Many2one('medical.patient', string="Patient")
    date = fields.Date(string='Date', default=datetime.now())
    cad_inr = fields.Char("INR")


class RenalLiverProfile(models.Model):
    _name = 'renal.liver.profile'

    medical_patient_id = fields.Many2one('medical.patient', string="Patient")
    date = fields.Date(string='Date', default=datetime.now())
    s_creatinine = fields.Char("S. Creatinine")
    s_na_plus = fields.Char("S.Na+")
    s_k_plus = fields.Char("S.K+")
    s_cl_minus = fields.Char("S.Cl-")
    sgpt = fields.Char("SGPT")


class PatientHoliday(models.Model):
    _name = 'patient.holiday'
    _description = "Patient Leave Informations"

    medical_patient_id = fields.Many2one('medical.patient', string="Patient")
    date = fields.Date(string='Date', default=datetime.now())
    remarks = fields.Char("Leave Remarks")


class PatientMedicineDocuments(models.Model):
    _name = 'patient.medicine.documents'
    _description = "Patient medicine documents"

    medical_patient_id = fields.Many2one('medical.patient', string="Patient")
    date = fields.Date(string='Date', default=datetime.now())
    remarks = fields.Char("Leave Remarks")
    documents = fields.Binary('Documents', attachement=True)
