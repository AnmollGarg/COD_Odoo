from odoo import http

class CodController(http.Controller):
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

    @http.route(['/payment/confirmation'], type='http', auth='public', website=True)
    def cod_confirmation(self, order_reference=None, **kwargs):
        sale_order = http.request.env['sale.order'].sudo().search([('name', '=', order_reference)], limit=1)
        if sale_order:
            sale_order.action_confirm()
            return http.request.redirect('/payment/status')

    @http.route(['/shop/confirmation'], type='http', auth='public', website=True)
    def shop_confirmation(self, **kwargs):
        return http.request.render('cod.payment_confirmation_template', {})