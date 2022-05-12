# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models

class ResConfigSettings(models.TransientModel):

    _inherit = 'res.config.settings'

    partner_dgii_autocomplete = fields.Boolean(string="DGII Autocomplete", config_parameter='l10n_do_accounting.dgii_autocomplete')