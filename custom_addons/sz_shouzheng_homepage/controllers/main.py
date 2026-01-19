from odoo import http
from odoo.http import request


class SzHomepageController(http.Controller):
    
    @http.route('/', type='http', auth='public', website=True)
    def homepage(self, **kwargs):
        """重定向根路径到自定义首页"""
        return request.redirect('/sz-homepage')
    
    @http.route('/sz-homepage', type='http', auth='public', website=True)
    def sz_homepage(self, **kwargs):
        """渲染自定义首页"""
        return request.render('sz_shouzheng_homepage.sz_homepage_page')
