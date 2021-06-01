import datetime
from odoo import models, fields, api, _, exceptions
from odoo.exceptions import UserError
import re


class napataUniversity(models.Model):
    _name = 'napata.presentation'
    _description = 'presentation information'
    _order="id desc"
    # get student name

    name = fields.Char(string='Full Name')
    first_name = fields.Char(string='First Name')
    second_name = fields.Char(string='Second Name')
    third_name = fields.Char(string='Third Name')
    forth_name = fields.Char(string='Fourth Name')
    # nationality
    nationality = fields.Many2one('res.country',
                                  string="Nationality")
    #
    id_type = fields.Selection([
        ('رقم وطني', 'رقم وطني'),
        ('بطاقة قومية', 'بطاقة قومية'),
        ('جواز سفر', ' جواز سفر'),
    ], string="ID Tyep")
    # id_number
    id_number = fields.Char(string="The National Number")
    # gender
    gender = fields.Selection([
        ('ذكر', 'ذكر'),
        ('انثي', 'انثي ')
    ], string="Gender")
    # gender
    religion = fields.Selection([
        ('مسلم', 'مسلم'),
        ('مسيحي', 'مسيحي '),
        ('اخري', 'اخري')], string="Religion")
    # Marital status
    social_status = fields.Selection([
        ('عازب', 'عازب'),
        ('متزوج', 'متزوج '),
        ('اخري', 'اخري')], string="Social Status")
    # brath_day
    brath_day = fields.Date(string=" Barth Day")
    address = fields.Char(string="Place of birth")

    # school
    school_name = fields.Char(string='School Name ')
    accept_year = fields.Char(string='accept_year ')
    # precentage
    precentage = fields.Float(string="Precentage")
    # course
    course = fields.Selection([
        ('علمي', 'علمي'),
        ('ادبي', 'ادبي')], string="The course")
    siting_number = fields.Char(string="Sitting Number")
    form_number = fields.Char(string='Form Number')

    # contact
    student_mobile = fields.Char(string="Mobile Number")
    watsapp_phone = fields.Char(string="watsapp")
    email = fields.Char(string="Email")
    # Certificate

    national_card = fields.Binary(string="National card")
    school_certificate = fields.Binary(string="High School Certificate")
    # fother
    applicant = fields.Char(string="applicant  Name")
    job = fields.Char(string="Profession")
    fother_adress = fields.Char(string="Fother Adress")
    telephone = fields.Char(string="Telphone")
    relative_relation = fields.Many2one('napata.parent',
                             ondelete='cascade',string="Relative Relation")

    # addeess
    states_id = fields.Char( string="State")
    Local_id = fields.Char( straing='local')
    # states_id = fields.Many2one('napata.state',
    #                             ondelete='cascade', string="State")
    # Local_id = fields.Many2one('napata.locals', straing='local')

    # @api.onchange('states_id')
    # def get_local(self):
    #     get_local_list = []
    #     Locals = self.env['napata.locals'].search(
    #         [('state_id', '=', self.states_id.id)])
    #
    #     if Locals:
    #         for rec in Locals:
    #              get_local_list.append(rec.id)
    #     return {'domain': {'Local_id': [('id', 'in', get_local_list)]}}

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

    def _get_year(self):
        year_list=[]
        for year in range(200,fields.Date.today().year):
            year_list.append((str(year),str(year)))
        return year_list
    exm_year = fields.Selection(_get_year,string=" exm_year", default=(lambda self: str(datetime.datetime.now().year - 1)))

    receipt_code = fields.Char(string='prenent code')

    # end of name field

    college_id = fields.Many2one("napata.collage", ondelete="cascade", string="college")
    main_desire = fields.Many2one("napata.program", ondelete="cascade", string="Main Desire")
    other_desire = fields.Many2many("napata.program", ondelete="cascade", string="Other Desire")

    data = fields.Char(string='Date ',  default=lambda self:datetime.datetime.today().strftime('%Y-%m-%d'))


    # Degree   Holders
    submet = fields.Char(straing='Ok')
    signup_valid = fields.Boolean(string='Submet')
    pay_date = fields.Char(string='Received  Date')
    done = fields.Boolean(string='done')

    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'done'),
    ], string='Status', default="draft", readonly=True)

    # about us desar
    @api.constrains('main_desire', 'other_desire')
    def _check_instructor_not_in_attendees(self):
        for r in self:
            if r.main_desire and r.main_desire in r.other_desire:
                raise exceptions.ValidationError(
                    "This desire has been chosen as the main desire that cannot be chosen within the sub-desire")

    # Validate address
    # @api.constrains('school_name')
    # def validate_school_name(self):
    #     if self.school_name:
    #         if not re.search(r'^(?:[^\W\d_]| )+$', self.school_name) != None:
    #             raise UserError(_('The value of school Name must only letters'))

    # Validate address
    @api.constrains('address')
    def validate_address(self):
        if self.address:
            if not re.search(r'^(?:[^\W\d_]| )+$', self.address) != None:
                raise UserError(_('The value of student Place of birth name must only letters'))

    # Validate student Number
    @api.constrains('id_number')
    def validate_id_number(self):
        if self.id_number:
            if not re.match("^[0-9]*$", self.id_number) != None:
                raise UserError(_('The value of Form  ID Number must be positive number'))

    # Validate applicant
    @api.constrains('applicant')
    def validate_applicant(self):
        if self.applicant:
            if not re.search(r'^(?:[^\W\d_]| )+$', self.applicant) != None:
                raise UserError(_('The value of applicant name must only letters'))

    # Validate job
    @api.constrains('job')
    def validate_job(self):
        if self.job:
            if not re.search(r'^(?:[^\W\d_]| )+$', self.job) != None:
                    raise UserError(_('The value of job  name must only letters')) # Validate job
    @api.constrains('fother_adress')
    def fother_fother_adress(self):
        if self.fother_adress:
            if not re.search(r'^(?:[^\W\d_]| )+$', self.fother_adress) != None:
                    raise UserError(_('The value of fother_adressmust only letters'))

    def action_confirm(self):
        pass
        # self.state = "done"
        val = " "
        for rec in self.other_desire:
            val += str(rec.name) + " \t - \t "
        self.env['napata.register'].create({

            'name': self.name,
            'first_name': self.first_name,
            'second_name': self.second_name,
            'third_name': self.third_name,
            'forth_name': self.forth_name,
            'college_id': self.college_id.id,
            'nationality': self.nationality.name,
            'address': self.address,
            'gender': self.gender,
            'religion': self.religion,
            'marital': self.social_status,
            'states': self.states_id,
            'local': self.Local_id,
            'type_id': self.id_type,
            'number_ids': self.id_number,
            'phone1': self.student_mobile,
            'phone2': self.watsapp_phone,
            'email': self.email,
            #     parint provider_name
            'provider_name': self.applicant,
            'fother_adress': self.fother_adress,
            'parent': self.relative_relation.name,
            'job': self.job,
            'phone3': self.telephone,
            # study  information
            'form_number': self.form_number,
            'school_name': self.school_name,
            'accept_year': self.accept_year,
            'cource': self.course,
            'siting_number': self.siting_number,
            'ratio': self.precentage,
            'program': self.main_desire.id,
            'athoer_desires': val,
            # fees
            'accept_type': self.type_acceptance,
            # 'application_fees': self.application_fees,
            'receipt_code': self.receipt_code,
            'pay_date': self.pay_date,
        })


