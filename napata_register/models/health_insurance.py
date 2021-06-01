
from odoo import models, fields, api,_
import datetime
import re

from odoo.exceptions import UserError


class napataHealthInsurance(models.Model):
    _inherit = ['mail.thread']
    _name = 'napata.health'
    _description = 'information admission'
    name = fields.Char(string="full name", compute="get_student_name")
    first=fields.Char(string="First Name")
    second=fields.Char(string="	Second Name")
    third=fields.Char(string="Third Name")
    last=fields.Char(string="Last Name")
    birth_date=fields.Char(string="Date of Birth")
    id_document=fields.Char(string="The Identification Document")
    the_number=fields.Char(string="The Identification Number")
    place_of_issue=fields.Char(string="Place Of Issue")
    social_status=fields.Char(string="Social ٍStatus")
    educational_level=fields.Char(string="Educational level")
    local=fields.Char(string="Local")
    unit=fields.Char(string="Administrative unit")
    neighborhood=fields.Char(string="Neighborhood ")
    the_phone=fields.Char(string="the phone ")
    e_mail=fields.Char(string="E-mail ")
    mother_name=fields.Char(string="Mother's name ")
    place_of_birth=fields.Char(string="place of birth ")
    chronic_diseases=fields.Char(string="chronic diseases ")
    health_center=fields.Char(string="Health center ")
    hospital=fields.Char(string="the hospital ")
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

    # def get_student_name(self):
    #     for re in self:
    #         re.name = str(re.first) + " " + str(re.second) + " " + str(re.third) + " " + str(re.last)
    # # Validate student Frist Name
    # @api.constrains('first')
    # def validate_student_full_name(self):
    #     if self.first:
    #         if not re.search(r'^(?:[^\W\d_]| )+$', self.first + " " + self.second + " " + self.third + " " + self.last) != None:
    #             raise UserError(_('The value of student name must only letters'))
    #
    # # Validate school name
    # @api.constrains('school_name')
    # def validate_school_name(self):
    #     if self.school_name:
    #         if not re.search(r'^(?:[^\W\d_]| )+$',self.school_name) != None:
    #             raise UserError(_('The value of student name must only letters'))
    # # Validate student Number
    # @api.constrains('studentNumber')
    # def validate_student_number(self):
    #     if self.studentNumber:
    #         if not re.match("^[0-9]*$", self.studentNumber) != None:
    #             raise UserError(_('The value of Form Number must be positive number'))
    #
    #
    #
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
    #         'form_number': result['studentNumber'],
    #         'main_desire': result['program']['id'],
    #         'type_acceptance':result['presntaion_type']['name'],
    #         'school_name':result['school_name'],
    #     })
    #     return result
    #
    # def action_confirm_admission(self):
    #     self.state = "done"
    #
    #
