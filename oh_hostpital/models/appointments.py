# -*- coding: utf-8 -*-

from odoo import models, fields, api,_


class HospitalAppintments(models.Model):
    _name = 'hospital.appointments'
    _description = 'appintments table '
    _order ="id desc"
    rec_name='patient_id'
    name = fields.Char(string="Name")
    patient_id = fields.Many2one( 'hospital.patient',string="Patient")
    patient_age = fields.Integer(string="Age", related='patient_id.patient_age')
    note = fields.Text(string="notes")
    date = fields.Date(string="Date")
    state = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('confirm', 'confirm'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')
    ], string='Status', readonly=True,
        default='draft')
    sequns_name = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,index=True, default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        if vals.get('sequns_name', _('New')) == _('New'):
           vals['sequns_name'] = self.env['ir.sequence'].next_by_code('hospital.appintments.sequence') or _('New')


        result = super(HospitalAppintments, self).create(vals)
        return result
    def action_confirm(self):
        for rec in self:
            rec.state="confirm"

    def action_done(self):
        for rec in self:
            rec.state = "done"
    def action_concel(self):
        for rec in self:
            rec.state = "draft"
    #     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
