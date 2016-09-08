while 1:
	try:
		texto = input();
		resultado = ""
		cont = 1;
		
		for i in texto:
			if i != " ":
				if (cont % 2) == 0:
					i = i.lower()
					cont += 1
					resultado += i
				else:
					i = i.upper()
					cont += 1
					resultado += i
					
			else:
				resultado += i
		
		
		print(resultado)
		
	except:
		break;
