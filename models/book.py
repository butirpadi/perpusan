# -*- coding: utf-8 -*-

from flectra import models, fields, api

class Book(models.Model):
    _inherit = 'product.template'
    _name = 'perpusan.book'

    
    
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100