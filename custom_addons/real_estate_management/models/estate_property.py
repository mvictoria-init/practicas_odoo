from odoo import models, fields, api
from odoo.exceptions import ValidationError


class EstateProperty(models.Model):

    # Metadata of model EstateProperty
    _name = 'estate.property'
    _description = 'Propiedad Inmobiliaria'
    _order = 'id desc'

    # Basic fields about property
    name = fields.Char( string='Nombre', required=True )
    description = fields.Text( string='Descripción')
    postcode = fields.Char( string='Código Postal' )
    date_availability = fields.Date( string='Disponible desde', default=fields.Date.today )
    expected_price = fields.Float( string='Precio Esperado', required=True )
    selling_price = fields.Float( string='Precio de Venta', readonly=True )
    bedrooms = fields.Integer( string='Habitaciones', default=2 )

    state = fields.Selection(
        selection=[
            ('new', 'Nuevo'),
            ('offer_received', 'Oferta Recibida'), 
            ('offer_accepted', 'Oferta Aceptada'),
            ('sold', 'Vendido'),
            ('canceled', 'Cancelado'),
        ],
        string='Estado', default='new', required=True,
    )

    living_area = fields.Float( string='Superficie (m2)' )
    
    property_type_id = fields.Many2one( 'estate.property.type', string='Tipo' )

    price_per_sqm = fields.Float( string='Precio por m2', compute='_compute_price_per_sqm', store=True )
    # store=True - Optional: Save the value in the database to allow sorting/filtering

    # Compute price for m**2
    @api.depends('expected_price', 'living_area')
    def _compute_price_per_sqm(self):
        for record in self:
            if record.living_area > 0:
                record.price_per_sqm = record.expected_price / record.living_area
            else:
                record.price_per_sqm = 0.0

    # Price validation
    @api.constrains('expected_price')
    def _check_expected_price(self):
        for record in self:
            if record.expected_price <= 0:
                raise ValidationError('El precio esperado debe ser mayor que 0.')