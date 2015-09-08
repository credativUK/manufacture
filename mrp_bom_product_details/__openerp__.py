# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2013 Solutions Libergia inc. (<http://www.libergia.com>).
#                  2015 credativ Ltd (<http://credativ.co.uk>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Bom product details',
    'version': '8.0.0.0.1',
    'author': "Solutions Libergia inc.,"
              "credativ ltd.,"
              "Odoo Community Association (OCA)",
    'license': 'GPL-3 or any later version',
    'category': 'Manufacturing',
    'depends': ["mrp"],
    'data': ['views/mrp_bom_product_details.xml'],
    'auto_install': False,
    'installable': True,
}
