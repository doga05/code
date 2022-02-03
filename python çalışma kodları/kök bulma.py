#ax^2 + bx + c 

def kökbul(a,b,c):
    delta = (b*b-4*a*c)
    if delta <0:
        print("Reel kök yok")
        return
    
    x1 = (-b-delta**0.5)/(2*a)
    x2 = (-b+delta**0.5)/(2*a)

    return (x1,x2)

a= int(input("a:"))
b= int(input("b:"))
c= int(input("c:"))

sonuç = kökbul(a,b,c)
print(sonuç)
