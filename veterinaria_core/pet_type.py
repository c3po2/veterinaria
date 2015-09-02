# b-*- encoding: utf-8 -*-

from datetime import timedelta
from openerp import models, fields, api

class Pet_Type(models.Model):
    _name ='veterinaria.pet_type'
    
    name = fields.Char(string="Pet Type", required=True)
    pet_ids = fields.One2many(comodel_name='veterinaria.pet_type', inverse_name='name', string="Pets")


        
