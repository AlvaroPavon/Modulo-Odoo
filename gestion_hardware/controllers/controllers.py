# -*- coding: utf-8 -*-
# from odoo import http


# class GestionHardware(http.Controller):
#     @http.route('/gestion_hardware/gestion_hardware', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestion_hardware/gestion_hardware/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestion_hardware.listing', {
#             'root': '/gestion_hardware/gestion_hardware',
#             'objects': http.request.env['gestion_hardware.gestion_hardware'].search([]),
#         })

#     @http.route('/gestion_hardware/gestion_hardware/objects/<model("gestion_hardware.gestion_hardware"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestion_hardware.object', {
#             'object': obj
#         })

