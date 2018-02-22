#!/bin/bash
#Daniel Vila
#Script per a executarlo en classe

#Ejecuta actualizando el modulo puesto a continuacion.
#Igual que tambien tenemos que poner la empresa a ejecutar
echo "Modelos:"
echo ""
ls -d */
echo ""
echo "Introduzca el nombre del modulo:"
read modul

#odoo --config /var/lib/odoo/.odoo_serverrc -d ccx -u tasks --save
odoo --config /var/lib/odoo/.odoo_serverrc -d ccx -u $modul
