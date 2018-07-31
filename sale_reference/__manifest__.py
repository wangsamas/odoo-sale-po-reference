# -*- coding: utf-8 -*-
{
    'name': "sale_reference",

    'summary': """
        Customer Purchase Order reference on Sale Order""",

    'description': """
        This module add new field for customer purchase order reference to be displayed on Sale Order, Delivery and Invoice 
    """,

    'author': "Kusuma Ruslan",
    'website': "http://www.wangsamas.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['sale_management', 'stock'],

    'data': [
        'views/views.xml',
        'views/templates.xml',
    ],
}