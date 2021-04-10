# -*- encoding: utf-8 -*-

from odoo import api, fields, models, _


class PatientReference(models.Model):
    _name = 'patient.reference'
    _description = 'Patient Reference'

    name = fields.Char("Reference")
    mobile = fields.Char("Mobile")
    address = fields.Char("Address")
