
from odoo import models, fields, api 
class napataNationalities(models.Model):
    _name = 'napata.nationalities'
    _description = 'nationalities name '
    name = fields.Char(string="Nationalities", required=True,help="Nationalities")


