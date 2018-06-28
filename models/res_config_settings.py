# -*- coding: utf-8 -*-

from odoo import fields, models, api
from odoo.exceptions import AccessDenied


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    verifynum_api_key = fields.Char("VerifyNum Api Key")
    enable_verifynum = fields.Boolean("Enable VerifyNum")

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        get_param = self.env['ir.config_parameter'].sudo().get_param
        res.update(
            enable_verifynum=get_param('enable_verifynum'),
            verifynum_api_key=get_param('verifynum_api_key', default=''),
        )
        return res

    def set_values(self):
        if not self.user_has_groups('website.group_website_designer'):
            raise AccessDenied()
        super(ResConfigSettings, self).set_values()
        set_param = self.env['ir.config_parameter'].sudo().set_param
        set_param('enable_verifynum', self.enable_verifynum)
        set_param('verifynum_api_key', (self.verifynum_api_key or '').strip())
