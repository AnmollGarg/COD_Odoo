from odoo import models, fields, api, exceptions

class CODPaymentCollection(models.Model):
    _name= 'cod.payment.collection'
    _description = 'COD Payment Collection'
    _rec_name = 'sale_order_id'

    sale_order_id = fields.Many2one('sale.order', required=True)
    partner_id = fields.Many2one('res.partner', string='Customer', related='sale_order_id.partner_id')
    delivery_person_id = fields.Many2one('res.users',string='Delivery Company/Person',default=lambda self: self.env.user)
    order_amount = fields.Monetary(related='sale_order_id.amount_total')
    collection_amount = fields.Monetary(required =True)
    currency_id = fields.Many2one('res.currency', string='Currency', required=True, default=lambda self: self.env.company.currency_id)
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)
    notes = fields.Text(string='Notes')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
        ('cancel', 'Cancel'),
    ], string='Status', default='draft')

    _sql_constraints = [
        ('unique_sale_order', 'unique(sale_order_id)', 'You cannot create multiple COD Payment Collections for one Sale Order!')
    ]

    @api.model
    def create(self, vals):
        if self.search_count([('sale_order_id', '=', vals.get('sale_order_id'))]):
            raise exceptions.UserError('You cannot create multiple COD Payment Collections for one Sale Order!')
        return super(CODPaymentCollection, self).create(vals)

    # Button actions
    def action_confirm(self):
        self.write({'state': 'confirmed'})

    def action_done(self):
        self.write({'state': 'done'})

    def action_cancel(self):
        self.write({'state': 'cancel'})

    def print_cod_report(self):
        return self.env.ref('cod.action_report').report_action(self)