
from odoo import models, fields, api,_
import re
#
from odoo.exceptions import UserError


class napataDepartment(models.Model):
    _inherit = ['mail.thread']
    _name = 'napata.program'
    _description = ' department name '
    name = fields.Char(string="Programs", required=True,help="enter Name of Department")
    collage_id= fields.Many2one('napata.collage',
        ondelete='cascade', string="Collage Name", required=True,
    default = lambda self: self.env['napata.collage'].search([]))


    code=fields.Char(string="Code" ,required=True,size=12)

    @api.constrains('name')
    def validate_student_full_name(self):
        if self.name:
            if not re.search(r'^(?:[^\W\d_]| )+$', self.name) != None:
                raise UserError(_('The value of college name must only letters'))

    @api.constrains('code')
    def validate_college_code(self):
        if self.code:
            if self.code == None:
                raise UserError(_('The value of college code must be positive number'))

    _sql_constraints = [
        ('name_unique',
         'UNIQUE(name)',
         "The name must be unique"),
        ('code_unique',
         'UNIQUE(code)',
         "The code  must be unique"),
    ]





