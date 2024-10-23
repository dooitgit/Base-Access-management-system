# DooIT
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

# -*- coding: utf-8 -*-
from odoo import models, fields, api, _  

class AMSUser(models.Model):
    _name = 'ams.user'
    
    name = fields.Char(string='Nombre')
    national_identity_document = fields.Char(string='DNI')
    biometric_data = fields.Char(string='Biometric data')

    autorization_id = fields.Many2one('ams.autorization', string='Autorization')

    