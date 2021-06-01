from odoo import models, fields, api, exceptions

class  dismissalReasons(models.Model):
    _inherit = ['mail.thread']
    _name = 'napata.dismissalreasons'
    _description = 'dismissal Reasons'
    name = fields.Char(string="Reasons ")
