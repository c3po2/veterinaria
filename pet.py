# b-*- encoding: utf-8 -*-

from openerp import models, fields, osv

class Pet(models.Model):
    _name = 'veterinaria.pet'
    
    name = fields.Char(string="Pet Name", required=True)
    type = fields.Many2one(comodel_name='veterinaria.pet_type', string='Type')
    size = fields.Many2one(comodel_name='res.users', string='Size')
    birthdate= fields.Date('Birthdate')
    comment = fields.Text(string="Comment")
    
    visit_ids = fields.One2many(comodel_name='veterinaria.visit', inverse_name='pet_id', string="Visits")
    



    
    
    