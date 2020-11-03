név = input('Hogy híjják kendet? ')
kor = input('És hány éves kend? ') 
kor = int(kor)
évszám = input ('Melyik év van?')
év = int(évszám)
születési_év = év - kor
print(név, ', kend ', születési_év, '-ban született.', sep='')