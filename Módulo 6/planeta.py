planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']



number_of_planets = len(planets)
print('There are', number_of_planets, 'planets in the solar system.')


planeta = input('Escribe  un planeta \n' )
planets.append(planeta)

number_of_planets = len(planets)
print('There are actually', number_of_planets, 'planets in the solar system.')

print('Elemento agregados ' + planets[-1])

#primera parte

planeta_index = planets.index(planeta)

print(planeta_index)


print('El ultimo planeta que se introdujo es: ' + planeta)
print(planets[0:planeta_index])


print('Here are the planets further than ' + planeta)
print(planets[planeta_index + 1:])



planets.pop()  # Goodbye, Pluto
number_of_planets = len(planets)
print('No, there are definitely', number_of_planets, 'planets in the solar system.')

print('The last planet is', planets[-1])
print('The penultimate planet is', planets[-2])





