print ("Hello, Django girls!")
print('Jak masz na imię?')
name=input()
if name == 'Ola':
    print('Hej Ola!')
elif name == 'Karolina':
    print('Hej Karo!')
else:
    print('Hej nieznajoma!')
print('Jaką głośność ustawić?')
glosnosc=input()
glosnosc=int(glosnosc)
if glosnosc < 20:
    print("Prawie nic nie slychac.")
elif 20 <= glosnosc < 40:
    print("O, muzyka leci w tle.")
elif 40 <= glosnosc < 60:
    print("Idealnie, moge uslyszec wszystkie detale")
elif 60 <= glosnosc < 80:
    print("Dobre na imprezy")
elif 80 <= glosnosc < 100:
    print("Troszeczke za glosno!")
else:
    print("Ojoj! Moje uszy! :(")