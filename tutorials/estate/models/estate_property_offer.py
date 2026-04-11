# -*- coding: utf-8 -*-
from odoo import models, fields

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Real Estate Property Offer"

    price = fields.Float()
    status = fields.Selection(
        [('accepted', 'Accepted'), ('refused', 'Refused')],
        copy=False
    )
    partner_id = fields.Many2one("res.partner", required=True, string="Buyer")
    
    # This is the REQUIRED Many2one that the One2many will use to link back!
    property_id = fields.Many2one("estate.property", required=True)