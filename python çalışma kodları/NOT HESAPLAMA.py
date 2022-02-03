# NOT HESAPLAMA PROGRAMI

VizeNotu = int(input("Vize Notunu Girin: "))
FinalNotu = int(input("Final Notunu Girin: "))
Devamsızlık = int(input("Devamsızlığı Girin: "))

ToplamNot = VizeNotu * 40/100 + FinalNotu * 60/100

if Devamsızlık > 7:
    print("Öğrenci devamsızlıktan kaldı. F")
else:
    if ToplamNot >= 85:
        print("Not AA")
    elif ToplamNot <85 and ToplamNot >= 70:
        print("Not BB")
    elif ToplamNot < 70 and ToplamNot >= 55:
        print("Not CC")
    elif ToplamNot < 55 and ToplamNot >= 45:
        print("Not DD")
    else:
        print("Not FF")