# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class PatientDrugAllergie(models.Model):
    _name = 'patient.drug.allergie'
    _description = 'Patient Drug Allergie'
    # _rec_name = 'patient_consultation_id'

    name = fields.Char('Medication Name')
    medication_dose = fields.Float('Medication Dose')
    medication_frequency = fields.Float('Medication Frequency')
    patient_consultation_id = fields.Many2one('patient.consultation.detail', string="Patient Consultation")
