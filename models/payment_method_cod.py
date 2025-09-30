from odoo import models, fields

class PaymentProviderCod(models.Model):
    _inherit = 'payment.provider'

    name = fields.Char(string = "Method Name")