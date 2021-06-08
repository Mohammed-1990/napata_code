
from odoo import models, fields, api,_
import datetime
import re

from odoo.exceptions import UserError


class napataAdmissions(models.Model):
    _inherit = ['mail.thread']
    _order = "id desc"
    _name = 'napata.admission'
    _description = 'information admission'
    name = fields.Char(string="full name", compute="get_student_name")
    first=fields.Char(string="First Name")
    second=fields.Char(string="	Second Name")
    third=fields.Char(string="Third Name")
    last=fields.Char(string="Last Name")
    college_id = fields.Many2one('napata.collage', string='College',
                            ondelete='cascade',
                            default=lambda self: self.env['napata.collage'].search([]))
    program=fields.Many2one("napata.program",ondelete="cascade",string="program")
    presntaion_type=fields.Many2one("napata.presentationtype",ondelete="cascade",string="Presntaion Type")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'done'),
    ], string='Status', default="draft", readonly=True)
    school_name=fields.Char(string="School Name ")
    studentNumber=fields.Char(string="Form Number" ,size=10)
    year = fields.Char('Admission Year',  default=lambda self: str(datetime.datetime.now().year -1)
                                                               +" / "+str(datetime.datetime.now().year))
    accept_year = fields.Char('Admission Year',  default=lambda self: datetime.datetime.now().year)

    def get_student_name(self):
        for re in self:
            re.name = str(re.first) + " " + str(re.second) + " " + str(re.third) + " " + str(re.last)
    # Validate student Frist Name
    @api.constrains('first')
    def validate_student_full_name(self):
        if self.first:
            if not re.search(r'^(?:[^\W\d_]| )+$', self.first + " " + self.second + " " + self.third + " " + self.last) != None:
                raise UserError(_('The value of student name must only letters'))

    @api.onchange('college_id')
    def get_program(self):
        get_program_lest = []
        collage = self.env['napata.program'].search([('collage_id', '=', self.college_id.id)])
        if collage:
            for rec in collage:
                get_program_lest.append(rec.id)

            return {'domain': {'program': [('id', 'in', get_program_lest)]}}
    # Validate student Number
    @api.constrains('studentNumber')
    def validate_student_number(self):
        if self.studentNumber:
            if not re.match("^[0-9]*$", self.studentNumber) != None:
                raise UserError(_('The value of Form Number must be positive number'))



    # @api.model
    # def create(self, vals):
    #     result = super(napataAdmissions, self).create(vals)
    #     self.env['napata.presentation'].create({
    #         'name': result['name'],
    #         'first_name': result['first'],
    #         'second_name': result['second'],
    #         'third_name': result['third'],
    #         'forth_name': result['last'],
    #         'done': True,
    #         'accept_year':result['accept_year'],
    #         'form_number': result['studentNumber'],
    #         'main_desire': result['program']['id'],
    #         'college_id': result['college_id']['id'],
    #         'type_acceptance':result['presntaion_type']['name'],
    #         'school_name':result['school_name'],
    #     })
    #     return result

    def action_confirm_admission(self):
        self.state = "done"
        self.env['napata.presentation'].create({
                'name': self.name,
                'first_name': self.first,
                'second_name':self.second,
                'third_name': self.third,
                'forth_name': self.last,
                'done': True,
                'accept_year':self.accept_year,
                'form_number': self.studentNumber,
                'main_desire': self.program.id,
                'college_id': self.college_id.id,
                'type_acceptance':self.presntaion_type.id,
                'school_name':self.school_name,
            })


