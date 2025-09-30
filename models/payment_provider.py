from odoo import models, fields, api

class PaymentProvider(models.Model):
    _inherit = 'payment.provider'
    
    code = fields.Selection(
        selection_add=[('cod', "Cash on Delivery")], ondelete={'cod': 'set default'}
    )
    image = fields.Binary(string="Image")
    config_ids = fields.Many2one('cod.config', string="COD Configurations")

    cod_fees = fields.Float(string="COD Fees", default=0.0)

    def get_cod_fee(self, order):
        return self.cod_fees or 0.0

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    cod_available = fields.Boolean(
        string="COD Available",
        compute="_compute_cod_available",
        store=False
    )
    cod_message = fields.Char(
        string="COD Message",
        compute="_compute_cod_message",
        store=False
    )
    cod_policy_link = fields.Char(
        string="COD Policy Link",
        compute="_compute_cod_policy_link",
        store=False
    )
    cod_expected_delivery = fields.Char(
        string="Expected Delivery",
        compute="_compute_cod_expected_delivery",
        store=False
    )

    def _compute_cod_message(self):
        for product in self:
            config = self.env['cod.config'].search([], limit=1)
            product.cod_message = config.cod_availability_alert if product.cod_available else config.cod_unavailable_message

    def _compute_cod_policy_link(self):
        for product in self:
            config = self.env['cod.config'].search([], limit=1)
            product.cod_policy_link = config.cod_policy_link

    def _compute_cod_expected_delivery(self):
        for product in self:
            config = self.env['cod.config'].search([], limit=1)
            if config.display_expected_delivery:
                product.cod_expected_delivery = f"This Product will be Delivered within {config.expected_delivery_interval} days."
            else:
                product.cod_expected_delivery = ""

    def _compute_cod_available(self):
        for product in self:
            config = self.env['cod.config'].search([], limit=1)
            if config:
                is_unavailable = product.id in config.cod_unavailable_products.ids
                meets_min = product.list_price >= config.min_order_amount if config.min_order_amount else True
                meets_max = config.max_order_amount == 0.0 or product.list_price <= config.max_order_amount
                product.cod_available = not is_unavailable and meets_min and meets_max
            else:
                product.cod_available = True





