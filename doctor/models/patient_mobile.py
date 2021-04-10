# -*- encoding: utf-8 -*-

from odoo import api, fields, models, _


class PatientMobile(models.Model):
    _name = 'patient.mobile'
    _description = 'Patient Mobile Details'

    name = fields.Char('Name')
    mobile = fields.Char('Mobile')
    partner_id = fields.Many2one('res.partner', string='Patient')
