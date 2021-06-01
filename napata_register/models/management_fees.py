from odoo import models, fields, api
import datetime

class managementFees(models.Model):
    _inherit = ['mail.thread']
    _name = 'napata.managemanentfees'
    _description = 'information managemanentfees'
    name = fields.Many2one('napata.feestype', string="Fees Type ",
                                ondelete='cascade')
    sudanes_managemanentfees=fields.Integer(string="Sudanes ",required=True)
    # sudanes=fields.Float(string="The Sudanese",required=True)
    # foreig=fields.Float(string="The Sudanese",required=True)
    foreig_managemanentfees=fields.Integer(string="Foreign ",required=True)
    year = fields.Char('Study Year',  default=lambda self: datetime.datetime.now().year)