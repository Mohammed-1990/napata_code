from odoo import models, fields, api, exceptions,_


class LapPatient(models.Model):
    _name = 'napata.eye'
    _description = 'Eye'

    patient_image = fields.Binary(string='Photo')
    patient_id = fields.Char(string='Patient ID', readonly=True)
    name = fields.Char(string="full name", readonly=True)
    first = fields.Char(string="First Name", readonly=True)
    second = fields.Char(string="Second Name", readonly=True)
    third = fields.Char(string="Third Name", readonly=True)
    last = fields.Char(string="Last Name", readonly=True)
    gender=fields.Char(string="gender", readonly=True)
    dob = fields.Date(string='Date Of Birth')
    age = fields.Integer(string='Age')
    date = fields.Date(string='Date Requested')
    phone = fields.Char(string="Phone", readonly=True)
    email = fields.Char(string="Email", readonly=True)
    nationality = fields.Char(string='Nationality', readonly=True)
    religion = fields.Char(string='Religion', readonly=True)
    program = fields.Char(string='Program', readonly=True)
    # The End Personal Information
    
    general = fields.Char(string="General Vision")
    withoutglss = fields.Char(string="With Out Glasses")
    withglasses = fields.Char(string='With  Glasses')
    color = fields.Char(string='Color Vision')
    near = fields.Char(string='Near Vision')
    opthahmologist = fields.Char(string='Opthahmologist', readonly=True)
    hom = fields.Char(string="Home")
    
    assessment = fields.Text(string="Assessment")
    diagonis = fields.Text(string='Diagonis')

    is_assessment = fields.Boolean(string="Is assessment")


    def get_student_name(self):
        for re in self:
            re.name = str(re.first) + " " + str(re.second) + " " + str(re.third) + " " + str(re.last)

   # Func send to assessment
    def send_student_assessment(self):
        if self.assessment and self.diagonis:
            pass
        else:
            raise exceptions.UserError(_('You must fill in both diagonis and assessment for student'))

        result = self.env['napata.assessment'].search([('patient_id', '=', self.patient_id)])
        if result:
            for rec in result:
                rec.update(
                    {
                    'eye_assessment': self.assessment,
                    'eye_diagonis': self.diagonis,
                    }
                )
        else:
            self.env['napata.assessment'].create({
                    'name': self.name,
                    'first': self.first,
                    'second': self.second,
                    'third': self.third,
                    'last': self.last,
                    'gender': self.gender,
                    'email': self.email,
                    'nationality': self.nationality,
                    'religion': self.religion,
                    'program': self.program,
                    'patient_id': self.patient_id,
                    'phone': self.phone,
                    'eye_assessment': self.assessment,
                    'eye_diagonis': self.diagonis,
                   })

        # Nursing Do assessment
        self.is_assessment = True
        self.opthahmologist = self.env.user.name


