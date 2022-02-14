
planet = {
    'name': 'Tierra',
    'moons': 1
}

planet = {
    'name': 'Venus',
    'moons': 0

}

planet = {
    'name': 'Marte',
    'moons': 2
}


print(planet.get('name'))


planet['orbital period'] = 4333

print(planet.get('name'))
print(planet.get('moons'))
print(planet.get('orbital period'))


planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}


moons = planet_moons.values()
planets = len(planet_moons.keys())


total_moons = 0
for moon in moons:
    total_moons = total_moons + moon


promedio = total_moons / planets

# Muestra el promedio
print(promedio)
