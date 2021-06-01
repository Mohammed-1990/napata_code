

from odoo import models, fields, api 


class napataUniversity(models.Model):
    _inherit = ['mail.thread']
    _name = 'napata.semester'
    _description = 'Semester name '
    name = fields.Char(string="Semester", required=True)
    academic_id = fields.Many2one('napata.level', string='Academic level')



