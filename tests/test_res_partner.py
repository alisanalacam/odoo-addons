# -*- coding: utf-8 -*-
# © 2016 Digitalcake - Alisan Alacam
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase
from openerp.exceptions import ValidationError


class TestResPartner(TransactionCase):

    def test_check_sectors(self):
        with self.assertRaises(ValidationError):
            self.env['res.partner'].create(
                {'name': 'Test', 'social_facebook': 'facebook_address', 'social_linkedin': 'facebook_address',
                 'social_youtube': 'youtube_address', 'social_twitter': 'twitter_address',
                 'social_google_plus': 'google_plus_address',
                 })
