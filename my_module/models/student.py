# -*- coding: utf-8 -*-

from odoo import api, models, fields
import datetime
from datetime import timedelta


class StudentStudent(models.Model):
    _name = 'student.student'


    @api.multi
    def _compute_days(self):
        for el in self:
            if el.number and el.today:
                el.compute_days = el.today + datetime.timedelta(days=el.number)
            pass

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    photo = fields.Binary(string='Image')
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female'), ('others', 'Others')],
        string='Gender')
    student_dob = fields.Date(string="Date of Birth")
    student_blood_group = fields.Selection(
        [('A+', 'A+ve'), ('B+', 'B+ve'), ('O+', 'O+ve'), ('AB+', 'AB+ve'),
         ('A-', 'A-ve'), ('B-', 'B-ve'), ('O-', 'O-ve'), ('AB-', 'AB-ve')],
        string='Blood Group')
    nationality = fields.Many2one('res.country', string='Nationality')
    clases_id = fields.Many2one('clases.clases', 'Clases')
    today = fields.Datetime('Today', default=lambda self: fields.Datetime.now())
    number = fields.Integer('You number')
    compute_days = fields.Datetime(compute='_compute_days',
                                  string='Compute Days')
