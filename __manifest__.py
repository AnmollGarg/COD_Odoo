{
    'name' : 'Cash on Delivery',
    'version' : '1.0',
    'summary': 'Cash on Delivery Payment Method',
    'description': 'Module to add Cash on Delivery as a payment method in Odoo',
    'category': 'Accounting',
    'depends' : ['payment', 'sale', 'account', 'website', 'website_sale', 'payment'],
    'data': [
        'views/website_cod_product.xml',
        'views/website_cod_payment.xml',
        'security/ir.model.access.csv',
        'views/payment_provider_views.xml',
        'data/payment_provider_data.xml',
        'views/cod_config_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}