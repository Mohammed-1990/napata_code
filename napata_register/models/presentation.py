# -*- coding: utf-8 -*-

import datetime

from odoo import models, fields, api, exceptions


class  napataPresentation(models.Model):
    _name = 'napata.presentation'
    _description = 'information presentation'
    name = fields.Char(string="Full name", readonly=True)
    college_id = fields.Many2one('napata.collage', string='College',
                                 ondelete='cascade')
    prenent_code = fields.Char(string='prenent code')
    is_done = fields.Boolean(string="Can apply")
    # get student name

    first_name = fields.Char(string='First Name')
    second_name = fields.Char(string='Second Name')
    third_name = fields.Char(string='Third Name')
    forth_name = fields.Char(string='Fourth Name')


    # end of name field
    nationality= fields.Many2one('res.country',
      string="Nationality")
    # nationality= fields.Char(straing='Nationalities')
    idtype=fields.Selection([
                        ('number', 'National number'),
                         ('card', 'National card'),
                        ('passport', 'Passport'),
                        ('other', 'Other')

    ],string="ID Tyep")
    id_number = fields.Char(string="The National Number")
    phone_1=fields.Integer(string="Phone Number")
    phone_2=fields.Integer(string="watsapp")
   
    Certificate = fields.Selection([
                        ('sudanese', 'Sudanese'),
                         ('arabic', 'Arabic'),
                        ('foreign', 'foreign'),
                        ('other', 'Other')

    ],string="Certificate Tyep")
    form = fields.Char(string="Form  Number")

    #
    # abut Us
    facebook=fields.Boolean(string="Face Book")
    website=fields.Boolean(string="Web Site")
    newspaper=fields.Boolean(string="Newspaper")
    tv=fields.Boolean(string="TV")
    radio=fields.Boolean(string="Radio")
    admission_book = fields.Boolean(string="Admission Book")

    course = fields.Selection([
                        ('Scientific', 'Scientific'),
                        ('literary', 'literary')],string="The course")
    sit_number = fields.Integer(string="Sitting Number")
    ratio=fields.Float(string="The ratio")
    # form_number= fields.Char(string='Form Number',
    #                        required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
    exm_year= fields.Char(string=" exm_year" , default=(lambda self: str(datetime.datetime.now().year-1)+" / "+str(datetime.datetime.now().year) ))

    provider=fields.Char(string="Applicant Name")
    job=fields.Char(string="job")








    National_card=fields.Binary(string="National card")
    School_card=fields.Binary(string="High School Certificate")
    phone3=fields.Integer(string="Phone Number")
    parent= fields.Many2one('napata.parent',
        ondelete='cascade')



    main=fields.Many2one("napata.program",ondelete="cascade",string="Main Desire")
    sub=fields.Many2many("napata.program",ondelete="cascade",string="Sub Desire")
    preType2=fields.Char(string="PresntaionType")


    fees = fields.Char(straing='Fees')
    data = fields.Char('Date current action', default=(lambda self: datetime.datetime.now().year))
    admission_ids = fields.Char(string='admission_ids')
    register = fields.Char(string='register')
    #
    pay_date = fields.Char()



    attendees_count = fields.Integer(
        string="Attendees count", compute='_get_attendees_count', store=True)
    # Degree   Holders
    submet=fields.Char(straing='Ok',default=("No hierarchy position.This employee has no manager or subordinate.In order to get an organigram, set a manager and save the record"))
    signup_valid = fields.Boolean(string='Submet')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'done'),
    ], string='Status', default="draft", readonly=True)
    # about us desar
    @api.constrains('main', 'sub')
    def _check_instructor_not_in_attendees(self):
         for r in self:
            if r.main and r.main in r.sub:
                raise exceptions.ValidationError("This desire has been chosen as the main desire that cannot be chosen within the sub-desire")
    # about us validation
    @api.constrains('facebook',"website","newspaper","tv","radio","admission_book")
    def _check_validation(self):
        is_valid=False

        if self.facebook == True:
            is_valid = True
        elif self.website == True:
            is_valid = True
        elif self.newspaper == True:
            is_valid = True
        elif self.tv == True:
            is_valid = True
        elif self.radio == True:
            is_valid = True
        elif self.admission_book == True:
            is_valid = True
        if is_valid==False:
            raise exceptions.ValidationError("not valid")
    # Submet
    @api.constrains("signup_valid")
    def _check_submet(self):
        if self.signup_valid == False:
            raise exceptions.ValidationError("not signup valid")

        # code Serial auto no





    def action_confirm(self,vals):
        self.env['napata.register'].write({

            'name': self.name,
            'first_name': self.first_name,
            'second_name': self.second_name,
            'third_name': self.third_name,
            'forth_name': self.forth_name,
            'college_id': self.college_id.id,
            'nationality': self.nationality.name,
            'type_id': self.idtype,
            'number_ids': self.id_number,
            'phone1': self.phone,
            'phone2': self.phone_2,
            #     parint provider_name
            'provider_name': self.provider,
            'parent': self.parent.name,
            'job': self.job,
            'phone3': self.phone3,
            # fees
            'accept_type': self.preType2,
            'total_fees': self.fees,
            # study  information
            'cource': self.course,
            'ratio': self.ratio,
            'main_desires': self.main.name,
            # 'athoer_desires':self.name,
            'siting_number': self.sit_number,
            'form_number': self.form,
            'pay_date': self.pay_date,
            'admission_ids': self.admission_ids,

        })
        res = super(napataPresentation, self).write(vals)
        return res

    # @api.model
    # def create(self, vals):
    #     if vals.get('form_number', _('New')) == _('New'):
    #         vals['form_number'] = self.env['ir.sequence'].next_by_code('napata_register.presentation.sequence') or _('New')
    #     result = super(napataPresentation, self).create(vals)
    #     return result


    



  
    
   