from odoo import models, fields, api,_
import re
#
from odoo.exceptions import UserError


class napatapresntaionTyp(models.Model):
    _inherit = ['mail.thread']
    _name = 'napata.presentationtype'
    _description = 'presentationtype '
    name = fields.Char(string="PresntaionType", required=True)

    @api.constrains('name')
    def validate_presentaion_type_name(self):
        if self.name:
            if not re.search(r'^(?:[^\W\d_]| )+$', self.name) != None:
                raise UserError(_('The value of Presntaion Type  must only letters'))

    _sql_constraints = [
        ('name_unique',
         'UNIQUE(name)',
         "The Presntaion type must be unique"),
    ]


