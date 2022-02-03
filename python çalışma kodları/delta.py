a=input('a = ')
b=input('b = ')
c=input('c = ')

delta=b*b-4*a*c

if delta>0:
    x1=(-b-delta^0.5)/(2*a)
    x2=(-b+delta^0.5)/(2*a)

    print('Iki reel kök; x1 = %f x2 = %f n',x1,x2)

elif delta==0:
    print('Tek kök var; x1 = x2= %f n',-b/(2*a))
    
else:
    print('Kökler sanal n')