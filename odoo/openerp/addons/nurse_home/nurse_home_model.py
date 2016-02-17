# -*- coding: utf-8 -*-
__author__ = 'flopez'
from openerp import models, fields
class NurseHome(models.Model):
    _name= 'nurse.task'
    name = fields.Char('Description', required=True)
    is_done = fields.Boolean('Done?')
    active = fields.Boolean('Active?', default=True)
