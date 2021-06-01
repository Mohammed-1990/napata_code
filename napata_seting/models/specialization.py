
from odoo import models, fields, api

class napataSpecialization(models.Model):
    _inherit = ['mail.thread']
    _name = 'napata.specialization'
    _description = 'specialization name '
    name = fields.Char(string="Specialization", required=True,help="enter Name of Specialization")
    college_id= fields.Many2one('napata.collage',
        ondelete='cascade', string="Collage ", required=True)
    program_id= fields.Many2one('napata.program',
        ondelete='cascade', string="Programs", required=True )
    
  


