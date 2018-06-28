# -*- coding: utf-8 -*-
import requests
from werkzeug.exceptions import Forbidden

from odoo import _
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSale(WebsiteSale):

    def checkout_form_validate(self, mode, all_form_values, data):
        """
        This method is modifying the original one to check if the phone number that the customer will add in the
        checkout form is valid and matching with the country
        :param mode: tuple ('new/edit', 'billing/shipping')
        :param all_form_values: dict Holds all values before preprocess
        :param data: dict Holds values after preprocess
        :return:
        error: Specifying if a certain field is not valid.
        error_message: The message that will be raised if a certain field is not valid.
        """

        error, error_message = super(WebsiteSale, self).checkout_form_validate(mode=mode, all_form_values=all_form_values, data=data)

        config = request.env['res.config.settings'].sudo().create({})

        # Get the country's code for the country that the user has entered
        country_code = request.env['res.country'].sudo().search([('id', '=', all_form_values.get('country_id'))], limit=1).code

        # Check if the VerifyNum is enabled
        if config.enable_verifynum:
            api_access_key = config.verifynum_api_key
            url = 'http://apilayer.net/api/validate?access_key=%s&number=%s&format=1' % (
            api_access_key, all_form_values.get('phone'))

            response = requests.get(url).json()

            # Add the errors that will be raised if something was not valid.
            if 'valid' in response.keys() and response.get('valid') and not response.get('country_code') == country_code:
                error['country_id'] = 'error'
                error_message.append(_('The country is not matching the phone number'))
            elif 'valid' in response.keys() and not response.get('valid'):
                error['phone'] = 'error'
                error_message.append(_('Phone Number is not correct'))
        return error, error_message
