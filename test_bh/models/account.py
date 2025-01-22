# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.model
    def default_get(self, fields):
        res = super(AccountMove, self).default_get(fields)
        if self._context.get('from_billing_deposit'):
            res['is_from_bh'] = True
        return res

    patient_id = fields.Many2one('medical.patient', 'Patient')
    is_from_bh = fields.Boolean(compute='check_is_bh')
    bh_total_amount = fields.Char("Total (In Words)", default="1 Lac Twenty Five Thousands Only")

    def check_is_bh(self):
        for rec in self:
            if self._context.get('from_billing_deposit'):
                rec.is_from_bh = 1
            else:
                rec.is_from_bh = 0

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
            if rec.type == 'out_refund' and rec.state != 'posted' and self._context.get(
                    'active_model') == 'medical.patient':
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
    
 
class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    session_date = fields.Date(string='Session Date', default=lambda self: fields.datetime.now())

