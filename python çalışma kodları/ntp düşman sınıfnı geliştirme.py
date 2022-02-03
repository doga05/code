import random
class dusman:
    def __init__(self,isim,kalancan,saldırıgucu,mermisayısı):#yapıcı fonkiyondur.burda parametrelere değer atanabilir.
        self.isim = isim#self. demek zorundayız yoksa bu fonksiyona ait olduklarını anlamazlar
        self.kalancan = kalancan#bunları kendilerine eşitlediki çünkü dışardan alıcaz
        self.saldırıgucu = saldırıgucu
        self.mermisayısı = mermisayısı  
    def saldır(self):
        print(self.isim + " saldırıyor")
        harcananmermi = random.randrange(0,10)
        print(str(harcananmermi) + " kadar harcandı")
        self.mermisayısı -= harcananmermi

        return (harcananmermi,self.saldırıgucu)
    def saldırıyaugra(self,harcananmermi,saldırıgucu):
        print("vuruldum")
        self.kalancan -= (harcananmermi * saldırıgucu)
    def mermibitti(self):
        if(self.mermisayısı <= 0):
            print(self.isim + "mermim bitti")
            return True
        return False
    def hayattamu(self):
        if(self.kalancan <=0):
            print(self.isim + "öldüü")
    def print (self):
        print("\nİsim:",self.isim,"\nKalan Can:",self.kalancan,"\nSaldırı Gücü:",self.saldırıgucu,"\nMermi Sayısı:",self.mermisayısı)

dusmanlar = []

i = 0
while i < 10 :
    rastgelecan = random.randrange(100,200)
    rastgelesaldırıgucu = random.randrange(1000,2000)
    rastgelemermisayısı = random.randrange(100,150)
    yenidusman = dusman("Düşman" + str(i+1),rastgelecan,rastgelesaldırıgucu,rastgelemermisayısı)
    dusmanlar.append(yenidusman)

    i += 1

for dusman in dusmanlar:
    dusman.print()