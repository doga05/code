'''fonksiyonlar yazılır ve daha sonra onu çağırırsın ne kadar çağırırsan o kadar çalışır. def kullanılr ve snra fonk.ismi yazılır.
parantez açılır ve parantezin içine parametreler yazılabilir. girinti olan her yer fonksiyona aittir.fonksiyon çağırılırken def olmadan
yazılır. parametresi varsa onlar da yazılır. Örneğin;
def merhaba():
    print("Merhaba dünya")
merhaba() bir fonksiyon örneğidir. Eğer parantez içinde parametre olsaydı çağırılırken onlar da yazılırdı.'''

'''def fak(sayı):
    faktoriyel = 1
    for i in range(1,sayı+1):
        faktoriyel*=i
    print("Faktoriyel:",faktoriyel)

sayı = int(input("Sayı Giriniz:"))

fak(sayı)
fak(6)'''

'''fonksiyonlarda return döndürmek demektir ve fonksiyonlarn içinden hesapladığımız değeri çağırdığımız yere döndürür.'''

def fak(sayı):
    faktoriyel = 1
    for i in range(1,sayı+1):
        faktoriyel*=i
    #print("Faktoriyel:",faktoriyel)
    return faktoriyel#burda sonucu dışarı aktarıyor ve bunu bir yere atamamız lazım

sayı = int(input("Sayı Giriniz:"))
a = fak(sayı)#burda return ile dışarı atılan faktoriyel değerini a'ya atar ve bastırırız. Eğer return olmasaydı ve bu yine olsaydı
             #boş olucağı için none döndürürdü.
print(a)