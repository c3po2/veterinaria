# b-*- encoding: utf-8 -*-

from openerp import models, fields

class Visit(models.Model):
    _name = 'veterinaria.visit'
    
    date = fields.Date(string="Visit Date")
    operation = fields.Text(string="Operation")
    price = fields.Integer(string="Price")
    result = fields.Text(string="Result")
    aftercares = fields.Text(string="Aftercares")

    # link visits to pets
    pet_id = fields.Many2one('veterinaria.pet', string="Pet", required=True)
