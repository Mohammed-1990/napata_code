# -*- coding: utf-8 -*-
{
    'name': "Hospital Management System",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "mohamed Ibarhim",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',
              
                ],

    # always loaded
    'data': [
        # 'security/presentation_security.xml',
      'security/ir.model.access.csv',
       'data/ir_sequence_data.xml',
       'data/ir_appointments_data.xml',
       'views/patient.xml',
       'views/appointments.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
