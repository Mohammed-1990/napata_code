# -*- coding: utf-8 -*-

from odoo import models, fields, api

class  napataLocal(models.Model):
    _name = 'napata.locals'
    _description = 'local '
    name = fields.Char(string="Local", required=True)
    state_id= fields.Many2one('napata.state',
        ondelete='cascade', string="State", required=True)
    
