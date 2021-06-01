
from odoo import models, fields, api, _, exceptions
from odoo.exceptions import ValidationError, UserError
import re


class napataCollage(models.Model):
    _inherit = ['mail.thread']
    _name = 'napata.collage'
    _description = 'collage name '
    name = fields.Char(string="Collage Name", required=True,help="enter Name of Collage" )

    @api.constrains('name')
    def validate_student_full_name(self):
            if self.name:
                if not re.search(r'^(?:[^\W\d_]| )+$',self.name) != None:
                    raise UserError(_('The value of college name must only letters'))




