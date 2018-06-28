# -*- coding: utf-8 -*-
from odoo import http

# class OdooNumverify(http.Controller):
#     @http.route('/odoo_numverify/odoo_numverify/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_numverify/odoo_numverify/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_numverify.listing', {
#             'root': '/odoo_numverify/odoo_numverify',
#             'objects': http.request.env['odoo_numverify.odoo_numverify'].search([]),
#         })

#     @http.route('/odoo_numverify/odoo_numverify/objects/<model("odoo_numverify.odoo_numverify"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_numverify.object', {
#             'object': obj
#         })