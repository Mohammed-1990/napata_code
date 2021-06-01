import datetime
from odoo import models, fields, api, exceptions,_



class NursingLap(models.Model):
    _name = 'napata.nursing'
    _description = 'Nursing'

    # patient_image = fields.Binary(string='Photo')
    patient_id = fields.Char(string='Patient ID', readonly=True)
    name = fields.Char(string="Full Name", compute="get_student_name")
    first = fields.Char(string="First Name", readonly=True)
    second = fields.Char(string="Second Name", readonly=True)
    third = fields.Char(string="Third Name", readonly=True)
    last = fields.Char(string="Last Name", readonly=True)
    gender = fields.Char(string="gender", readonly=True)
    dob = fields.Date(string='Date Of Birth')

    # age = fields.Many2one('na.collage',
    #                             ondelete='cascade', string=" School Name", required=True)
    age = fields.Integer(string='Age')
    date = fields.Date(string='Date ',defualt= lambda sef:datetime)
    phone = fields.Char(string="Phone", readonly=True)
    email = fields.Char(string="Email", readonly=True)

    # nationality
    nationality = fields.Char(string="Nationality", readonly=True)
    #
    
    religion = fields.Char(string='Religion', readonly=True)

    program = fields.Char(string='Program', readonly=True)

    hom = fields.Char(string="Home", readonly=True)
    # The end personal information
    
    elementary = fields.Char(string="Elementary")
    intermediate = fields.Char(string='Intermediate')
    secondary = fields.Char(string='Secondary')
    home = fields.Char(string='Home')
    University = fields.Char(string="University fee ls")
    bursary = fields.Char(string='Bursary ls')
    height = fields.Char(string='Height')
    weight = fields.Char(string='Weight')
    pulse = fields.Char(string="Pulse")
    bp = fields.Char(string='B.P')
    # start famiy
    tube = fields.Boolean('Tuberculosis')
    chronic = fields.Boolean('Chronic Cough')
    diabetes = fields.Boolean('Diabetes Mellitus')
    hypertension = fields.Boolean('Hypertension')
    heart = fields.Boolean('HeartDisease')
    typhoid = fields.Boolean('typhoid')
    dysentery = fields.Boolean('Dysentery')
    asthma = fields.Boolean('Asthma')
    syphlls = fields.Boolean('Syphllls')
    hay2 = fields.Boolean('Hay Fever')
    eczema2 = fields.Boolean('Eczema')
    skin = fields.Boolean('Other Skin Disease')
    pept = fields.Boolean('Peptic Ulcer')
    migrain = fields.Boolean('Megraine')
    epile = fields.Boolean('Epilepsy')
    nervous = fields.Boolean('Nervous Trouble')
    illness = fields.Boolean('Other Illness')
    hepatit = fields.Boolean('Hepatitis')
    # end family
    
# start history
    malaria = fields.Boolean('Malaria')
    infective2 = fields.Boolean('Infective Hepatitis')
    sore = fields.Boolean('Sore throat')
    chest = fields.Boolean('Chest Trouble')
    eczema = fields.Boolean('Eczema')
    hay = fields.Boolean('Hay Feve')
    none = fields.Boolean('None')
    bilharz = fields.Boolean('Bilharzias')
    cough = fields.Boolean('Whooping Cough')
    mumps = fields.Boolean('Mumps')
    tuber = fields.Boolean('Tuberculosis')
    trouble = fields.Boolean('Heart Trouble')
    rheumatism = fields.Boolean('Rheumatism')
    pain = fields.Boolean('Chronic Abdominal Pain')
    peptic_ulcer = fields.Boolean('Peptic Ulcer')
    worms = fields.Boolean('Intestinal Worms')
    dysant = fields.Boolean('Dysantery')
    onchocer = fields.Boolean('Onchocerciasis')
    sensitiv = fields.Boolean('sensitivity to any drug')
    breakdown = fields.Boolean('Nervous Breakdown')
    exams = fields.Boolean('Nervous trouble with exams')
    dysam = fields.Boolean('Dysamenmhoea')

    # end history
    tonsillectomy = fields.Boolean('Tonsillectomy')
    appendisectomy = fields.Boolean('Appendisectomy')
    peptic = fields.Boolean('Peptic')
    accidents = fields.Boolean('Accidentse')
    other = fields.Date('Other')
    small = fields.Date('Small Box')
    yellow = fields.Date('Yellow Fever')
    bcg = fields.Date('B.C.G')
    typhoid1 = fields.Date('Typhoid')
    infective = fields.Date('Infective Hepatitis')
    other2 = fields.Boolean('Others')
    alive = fields.Boolean('IS HE ALIVE?')
    dead = fields.Boolean('Dead')
    age = fields.Char('Your age when he died')
    occupation = fields.Char('job')
    education = fields.Char('Educational Level')
    alive2 = fields.Boolean('IS HE ALIVE?')
    dead2 = fields.Boolean('Dead')
    age2 = fields.Integer('Your age when he died')
    divorced2 = fields.Char('divorced')
    education2 = fields.Char('Educational Level')
    parents = fields.Boolean('Both Parents')
    father = fields.Boolean(' With Father')
    mother = fields.Boolean('With Mother')
    relative = fields.Boolean('With Relative')
    sibling = fields.Char('Number of Sibling')
    place = fields.Char('Your Arrangement in The Family')
    alcohol = fields.Boolean('Do You Use Alcohol')
    tobacco = fields.Boolean('Do You Use Tobacco')
    snuff = fields.Boolean('Do You Use Snuff')
    hashish = fields.Boolean('Do You Use Hashish')
    otherh = fields.Boolean('Other Habits')
    assessment = fields.Text(string="Assessment")
    diagonis = fields.Text(string='Diagonis')
    nursing = fields.Char(string='Name', readonly=True)
    
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
                    'nursing_assessment': self.assessment,
                    'nursing_diagonis': self.diagonis,
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
                    'nursing_assessment': self.assessment,
                    'nursing_diagonis': self.diagonis,
                   })

        # Nursing Do assessment
        self.is_assessment= True
        self.nursing = self.env.user.name






    