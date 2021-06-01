# -*- coding: utf-8 -*-
# from odoo import http


# class NapataAdmission(http.Controller):
#     @http.route('/napata_admission/napata_admission/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/napata_admission/napata_admission/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('napata_admission.listing', {
#             'root': '/napata_admission/napata_admission',
#             'objects': http.request.env['napata_admission.napata_admission'].search([]),
#         })

#     @http.route('/napata_admission/napata_admission/objects/<model("napata_admission.napata_admission"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('napata_admission.object', {
#             'object': obj
#         })
