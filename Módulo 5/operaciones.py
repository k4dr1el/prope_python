t = 149597870
j=778547200

d= j-t
print(d)

dm= d*0.621
print(dm)


distancia_1 = input('Escribe  la distancia del planeta al sol del primer planeta  \n' )
distancia_2 = input('Escribe  la distancia del planeta al sol del segundo planeta  \n' )

distancia_1 = int(distancia_1)

distancia_2 = int(distancia_2)

print("Disntacia 1: " + str(distancia_1) +" distancia 2: " + str(distancia_2))
distancia_total = distancia_2 - distancia_1

ditancia_total_millas = distancia_total*0.621

print("Distnacia total en km:" + str(abs(distancia_total)))
print("Distnacia total en ml:" + str(abs(ditancia_total_millas)))