import random


def buyukluk_sor():
    while True:
        deger = int(input("1 ile 50 arasında bir saldırı büyüklüğü seçiniz: "))

        if deger > 50:
            print ("Saldırı büyüklüğü 1 ile 50 arasında olmalıdır .")
        elif deger < 1:
            print ("Saldırı büyüklüğü 1 ile 50 arasında olmalıdır .")
        else:
            return deger
        
def saldırı(puan,isim):

    zarar_verme_sansı = random.randint(0, 100)

    print("---------------", isim, "Attacks !! ---------------")

    saldırı_buyuklugu = buyukluk_sor()

    if zarar_verme_sansı > saldırı_buyuklugu :
        print (isim , "vuruş", saldırı_buyuklugu, "Hasar!!")
        puan -= saldırı_buyuklugu
    else:
        print ("Ooopsy!", isim , "saldırıyı kaçırdı!")

    return puan 


 # BU KISIMDA OLMALI 
    
def isim_sor(metın,diger_kahraman_listesi):
  
    while True:
        print ('-----', metın, 'kahraman -----')

        isim = input("Lütfen kahramanınızın ismini giriniz: ")
        isim = isim.capitalize()

        if len(isim) <= 1:
            print ("Kahraman adı boş bırakılamaz.")        
        elif isim in diger_kahraman_listesi:
            print (isim, "alındı, lütfen başka isim giriniz !")
        else:
            print (metın, "kahramanınızın adı ", isim)
            break

    return isim


def esas():

    oyuncu_listesi = []

    kahraman_adı0 = isim_sor("Birinci",oyuncu_listesi)
    oyuncu_listesi.append(kahraman_adı0)

    kahraman_adı1 = isim_sor("İkinci", oyuncu_listesi)
    oyuncu_listesi.append(kahraman_adı1)

    random.shuffle(oyuncu_listesi)

    yazı_tura = oyuncu_listesi[0]
    oyuncu    = oyuncu_listesi[1] 

    print ("Yazı tura sonucu: %s önce başlar!" % yazı_tura) #Coin toss result
 

    # --- loop ----

    çalış = True

    while çalış:

     
        hp1, hp2 = (100, 100)

     

        while hp1 > 1 and hp2 > 1:
            hp1 = saldırı(hp1, yazı_tura)
            (hp1, hp2, yazı_tura, oyuncu)

            if hp1 <= 1:
                break

            hp2 = saldırı(hp2, oyuncu)
            (hp1, hp2, yazı_tura , oyuncu)

        # --- game over ---

        if hp1 <= 1:
            print        ("#################################################################")
            print        ("#####################" + yazı_tura, " KAZANDI  #########################")
            print        ("#################################################################")
        if hp2 <= 1:
            print         ("######################################################################")
            print        ("############################" + oyuncu ," KAZANDI ########################")
            print         ("######################################################################")


        cevap = input('Tekrar oynamak ister misiniz [evet/hayır]?').strip()
        if cevap == 'hayır':
            çalış = False
        if çalış == False:

            print("Oynadığınız için teşekkürler! Tekrar görüşmek üzere!")

esas()