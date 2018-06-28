# -*- coding: utf-8 -*-
{
    'name': "Odoo NumVerify",

    'summary': """
    Verify phone numbers in Odoo checkout form using NumVerify APIs
    """,

    'description': """
        Long description of module's purpose
    """,

    'author': "MorePython",
    'website': "http://www.morepython.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}