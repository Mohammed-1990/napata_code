# -*- coding: utf-8 -*-

import datetime

from odoo import models, fields, api, exceptions


class napataPresentation(models.Model):
    _inherit = ['mail.thread']
    _name = 'napata.new_presentation'
    _description = 'new_presentation information'
    name = fields.Char(string="Full name", readonly=True)
    # get student name

    first_name = fields.Char(string='First Name')
    second_name = fields.Char(string='Second Name')
    third_name = fields.Char(string='Third Name')
    forth_name = fields.Char(string='Fourth Name')
    # nationality
    nationality = fields.Many2one('res.country',
                                  string="Nationality")
    #
    idtype = fields.Selection([
        ('number', 'National number'),
        ('card', 'National card'),
        ('passport', 'Passport'),
        ('other', 'Other')

    ], string="ID Tyep")
    # id_number
    id_number = fields.Char(string="The National Number")
    # gender
    gender = fields.Selection([
        ('M', 'Mail'),
        ('F', 'Fmail '),
        ('O', 'Other')],string="Gender")
    # gender
    religion = fields.Selection([
        ('M', 'Muslim'),
        ('C', 'Christian '),
        ('O', 'Other')], string="Religion")
    # Marital status
    marital = fields.Selection([
        ('S', 'Single'),
        ('M', 'Married '),
        ('O', 'Other')], string="Marital Status")
    # brath_day
    brath_day=fields.Date(string=" Barth Day")
    # school
    # school = fields.Char(string='School ')
    certificate_type = fields.Char(string=" Type of certificate")
    # precentage
    ratio = fields.Float(string="Precentage")
    # course
    course = fields.Selection([
        ('Scientific', 'Scientific'),
        ('literary', 'literary')], string="The course")
    sit_number = fields.Integer(string="Sitting Number")
    form_number= fields.Char(string='Form Number')


    # contact
    phone = fields.Integer(string="Phone Number")
    watsapp = fields.Integer(string="watsapp")
    # Certificate
    Certificate = fields.Selection([
        ('sudanese', 'Sudanese'),
        ('arabic', 'Arabic'),
        ('foreign', 'foreign'),
        ('other', 'Other')

    ], string="Certificate Tyep")
    National_card = fields.Binary(string="National card")
    # National_card = fields.Many2one(string="Main Attachment", comodel_name='ir.attachment', index=True, copy=False)

    School_card = fields.Binary(string="High School Certificate")
    # fother
    provider = fields.Char(string="Fathor  Name")
    job = fields.Char(string="Profession")
    phone3 = fields.Integer(string="Phone Number")
    parent = fields.Many2one('na.parent',
                             ondelete='cascade')

    # addeess
    states_id = fields.Many2one('na.state',
                                ondelete='cascade', string="State")
    Local_id = fields.Many2one('na.locals', straing='local')

    # ), compute='get_local',ondelete='cascade', readonly=False, store=True)

    # abut Us
    facebook = fields.Boolean(string="Face Book")
    website = fields.Boolean(string="Web Site")
    newspaper = fields.Boolean(string="Newspaper")
    tv = fields.Boolean(string="TV")
    radio = fields.Boolean(string="Radio")
    admission_book = fields.Boolean(string="Admission Book")
    # fees

    type_acceptance = fields.Char(straing='Type of acceptance')
    application_fees = fields.Char(straing='Application Fees')




    #                        required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
    exm_year = fields.Char(string=" exm_year", default=(
        lambda self: str(datetime.datetime.now().year - 1) + " / " + str(datetime.datetime.now().year)))


    receipt_code = fields.Char(string='prenent code')


    # end of name field




    main = fields.Many2one("na.program", ondelete="cascade", string="Main Desire")
    sub = fields.Many2many("na.program", ondelete="cascade", string="Sub Desire")

    data = fields.Char('Date current action', default=(lambda self: datetime.datetime.now().year))

    # Degree   Holders
    submet = fields.Char(straing='Ok')
    signup_valid = fields.Boolean(string='Submet')
    pay_date = fields.Char(string='Received  Date')


    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'done'),
    ], string='Status', default="draft", readonly=True)

    # about us desar
    @api.constrains('main', 'sub')
    def _check_instructor_not_in_attendees(self):
        for r in self:
            if r.main and r.main in r.sub:
                raise exceptions.ValidationError(
                    "This desire has been chosen as the main desire that cannot be chosen within the sub-desire")

    # @api.onchange('states_id')
    # def get_local(self):
    #     get_local_list = []
    #     Locals = self.env['na.locals'].search(
    #           [('state_id', '=', self.states_id.id)])
    #     if Locals:
    #         for rec in Locals:
    #          get_local_list.append(rec.id)

        # return {'domain': {'Local_id': [('id', 'in', get_local_list)]}}
    # about us validation
    @api.constrains('facebook', "website", "newspaper", "tv", "radio", "admission_book")
    def _check_validation(self):
        is_valid = False

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
        if is_valid == False:
            raise exceptions.ValidationError("not valid")

    # Submet
    @api.constrains("signup_valid")
    def _check_submet(self):
        if self.signup_valid == False:
            raise exceptions.ValidationError("not signup valid")

        # code Serial auto no

    def action_confirm(self):
        val= " "
        for  rec  in self.sub:
         val+=str(rec.name)+" \t - \t "

        self.env['napata.register'].create({

            'name': self.name,
            'first_name': self.first_name,
            'second_name': self.second_name,
            'third_name': self.third_name,
            'forth_name': self.forth_name,
            'nationality': self.nationality.name,
            'type_id': self.idtype,
            'number_ids': self.id_number,
            'phone1': self.phone,
            'phone2': self.watsapp,
            #     parint provider_name
            'provider_name': self.provider,
            'parent': self.parent.name,
            'job': self.job,
            'phone3': self.phone3,
            # study  information
            # 'school': self.school,
            'certificate_type': self.certificate_type,
            'cource': self.course,
            'siting_number': self.sit_number,
            'ratio': self.ratio,
            'main_desires': self.main.name,
            'form_number': 123,
            'athoer_desires':val,
            # fees
            'accept_type': self.type_acceptance,
            'application_fees': self.application_fees,
            'receipt_code': self.receipt_code,
            'pay_date': self.pay_date,
        })










