from odoo import models, fields, api, exceptions

class clearanceRequest(models.Model):
    _inherit = ['mail.thread']
    _name = 'napata.clearance'
    name = fields.Char(string="full name")
    _description = 'Clearance information'
    program=fields.Char(string="program")
    level=fields.Char(string="level")
    semester = fields.Char(string='Semester')
    form_number = fields.Char(string='student number')
    student_sign = fields.Char(string='student signature ')
    student_sign_date = fields.Date(string='student signature date')
    program_coordinator = fields.Char(string='pogram coordinator ')
    program_coor_comment  = fields.Text(string=" program coordinator commet")
    program_coor_sign = fields.Char(string=' program coordinator signature ')
    program_coor_sign_date = fields.Date(string=' program coordinator signature date')
    lab_sup_comment  = fields.Text(string=" lab supervisor commet")
    lab_supervisor = fields.Char(string='Lab supervisor ')
    lab_sup_sign = fields.Char(string=' program coordinator signature ')
    lab_sup_sign_date = fields.Date(string='lab_supervisor signature date')

    student_supervisor = fields.Char(string='Student supervisor ')
    student_sup_commet = fields.Text(string='Student supervisor  commet')
    student_sup_sign = fields.Char(string='Student supervisor signature ')
    student_sup_sign_date = fields.Date(string='Student supervisor signature date')

    librarian_commet = fields.Text(string='Librarian commet')
    librarian = fields.Char(string='Librarian ')
    librarian_sign = fields.Char(string='Librarian signature ')
    librarian_sign_date = fields.Date(string='Librarian signature date')
     
    financial_commet = fields.Text(string='financial officer commet')
    financial_officer = fields.Char(string='Chief Financial Officer ')
    financial_off_sign = fields.Char(string='Chief Financial Officer signature ')
    financial_off_sign_date = fields.Date(string='Chief Financial Officer signature date')
    
    agent_commet = fields.Text(string='agent officer commet')
    agent_officer = fields.Char(string='agent')
    agent_sign = fields.Char(string='agent signature ')
    agent_sign_date = fields.Date(string='agentsignature date')

    decision = fields.Text(string='the decision')
    signature = fields.Char(string=' signature ')
    date = fields.Date(string='date')