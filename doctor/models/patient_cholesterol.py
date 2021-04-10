# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class PatientCholesterol(models.Model):
    _name = 'patient.cholesterol'
    _description = 'Patient Cholesterol'
    _rec_name = 'patient_consultation_id'

    # name = fields.Char('Name')
    patient_consultation_id = fields.Many2one(comodel_name='patient.consultation.detail', string="Patient Consultation",
                                              index=True, required=True, ondelete='cascade')
    cholesterol_date = fields.Date('Date')
    total_chol = fields.Float('Total chol.')
    total_chol_uom_id = fields.Many2one('uom.uom', string='Total chol. UOM')
    cholesterol_ldl = fields.Float('LDL')
    cholesterol_ldl_uom_id = fields.Many2one('uom.uom', string='LDL UOM')
    cholesterol_hdl = fields.Float('HDL')
    cholesterol_hdl_uom_id = fields.Many2one('uom.uom', string='HDL UOM')
    cholesterol_triglycerides = fields.Float('Triglycerides')
    cholesterol_triglycerides_uom_id = fields.Many2one('uom.uom', string='Triglycerides UOM')
    cholesterol_vldl = fields.Float('VLDL')
    cholesterol_vldl_uom_id = fields.Many2one('uom.uom', string='VLDL UOM')
    cholesterol_other_test = fields.Float('Other Test')
    cholesterol_other_uom_id = fields.Many2one('uom.uom', string='Other UOM')
    cholesterol_medications = fields.Char('Medicaions')
