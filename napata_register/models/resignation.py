
from odoo import models, fields, api,_
import datetime

from odoo.fields import Date


class Resignation(models.Model):
    _inherit = ['mail.thread']
    _name = 'napata.resignation'
    _description = 'studyfees information'
    student_ids = fields.Many2one(
        'napata.register', string='Student Name')
    college = fields.Many2one("napata.collage", ondelete="cascade", string="College"
    ,related='student_ids.college_id')
    program = fields.Many2one("napata.program", ondelete="cascade", string="Program"
    ,related='student_ids.program')
    level = fields.Many2one('napata.level', string='the level',
                            ondelete='cascade', related='student_ids.level')
    semester = fields.Many2one('napata.semester', string='Semester',
                               ondelete='cascade',related='student_ids.semester')
    sitting_number  = fields.Char(string='Sitting number',related='student_ids.siting_number')
    location_exam = fields.Char(string='School',related='student_ids.school_name')
    date_admission = fields.Char(string='Date of admission',related='student_ids.accept_year')
    academic_position = fields.Many2one('napata.result', string='academic position',
                                        ondelete='cascade',related='student_ids.academic_position')
    reasons =fields.Many2one('napata.dismissalreasons', string='Reason',
                            ondelete='cascade')
    nots =fields.Text(string="Comment")
    data=fields.Date(string="Date current action", required=False, readonly=True
                                , default=lambda self: fields.date.today())
    reg_name=fields.Char(string="System User " ,default=lambda self: self.env.user.name)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('registrar', 'Registrar'),
        ('coordinator', 'Coordinator'),
        ('scientific', 'Scientific affairs'),
        ('done', 'done'),
    ], string='Status', default="draft", readonly=True)















