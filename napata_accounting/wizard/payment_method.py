# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class MethodInvoice(models.TransientModel):
    _name = "payment.method"
    _rec_name = "money_type"
    _description = "Membership Invoice"
    student_ids = fields.Many2one(
        'napata.accounting', string='Student Name')
    money_type = fields.Selection([
        ('cash', 'Cash'),
        ('bank', 'Bank check'),
    ], string='Method Of Payment')

    # action for print account wizard report
    def create_accounting_wizard_report(self):
        money_type = self.money_type

        result = self.env['napata.accounting'].browse(self.student_ids.ids)
        result.update(
             {'money_type': self.money_type,
              'state': 'confirm'}
        )

