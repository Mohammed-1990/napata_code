from odoo import models, fields, api, exceptions,_


class PatientLaboratory(models.Model):
    _name = 'napata.laboratory'
    _description = 'laboratory'

    Photo= fields.Binary(string='Photo')
    patient_id = fields.Char(string='Patient ID', readonly=True)
    name = fields.Char(string="full name", readonly=True)
    first = fields.Char(string="First Name", readonly=True)
    second = fields.Char(string="   Second Name", readonly=True)
    third = fields.Char(string="Third Name", readonly=True)
    last = fields.Char(string="Last Name", readonly=True)
    gender=fields.Char(string="gender", readonly=True)
    dob = fields.Date(string='Date Of Birth')
    age = fields.Integer(string='Age')
    date = fields.Date(string='Date Requested')
    phone = fields.Integer(string="Phone", readonly=True)
    email = fields.Char(string="Email", readonly=True)
    nationality = fields.Char(string='Nationality', readonly=True)
    religion = fields.Char(string='Religion', readonly=True)
    program = fields.Char(string='Program', readonly=True)
    hom = fields.Char(string="Home", readonly=True)
    # The End Personal Information

    color = fields.Char(string="Color")
    reaction = fields.Char(string="Reaction")
    glucose = fields.Char(string='Glucose')
    protein = fields.Char(string='Protein')
    ketones = fields.Char(string='Ketones')
    pus = fields.Char(string="Pus Cells")
    rbs = fields.Char(string="R.B.Cs")
    epithel = fields.Char(string='Epithelial Cells')
    casts = fields.Char(string='Casts')
    crystals = fields.Char(string='Crystals')
    other = fields.Char(string='Others')

    hbv = fields.Char(string='HBV')
    hcv = fields.Char(string='HCV')
    hb = fields.Char(string='HB')
    ho = fields.Char(string='%')
    Blood_g = fields.Char(string='Blood Group')
    investig = fields.Char(string='Other Investigations')
    addiction = fields.Char(string='Drug Addiction')
    recommend = fields.Char(string='Recommendations')
    name_of = fields.Char(string='Name Of Examining doctor', readonly=True)
    date_two = fields.Date(string='Date')
    physician = fields.Char(string='PHYSICIAN')
    signature = fields.Char(string='Signature')
    
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
                    'laboratory_assessment': self.assessment,
                    'laboratory_diagonis': self.diagonis,
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
                    'laboratory_assessment': self.assessment,
                    'laboratory_diagonis': self.diagonis,
                   })

        # Nursing Do assessment
        self.is_assessment= True
        self.name_of = self.env.user.name



