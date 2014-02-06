# -*- coding: utf-8 -*-
import requests
import json

ciudades = {"1":"Almeria","2":"Cadiz","3":"Cordoba","4":"Granada","5":"Huelva","6":"Jaen","7":"Malaga","8":"Sevilla"}

print """
1. Almería
2. Cádiz
3. Córdoba
4. Granada
5. Huelva
6. Jaén
7. Málaga
8. Sevilla
		"""

peticion = raw_input("¿De qué ciudad quieres saber el tiempo?: ")
#print ciudades[peticion]

respuesta = requests.get('http://api.openweathermap.org/data/2.5/weather',params={'q':'%s,spain' % ciudades[peticion]})

dicc = json.loads(respuesta.text)

temperatura = dicc["main"]["temp"]

temperaturareal = temperatura - 273

print ,% temperaturareal
