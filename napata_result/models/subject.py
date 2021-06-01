
from odoo import models, fields, api
class subject(models.Model):
    _inherit = ['mail.thread']
    _name = 'napata.subject'
    _description = 'subject information '
    name = fields.Char(string="Subject")
    college_id = fields.Many2one('napata.collage', string='College',comput='get_program')
    program_id = fields.Many2one('napata.program', string='program')
    batch_id = fields.Many2one('napata.batch', string='batch')
    level_id = fields.Many2one('napata.level', string=' level')
    semester_id = fields.Many2one('napata.semester', string='semester',comput='get_semester')
    code = fields.Integer(string="Code")
    hours = fields.Integer(string="hours")
    date = fields.Date(string="Date")
    @api.onchange('level_id')
    def get_semester(self):
        get_semester_lest =[]
        level=self.env['napata.semester'].search([('academic_id','=',self.level_id.id)])
        if level:
            for rec in level:
                get_semester_lest.append(rec.id)

            return {'domain':{'semester_id':[('id','in',get_semester_lest)]}}

#
    @api.onchange('college_id')
    def get_program(self):
        get_program_lest =[]
        collage=self.env['napata.program'].search([('collage_id','=',self.college_id.id)])
        if collage:
            for rec in collage:
                get_program_lest.append(rec.id)

            return {'domain':{'program_id':[('id','in',get_program_lest)]}}

