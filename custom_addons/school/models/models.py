# -*- coding: utf-8 -*-
# Aquí va nuestro modelo

from odoo import models, fields

class Student (models.Model):
    # Metadatos del módelo para crear la tabla de estudiantes
    _name = 'school.student'
    _description = 'Tabla de estudiantes'

    # Los datos de los estudiantes 
    name = fields.Char(string='Nombre', required=True)
    age = fields.Integer(string='Edad')


# class school(models.Model):
#     _name = 'school.school'
#     _description = 'school.school'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

