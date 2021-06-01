# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
class accountReport(models.TransientModel):
    _name = "account.report"
    _rec_name = "money_type"
    _description = "account Report"
    student_ids = fields.Many2one(
        'napata.accounting', string='Student Name')
    program=fields.Many2one("napata.program",ondelete="cascade",string="program")
    presntaion_type=fields.Many2one("napata.presentationtype",ondelete="cascade",string="Presntaion Type")
    date  = fields.Date(string="date")
    money_type = fields.Selection([
        ('cash', 'Cash'),
        ('bank', 'Bank check'),
    ], string='Method Of Payment')


    # def print_account_report(self):
    #   return self.env.ref('napata_accounting.report_session').report_action(self)
     
    def print_accunt_report(self):
        account_ids = self.env['napata.accounting'].search([])
        data={}
        account_list=[]
        if self.program:
           for rec in account_ids:
               if rec.id == self.program:
                   account_list.append(rec.id)
                   account_ids = self.env['napata.accounting'].search(['id','in',account_list])
                   account_list=[]
        for rec in account_ids:
            account_list.append(rec.id)
        data={'account_ids':account_list}
        return self.env.ref('napata_accounting.report_account_report').report_action(self, data=data)
class AccountReport(models.AbstractModel):
    _name = 'report.napata_accounting.report_account_templet'
    def _get_report_values(self, docids, data=None):
            account_ids = self.env['napata.accounting'].search(['id','in',data['account_ids']])
            docids=docids
            return{
                'data':account_ids
            }



        
        

