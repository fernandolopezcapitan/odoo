# -*- coding: utf-8 -*-

from openerp import models, fields, api

class lavanderia(models.Model):
    _name = 'lavanderia.lavanderia'
    name = fields.Char('Descripcion', required=True)
    tipo = fields.Char('')