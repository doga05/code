n=int(input("Faktoriyelini öğrenmek istediğiniz sayıyı girin: "))
fak=1
for i in range(n):
    fak*=i+1
print("Faktoriyel: ",fak)