from odoo import http
from odoo.http import request, route

class CodController(http.Controller):

    @http.route('/cod/check_zip', type='json', auth='public')
    def check_cod_zip(self, zip_code, product_id):
        cod_config = request.env['cod.config'].sudo().search([], limit=1)
        allowed_zip_ids = cod_config.cod_allowed_zip_codes.ids
        allowed_zips = request.env['cod.zipcode'].sudo().browse(allowed_zip_ids).mapped('name')
        is_allowed = zip_code in allowed_zips
        return {'cod_available': is_allowed}

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