from odoo import models, fields, api

class EstatePropertyType(models.Model):

    # Metadata of model EstatePropertyType
    _name = 'estate.property.type'
    _description = 'Tipo de propiedad'
    _order = 'name'

    # Basic Fiel
    name = fields.Char( string='Nombre', required=True )

