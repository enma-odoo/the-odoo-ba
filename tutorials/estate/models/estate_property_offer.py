# -*- coding: utf-8 -*-
from datetime import timedelta
from odoo import models, fields, api

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Real Estate Property Offer"

    price = fields.Float()
    status = fields.Selection(
        [('accepted', 'Accepted'), ('refused', 'Refused')],
        copy=False
    )
    partner_id = fields.Many2one("res.partner", required=True, string="Buyer")
    property_id = fields.Many2one("estate.property", required=True)

    # NEW FIELDS FOR CHAPTER 8
    validity = fields.Integer(default=7, string="Validity (days)")
    
    # Notice the inverse parameter!
    date_deadline = fields.Date(
        compute="_compute_date_deadline", 
        inverse="_inverse_date_deadline", 
        string="Deadline"
    )

    # THE COMPUTE FUNCTION: Calculates the Date based on the Days
    @api.depends("create_date", "validity")
    def _compute_date_deadline(self):
        for offer in self:
            # If the offer isn't saved yet, it won't have a create_date. Use today's date instead.
            start_date = offer.create_date.date() if offer.create_date else fields.Date.today()
            offer.date_deadline = start_date + timedelta(days=offer.validity)

    # THE INVERSE FUNCTION: Calculates the Days based on the Date
    def _inverse_date_deadline(self):
        for offer in self:
            start_date = offer.create_date.date() if offer.create_date else fields.Date.today()
            # We use .days to convert the timedelta object back into a standard Integer
            offer.validity = (offer.date_deadline - start_date).days