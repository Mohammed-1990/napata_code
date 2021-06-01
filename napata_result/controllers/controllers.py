# -*- coding: utf-8 -*-
# from odoo import http


# class NapataResult(http.Controller):
#     @http.route('/napata_result/napata_result/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/napata_result/napata_result/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('napata_result.listing', {
#             'root': '/napata_result/napata_result',
#             'objects': http.request.env['napata_result.napata_result'].search([]),
#         })

#     @http.route('/napata_result/napata_result/objects/<model("napata_result.napata_result"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('napata_result.object', {
#             'object': obj
#         })
