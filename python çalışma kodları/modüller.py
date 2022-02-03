'''modüller:her dosya bir modüldür ve o modüldeki fonksiyonları programımıza dahil ederek kullanabiliyoruz. Yani başka bir dosyada 
yazdığımız fonksiyonu tekrar başka bir dosyada kullanmak için onu yeniden yazmak yerine modüllerle yeni dosyaya getirip kullanabiliriz.
hazr modüller ve kendi yazdığımız modüller olarak ikiye ayrılır. Kendi yazdığımız modülü başka bir yerde kullanmak istiyorsak dosya ve
modülün aynı dizinde olması gerekir ki çağırabilelim. 2 yöntem varıdr. birincisi import yazarak kullanılır. 
ikincisi from yazarak olur from .... import şeklinde
MODÜL YARATMA: bir modül yaratıp 'modül ekstra' kodunda kullanacağız'''

def naber ():
    print("kodumun kodu")
def mutlak(numara):
    if numara <0:
        return -numara
    return numara

import math

print(math.factorial(6)) # faktoriyel modülü