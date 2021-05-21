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
