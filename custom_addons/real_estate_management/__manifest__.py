# -*- coding: utf-8 -*-
{
    'name': "real_estate_management",

    'summary': "Gestión de bienes raíces",

    'description': """
        Un módulo para agencias inmobiliarias que gestionan la venta y alquiler de propiedades,
        ofertas de compradores y comisiones.
    """,

    'author': "Maria Victoria",
    'website': "https://my-portfolio-flame-six-94.vercel.app/",
    'category': 'management',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property.xml',       # Aquí está menu_estate_root y menu_estate_property
        'views/estate_property_type.xml',  # Aquí está menu_estate_property_type con parent
    ],


    # Is application
    'application': True,
}

