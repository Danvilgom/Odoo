#!/bin/bash
#DanielVila

#Hacer git de toda la carpeta entera
git add *
#Escribir comentario
echo 'Escribe el mensaje para el commit : '
read nombre

git commit -m "$nombre"
#hacer el push para subir los archivos
git push -u origen master
