# -*- coding: utf-8 -*-

from datetime import datetime
from odoo import models, fields, api, exceptions


class napataRegister(models.Model):
    _inherit = ['mail.thread']
    _order = "id desc"
    _name = 'napata.register'
    _description = 'information register'

    name = fields.Char(string="student's name", readonly=True)
    first_name = fields.Char(string='First Name')
    second_name = fields.Char(string='Second Name')
    third_name = fields.Char(string='Third Name')
    forth_name = fields.Char(string='Fourth Name')
    certificate_type = fields.Selection([
        ('sudanese', 'Sudanese'),
        ('foreign', 'Foreign'), ],
        string="Nationality")
    address=fields.Char(string="address")
    nationality=fields.Char(string="Nationality")
    type_id=fields.Char(string="Type of identification")
    number_ids=fields.Char(string="identification Number")
    gender=fields.Char(string="gender")
    religion=fields.Char(string="religion")
    marital=fields.Char(string="marital")
    phone1 = fields.Char(string=" Phone Number")
    phone2 = fields.Char(string="WatsApp")
    email = fields.Char(string="Email")
    states= fields.Char(string="State Name")
    local = fields.Char(string="Local Name")
    # Parent info
    provider_name = fields.Char(string="Applicant Name")
    fother_adress = fields.Char(string="fother Adress")
    job = fields.Char(string="job")
    parent = fields.Char(string="parent")
    phone3 = fields.Char(string="Phone Number")
    # education info
    year = fields.Char(string='Study Year', default=str(datetime.today().year)+" - "+str(datetime.today().year+1))
    accept_type=fields.Many2one("napata.presentationtype",ondelete="cascade", string='acceptance Type')
    accept_year = fields.Char(straing=' Year of acceptance')
    school_name = fields.Char(string="School Name")
    exam_year = fields.Date(string='Exam year')
    cource = fields.Char(straing='cource')
    siting_number= fields.Char(string="Sitting Number" )
    ratio = fields.Float(string="The Precentage")
    program =fields.Many2one("napata.program", ondelete="cascade", string="Program")

    athoer_desires =fields.Char(straing='other Desires')
    pay_date = fields.Char(string='Received  Date')
    # fees
    fee_paid_id = fields.One2many(
        'napata.feepaid', 'student_id', string="Sessions")
    certificate_type = fields.Selection([
        ('sudanese', 'Sudanese'),
        ('foreign', 'Foreign'), ],
        string="Nationality")
    discount = fields.Selection([
        ('0', '00%'),
        ('10', '10%'),
        ('20', '20%'),
        ('30', '30%'),
        ('40', '40%'), ], default='0',
        string="Discount Percentage")
    total_fees = fields.Float(string="Total Assessed Fees")
    register_fees = fields.Float(string="register  Fees")
    discount_fees = fields.Float(string="discount Fees")
    total_received = fields.Float(string="Total Received Fees")
    Remaining_amount = fields.Float(string="Remaining amount ")
    is_first_installment = fields.Boolean( default=True )
    degree = fields.Float(string='degree')
    id_type = fields.Char(string='Type of identification')
    id_number= fields.Integer(string="ID Number" )
    receipt_code = fields.Char(string='	Receipt Number ')
#     acadimaic
    form_number = fields.Char(string=' Form number')
    college_id =fields.Many2one('napata.collage', string='college',
                             ondelete='cascade')
    semester = fields.Many2one('napata.semester',string='Semester',
                               ondelete='cascade',
                               default=lambda self: self.env['napata.semester'].search([]))

    level=fields.Many2one('napata.level', string='the level',
                             ondelete='cascade',
                          default=lambda self: self.env['napata.level'].search([]))

    batch = fields.Many2one('napata.batch',string='batch',
                               ondelete='cascade')
    academic_position=fields.Many2one('napata.result', string='academic position',
                             ondelete='cascade')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'done'),
    ], string='Status', default="draft", readonly=True)
    # medicalreport
    comment = fields.Text(string="medical report")
    doctor_name = fields.Char(string="Doctor's name")
    result = fields.Char(string="result")
    result_data = fields.Char(string="Result date")
    # The new added
    is_clinic = fields.Boolean(string="Is Clinic")



    @api.onchange('certificate_type')
    def get_study_and_regist_fees(self):
        curr_year = datetime.now().year
        print(curr_year)
        fees = self.env['napata.studyfees'].search([('year', '=',self.accept_year)])
        if fees:

            # if self.certificate_type:
            for rec in fees:
                if rec.program.id == self.program.id:

                    if self.certificate_type == 'sudanese':
                        self.total_fees = rec.sudaness_study
                        self.register_fees = rec.sdn_register_fees
                        self.total_received = rec.sudaness_study
                        self.Remaining_amount = rec.sudaness_study
                    elif self.certificate_type == 'foreign':
                        self.total_fees = rec.foreigners_study
                        self.Remaining_amount = rec.foreigners_study
                        self.total_received = rec.foreigners_study
                        # self.fina_flees = rec.foreigners_study
                        self.register_fees = rec.foriegn_register_fees
                    # else:
                    #     self.program_fees = 0.0
                    #     self.fina_flees = 0.0
                    #     self.register_fees = 0.0
                    #     self.discount_fees = 0.0
                    #     self.total_received = 0.0
                    #     self.the_register_amount = ""

    @api.onchange('discount')
    def get_discount(self):
        if self.total_fees > 0.0:
            self.discount_fees = (self.total_fees * float(self.discount)) / 100
            self.Remaining_amount = self.total_fees - (self.total_fees * float(self.discount)) / 100
            self.total_received = self.total_fees - (self.total_fees * float(self.discount)) / 100
        else:
            self.discount_fees = 0.0



    # Func to open wizard
    def send_student_clinic(self):
        self.is_clinic= True
        # 1- For Nursing
        self.env['napata.nursing'].create({
                'name': self.name,
                'first': self.first_name,
                'second': self.second_name,
                'third': self.third_name,
                'last': self.forth_name,
                'gender': self.gender,
                # 'dob': self.age,
                'email': self.email,
                'nationality': self.nationality,
                'religion': self.religion,
                'program': self.program,
                'patient_id': self.receipt_code,
                'phone': self.phone1,
                'hom': self.address,
               })

        # 2- For Eye
        self.env['napata.eye'].create({
                'name': self.name,
                'first': self.first_name,
                'second': self.second_name,
                'third': self.third_name,
                'last': self.forth_name,
                'gender': self.gender,
                # 'dob': self.age,
                'email': self.email,
                'nationality': self.nationality,
                'religion': self.religion,
                'program': self.program.id,
                'patient_id': self.receipt_code,
                'phone': self.phone1,
                'hom': self.address,
               })

        # # 3- For Mouth
        self.env['napata.mouth'].create({
                'name': self.name,
                'first': self.first_name,
                'second': self.second_name,
                'third': self.third_name,
                'last': self.forth_name,
                'gender': self.gender,
                # 'dob': self.age,
                'email': self.email,
                'nationality': self.nationality,
                'religion': self.religion,
                'program': self.program,
                'patient_id': self.receipt_code,
                'phone': self.phone1,
                'hom': self.address,
               })

        # # 4- For Physical
        self.env['napata.physical'].create({
                'name': self.name,
                'first': self.first_name,
                'second': self.second_name,
                'third': self.third_name,
                'last': self.forth_name,
                'gender': self.gender,
                # 'dob': self.age,
                'email': self.email,
                'nationality': self.nationality,
                'religion': self.religion,
                'program': self.program,
                'patient_id': self.receipt_code,
                'phone': self.phone1,
                'hom': self.address,
               })

        # # 5- For Laboratory
        self.env['napata.laboratory'].create({
                'name': self.name,
                'first': self.first_name,
                'second': self.second_name,
                'third': self.third_name,
                'last': self.forth_name,
                'gender': self.gender,
                # 'dob': self.age,
                'email': self.email,
                'nationality': self.nationality,
                'religion': self.religion,
                'program': self.program,
                'patient_id': self.receipt_code,
                'phone': self.phone1,
                'hom': self.address,
               })


































