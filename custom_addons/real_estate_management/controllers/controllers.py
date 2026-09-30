# -*- coding: utf-8 -*-
# from odoo import http


# class RealEstateManagement(http.Controller):
#     @http.route('/real_estate_management/real_estate_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/real_estate_management/real_estate_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('real_estate_management.listing', {
#             'root': '/real_estate_management/real_estate_management',
#             'objects': http.request.env['real_estate_management.real_estate_management'].search([]),
#         })

#     @http.route('/real_estate_management/real_estate_management/objects/<model("real_estate_management.real_estate_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('real_estate_management.object', {
#             'object': obj
#         })

