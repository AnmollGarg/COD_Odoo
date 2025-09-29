from odoo import http
from odoo.addons.website_sale.controllers.main import WebsiteSale

class CodWebsiteController(WebsiteSale):
    @http.route(['/product/cod_info/<int:product_id>'], type='json', auth='public')
    def cod_info(self, product_id):
        product = http.request.env['product.product'].sudo().browse(product_id)
        cod_config = http.request.env['cod.config'].sudo().search([], limit=1)
        eligible = product not in cod_config.cod_unavailable_products
        return {
            'cod_available': eligible,
            'cod_alert': cod_config.cod_availability_alert if eligible else cod_config.cod_unavailable_message,
            'expected_delivery': cod_config.expected_delivery_interval if cod_config.display_expected_delivery else False,
        }