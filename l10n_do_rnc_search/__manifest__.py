# -*- coding: utf-8 -*-
{
    'name': "RNC DGII Search",

    'summary': """
      Buscador de RNC en DGII
          """,

    'description': """
         Buscador de RNC en DGII
    """,

    'website': 'https://astratech.com.do',
    'author': 'Astra Tech SRL',
    'category': 'Localization',
      'version': '13.0',

    # any module necessary for this one to work correctly
    'depends': ['base','l10n_do_accounting'],

    # always loaded
     'data': [
       'data/ir_config_parameters.xml',
        'views/backend_js.xml',
        'views/res_partner_views.xml',


    ],

}
