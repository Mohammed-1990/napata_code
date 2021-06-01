

from odoo import models, fields, api 


class napataLevel(models.Model):
    _inherit = ['mail.thread']
    _name = 'napata.level'
    _description = 'university name '
    name = fields.Char(string="Academic level", required=True)
    # college = fields.Many2one("napata.collage", ondelete="cascade", string="College")
    # program = fields.Many2one("napata.program", ondelete="cascade", string="Brogram")




