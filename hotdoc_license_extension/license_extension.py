# -*- coding: utf-8 -*-
#
# Copyright © 2016 Mathieu Duponchelle <mathieu.duponchelle@opencreed.com>
# Copyright © 2016 Collabora Ltd
#
# This library is free software; you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation; either version 2.1 of the License, or (at your option)
# any later version.
#
# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this library.  If not, see <http://www.gnu.org/licenses/>.

import os

from hotdoc.core.base_extension import BaseExtension

DESCRIPTION=\
"""
This extension helps licensing your hotdoc project
"""


class LicenseExtension(BaseExtension):
    extension_name = 'license-extension'
    argument_prefix = 'license'

    def setup(self):
        pass

    @staticmethod
    def add_arguments(parser):
        group = parser.add_argument_group('License extension',
                DESCRIPTION)

    @staticmethod
    def parse_config(doc_repo, config):
        pass

def get_extension_classes():
    return [LicenseExtension]
