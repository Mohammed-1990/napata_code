# -*- coding: utf-8 -*-
{
    'name': "napata_seting",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'mail',
                ],

    # always loaded
    'data': [
        'security/setting_security.xml',
        'security/ir.model.access.csv',
        'views/collage.xml',
        'views/program.xml',
        'views/specialization.xml',
        'views/parent.xml',
         'views/result.xml',
         'views/level.xml',
        'views/semester.xml',
        'views/batch.xml',
        'views/fees_type.xml',
        'views/presentationTyep.xml',

        # menus
        'menus/collage.xml',
        'menus/parent.xml',
        # 'menus/address.xml',
        'menus/presentationTyep.xml',
         'menus/acdimac.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
