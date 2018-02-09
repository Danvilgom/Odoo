#!/bin/bash
#Daniel Vila

#ejecutar el servicio de odoo con los modulos por defecto y los nuestros
#del usuario odoo
odoo --addons-path="/var/lib/odoo/modules,/usr/lib/python2.7/dist-packages/odoo/addons" --save
