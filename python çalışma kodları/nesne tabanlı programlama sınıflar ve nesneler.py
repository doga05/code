'''nesne tabanlı programlama(ntp): nesnelere özellik yüklenir.insan uvuzlarının kendine ait özellikleri olması gibi.
bir sınıf yaratıp ona özellikler yükleriz. her masanın aynı renkte olmaması gibi.bir insan sınıfı tanımlayıp insanların özelliklerinin
farklı olmas gibi.'''

class dusman:
    kalancan = 3
    def saldır(self):
        print("hücuuğmm")
        self.kalancan -= 1
    def hayattami (self):
        if self.kalancan <=0:
            print("ÖLÜĞ")
        else:
            print(str(self.kalancan) + " canım kaldı")
    
dusman1 = dusman()
dusman2 = dusman()

'''dusman1.saldır()
dusman1.saldır()
dusman1.hayattami()'''

dusman2.saldır()
dusman2.saldır()
dusman2.saldır()
dusman2.hayattami()