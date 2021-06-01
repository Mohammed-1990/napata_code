from odoo import models, fields, api, exceptions
class registerResignation(models.Model):
    _inherit = ['mail.thread']
    _name = 'napata.register.esignation'
    _description = 'freezing information'
    name = fields.Char(string="full name")
    college = fields.Many2one("napata.collage", ondelete="cascade", string="College")
    program = fields.Many2one("napata.program", ondelete="cascade", string="Program")
    level = fields.Many2one('napata.level', string='the level',ondelete='cascade')
    semester = fields.Many2one('napata.semester', string='Semester',ondelete='cascade')
    sitting_number = fields.Integer(string='Sitting number')
    location_exam = fields.Char(string='School')
    date_admission = fields.Char(string='Date of admission')
    academic_position = fields.Many2one('napata.result', string='academic position', ondelete='cascade')
    reasons = fields.Many2one('napata.dismissalreasons', string='Reason', ondelete='cascade')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('registrar', 'Registrar'),
        ('coordinator', 'Coordinator'),
        ('scientific', 'Scientific affairs'),
        ('done', 'done'),
    ], string='Status', default="draft", readonly=True)
    date = fields.Date(string='date')
