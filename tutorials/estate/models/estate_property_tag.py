# -*- coding: utf-8 -*-
from odoo import models, fields

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Real Estate Property Tag"
    _unique_name = models.Constraint(
        "UNIQUE(name)",
        "The tag name must be unique"
    )

    name = fields.Char(required=True)
    color = fields.Integer()