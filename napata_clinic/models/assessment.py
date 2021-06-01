from odoo import models, fields, api, exceptions,_



class MedicalAssessment(models.Model):
    _name = 'napata.assessment'
    _description = 'napata Assessment'

    patient_id = fields.Char(string='Patient ID', readonly=True)
    name = fields.Char(string='Student Name', readonly=True)
    first = fields.Char(string="First Name", readonly=True)
    second = fields.Char(string="Second Name", readonly=True)
    third = fields.Char(string="Third Name", readonly=True)
    last = fields.Char(string="Last Name", readonly=True)
    gender=fields.Char(string="gender", readonly=True)
    dob = fields.Date(string='Date Of Birth')
    age = fields.Integer(string='Age', readonly=True)
    date = fields.Date(string='Date Requested')
    phone = fields.Integer(string="Phone", readonly=True)
    email = fields.Char(string="Email", readonly=True)
    nationality = fields.Char(string='Nationality', readonly=True)
    religion = fields.Char(string='Religion', readonly=True)
    program = fields.Char(string='Program', readonly=True)
    # The End Personal Infformation

    # For Nursing Lab

    nursing_diagonis = fields.Char(readonly=True, string='Nursing Diagonis')
    nursing_assessment = fields.Char(readonly=True, string='Nursing Assessment')
    
    # For Eye Lab
    eye_diagonis = fields.Char(readonly=True, string='Eye Diagonis')
    eye_assessment = fields.Char(readonly=True, string='Eye Assessment')

    # For Mouth Lab
    mouth_diagonis = fields.Char(readonly=True, string='Eye Diagonis')
    mouth_assessment = fields.Char(readonly=True, string='Eye Assessment')

    # For Physical Lab
    physical_diagonis = fields.Char(readonly=True, string='Physical Diagonis')
    physical_assessment = fields.Char(readonly=True, string='Physical Assessment')

    # For Laboratory Lab
    laboratory_diagonis = fields.Char(readonly=True, string='Laboratory Diagonis')
    laboratory_assessment = fields.Char(readonly=True, string='Laboratory Assessment')

    assess = fields.Text(string="The Evaluation Of Doctor")
    doctor = fields.Char(string='Doctor', readonly=True)
    date_exm = fields.Date(string="Date Of Examination")
    assess_type = fields.Selection(
        [('nursing', 'Nursing'), ('eye', 'Eye'),('mouth', 'Mouth'), ('physical', 'Physical'), ('labortory', 'Labortory')
         ])
    result = fields.Selection([('fitness', 'Fitness'), ('un fitness', 'Un Fitness')])
    is_register = fields.Boolean(string="Is Register")

    def _get_report_base_filename(self):
        return "My Main Report.pdf"

    # action for print report
    def print_assessment_report(self):
        # data = {
        #     'active_id': self._context.get('active_id'),
        #     }
        action = self.env.ref('napata_clinic.action_report_napata_assessment').report_action(self)
        action['context'] = {
            'active_id': self._context.get('active_id'),
            'active_model': 'napata.assessment',
        }
        return action

    def get_student_name(self):
        for re in self:
            re.name = str(re.first) + " " + str(re.second) + " " + str(re.third) + " " + str(re.last)


    # Func send to registeration
    def send_to_register(self):
        if (self.nursing_diagonis and self.nursing_assessment) and (self.eye_diagonis and self.eye_assessment) and (self.mouth_diagonis and self.mouth_assessment) and (self.physical_diagonis and self.physical_assessment) and (self.laboratory_diagonis and self.laboratory_assessment):
            pass
        else:
            raise exceptions.UserError(_('All assessment must be completed'))


        result = self.env['napata.register'].search([('receipt_code', '=', self.patient_id)])
        if result:
            for rec in result:
                rec.update(
                    {
                    'result': self.result,
                    }
                )
        else:
        
            self.env['napata.register'].create({
                'name': self.name,
                'first_name': self.first,
                'second_name': self.second,
                'third_name': self.third,
                'forth_name': self.last,
                'gender': self.gender,
                'email': self.email,
                'nationality': self.nationality,
                'religion': self.religion,
                'program': self.program,
                'receipt_code': self.patient_id,
                'phone1': self.phone,
                'medical_report': self.assess,
                'result': self.result,
                'doctor_name': self.doctor,
                'doctor_date': self.date_exm,
               })

        # Cofirm
        self.is_register= True
        self.doctor = self.env.user.name
       