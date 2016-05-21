def hej(imie):
	
	if imie == 'Ola':
		print('Hej Alealeksandro!')
	elif imie == 'Karo':
		print('Hej Karcia!')
	else:
		print('Hej'+' '+imie+ '!')
dziewczyny = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'Ty']
for imie in dziewczyny:
	hej(imie)
	print('Kolejna dziewczyna')
for i in range(1, 6):
    print(i)