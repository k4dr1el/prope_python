

print("Se detecto un asteroide, a continuación escribe los datos:")
vel_asteroide = input('¿A que velocidad se acerca el asteroide?  \n' )
tam_asteroide = input("¿De que tamaño es el asteroide? \n")

if int(vel_asteroide) >= 25 and int(tam_asteroide) >= 25 :
	print("Asteroide peligroso se acerca")
elif int(vel_asteroide) < 25 and int(tam_asteroide) >= 25 :
		print("Asteroide grande se acerca")
elif int(vel_asteroide) >= 25 and int(tam_asteroide) < 25 :
		print("Asteroide rapido se acerca")
else:
	print(" Puede que se acerque o no un asteroide")