# -*- coding: utf-8 -*-
{
    'name': "library_rental",

    'summary': " Gestión de Préstamos de Biblioteca ",

    'description': """
        * Registrar libros, géneros y autores
        * Gestionar las solicitudes de préstamo de los usuarios
        * Calcular automáticamente los días de retraso y si el libro está disponible para ser prestado.
    """,

    'author': "Maria Victoria",
    'website': "https://my-portfolio-flame-six-94.vercel.app/",
    'category': 'management',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],

    # Is application
    'application': True,
}

