# -*- coding: utf-8 -*-
# © 2016 Digitalcake - Alisan Alacam
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    social_facebook = fields.Char(string='Facebook')
    social_twitter = fields.Char(string='Twitter')
    social_linkedin = fields.Char(string='Linkedin')
    social_youtube = fields.Char(string='Youtube')
    social_google_plus = fields.Char(string='Google Plus')

