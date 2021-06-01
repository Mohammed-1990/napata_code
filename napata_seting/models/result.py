

from odoo import models, fields, api 


class result(models.Model):
    _inherit = ['mail.thread']
    _name = 'napata.result'
    _description = 'university result '
    name = fields.Char(string="Academic position", required=True)




