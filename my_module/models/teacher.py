# -*- coding: utf-8 -*-

from odoo import api, models, fields
import datetime
from datetime import timedelta


class Teacher(models.Model):
    _name = 'teacher.teacher'


    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')],
                              string='Gender')
    subject = fields.Selection(
                    [('math', 'Math'), ('engl', 'Engl'), ('law', 'Law')],
                    string='Subject')
    clases_id = fields.Many2one('clases.clases', 'Clases')
