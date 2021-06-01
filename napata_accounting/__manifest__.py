# -*- coding: utf-8 -*-
{
    'name': "napata_accounting",

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
    'depends': [
                'mail',
                 'napata_register',
                 ],

    'images': [
        'static/description/icon.png',
    ],

    # always loaded
    'data': [
        'security/account_security.xml',
        'security/ir.model.access.csv',
        'data/sequence.xml',

        'wizard/payment_method_views.xml',
        'wizard/account_repot_wizard.xml',
        'views/accounting.xml',

       # menus
        'menus/account.xml',
        # 'menus/report.xml',
       #report
        #  'report/presentation_report.xml',
        # 'report/presentation_templet_report.xml',
        #


    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
