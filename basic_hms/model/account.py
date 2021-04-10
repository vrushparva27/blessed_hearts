# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

from lxml import etree


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    def unlink(self):
        for move in self:
            if move.state != 'draft':
                if not self.env.user.has_group('hspl_hide_menu.hspl_hide_menu_group'):
                    raise UserError(_('Sorry !!! Please Contact Your Administrator'))
        return super(AccountPayment, self).unlink()

    @api.model
    def create(self, vals):
        if vals.get('payment_type') == 'outbound' and self._context.get('active_model') == 'medical.patient':
            medical_patient = self.env[self._context.get('active_model')].browse(self._context.get('active_id'))
            total_refund_amt = medical_patient.total_deposit_amt - medical_patient.total_deposit_refund_amt
            if vals.get('amount') > total_refund_amt:
                raise UserError(_("Sorry !!! amount cannot be more than deposit."))
        return super(AccountPayment, self).create(vals)

    def write(self, vals):
        for rec in self:
            if rec.payment_type == 'outbound' and self._context.get('active_model') == 'medical.patient':
                medical_patient = self.env[self._context.get('active_model')].browse(
                    self._context.get('active_id')) or rec.patient_id
                total_refund_amt = medical_patient.total_deposit_amt - medical_patient.total_deposit_refund_amt
                amount = vals.get('amount') or rec.amount
                if amount > total_refund_amt:
                    raise UserError(_("Sorry !!! amount cannot be more than deposit."))
        return super(AccountPayment, self).write(vals)

    def post(self):
        if self.payment_type == 'outbound' and self._context.get('active_model') == 'medical.patient':
            medical_patient = self.env[self._context.get('active_model')].browse(
                self._context.get('active_id')) or self.patient_id
            total_refund_amt = medical_patient.total_deposit_amt - medical_patient.total_deposit_refund_amt
            if self.amount > total_refund_amt:
                raise UserError(_("Sorry !!! amount cannot be more than deposit."))
        return super(AccountPayment, self).post()

    @api.model
    def default_get(self, fields):
        res = super(AccountPayment, self).default_get(fields)
        if self._context.get('from_billing_deposit'):
            res['is_from_hms'] = True
        return res

    is_from_hms = fields.Boolean(compute='check_is_hms')
    patient_id = fields.Many2one('medical.patient', 'Patient')

    def check_is_hms(self):
        for rec in self:
            if self._context.get('from_billing_deposit'):
                rec.is_from_hms = 1
            else:
                rec.is_from_hms = 0


class AccountMove(models.Model):
    _inherit = 'account.move'

    def unlink(self):
        for move in self:
            if move.state != 'draft':
                if not self.env.user.has_group('hspl_hide_menu.hspl_hide_menu_group'):
                    raise UserError(_('Sorry !!! Please Contact Your Administrator'))
        return super(AccountMove, self).unlink()

    @api.model
    def default_get(self, fields):
        res = super(AccountMove, self).default_get(fields)
        if self._context.get('from_billing_deposit'):
            res['is_from_hms'] = True
        return res

    patient_id = fields.Many2one('medical.patient', 'Patient')
    is_from_hms = fields.Boolean(compute='check_is_hms')

    def check_is_hms(self):
        for rec in self:
            if self._context.get('from_billing_deposit'):
                rec.is_from_hms = 1
            else:
                rec.is_from_hms = 0

    @api.model
    def create(self, vals):
        res = super(AccountMove, self).create(vals)
        if res.type == 'out_refund' and self._context.get('active_model') == 'medical.patient':
            medical_patient = self.env[self._context.get('active_model')].browse(self._context.get('active_id'))
            total_refund_amt = medical_patient.total_inv_amt - medical_patient.total_inv_refund_amt
            if res.amount_total > total_refund_amt:
                raise UserError(_("Sorry !!! amount cannot be more than deposit."))
        return res

    def write(self, vals):
        res = super(AccountMove, self).write(vals)
        for rec in self:
            if rec.type == 'out_refund' and rec.state != 'posted' and self._context.get('active_model') == 'medical.patient':
                medical_patient = self.env[self._context.get('active_model')].browse(
                    self._context.get('active_id')) or rec.patient_id
                total_refund_amt = medical_patient.total_inv_amt - medical_patient.total_inv_refund_amt
                if rec.amount_total > total_refund_amt:
                    raise UserError(_("Sorry !!! amount cannot be more than deposit."))
        return res

    def action_post(self):
        if self.type == 'out_refund' and self._context.get('active_model') == 'medical.patient':
            medical_patient = self.env[self._context.get('active_model')].browse(
                self._context.get('active_id')) or self.patient_id
            total_refund_amt = medical_patient.total_inv_amt - medical_patient.total_inv_refund_amt
            if self.amount_total > total_refund_amt:
                raise UserError(_("Sorry !!! amount cannot be more than deposit."))
        return super(AccountMove, self).action_post()
