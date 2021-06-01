
from odoo import models, fields, api, exceptions
import datetime

class activePresentaion(models.Model):
    _inherit = ['mail.thread']
    _name = 'napata.activepresentaion'
    _description = 'active presentaion '
    name = fields.Many2one('napata.presentationtype', string='PresntaionType',
                             ondelete='cascade', required=True)
    year = fields.Char(string='Date ',  default=lambda self:datetime.datetime.today().strftime('%Y-%m-%d'))
    @api.onchange('name')
    def _get_active_presentaion(self):
        val= self.env['napata.accounting'].search([])
        val="alli"

        print("*"*10)
        for re in val:

         print("*"*10)
         print(re.id)
         print("*"*10)
                          


  









