# -*- coding: utf-8 -*-

from odoo import models, fields, api

class taller(models.Model):
    _name = 'taller.taller'

    name = fields.Char()
    logo = fields.Binary()
    adress = fields.Char()
    phone = fields.Char()
    schedule = fields.Char()
    worker = fields.Many2many('res.partner')
    director = fields.Many2one('res.partner')
