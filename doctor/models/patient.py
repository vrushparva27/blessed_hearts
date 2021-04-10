patient.file.number# -*- encoding: utf-8 -*-

from odoo import api, fields, models, _
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as df, DEFAULT_SERVER_DATETIME_FORMAT as dtf


class MedicalPatient(models.Model):
    _inherit = 'res.partner'
    _description = 'Patient Details'

    # first_name = fields.Char('First Name')
    # last_name = fields.Char('Last Name')
    birth_date = fields.Date('Date Of Birth')
    age = fields.Char(string="Age", compute='_compute_age')
    age_years = fields.Integer(
        string="Age (years/ old)", compute='_compute_age')
    gender = fields.Selection([('m', 'Male'), ('f', 'Female')], default='m')
    is_patient = fields.Boolean('Is Patient')
    file_number = fields.Char('File Number')
    prev_file_number = fields.Char('Previous File Number')
    reference_id = fields.Many2one("patient.reference", string="Reference")
    occupation_id = fields.Many2one("patient.occupation", string="Occupation")
    patient_mobile_ids = fields.One2many("patient.mobile", 'partner_id', string='Contacts')

    @api.model
    def default_get(self, fields):
        res = super(MedicalPatient, self).default_get(fields)
        patient_id = self.search([('is_patient', '=', True)], order='id DESC', limit=1)
        res['prev_file_number'] = patient_id.file_number
        return res

    @api.multi
    @api.constrains('mobile')
    def _check_mobile(self):
        for rec in self:
            if rec.mobile and len(rec.mobile) != 10:
                raise ValidationError(_("Please Enter 10digit mobile no"))
            elif rec.mobile and not str(rec.mobile).isdigit():
                raise ValidationError(_("please Enter only Number"))
            return True

    @api.model
    def create(self, vals):
        if vals.get('name'):
        # if vals.get('first_name') or vals.get('last_name'):
            # vals['name'] = '%s %s' % (vals.get('first_name'), vals.get('last_name'))
            vals['file_number'] = self.env['ir.sequence'].next_by_code('patient.file.number')
        res = super(MedicalPatient, self).create(vals)
        return res

    @api.multi
    @api.depends('birth_date')
    def _compute_age(self):
        """ Age computed depending based on the birth date in the
         membership request.
        """
        now = datetime.now()
        for record in self:
            years_months_days = False
            years = False
            if record.birth_date:
                birth_date = fields.Datetime.from_string(
                    record.birth_date,
                )
                delta = relativedelta(now, birth_date)
                years_months_days = '%d%s %d%s %d%s' % (
                    delta.years, _('y'), delta.months, _('m'),
                    delta.days, _('d')
                )
                years = delta.years
            record.age = years_months_days
            if years:
                record.age_years = years

    @api.multi
    def open_consultation(self):
        self.ensure_one()
        action = self.env.ref('doctor.action_patient_consultation_detail').read()[0]
        consultation_env = self.env['patient.consultation.detail']
        record = consultation_env.search([('partner_id', '=', self.id), ('is_compelete', '=', 0)], limit=1)
        if not record:
            history_data = consultation_env.search(
                [('partner_id', '=', self.id), ('is_compelete', '=', 1)])
            record = consultation_env.create({'partner_id': self.id, 'child_ids': [(6, 0, history_data.ids)]})
        action['res_id'] = record.id
        record.consultation_date = datetime.now().strftime(dtf)
        return action

    @api.multi
    @api.constrains('mobile')
    def _check_mobile(self):
        for rec in self:
            if rec.mobile and len(rec.mobile) != 10:
                raise ValidationError(_("Please Enter 10digit mobile no"))
            elif rec.mobile and not str(rec.mobile).isdigit():
                raise ValidationError(_("please Enter only Number"))
            return True
