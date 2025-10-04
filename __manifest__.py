{
    'name' : 'Cash on Delivery',
    'version' : '1.0',
    'summary': 'Cash on Delivery Payment Method',
    'description': 'Module to add Cash on Delivery as a payment method in Odoo',
    'category': 'Accounting',
    'depends' : ['payment', 'sale', 'account', 'website', 'website_sale', 'payment', 'product', 'sale_management'],
    'data': [
        'views/cod_menu_views.xml',
        'views/cod_payment_collections_views.xml',  # <-- Add this line
        'views/payment_cod_templates.xml',
        'data/cod_fee_product.xml',
        'data/payment_method_data.xml',
        'data/payment_provider_data.xml',
        'views/website_cod_product.xml',
        'security/ir.model.access.csv',
        'views/payment_provider_views.xml',
        'views/cod_config_views.xml',
    ],
    # 'assets': {
    #     'web.assets_frontend': [
    #         'cod/static/src/js/post_processing.js',
    #     ],
    # },
    'installable': True,
    'application': False,
    'auto_install': False,
}