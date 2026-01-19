# -*- coding: utf-8 -*-
{
    'name': '示例模块',
    'version': '19.0.1.0.0',
    'category': 'Tools',
    'summary': 'Odoo 19 自定义模块开发示例',
    'description': '''
        这是一个 Odoo 19 自定义模块开发示例。
        
        功能特点:
        - 基础模型定义
        - 视图和菜单配置
        - 权限控制
        - 业务逻辑示例
    ''',
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'license': 'LGPL-3',
    
    # 依赖模块
    'depends': ['base', 'mail'],
    
    # 数据文件 (按加载顺序)
    'data': [
        # 安全/权限
        'security/ir.model.access.csv',
        
        # 视图
        'views/example_views.xml',
        
        # 菜单
        'views/menu_views.xml',
    ],
    
    # 演示数据
    'demo': [],
    
    # 模块配置
    'installable': True,
    'application': True,
    'auto_install': False,
}
