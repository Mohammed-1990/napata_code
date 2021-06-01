
from odoo import models, fields, api
import datetime

class feesPaid(models.Model):
    _inherit = ['mail.thread']
    _name = 'napata.feepaid'
    _order = "id  desc"
    _rec_name="fees_type"
    _description = 'information feepaid'
    student_id = fields.Many2one('napata.register', string="Student  ID",
                                 ondelete='cascade')
    level = level = fields.Many2one('napata.level', string='The Level',
                                    ondelete='cascade', required=True)
    semester = fields.Many2one('napata.semester', string='Semester',
                               ondelete='cascade')
    fees_type = fields.Char(string="Fee type")
    type = fields.Char(string="Fee type")
    amount = fields.Char(straing=' amount')
    the_amount = fields.Char(straing='The Amount')
    receipt_number = fields.Char(straing='Receipt Number')
    paid_date = fields.Date(string="Date")
