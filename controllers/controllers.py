# -*- coding: utf-8 -*-
from flectra import http

# class Perpusan(http.Controller):
#     @http.route('/perpusan/perpusan/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/perpusan/perpusan/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('perpusan.listing', {
#             'root': '/perpusan/perpusan',
#             'objects': http.request.env['perpusan.perpusan'].search([]),
#         })

#     @http.route('/perpusan/perpusan/objects/<model("perpusan.perpusan"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('perpusan.object', {
#             'object': obj
#         })