# DooIT
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

# -*- coding: utf-8 -*-
from odoo import models, fields, api, _  

class AMSLocation(models.Model):
    _name = 'ams.location'
    
    name = fields.Char(string='Location name')
    
    autorization_id = fields.Many2one('ams.autorization', string='Autorization')