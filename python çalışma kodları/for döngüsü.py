''' for döngüsü
string="gollum" 
for i in string: (bu satırda i'nin stringin içinde gezineceğini belirtiyoruz.ilk döngüde g ikincisinde o olur ve sırayla dener.
string bitince döngüde biter. yukardan aşağı harf harf yazdırır.)
pitonda *rande diye bir kullanım var idleda print(*range(10)) olarak kullanılıyor. bu fonksiyon 0dan 10a kadar ama 10 dahil değil olan
sayıları yazdırmaya yarıyor. for i in range olayındaki range burdan geliyor.Örneğin;

for i in range(10):
    print(i) gibi.bu loop 0'dan 9'a kadar rakamları yazar.Faktoriyelde de ya da şekil yazdırmada da kullanılabilir.'''

faktoriyel = 1

while True:
    sayı = int(input("Negatif olmayan bir sayı giriniz:"))
    if sayı <=0:
        print("Negatif olmayan bir sayı giriniz:")
    else:
        for i in range(1,sayı+1):
            faktoriyel *=i
        print("Faktoriyel:",faktoriyel)
        break

'''listeler =[2,3,4]

for i in range(1,10):
    if in in listeler:
        continue
    print(i)
    çıktı = 1,5,6,7,8,9 olur. continue if'in içinde olduğu için devam eder ve o sayıları yazmaz.continue kullanırken dikkat etmek
    gerek. çünkü while ile kullanıldığında sonsuz döngüye sokabilir.'''