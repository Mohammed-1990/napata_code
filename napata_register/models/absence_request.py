
from odoo import models, fields, api,_
import datetime

from odoo.fields import Date


class absenceRequest(models.Model):
    _inherit = ['mail.thread']
    _name = 'napata.absence'
    name = fields.Char(string="full name")
    _description = 'studyfees information'
    program=fields.Char(string="program")
    level=fields.Char(string="level")
    semester = fields.Char(string='Semester')
    subject_one = fields.Char(string='subject one')
    subject_tow = fields.Char(string='subject tow')
    subject_three = fields.Char(string='subject three')
    subject_four = fields.Char(string='subject four')
    day = fields.Char('Study Year',  default=lambda self: Date)
    Agree = fields.Char(string='Agree')
    reasons = fields.Text(string='For the reasons')
    telephone=fields.Char(string='telephone')
    student_signature=fields.Char(string='Student signature')
    lecturer_recommendation = fields.Text(string='The lecturers recommendation')
    professor_recommendation = fields.Text(string='Lab professor’s recommendation')
    professor_name = fields.Char(string='Professor name')
    lecturerr_name = fields.Char(string='lecturer name')
    professor_Signature = fields.Char(string='Signature of the professor')
    lecturer_Signature = fields.Char(string='Signature of the lecturer')
    lecturer_Signature_date = fields.Date(string='date of Signature of the lecturer')
    professor_Signature_date = fields.Date(string='date of Signature of the lecturer')
    decision = fields.Text(string='the decision')
    coordinator_name  = fields.Char(string=' coordinator name')
    coordinator_Signature = fields.Char(string='Signature of the  coordinator')
    coordinator_Signature_date = fields.Date(string='date of Signature of the  coordinator')





