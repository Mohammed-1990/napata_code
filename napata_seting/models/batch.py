from datetime import datetime
from odoo import models, fields, api, _, exceptions
from odoo.exceptions import ValidationError, UserError
import re


class napataBatch(models.Model):
    _inherit = ['mail.thread']
    _name = 'napata.batch'
    _order = "id desc"
    _description = 'the batch name '
    college_id = fields.Many2one('napata.collage',
        ondelete='cascade', string="Collage Name", required=True,
    default = lambda self: self.env['napata.collage'].search([]))
    program_id = fields.Many2one('napata.program',  ondelete='cascade',string='program')
    name = fields.Char(string="Batch Name", required=True)
    year = fields.Char(string='Study Year', default=str(datetime.today().year)+" - "+str(datetime.today().year+1))
    add_year = fields.Char(default=datetime.today().year)
    @api.onchange('college_id')
    def get_program(self):
        get_program_lest = []
        collage = self.env['napata.program'].search([('collage_id', '=', self.college_id.id)])
        if collage:
            for rec in collage:
                get_program_lest.append(rec.id)

            return {'domain': {'program_id': [('id', 'in', get_program_lest)]}}






