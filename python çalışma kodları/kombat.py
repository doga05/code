import random
print("****Istinye KOMBAT****")
print("!!!Istinye KOMBAT'a HOŞGELDİNİZ!!!")


def buyukluk_sor():
    while True:
        deger = int(input("1 ile 50 arasında bir saldırı büyüklüğü seçiniz: "))
        if deger > 50:
            print("Saldırı büyüklüğü 1 ile 50 arasında olmalıdır .")
        elif deger < 1:
            print("Saldırı büyüklüğü 1 ile 50 arasında olmalıdır .")
        else:
            return deger


"""def saldiri(puan, isim):
    print("---------------", isim, "Attacks !! ---------------")
    saldiri_buyuklugu = buyukluk_sor()
    rastgele = random.randint(1, 100)
    hasar_sansi = 100 - saldiri_buyuklugu
    if hasar_sansi > rastgele:
        print(isim, "vuruş", saldiri_buyuklugu, "Hasar!!")
        puan -= saldiri_buyuklugu
    else:
        print("Ooopsy!", isim, "saldırıyı kaçırdı!")
   
    return puan"""


def saldiri(puan,isim):
    zarar_verme_sansı = random.randint(0, 100)
    print("---------------", isim, "Attacks !! ---------------")
    saldırı_buyuklugu = buyukluk_sor()
    if zarar_verme_sansı > saldırı_buyuklugu :
        print (isim , "vuruş", saldırı_buyuklugu, "Hasar!!")
        puan -= saldırı_buyuklugu
    else:
        print ("Ooopsy!", isim , "saldırıyı kaçırdı!")

    return puan 

def isim_sor(metin, diger_kahraman_listesi):
    while True:
        print('-----', metin, 'kahraman -----')
        isim = input("Lütfen kahramanınızın ismini giriniz: ")
        isim = isim.capitalize()
        if len(isim) <= 1:
            print("Kahraman adı boş bırakılamaz.")
        elif isim in diger_kahraman_listesi:
            print(isim, "alındı, lütfen başka isim giriniz !")
        else:
            print(metin, "kahramanınızın adı ", isim)
            break
    return isim


def isim_yazdir(hp1, hp2, oyuncu1, oyuncu2):
    print(oyuncu2+" "*(58-len(oyuncu1))+" "*5+oyuncu1)
    #print("HP["+str(hp1)+"]:"+"|"*(int(hp1/2))+" "*(int((100-hp1)/2))+" "*5+"HP["+str(hp2)+"]:"+"|"*(int(hp2/2)))
 
  
   #print("HP[{}]:".format(hp1), "/" * int(hp1/2), " "*int(60-(hp1/2 ) - len(str(hp1))))
    #print("HP[{}]".format(hp2), "/" * int(hp2/2))
    print("HP[{}]:".format(hp1), "|" * int(hp1/2), " "*(int((100-hp2)/2))+ " "*5+"HP[{}]".format(hp2), "|" * int(hp2/2), " "*(int((100-hp1)/2)))
  

def esas():
    hp1 = 100
    hp2 = 100

    oyuncu_listesi = []
    
    kahraman_ad = isim_sor("Birinci", oyuncu_listesi)
    oyuncu_listesi.append(kahraman_ad)
    
    kahraman_ad = isim_sor("İkinci", oyuncu_listesi)
    oyuncu_listesi.append(kahraman_ad)
    
    random.shuffle(oyuncu_listesi)
    yazi_tura = oyuncu_listesi[0]
    oyuncu = oyuncu_listesi[1]
    print("Yazı tura sonucu: %s önce başlar!" % yazi_tura)  # Coin toss result

    calis = True
    while calis:
        hp1 = 100
        hp2 = 100
        while hp1 > 1 and hp2 > 1:
            
            hp1 = saldiri(hp1, yazi_tura)
            isim_yazdir(hp1, hp2, yazi_tura, oyuncu)
          
            
            if hp1 <= 1:
                break
            
            hp2 = saldiri(hp2, oyuncu)
            isim_yazdir(hp1, hp2, yazi_tura, oyuncu)
            
        if hp1 <= 1:
            print("#################################################################")
            print("##################### " + yazi_tura, " KAZANDI  #########################")
            print("#################################################################")
        if hp2 <= 1:
            print("######################################################################")
            print("############################ " + oyuncu, " KAZANDI ########################")
            print("######################################################################")
        cevap = input('Tekrar oynamak ister misiniz [evet/hayır]?').strip()
        if cevap == 'hayır':
            calis = False
        if calis == False:
            print("Oynadığınız için teşekkürler! Tekrar görüşmek üzere!")


esas()

