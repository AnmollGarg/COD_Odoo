from odoo import models, fields

class CodConfig(models.Model):
    _name = 'cod.config'
    _description = 'Cash on Delivery Configuration'

    name = fields.Char(string="Configuration Name", required=True)
    min_order_amount = fields.Float(string="Minimum Order Amount", default=0.0)
    max_order_amount = fields.Float(string="Maximum Order Amount", default=0.0)

    cod_unavailable_products = fields.Many2many('product.template', string="Products Not Eligible for COD")

    cod_allowed_states = fields.Many2many('res.country.state', string="States Where COD is Available")
    cod_allowed_zip_codes = fields.Many2many('cod.zipcode', string="ZIP Codes Where COD is Available", help="Select ZIP codes")

    cod_availability_alert = fields.Text(string="COD Availability Alert", default="Cash on Delivery is available for your order.")
    display_expected_delivery = fields.Boolean(string="Display Expected Delivery Date", default=True)
    cod_policy_link = fields.Text(string="COD Policy Link")
    expected_delivery_interval = fields.Integer(string="Expected Delivery Interval (days)", default=2)
    cod_unavailable_message = fields.Text(string="COD Unavailability Messages", default="Cash on Delivery is not available for this product.")
    cod_unavailable_message_payment = fields.Text(string="COD Unavailability Message at Payment", default="Some of the products in your cart are not eligible for Cash on Delivery.")
