# -*- coding: utf-8 -*-
# from odoo import http


# class NapataPresntaion(http.Controller):
#     @http.route('/napata_presntaion/napata_presntaion/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/napata_presntaion/napata_presntaion/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('napata_presntaion.listing', {
#             'root': '/napata_presntaion/napata_presntaion',
#             'objects': http.request.env['napata_presntaion.napata_presntaion'].search([]),
#         })

#     @http.route('/napata_presntaion/napata_presntaion/objects/<model("napata_presntaion.napata_presntaion"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('napata_presntaion.object', {
#             'object': obj
#         })
