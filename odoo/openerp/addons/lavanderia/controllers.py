# -*- coding: utf-8 -*-
from openerp import http

# class Lavanderia(http.Controller):
#     @http.route('/lavanderia/lavanderia/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lavanderia/lavanderia/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('lavanderia.listing', {
#             'root': '/lavanderia/lavanderia',
#             'objects': http.request.env['lavanderia.lavanderia'].search([]),
#         })

#     @http.route('/lavanderia/lavanderia/objects/<model("lavanderia.lavanderia"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lavanderia.object', {
#             'object': obj
#         })