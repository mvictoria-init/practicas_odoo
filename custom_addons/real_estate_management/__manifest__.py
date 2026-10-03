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

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'management',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/estate_property.xml',
        'views/estate_property_type.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    # Is application
    'application': True,
}

