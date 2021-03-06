# -*- coding: utf-8 -*-
import requests
import json

ciudades = {"1":"Almería","2":"Cádiz","3":"Córdoba","4":"Granada","5":"Huelva","6":"Jaén","7":"Málaga","8":"Sevilla","9":"Dos Hermanas"}

print """
1. Almería
2. Cádiz
3. Córdoba
4. Granada
5. Huelva
6. Jaén
7. Málaga
8. Sevilla
9. Dos Hermanas
		"""

peticion = raw_input("¿De qué ciudad quieres saber el tiempo?: ")

respuesta = requests.get('http://api.openweathermap.org/data/2.5/weather',params={'q':'%s,spain' % ciudades[peticion]})

dicc = json.loads(respuesta.text)

temperatura = dicc["main"]["temp"]

tempreal = temperatura - 273

print "La temperatura actual de %s es %s grados centígrados" % (ciudades[peticion],tempreal)
