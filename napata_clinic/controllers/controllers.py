# -*- coding: utf-8 -*-
# from odoo import http


# class Marwa(http.Controller):
#     @http.route('/marwa/marwa/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/marwa/marwa/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('marwa.listing', {
#             'root': '/marwa/marwa',
#             'objects': http.request.env['marwa.marwa'].search([]),
#         })

#     @http.route('/marwa/marwa/objects/<model("marwa.marwa"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('marwa.object', {
#             'object': obj
#         })
