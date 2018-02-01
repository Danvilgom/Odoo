# -*- coding: utf-8 -*-

from odoo import models, fields, api
from openerp.exceptions import ValidationError

class taller(models.Model):
    _name = 'taller.taller'

    name = fields.Char()
    logo = fields.Binary()
    adress = fields.Char()
    phone = fields.Char()
    schedule = fields.Char()
    worker = fields.Many2many('res.partner')
    director = fields.Many2one('res.partner')

    @api.constrains('worker')
    def _check_something(self):
        for w in self.worker:
            for t in self.search([('id','!=',self.id)]):
                for w2 in t.worker:
                    if w.id == w2.id:
                        raise ValidationError("Trabajador duplicado.")

class section(models.Model):
    _name = 'taller.section'

    name = fields.Char()
    reparation = fields.One2many('product.template','section')

class reparation(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    name = fields.Char()
    section = fields.Many2one('taller.section')
    price = fields.Float()
    isReparation = fields.Boolean(default=False)

class work(models.Model):
    _name = 'taller.work'
    _inherit = 'product.template'

    name = fields.Char()
    workers = fields.Many2many('res.partner')
    reparation = fields.Many2one('product.template')
    type = fields.Selection([('garage','Garage'),('home','Home')])
    garage_location = fields.Many2one('taller.taller')
    home_location = fields.Char()
    overrun = fields.Float()
    status = fields.Selection([
        ('booking','Booking'),
        ('processing','Processing'),
        ('finalized','Finalized')
    ], default='booking')
    total_time = fields.Float()
    start_time = fields.Datetime()
    total = fields.Float(compute='_compute_total')

    # Campo compute por terminar
    @api.depends('reparation')
    def _compute_total(self):
        for r in self:
            preu = r.reparation.price
            r.total = (preu + (preu * r.total_time / 10)) + r.overrun

class booking(models.Model):
    _name = 'taller.booking'

    name = fields.Char()
    customer = fields.Many2one('res.partner')
    date = fields.Datetime()
    reparation = fields.Many2many('product.template')
    taller_aux = fields.Many2one('taller.taller');
    status = fields.Selection([
        ('booking','Booking'),
        ('processing','Processing'),
        ('finalized','Finalized')
    ], default='booking')

    @api.multi
    def change_status(self):
        for r in self:
            if r.status == 'booking':
                r.write({'status':'processing'})
            elif r.status == 'processing':
                r.write({'status':'finalized'})
            elif r.status == 'finalized':
                r.write({'status':'booking'})
