# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from datetime import date, datetime


class PatientMedicine(models.Model):
    _name = 'patient.medicine'
    _rec_name = 'name'

    name = fields.Char(string='Patient Name')
    date = fields.Date(string='Date', default=datetime.now())

    hr = fields.Char("Heart Rate")
    weight = fields.Integer("Weight")
    bp = fields.Char("Blood Pressure")
    spo2 = fields.Char("SpO2")

    # addons fields
    fbs = fields.Char("FBS")
    pp2bs = fields.Char("PP2BS")
    s_creatinine = fields.Char("S. Creatinine")
    rbs = fields.Char('RBS')

    medicines_list_ids = fields.Many2many(comodel_name='medicines.list',
                                          string='Medicines List')


class ListMedicines(models.Model):
    _name = 'medicines.list'
    _rec_name = 'name'

    name = fields.Char(string='Name')
    description = fields.Char(string='Description')
    frequency = fields.Char(string='Frequency', default="0-0-0")
