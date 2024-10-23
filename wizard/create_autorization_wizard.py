# DooIT
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class AMSCreateAutorization(models.TransientModel):
    _name='ams.create.autorization.wizard'

    user_name = fields.Char(string='Nombre')
    user_national_identity_document = fields.Char(string='DNI')
    user_biometric_data = fields.Char(string='Biometric data')
    
    location_name = fields.Char(string='Location name')
            
    autorization_type = fields.Selection([
        ('temporary', 'Temporary'),
        ('permanent', 'Permanent'),
        ])
    autorization_start_date = fields.Date(string='Start date')
    autorization_end_date = fields.Date(string='End date')
    autorization_shift = fields.Selection([
        ('every_day', 'Every day'),
        ('weekdays', 'Monday to Friday from 8am to 6pm'),
        ('weekdays_and_weekends', 'Monday to Friday from 8am to 6pm, and Saturdays from 8am to 12pm')
    ])
    autorization_device = fields.Char(string='Device')

    #----------------------------------------------------------------------------------------------------
    
    def get_tuples_ids(self, vals, model):
        new_vals_list = []
        vals_list = vals.split(sep=', ')
        for val in vals_list:
            val_id=self.env[model].create({'name':val})
            new_vals_list.append(val_id.id)
        locations_tuple = tuple(new_vals_list)
        
        return locations_tuple
    
    def action_create_autorization(self):
        new_autorization = self.env['ams.autorization'].create({
            'autorization_secuence': 'New',
            'autorization_type': self.autorization_type,
            'start_date': self.autorization_end_date,
            'end_date': self.autorization_end_date,
            'shift':self.autorization_shift,
            'device':self.autorization_device,
            'users_ids':[(0,0,{
                'name':self.user_name,
                'national_identity_document':self.user_national_identity_document,
                'biometric_data':self.user_biometric_data,
            })],
            'locations_ids': self.get_tuples_ids(self.location_name, 'ams.location')
        })
        
        action = self.env['ir.actions.act_window']._for_xml_id('ams.ams_autorization_action_view')
        action['views'] = [(self.env.ref('ams.ams_autorization_form_view', False).id, 'form')]
        action['res_id'] = new_autorization.id
        
        return action
