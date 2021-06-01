# -*- coding: utf-8 -*-
# from odoo import http


# class NapataHr(http.Controller):
#     @http.route('/napata_hr/napata_hr/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/napata_hr/napata_hr/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('napata_hr.listing', {
#             'root': '/napata_hr/napata_hr',
#             'objects': http.request.env['napata_hr.napata_hr'].search([]),
#         })

#     @http.route('/napata_hr/napata_hr/objects/<model("napata_hr.napata_hr"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('napata_hr.object', {
#             'object': obj
#         })
