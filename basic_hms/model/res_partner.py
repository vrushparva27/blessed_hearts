# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class res_partner(models.Model):
    _inherit = 'res.partner'

    relationship = fields.Char(string='Relationship')
    relative_partner_id = fields.Many2one('res.partner', string="Relative_id")
    is_patient = fields.Boolean(string='Patient')
    is_person = fields.Boolean(string="Person")
    is_doctor = fields.Boolean(string="Doctor")
    is_insurance_company = fields.Boolean(string='Insurance Company')
    is_pharmacy = fields.Boolean(string="Pharmacy")
    patient_insurance_ids = fields.One2many('medical.insurance', 'patient_id')
    is_institution = fields.Boolean('Institution')
    company_insurance_ids = fields.One2many('medical.insurance', 'insurance_compnay_id', 'Insurance')
    reference = fields.Char('ID Number')
    state_id = fields.Many2one("res.country.state", string='State', ondelete='restrict',
                               domain="[('country_id', '=?', country_id)]",
                               default=lambda s: s.env['res.country.state'].search([('name', '=', 'Gujarat')], limit=1))
    @api.model
    def create(self, vals):
        if self.env.context.get('default_is_patient'):
            vals.update({'company_type': 'person',
                         'customer_rank': 1,
                         'supplier_rank': 0})
        return super(res_partner, self).create(vals)
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
