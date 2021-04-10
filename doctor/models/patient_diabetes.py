# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class PatientDiabetes(models.Model):
    _name = 'patient.diabetes'
    _description = 'Patient Diabetes'
    _rec_name = 'patient_consultation_id'

    # name = fields.Char('Name')
    patient_consultation_id = fields.Many2one(comodel_name='patient.consultation.detail', string="Patient Consultation",
                                              index=True, required=True, ondelete='cascade')
    diabetes_date = fields.Date('Date')
    fast_blood_sugar = fields.Float('Fasting Blood Sugar')
    fast_blood_sugar_uom_id = fields.Many2one('uom.uom', string='Fasting Blood Sugar UOM')
    ppbs = fields.Float('PPBS')
    rbs = fields.Float('RBS')
    hba1c = fields.Float('HbA1c')
    mbs = fields.Float('MBS')
