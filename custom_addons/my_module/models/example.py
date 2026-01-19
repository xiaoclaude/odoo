# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ExampleModel(models.Model):
    """示例模型 - 演示 Odoo 模型的基本结构"""
    
    _name = 'my.example'
    _description = '示例记录'
    _inherit = ['mail.thread', 'mail.activity.mixin']  # 启用消息跟踪
    _order = 'sequence, id'
    
    # ========== 基本字段 ==========
    name = fields.Char(
        string='名称',
        required=True,
        tracking=True,
        help='记录的名称'
    )
    
    description = fields.Text(
        string='描述',
        help='详细描述信息'
    )
    
    active = fields.Boolean(
        string='激活',
        default=True,
        help='取消勾选以归档记录'
    )
    
    sequence = fields.Integer(
        string='序号',
        default=10,
        help='用于排序'
    )
    
    # ========== 选择字段 ==========
    state = fields.Selection([
        ('draft', '草稿'),
        ('confirmed', '已确认'),
        ('done', '完成'),
        ('cancelled', '已取消'),
    ], string='状态', default='draft', tracking=True)
    
    priority = fields.Selection([
        ('0', '低'),
        ('1', '中'),
        ('2', '高'),
        ('3', '紧急'),
    ], string='优先级', default='1')
    
    # ========== 日期字段 ==========
    date_start = fields.Date(
        string='开始日期',
        default=fields.Date.context_today
    )
    
    date_end = fields.Date(
        string='结束日期'
    )
    
    # ========== 数值字段 ==========
    amount = fields.Float(
        string='金额',
        digits=(16, 2),
        default=0.0
    )
    
    quantity = fields.Integer(
        string='数量',
        default=1
    )
    
    # ========== 关系字段 ==========
    user_id = fields.Many2one(
        'res.users',
        string='负责人',
        default=lambda self: self.env.user,
        tracking=True
    )
    
    partner_id = fields.Many2one(
        'res.partner',
        string='联系人'
    )
    
    company_id = fields.Many2one(
        'res.company',
        string='公司',
        default=lambda self: self.env.company
    )
    
    tag_ids = fields.Many2many(
        'my.example.tag',
        string='标签'
    )
    
    # ========== 计算字段 ==========
    total_amount = fields.Float(
        string='总金额',
        compute='_compute_total_amount',
        store=True
    )
    
    display_name = fields.Char(
        string='显示名称',
        compute='_compute_display_name'
    )
    
    # ========== 计算方法 ==========
    @api.depends('amount', 'quantity')
    def _compute_total_amount(self):
        for record in self:
            record.total_amount = record.amount * record.quantity
    
    @api.depends('name', 'state')
    def _compute_display_name(self):
        for record in self:
            state_label = dict(self._fields['state'].selection).get(record.state, '')
            record.display_name = f"[{state_label}] {record.name or ''}"
    
    # ========== 约束 ==========
    @api.constrains('date_start', 'date_end')
    def _check_dates(self):
        for record in self:
            if record.date_start and record.date_end:
                if record.date_start > record.date_end:
                    raise ValidationError('结束日期不能早于开始日期！')
    
    _sql_constraints = [
        ('name_unique', 'UNIQUE(name, company_id)', '同一公司下名称必须唯一！'),
    ]
    
    # ========== 业务方法 ==========
    def action_confirm(self):
        """确认操作"""
        for record in self:
            if record.state == 'draft':
                record.state = 'confirmed'
                record.message_post(body='记录已确认')
    
    def action_done(self):
        """完成操作"""
        for record in self:
            if record.state == 'confirmed':
                record.state = 'done'
                record.message_post(body='记录已完成')
    
    def action_cancel(self):
        """取消操作"""
        for record in self:
            if record.state not in ('done', 'cancelled'):
                record.state = 'cancelled'
                record.message_post(body='记录已取消')
    
    def action_reset_draft(self):
        """重置为草稿"""
        for record in self:
            record.state = 'draft'
            record.message_post(body='记录已重置为草稿')
    
    # ========== CRUD 重写 ==========
    @api.model_create_multi
    def create(self, vals_list):
        """重写创建方法"""
        # 在创建前可以进行数据处理
        for vals in vals_list:
            if not vals.get('name'):
                vals['name'] = '新记录'
        return super().create(vals_list)
    
    def write(self, vals):
        """重写更新方法"""
        # 在更新前可以进行验证
        return super().write(vals)
    
    def unlink(self):
        """重写删除方法"""
        # 防止删除已完成的记录
        for record in self:
            if record.state == 'done':
                raise ValidationError('不能删除已完成的记录！')
        return super().unlink()


class ExampleTag(models.Model):
    """示例标签模型"""
    
    _name = 'my.example.tag'
    _description = '示例标签'
    
    name = fields.Char(
        string='标签名称',
        required=True
    )
    
    color = fields.Integer(
        string='颜色索引'
    )
    
    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', '标签名称必须唯一！'),
    ]
