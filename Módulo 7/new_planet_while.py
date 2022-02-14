new_planet  = ''

planets =[]


while new_planet != 'done':

	if new_planet:
		planets.append(new_planet)
	new_planet = input("Introduce un nuevo planeta, o escribe done cuando termines \n")

	for planet in planets:
		print(planet)
	