# -*- coding: utf-8 -*-

from odoo import models, fields


class Clases(models.Model):
    _name = 'clases.clases'

    name = fields.Char(string='Name', required=True)
    quantity = fields.Integer(string='Quantity students')
    specification = fields.Selection(
        [('math', 'Math'), ('engl', 'Engl'), ('law', 'law')],
        string='Specification')
    students_id = fields.Many2one('student.student', 'All Students')
    students_ids = fields.One2many('student.student', 'clases_id', string='Students')

