# DooIT
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

# -*- coding: utf-8 -*-
from odoo import models, fields, api, _  

class AMSAutorization(models.Model):
    _name = 'ams.autorization'
    
    autorization_secuence = fields.Char(string='Autorization secuence', default='New',  readonly=True )
        
    autorization_type = fields.Selection([
        ('temporary', 'Temporary'),
        ('permanent', 'Permanent'),
        ])
    start_date = fields.Date(string='Start date')
    end_date = fields.Date(string='End date')
    shift = fields.Selection([
        ('every_day', 'Every day'),
        ('weekdays', 'Monday to Friday from 8am to 6pm'),
        ('weekdays_and_weekends', 'Monday to Friday from 8am to 6pm, and Saturdays from 8am to 12pm')
    ])
    device = fields.Char(string='Device')
    
    users_ids = fields.One2many('ams.user', 'autorization_id', string='Users')
    locations_ids = fields.One2many('ams.location', 'autorization_id', string='Locations')
    
    @api.model
    def create(self, vals_list):
        vals_list['autorization_secuence'] = (self.env['ir.sequence'].next_by_code('ams.autorization'))
            
        return super().create(vals_list)
    
    def create_autorization_field(self):
        return {
            'name':'Create autorization',
            'type':'ir.actions.act_window',
            'res_model':'ams.create.autorization.wizard',
            'view_mode':'form',
            'target':'new',
        }
