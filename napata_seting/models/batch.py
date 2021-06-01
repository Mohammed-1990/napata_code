
from odoo import models, fields, api, _, exceptions
from odoo.exceptions import ValidationError, UserError
import re


class napataBatch(models.Model):
    _inherit = ['mail.thread']
    _name = 'napata.batch'
    _description = 'the batch name '
    name = fields.Char(string="Batch Name", required=True)






