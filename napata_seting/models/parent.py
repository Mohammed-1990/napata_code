
from odoo import models,fields,api
class napataParents(models.Model):
    _inherit = ['mail.thread']
    _name='napata.parent'
    _description="relative relation" 
    name=fields.Char(string="parent",required=True)
    



