# -*- coding: utf-8 -*-

from odoo import models, fields, api


class  napataState(models.Model):
    _name = 'napata.state'
    _description = 'state '
    name = fields.Char(string="State", required=True)
   