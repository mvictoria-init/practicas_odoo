from odoo import models, fields, api

class LibraryBook(models.Model):

    # Metadata of model LibraryBook
    _name = 'library.book'
    _description = 'Libro de Biblioteca'

    # Basic fields about LibraryBook
    name = fields.Char( string='Nombre', required=True )
    autor = fields.Char( string='Nombre del Autor')
    # ISBN =  International Standard Book Number in Odoo (fields.Char)
    isbn = fields.Char(string='ISBN', help='Número de identificación internacional del libro')
    description = fields.Text(string='Sinopsis del libro')


    state = fields.Selection(
        selection=[
            ('Available', 'Disponible'),
            ('Loaned', 'Prestado'), 
            ('Maintenance', 'Maintenance'),
        ],
        string='Estado', default='Available', required=True,
    )