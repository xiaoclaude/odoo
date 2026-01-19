# -*- coding: utf-8 -*-
{
    'name': '首正会计师事务所主页',
    'version': '19.0.1.0.0',
    'category': 'Website',
    'summary': '深圳市首正会计师事务所官网主页',
    'description': '''
        深圳市首正会计师事务所（普通合伙）官方网站主页模块
        
        设计风格：
        - Trust & Authority + Minimalism
        - 专业、简洁、可信赖
        - 去除 Odoo 原有风格
    ''',
    'author': '深圳市首正会计师事务所',
    'website': 'https://www.shouzheng-cpa.com',
    'license': 'LGPL-3',
    
    'depends': ['website'],
    
    'data': [
        'views/homepage_templates.xml',
    ],
    
    'assets': {
        'web.assets_frontend': [
            'sz_shouzheng_homepage/static/src/css/homepage.css',
        ],
    },
    
    'installable': True,
    'application': False,
    'auto_install': False,
}
