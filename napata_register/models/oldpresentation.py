# -*- coding: utf-8 -*-

import datetime
from odoo import models, fields, api, exceptions
class  napataPresentation(models.Model):
    _name = 'napata.oldpresentation'
    _description = 'information oldpresentation'
    name = fields.Char(string="Name", readonly=True)
    
    # get student name
    first_name = fields.Char(string='First Name')
    second_name = fields.Char(string='Second Name')
    third_name = fields.Char(string='Third Name')
    forth_name = fields.Char(string='Fourth Name')
    # end of name field
    nat_number= fields.Char( string="Nationalities")
    id_number = fields.Char(string="The National Number")
    phone_1=fields.Integer(string="First Phone Number")
    phone_2=fields.Integer(string="Second Phone Number")
   
    Certificate = fields.Selection([
                        ('Sudanese', 'Sudanese'),
                        ('foreign', 'foreign')],string="Certificate Tyep")

    course = fields.Selection([
                        ('Scientific', 'Scientific'),
                        ('literary', 'literary')],string="The course")
    sit_number= fields.Integer(string="Sitting Number" ) 
    ratio=fields.Float(string="The ratio")
    exa_center= fields.Char(string="Exam center" )
    form_number= fields.Integer(string="Form Number" )  
    exm_year= fields.Integer(string=" exm_year" )

    provider=fields.Char(string="Applicant Name")





    university=fields.Char(string="University")
    resigning = fields.Binary(string="Resigning")
    reason=fields.Text(string="The Reason For Resigning")



    National_card=fields.Binary(string="National card")
    School_card=fields.Binary(string="High School Certificate")
    phone3=fields.Integer(string="Phone Number")
    parent=fields.Char(string="parent")
    main=fields.Char(string="Main Desire")
    sub=fields.Char(string="Sub Desire")
    preType=fields.Char(string="PresntaionType")
    fees = fields.Integer(straing='Fees')
    data = fields.Char('Date current action', default=(lambda self: datetime.datetime.now().year))

    attendees_count = fields.Integer(
        string="Attendees count", compute='_get_attendees_count', store=True)
    # Degree   Holders



    # @api.constrains('main', 'sub')
    # def _check_instructor_not_in_attendees(self):
    #      for r in self:
    #         if r.main and r.main in r.sub:
    #             raise exceptions.ValidationError("This desire has been chosen as the main desire that cannot be chosen within the sub-desire")

    # @api.onchange('preType')
    # def _onchange_price(self):
    #     fees=[]
    #     Presantaion = self.env['na.presentationfees'].search([('preType','=',self.preType.name)])
    #     if Presantaion:
    #             for rec in Presantaion:
    #                 fees.append(rec.id)
    #                 return {'domain': {'fees': [('fees', 'in',fees)]}}


  
    
   