from odoo import models, fields, api,_
import re
#
from odoo.exceptions import UserError



class feesType(models.Model):
    _inherit = ['mail.thread']
    _name = 'napata.feestype'
    _description = 'fees Type'
    name = fields.Char(string="Fees Type", required=True)

    # @api.constrains('name')
    # def validate_fees_type(self):
    #     if self.name:
    #         if not re.search(r'^(?:[^\W\d_]| )+$', self.name) != None:
    #             raise UserError(_('The value of  fees Type  must only letters'))

    _sql_constraints = [
        ('name_unique',
         'UNIQUE(name)',
         "The fees Type   must be unique"),
    ]





