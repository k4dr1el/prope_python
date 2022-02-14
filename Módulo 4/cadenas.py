name = "Moon"
gravity = 0.00162 # in kms
planet = "Earth"


titulo = f'La {name} y the {planet}'

hechos = f"""{'-'*80} 
Nombre del planeta: {planet} 
Gravedad en {name}: {gravity * 1000} m/s2""" 

template = f"""{titulo.title()} {hechos} """ 
print(hechos)

planet = "Marte"
gravity  = 0.00143
name = "Ganímedes"


hechos = f"""{'-'*80} 
Nombre del planeta: {planet} 
Gravedad en {name}: {gravity * 1000} m/s2"""

print(hechos)



