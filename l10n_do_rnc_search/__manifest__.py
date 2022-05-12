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
      'version': '15.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','l10n_do_accounting'],
    
    'assets': {
        'web.assets_backend': [
            'l10n_do_rnc_search/static/src/js/l10n_do_accounting.js',
        ]

    },

    # always loaded
     'data': [
       'data/ir_config_parameters.xml',
        'views/res_partner_views.xml',
        'views/res_config_settings.xml'


    ],

}
