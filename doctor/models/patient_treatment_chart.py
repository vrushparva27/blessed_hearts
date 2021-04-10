# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class PatientTreatmentChart(models.Model):
    _name = 'patient.treatment.chart'
    _description = 'Patient Treatment Chart'
    _rec_name = 'patient_consultation_id'

    patient_consultation_id = fields.Many2one(comodel_name='patient.consultation.detail', string="Patient Consultation",
                                              index=True, required=True, ondelete='cascade')
    treatment_date = fields.Date('Date')
    treatment_pre_hr = fields.Char('Pre HR')
    treatment_pre_hr_uom = fields.Many2one(string="Pre HR UoM", comodel_name="uom.uom",
                                           default=lambda self: self.env.ref('uom.product_uom_kgm', False), )

    treatment_pre_bp = fields.Char('Pre BP')
    treatment_pre_bp_uom = fields.Many2one(string="Pre BP UoM", comodel_name="uom.uom",
                                           default=lambda self: self.env.ref('uom.product_uom_kgm', False), )
    diastolic_systolic_augmentation_ratio = fields.Char('Diastolic / systolic Augmentation Ratio')
    treatment_post_hr = fields.Char('Post HR')
    treatment_post_hr_uom = fields.Many2one(string="Post HR UoM", comodel_name="uom.uom",
                                            default=lambda self: self.env.ref('uom.product_uom_kgm', False), )
    treatment_post_bp = fields.Char('Post BP')
    treatment_post_bp_uom = fields.Many2one(string="Post BP UoM", comodel_name="uom.uom",
                                            default=lambda self: self.env.ref('uom.product_uom_kgm', False), )
    treatment_weight = fields.Float('Weight')
    treatment_weight_uom = fields.Many2one(string="Weight UoM", comodel_name="uom.uom",
                                           default=lambda self: self.env.ref('uom.product_uom_kgm', False), )
    treatment_complaints = fields.Text('Complaints (If Any)')
