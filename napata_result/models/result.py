
from odoo import models, fields, api
class result(models.Model):
    _inherit = ['mail.thread']
    _name = 'napata.degree'
    _description = 'result information '

    @api.onchange('semester_id')
    def get_subject(self):
        get_subject_lsit = []
        collage = self.env['napata.subject'].search([])
        for rec in collage:
            if rec.program_id.name == self.program_id.name:
                if rec.level_id.name == self.level_id.name:
                    if rec.semester_id.name == self.semester_id.name:
                        get_subject_lsit.append((str(rec.name), str(rec.name)))
        return get_subject_lsit
    name = fields.Selection(get_subject,string=" exm_year")

    college_id = fields.Many2one('napata.collage', string='College',comput='get_program')
    program_id = fields.Many2one('napata.program', string='program')
    batch_id = fields.Many2one('napata.batch', string='batch')
    level_id = fields.Many2one('napata.level', string=' level')
    semester_id = fields.Many2one('napata.semester', string='semester',comput='get_semester')
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






