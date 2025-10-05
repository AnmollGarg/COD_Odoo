from odoo import models, fields, api

class CODPaymentCollection(models.Model):
    _name= 'cod.payment.collection'
    _description = 'COD Payment Collection'
    
    sale_order_id = fields.Many2one('sale.order', string='Sale Order', required=True)
    partner_id = fields.Many2one('res.partner', string='Customer', related='sale_order_id.partner_id', store=True)
    delivery_person_id = fields.Many2one('res.users',string='Delivery Company/Person',default=lambda self: self.env.user
    )
    order_amount = fields.Monetary(string='Order Amount', related='sale_order_id.amount_total', store=True)
    collection_amount = fields.Monetary(string='Collection Amount')
    currency_id = fields.Many2one('res.currency', string='Currency', required=True, default=lambda self: self.env.company.currency_id)
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)
    notes = fields.Text(string='Notes')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
        ('cancel', 'Cancel'),
    ], string='Status', default='draft')

    # Button actions
    def action_confirm(self):
        self.write({'state': 'confirmed'})

    def action_done(self):
        self.write({'state': 'done'})

    def action_cancel(self):
        self.write({'state': 'cancel'})