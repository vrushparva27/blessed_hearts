# -*- encoding: utf-8 -*-

from odoo import api, fields, models, _


class PatientOccupation(models.Model):
    _name = 'patient.occupation'
    _description = 'Patient Occupation'

    name = fields.Char("Occupation")
