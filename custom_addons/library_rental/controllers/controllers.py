# -*- coding: utf-8 -*-
# from odoo import http


# class LibraryRental(http.Controller):
#     @http.route('/library_rental/library_rental', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/library_rental/library_rental/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('library_rental.listing', {
#             'root': '/library_rental/library_rental',
#             'objects': http.request.env['library_rental.library_rental'].search([]),
#         })

#     @http.route('/library_rental/library_rental/objects/<model("library_rental.library_rental"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('library_rental.object', {
#             'object': obj
#         })

