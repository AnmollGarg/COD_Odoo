from odoo import models, fields

class CodZipCode(models.Model):
    _name = 'cod.zipcode'
    _description = 'COD ZIP Code'

    name = fields.Char(string="ZIP Code", required=True)
    country_id = fields.Many2one('res.country', string="Country")