
from odoo import models, fields,api

class AssessmentReprtWizard(models.TransientModel):
    _name = 'assessment.wizardreport'
    _description = "Create Medical Assessment Report"
    

    patient_id = fields.Many2one('nursing.lap', string='Patient ID', readonly=True)
    name = fields.Char(string='Student Name')
    gender = fields.Selection(
        [('m', 'Male'), ('f', 'Female'),
         ], 'Gender', required=True)
    dob = fields.Date(string='Date Of Birth', required=True)
    age = fields.Char(string='Age')
    date = fields.Date(string='Date Requested')
    phone = fields.Char(string="Phone", required=True)
    email = fields.Char(string="Email", required=True)
    nationality = fields.Char(string='nationality', required=True)
    religion = fields.Char(string='religion')
    program = fields.Char(string='program')
    
    assessment = fields.Text(string="Assessment", required=True)
    diagonis = fields.Text(string='Diagonis', required=True)
    signature = fields.Char(string='Signature')
    doctor = fields.Char(string='Doctor')
    assess_type = fields.Selection(
        [('nursing', 'Nursing'), ('eye', 'Eye'),('mouth', 'Mouth'), ('physical', 'Physical'), ('labortory', 'Labortory')
         ],  required=True)

    def create_assessment_wizard(slef):
        



        print("OK")





