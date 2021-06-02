# -*- coding: utf-8 -*-

from odoo import models, fields, api,_


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'patient table '
    _order ="id desc"
    name = fields.Char(string="Name")
    patient_age = fields.Integer(string="Age")
    description = fields.Text(string="description")
    image = fields.Binary(string="Image")
    count=fields.Integer(string ='count',compute="appointment_count")
    sequns_name = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,index=True, default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        if vals.get('sequns_name', _('New')) == _('New'):
           vals['sequns_name'] = self.env['ir.sequence'].next_by_code('hospital.patient.sequence') or _('New')


        result = super(HospitalPatient, self).create(vals)
        return result
    #     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

    def open_patient_appointment(self):
        return {
            'name': _('Appointment'),
            'type': 'ir.actions.act_window',
            'res_model': 'hospital.appointments',
            'view_id': False,
            'view_mode': 'tree,form',
            'domain': [('patient_id','=',self.id)],
        }
    def appointment_count(self):
        acount=self.env['hospital.appointments'].search_count([('patient_id','=',self.id)])
        self.count=acount
