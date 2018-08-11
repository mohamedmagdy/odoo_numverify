# -*- coding: utf-8 -*-

import requests
from odoo import models, api, _
from odoo.exceptions import UserError


class Partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    @api.constrains('country_id', 'phone')
    def _check_country_vs_phone(self):
        for rec in self:
            if rec.country_id and rec.phone:
                # Get the country's code for the country that the user has entered
                country_code = rec.country_id.code

                # Check if the VerifyNum is enabled

                params = rec.env['ir.config_parameter'].sudo()
                enable_verifynum=params.get_param('enable_verifynum')
                verifynum_api_key=params.get_param('verifynum_api_key', default='')

                if enable_verifynum and verifynum_api_key:
                    url = 'http://apilayer.net/api/validate?access_key=%s&number=%s&format=1' % (verifynum_api_key, rec.phone)
                    response = requests.get(url).json()
                    # Raise the errors if something was not valid.
                    if 'valid' in response.keys() and response.get('valid') and not response.get('country_code') == country_code:
                        raise UserError(_('The country is not matching the phone number'))
                    elif 'valid' in response.keys() and not response.get('valid'):
                        raise UserError(_('Phone Number is not correct'))
                elif enable_verifynum and not verifynum_api_key:
                    raise UserError(_('NumVerify is enabled but the Access Key is not configured!'))
                else:
                    pass

    @api.constrains('country_id', 'mobile')
    def _check_country_vs_mobile(self):
        for rec in self:
            if rec.country_id and rec.mobile:
                # Get the country's code for the country that the user has entered
                country_code = rec.country_id.code

                # Check if the VerifyNum is enabled

                params = rec.env['ir.config_parameter'].sudo()
                enable_verifynum=params.get_param('enable_verifynum')
                verifynum_api_key=params.get_param('verifynum_api_key', default='')

                if enable_verifynum and verifynum_api_key:
                    url = 'http://apilayer.net/api/validate?access_key=%s&number=%s&format=1' % (verifynum_api_key, rec.mobile)
                    response = requests.get(url).json()
                    # Raise the errors if something was not valid.
                    if 'valid' in response.keys() and response.get('valid') and not response.get('country_code') == country_code:
                        raise UserError(_('The country is not matching the mobile number'))
                    elif 'valid' in response.keys() and not response.get('valid'):
                        raise UserError(_('Mobile Number is not correct'))
                elif enable_verifynum and not verifynum_api_key:
                    raise UserError(_('NumVerify is enabled but the Access Key is not configured!'))
                else:
                    pass
