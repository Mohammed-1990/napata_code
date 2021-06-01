import datetime
from num2words import num2words
from odoo import models, fields, api, _
from odoo.exceptions import UserError


class CreateRegister(models.TransientModel):
    _name = 'create.register'
    _description = "Create User for selected Student(s)"
    managemanent_fees = fields.Many2one(
        'napata.managemanentfees', string='Managemanent Fees')
    student_ids = fields.Many2one(
        'napata.register', string='Student Name')
    other_ids = fields.Many2one(
        'napata.feestype', string='Other Expenses')
    appointment_date = fields.Char(string="appointment Date")
    main_desires = fields.Many2one("napata.program", ondelete="cascade",string="oprogram")
    college =fields.Many2one('napata.collage', string='the college',
                             ondelete='cascade', required=True )
    level = fields.Many2one('napata.level', string='the level',
                            ondelete='cascade', required=True)
    semester = fields.Many2one('napata.semester',string='Semester',
                               ondelete='cascade')

    register_fees = fields.Float(straing='Register Fees')
    the_amount  = fields.Float(straing='the amount')
    inser_amount  = fields.Float(straing='Specified amount')
    program_fees = fields.Float(string="Study Fees")
    certificate_type = fields.Char(string="certificate type Fees")
    other_fees = fields.Float(string="Other Fees")
    firest_installment_fees = fields.Selection([
        ('1', '100%'),
        ('2', '50%'), ],string="First installment")

    discount_fees= fields.Float(string=" The Discount")
    fina_flees=fields.Float(string="Final Fees")
    total_received = fields.Float(string="Total Received Fees")
    is_pay_sd = fields.Boolean(string="Pay in Sudanese", required=True)
    is_first_installment= fields.Boolean()
    student_managemanent_fees = fields.Float(string="managemanent Fees")
    the_register_amount = fields.Char(string="the  student Amount ")
    the_abut = fields.Char(string="the  Managemanent Amount ")
    is_managemanent = fields.Boolean( default=False )
    @api.onchange('managemanent_fees')
    def get_student_management_fees(self):
        curr_year = datetime.datetime.now().year
        managemanentfees = self.env['napata.managemanentfees'].search([('year', '=', curr_year)])
        if managemanentfees:
            self.the_register_amount=" "
            self.total_received=0.0
            for rec in managemanentfees:
                if rec == self.managemanent_fees:
                    if self.certificate_type == "sudanese":
                        self.student_managemanent_fees = self.managemanent_fees.sudanes_managemanentfees
                        self.the_abut = " فقط " + str(
                                "\t " + num2words(self.student_managemanent_fees, lang='ar')) + " \t    جنية سوداني لا  غير"
                    elif self.certificate_type == 'foreign':
                           if self.is_pay_sd:
                               self.student_managemanent_fees = self.managemanent_fees.sudanes_managemanentfees
                               self.the_abut = " فقط " + str(
                                   "\t " + num2words(self.student_managemanent_fees,
                                                     lang='ar')) + " \t    جنية سوداني لا  غير"
                           else:
                               self.student_managemanent_fees = self.managemanent_fees.foreig_managemanentfees
                               self.the_abut = " فقط " + str(
                                   "\t " + num2words(self.student_managemanent_fees, lang='ar')) + " \t     دولار  امريكي لا  غير"

                    else:
                        self.student_managemanent_fees = 0.0



    @api.onchange('student_ids')
    def create_appointment(self):
        filtered_b_ids = self.env['napata.register'].search([('id', '=', int(self.student_ids.id))])
        if filtered_b_ids:
            self.appointment_date = filtered_b_ids.accept_type
            self.main_desires = filtered_b_ids.program.id
            self.certificate_type=filtered_b_ids.certificate_type
            self.register_fees=filtered_b_ids.register_fees
            self.discount_fees=filtered_b_ids.discount_fees
            self.college=filtered_b_ids.college_id
            self.level = filtered_b_ids.level
            self.semester = filtered_b_ids.semester
            self.program_fees=filtered_b_ids.Remaining_amount
            self.is_first_installment=filtered_b_ids.is_first_installment



    

    @api.onchange('firest_installment_fees')
    def _get_total_fees(self):
        if self.firest_installment_fees:
            self.the_abut = " "
            self.student_managemanent_fees = 0.0
            if self.certificate_type == "sudanese":
                if self.firest_installment_fees == '1':
                    if self.is_first_installment:

                        self.total_received = self.program_fees + self.register_fees
                        self.the_register_amount = " فقط " + str(
                            "\t " + num2words(self.total_received, lang='ar')) + " \t    جنية سوداني لا  غير"


                    else:
                        self.total_received = self.program_fees
                        self.the_register_amount = " فقط " + str(
                            "\t " + num2words(self.total_received, lang='ar')) + " \t    جنية سوداني لا  غير"

                elif  self.firest_installment_fees == '2':
                    if self.is_first_installment:
                        self.total_received = (self.program_fees /2)+ self.register_fees
                        self.the_register_amount = " فقط " + str(
                            "\t " + num2words(self.total_received, lang='ar')) + " \t    جنية سوداني لا  غير"
                    else:
                        self.total_received = (self.program_fees/2)
                        self.the_register_amount = " فقط " + str(
                            "\t " + num2words(self.total_received, lang='ar')) + " \t    جنية سوداني لا  غير"
            elif self.certificate_type == "foreign":
                if self.firest_installment_fees == '1':
                    if self.is_first_installment:
                        self.total_received = self.program_fees + self.register_fees
                        self.the_register_amount = " فقط " + str(
                                "\t " + num2words(self.total_received, lang='ar')) + " \t     دولار  امريكي لا  غير"
                    else:
                        self.total_received = self.program_fees
                        self.the_register_amount = " فقط " + str(
                            "\t " + num2words(self.total_received, lang='ar')) + " \t     دولار  امريكي لا  غير"
                elif self.firest_installment_fees == '2':
                    if self.is_first_installment:
                        self.total_received = (self.program_fees / 2) + self.register_fees
                        self.the_register_amount = " فقط " + str(
                            "\t " + num2words(self.total_received, lang='ar')) + " \t     دولار  امريكي لا  غير"
                    else:
                        self.total_received = (self.program_fees / 2)
                        self.the_register_amount = " فقط " + str(
                            "\t " + num2words(self.total_received, lang='ar')) + " \t     دولار  امريكي لا  غير"
        else:
            self.total_received=0.0
            self.the_register_amount= ""

    def create_registration(self):
        program=self.main_desires.id
        the_amount=self.the_register_amount
        the_fees=0.0
        if  self.total_received >  1:
            the_fees= self.total_received
            the_about="رسوم دراسية"



        elif self.student_managemanent_fees > 1:
         the_about=self.managemanent_fees.name.name
         the_fees=self.student_managemanent_fees
         the_amount=self.the_abut
         self.is_managemanent = True

        if the_fees == 0.0 :
            raise UserError(_('The value of student name must only letters'))

        else:
            self.env['napata.accounting'].create({
                    'name': self.student_ids.name,
                    'first': self.student_ids.first_name,
                    'second': self.student_ids.second_name,
                    'third': self.student_ids.third_name,
                    'last': self.student_ids.forth_name,
                    'college': self.college.id,
                    'level': self.level.id,
                    'semester': self.semester.id,
                    'program': program,
                    'presentation': True,
                    'register_office': True,
                    'type_of_fees': self.is_managemanent,
                    'the_fees': the_fees,
                    'the_amount': the_amount,
                     'about': the_about,
                })