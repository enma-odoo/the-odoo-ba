# -*- coding: utf-8 -*-
{
    'name': 'Real Estate',
    'version': '1.0',
    'category': 'Real Estate',
    'summary': 'Manage real estate properties and offers',
    'description': """
Real Estate Management
======================
This module allows you to:
- Manage real estate properties
- Track offers from potential buyers
- Handle buyer assignments
    """,
    'author': 'Enock Maseru',
    'website': 'https://www.eclickafrica.com',
    'license': 'LGPL-3',
    'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
