# -*- coding: utf-8 -*-

from odoo import models, fields


class Clases(models.Model):
    _name = 'clases.clases'

    name = fields.Char(string='Name', required=True)
    quantity = fields.Integer(string='Quantity students')
    specification = fields.Selection(
        [('math', 'Math'), ('engl', 'Engl'), ('law', 'law')],
        string='Specification')
