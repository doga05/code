def geometri(şekil):
    if len(şekil)==3:
        a=şekil[0]
        b=şekil[1]
        c=şekil[2]

        if (a+b) > c and (a+c)>b and (b+c)>a:
            if (a==b) and (b==c) and (c==a):
                print("Eşkenar üçgen")
            elif (a==b):
                print("ikizkenar üçgen")
            else:
                print("Çeşitkenar üçgen")
        else:
            print("üçgen belirtmiyor")

    elif len(şekil) == 4:
        a=şekil[0]
        b=şekil[1]
        c=şekil[2]
        d=şekil[3]
        if (a==b) and (a==c) and (a==d):
            print("kare")
        elif (a==c) and (b==d):
            print("dikdörtgen")
        else:
            print("normal dörtgen")
    else:
        print("herhangi bir şekil değil")
    
while True:
    elemansayısı= int(input("eleman sayısı giriniz: "))

    if elemansayısı == 3:
        a = int(input("a:"))
        b = int(input("b:"))
        c = int(input("c:"))
        geometri([a,b,c])

    elif elemansayısı == 4:
        a = int(input("a:"))
        b = int(input("b:"))
        c = int(input("c:"))
        d = int(input("d: "))
        geometri([a,b,c,d])

    else:
        print("lütfen tekrar girin")

