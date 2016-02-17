# -*- coding: utf-8 -*-
from openerp import http

# class NurseHome(http.Controller):
#     @http.route('/nurse_home/nurse_home/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nurse_home/nurse_home/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('nurse_home.listing', {
#             'root': '/nurse_home/nurse_home',
#             'objects': http.request.env['nurse_home.nurse_home'].search([]),
#         })

#     @http.route('/nurse_home/nurse_home/objects/<model("nurse_home.nurse_home"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nurse_home.object', {
#             'object': obj
#         })