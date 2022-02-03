from datetime import datetime
import colored
#form belirtilen ismi renklendirmek için colored yöntemi kullanılır.
color = colored.fg(130)
#kullanılan color ile terminal bölümündeki çıktıları "Turuncu" rengi alır.

#---------------------------------------------------------------------------------------------
#EKRAN ÇIKTILARININ TUTUNCU OLABİLMESİ İÇİN TERMİNAL BÖLÜMÜNE "pip install colored " yazmalıyız.
#---------------------------------------------------------------------------------------------


Envanter = {"kuşkonmaz": [10,5], "brokoli": [15,6], "havuç": [18,7], "elmalar": [20,5], "muz":[10, 8], "meyve": [30,3], 
"yumurta": [50,2], "karışık meyve suyu": [0,18], "balık çubukları":[25,12], "dondurma": [32,6], "elma suyu": [40,7], 
"portakal suyu": [30,8], "üzüm suyu":[10,9]}
#Markette ürünlerin bulunduğu bir "Envanter" değişkeni tanımlanmıştır.
# Kullanıcıların "kullanıcı_adı ve şifre" lerinin tutulduğu bir sözlük tanımlanmıştır.
kullanıcılar = {"ahmet":{"pwd":"İstinye123"},"meryem":{"pwd":"4444"}}
# Kulanıcıların sepetindeki ürünlerini  tutabilecek bir sözlük tanımlanmıştır.
sepet = {"ahmet":{},"meryem":{}}
# Kullanılan değişkenlerin ilk değer ve tip atamaları yapmak için değerler yazılır.
ana_menu_kontrolu, sepet_toplamı, toplam, numara_ogesi, fiyat, miktar, sayac, oge_sec, oge_adı, kullanıcı_adı, sifre, arama_ogesi, bulunan_ogeler =False, 0.0, 0.0, 0, 0, 0, 0, 0, "", "", "", "", []
# Kullanıcı giriş arayüzü devreye girer.
while True:
    print(color+"""** İstinye Online Market'e Hoşgeldiniz **
Lütfen kullanıcı kimlik bilgilerinizi sağlayarak giriş yapın:""")
#While döngüsü ile İstinye Online Market Kullanıcısına hoşgeldiniz der.Ardından;
# Kullanıcı_adı ve şifre girişini ister.
    kullanıcı_adı = input(color+"Kullanıcı adı: ")
    sifre = input(color+"Şifre: ")

    if kullanıcı_adı in kullanıcılar.keys() and kullanıcılar[kullanıcı_adı]["şifre"] == sifre:
        print(color+"Başarıyla giriş yapıldı!")
        print(color+f"Hoşgeldiniz {kullanıcı_adı}! Lütfen ilgili menü numarasını girerek aşağıdaki seçeneklerden birini seçin.\n")
# Eğer girilen kullanıcı_adı ve şifre "kullanıcılar" sözlüğünde varsa ve birbiriyle uyuşuyorsa giriş yap komutunu sağlar.
# Değilse uyarı ver ve bilgilerin tekrar girilmesini iste komutunu gönderir.
    else:
        print(color+"Kullanıcı adınız ve / veya şifreniz doğru değil. Lütfen tekrar deneyin!\n")
        continue
# Ana menü arayüzünde False , While True döngüsü ile birlikte kullanılmaktadır.
    while True:
        ana_menu_kontrolu = False
        secenek = int(input(color+"""Lütfen aşağıdaki hizmetlerden birini seçin:
1. Ürün ara
2. Sepete git
3. Satın al
4. Oturum Kapat
5. Çıkış yap"""))
# Eğer geçersiz menü numarası seçilmişse uyar vermesini istemeliyiz.
        if secenek not in [1,2,3,4,5]:
            print(color+"Lütfen geçerli bir menü numarası seçiniz!\n")
# Eğer "Ürün ara" seçilmiş ise ;
        elif secenek == 1:
            while True:
                arama_ogesi = input(color+"Ne arıyorsunuz? ")
 # Ana menüye dönüş yap komutunu verir.
                if arama_ogesi == "0":
                    ana_menu_kontrolu = True
                    break
# Eğer girilen arama kelimesi "Envanter" sözlüğündeki ürün isimleri içerisinde yer alıyorsa bulunan ürünleri "bulunan_ogeler" listesinin içine atmasını istemektedir.
                for item in Envanter.keys():
                    if arama_ogesi in item:
# Bulunan ürün sayısını sayan sayaç işleme devam eder.
                        sayac += 1
                        bulunan_ogeler.append(item)
# Eğer sayaç 0 ise hiç ürün bulunamamış demektir.
                if sayac > 0:
                    break
                else:
                    print(color+"Aramanız hiçbir öğeyle eşleşmedi. Lütfen başka bir şey deneyin (Ana menü için 0 girin):")
            if ana_menu_kontrolu == True:
                continue
# Bulunan ürünler print aracılığı ile ekrana yazdırılır.
            print(color+f"{sayac} benzer ürün bulundu:\n")
            for iter in range(len(bulunan_ogeler)):
                print(color+f"{iter+1}. {bulunan_ogeler[iter]} {Envanter[bulunan_ogeler[iter]][1]} $")
            print("\n")
# Bulunan ürünlerden hangilerinden kaç tane sepete eklemek istendiğini seçmesi beklenir.
            while True:
                oge_sec = int(input(color+"Lütfen sepetinize eklemek istediğiniz ürünü seçin (Ana menü için 0 girin): "))
# Ana menüye dönüş ;
# Eğer girilen değer bulunan ürünler listesinin uzunluğundan fazla ise uyarı ver ve tekrar değer girilmesini iste.
                if oge_sec == 0:
                    sayac = 0
                    bulunan_ogeler = []
                    ana_menu_kontrolu = True
                    break

                if oge_sec not in range(1,len(bulunan_ogeler)+1):
                    print(color+"Aramanız hiçbir öğeyle eşleşmedi. Lütfen başka bir şey deneyin (Ana menü için 0 girin):")
                    continue
#Sıra seçilen ürünü sepete ekleme işlemindedir.
                while True:
# Seçilen üründen kaç adet eklenecek komutunu sormaktadır.
# Eğer 0'dan büyük bir değer girilmezse uyar ve tekrar değer girilmesini ister.
                    numara_ogesi = int(input(color+f"{bulunan_ogeler[oge_sec-1]} ekleniyor. Adedi Girin: "))

                    if numara_ogesi > 0:
                        break
                    else:
                        print(color+"Lütfen en az 1 adet ürün seçiniz!\n")
# Seçilen ve adedi belirtilen ürünü sepete ekleme, stoktan düşme döngüsü;
                while True:
# Eğer seçilen üründen istenen adet stokta yeteri kadar varsa sepete ekle emrini verir.
                    if Envanter[bulunan_ogeler[oge_sec-1]][0] >= numara_ogesi:
                       
                        if  bulunan_ogeler[oge_sec-1] not in sepet[kullanıcı_adı].keys():
                            Envanter[bulunan_ogeler[oge_sec-1]][0] -= numara_ogesi
                            sepet[kullanıcı_adı].update({bulunan_ogeler[oge_sec-1]:numara_ogesi})
                            print(color+f"Sepetinize {bulunan_ogeler[oge_sec-1]} eklendi.\nAna menüye geri dönülüyor ...\n")
                            ana_menu_kontrolu = True
                            bulunan_ogeler = []
                            sayac = 0
                            break
# Eğer seçilen ürün daha önceden sepete eklenmişse, adet miktarına ekleme yap komutunu kullanır.
                        else:
                            Envanter[bulunan_ogeler[oge_sec-1]][0] -= numara_ogesi
                            sepet[kullanıcı_adı][bulunan_ogeler[oge_sec-1]] += numara_ogesi
                            print(color+f"Sepetinize {bulunan_ogeler[oge_sec-1]} eklendi.\nAna menüye geri dönülüyor ...\n")
                            ana_menu_kontrolu = True
                            bulunan_ogeler = []
                            sayac = 0
                            break
#Üründen istenen adet stokta yeteri kadar yoksa miktarı tekrar girmesini istemektedir.
                    else:
                        print(color+"Üzgünüm! Miktar sınırı aşıyor, Lütfen daha küçük bir miktarla tekrar deneyin")
                        numara_ogesi = int(input(color+"Miktar (Ana menü için 0 girin): "))
# Ana menüye dönüş yapılabilir.
                        if numara_ogesi == 0:
                            ana_menu_kontrolu = True
                            break
                if ana_menu_kontrolu == True:
                    break
            if ana_menu_kontrolu == True:
                continue
# "Sepete git" seçilmişse
        elif secenek == 2:
# Ve sepet boşsa uyarır ve ana menüye çıkar.
            if len(sepet[kullanıcı_adı]) == 0:
                print(color+"Sepetiniz boş.\n\tToplam 0 $")
                ana_menu_kontrolu = True
                continue
# Sepet boş değilse sepetin içeriğini, toplam fiyatı ve sepet menüsünü yazdır.
            else:
                print(color+"Sepetiniz şunları içerir:")
                for i in range(len(sepet[kullanıcı_adı])):
                    oge_adı = list(sepet[kullanıcı_adı].keys())[i]
                    fiyat = Envanter[list(sepet[kullanıcı_adı].keys())[i]][1]
                    miktar = list(sepet[kullanıcı_adı].values())[i]
                    toplam = fiyat*miktar
                    sepet_toplamı += toplam
                    print(color+f"\t{i+1}. {oge_adı} fiyatı = {fiyat} $ miktar = {miktar} toplam = {toplam} $")
                print(color+f"Toplam {sepet_toplamı} $")
                sepet_toplamı = 0.0
# Sepet menüsünde yer alan döngü işlenmektedir.
                while True:
                    sepet_sec = int(input(color+"""
Bir seçeneği seçiniz:
1. Tutarı güncelleyin
2. Bir öğeyi kaldırın
3. Satın al
4. Ana menüye dön"""))
# Girilen değer menü ögeleriyle uyuşmuyorsa uyarı ver ve tekrar denenmesini iste komutu devam etmektedir.
                    if sepet_sec not in [1,2,3,4]:
                        print(color+"Lütfen geçerli bir menü numarası seçiniz!\n")
                        continue
# "Tutarı güncelleyin" seçildiyse, Sepet içeriğini ve toplam tutarı yazdır.
                    elif sepet_sec == 1:

                        for i in range(len(sepet[kullanıcı_adı])):
                            oge_adı = list(sepet[kullanıcı_adı].keys())[i]
                            fiyat = Envanter[list(sepet[kullanıcı_adı].keys())[i]][1]
                            miktar = list(sepet[kullanıcı_adı].values())[i]
                            toplam = fiyat*miktar
                            sepet_toplamı += toplam
                            print(color+f"\t{i+1}. {oge_adı} fiyatı = {fiyat} $ miktar = {miktar} toplam = {toplam} $")
                        print(color+f"Toplam {sepet_toplamı} $")
                        sepet_toplamı = 0
# Geçerli ürün numarası girilene kadar ürün numarası ister.
                        while True:
                            sepet_oge_sec = int(input(color+"Lütfen miktarını değiştireceğiniz öğeyi seçin: "))
# Girilen ürün numarası sepet listesinin uzunluğundan büyük değilse uyarı ver ve tekrar girilmesini iste.
                            if sepet_oge_sec in range(1,len(sepet[kullanıcı_adı])+1):
                                break
                            else:
                                print(color+"Lütfen geçerli bir ürün numarası seçiniz!\n")
# Seçilen ürünün yeni miktarını iste Eğer girilene yeni miktar 0'dan küçük veya 0'a eşitse uyarı ver ve tekrar girilmesini iste komutunu verir.
                        while True:
                            while True:
                                item_new_qty = int(input(color+"Lütfen yeni miktarı yazın: "))

                                if item_new_qty > 0:
                                    break
                                else:
                                    print(color+"Lütfen en az 1 adet ürün seçiniz!\n")
# Eğer yeni girilen değer stoktaki seçilen ürünün miktarından büyükse uyarı ver ve tekrar değer girilmesini iste.
                            if item_new_qty <= Envanter[list(sepet[kullanıcı_adı])[sepet_oge_sec-1]][0]:
# Eski miktarı stoğa geri ekle ve yeni değeri stoktan eksilt.
                                item_old_qty = sepet[kullanıcı_adı][list(sepet[kullanıcı_adı].keys())[sepet_oge_sec-1]]
                                sepet[kullanıcı_adı][list(sepet[kullanıcı_adı].keys())[sepet_oge_sec-1]] = item_new_qty
                                Envanter[list(sepet[kullanıcı_adı])[sepet_oge_sec-1]][0] -= item_new_qty
                                Envanter[list(sepet[kullanıcı_adı])[sepet_oge_sec-1]][0] += item_old_qty
                                break
                            else:
                                print(color+"Üzgünüm! Miktar sınırı aşıyor, Lütfen daha küçük bir miktarla tekrar deneyin")
# Sepetin yeni halini yazdır.
                        print(color+"Sepetiniz artık şunları içeriyor:")
                        for i in range(len(sepet[kullanıcı_adı])):
                            oge_adı = list(sepet[kullanıcı_adı].keys())[i]
                            fiyat = Envanter[list(sepet[kullanıcı_adı].keys())[i]][1]
                            miktar = list(sepet[kullanıcı_adı].values())[i]
                            toplam = fiyat*miktar
                            sepet_toplamı += toplam
                            print(color+f"\t{i+1}. {oge_adı} fiyatı = {fiyat} $ miktar = {miktar} toplam = {toplam} $")
                        print(color+f"Toplam {sepet_toplamı} $")
                        sepet_toplamı = 0
# "Bir öğeyi kaldırın" seçildiyse;
                    elif sepet_sec == 2:
# Sepeti yazdır.
                        for i in range(len(sepet[kullanıcı_adı])):
                            oge_adı = list(sepet[kullanıcı_adı].keys())[i]
                            fiyat = Envanter[list(sepet[kullanıcı_adı].keys())[i]][1]
                            miktar = list(sepet[kullanıcı_adı].values())[i]
                            toplam = fiyat*miktar
                            sepet_toplamı += toplam
                            print(color+f"\t{i+1}. {oge_adı} fiyatı = {fiyat} $ miktar = {miktar} toplam = {toplam} $")
                        print(color+f"Toplam {sepet_toplamı} $")
                        sepet_toplamı = 0
# Silinmek istenen ürünü seç. Eğer seçilen ürün sırası listede yoksa uyarı ver ve tekrar seçilmesini iste komutunu gönder.
                        while True:
                            sepet_oge_sec = int(input(color+"Lütfen silmek istediğiniz öğeyi seçin: "))

                            if sepet_oge_sec in range(1,len(sepet[kullanıcı_adı])+1):
                                break
                            else:
                                print(color+"Lütfen geçerli bir ürün numarası seçiniz!\n")
# Silinmek için seçilen ürünün miktarını stoğa iade et ve sepetten sil işlemini gerçekleştir.
                        removed_item_qty = sepet[kullanıcı_adı][list(sepet[kullanıcı_adı].keys())[sepet_oge_sec-1]]
                        Envanter[list(sepet[kullanıcı_adı])[sepet_oge_sec-1]][0] += removed_item_qty
                        sepet[kullanıcı_adı].pop(list(sepet[kullanıcı_adı].keys())[sepet_oge_sec-1])
# Sepet boş kalmışsa uyarı ver.
                        if len(sepet[kullanıcı_adı]) == 0:
                            print(color+"Sepetiniz boş.\n\tToplam 0 $")
# Eğer sepet boş değilse sepeti yazdır.
                        else:
                            for i in range(len(sepet[kullanıcı_adı])):
                                oge_adı = list(sepet[kullanıcı_adı].keys())[i]
                                fiyat = Envanter[list(sepet[kullanıcı_adı].keys())[i]][1]
                                miktar = list(sepet[kullanıcı_adı].values())[i]
                                toplam = fiyat*miktar
                                sepet_toplamı += toplam
                                print(color+f"\t{i+1}. {oge_adı} fiyatı = {fiyat} $ miktar = {miktar} toplam = {toplam} $")
                            print(color+f"Toplam {sepet_toplamı} $")
                            sepet_toplamı = 0
# "Satın al" seçildiyse;
                    elif sepet_sec == 3:
#  sepet boşsa,
                        if len(sepet[kullanıcı_adı]) == 0:
                            print(color+"Sepetiniz boş.\n\tToplam 0 $")
# sepet boş değilse makbuzu yazdır
                        else:
                            print(color+f"""
Makbuzunuz işleniyor ...
*** İstinye Online Market ***
**************
\t0850 283 6000
\tistinye.edu.tr
————————————————————————————————————————————————————————————————""")
                            for i in range(len(sepet[kullanıcı_adı])):
                                oge_adı = list(sepet[kullanıcı_adı].keys())[i]
                                fiyat = Envanter[list(sepet[kullanıcı_adı].keys())[i]][1]
                                miktar = list(sepet[kullanıcı_adı].values())[i]
                                toplam = fiyat*miktar
                                sepet_toplamı += toplam
                                print(color+f"\t{i+1}. {oge_adı} fiyatı = {fiyat} $ miktar = {miktar} toplam = {toplam} $")
                            print(color+"————————————————————————————————————————————————————————————————")
                            print(color+f"Toplam {sepet_toplamı} $")
                            print(color+"————————————————————————————————————————————————————————————————")
                            print(color+datetime.now().strftime("%Y/%m/%d %H:%M"))
                            print(color+"Online Market’imizi kullandığınız için teşekkür ederiz!")
                            sepet_toplamı = 0
                            ana_menu_kontrolu = True
                            sepet[kullanıcı_adı] = {}
# Ana menüye dönüş yap komutu,
                        if ana_menu_kontrolu == True:
                            continue
# Eğer "Ana menüye dön" seçildiyse,
                    elif sepet_sec == 4:
                        break
# Ana menüden "Satın al" seçildiyse işlemler gerçekleşir.Ardından makbuz işleniyor devreye girer.
        elif secenek == 3:
            if len(sepet[kullanıcı_adı]) == 0:
                print(color+"Sepetiniz boş.\n\tToplam 0 $")
            else:
                print(color+f"""
Makbuzunuz işleniyor ...
*** İstinye Online Market ***
**************
\t0850 283 6000
\tistinye.edu.tr
————————————————————————————————————————————————————————————————""")
                for i in range(len(sepet[kullanıcı_adı])):
                    oge_adı = list(sepet[kullanıcı_adı].keys())[i]
                    fiyat = Envanter[list(sepet[kullanıcı_adı].keys())[i]][1]
                    miktar = list(sepet[kullanıcı_adı].values())[i]
                    toplam = fiyat*miktar
                    sepet_toplamı += toplam
                    print(color+f"\t{i+1}. {oge_adı} fiyatı = {fiyat} $ miktar = {miktar} toplam = {toplam} $")
                print(color+"————————————————————————————————————————————————————————————————")
                print(color+f"Toplam {sepet_toplamı} $")
                print(color+"————————————————————————————————————————————————————————————————")
                print(color+datetime.now().strftime("%Y/%m/%d %H:%M"))
                print(color+"Online Market’imizi kullandığınız için teşekkür ederiz!")
                sepet_toplamı = 0
                sepet[kullanıcı_adı] = {}
# "Oturumu kapat" seçildiyse ana menüden çık ve oturum açma arayüzüne dön komutu devreye girer.
        elif secenek == 4:
            break
# Eğer "Çıkış yap" seçildiyse programı sonlandır ve işlem biter.
        elif secenek == 5:
            quit()



#---------------------------------------------------------------------------------------------
#EKRAN ÇIKTILARININ TUTUNCU OLABİLMESİ İÇİN TERMİNAL BÖLÜMÜNE "pip install colored " yazmalıyız.
#---------------------------------------------------------------------------------------------





        #KAYNAKÇA
# https://www.youtube.com/watch?v=vQPNf2KGwE4 (pythonda sözlük oluşturma )
# https://www.youtube.com/watch?v=MgFL--tZ2tQ (pythonda tuple, liste oluşturma )
# https://stackoverflow.com/questions/27265322/how-to-print-to-console-in-color    (konsola renkli yazı yazdırma)
# https://www.geeksforgeeks.org/print-colors-python-terminal/    (terminalde coloroma yöntemi nasıl kullanılır.)
# https://stackoverflow.com/questions/39473297/how-do-i-print-colored-output-with-python-3  (Pythonda renkli çıktı elde etmek.)
# https://stackoverflow.com/questions/4843158/check-if-a-python-list-item-contains-a-string-inside-another-string (Pythonda dizi içeriğini kontrol etmek.)
# https://www.programiz.com/python-programming/methods/built-in/iter (Pythonda yineleme işlevi)
# https://www.programiz.com/python-programming/datetime/current-datetime (pythonda güncel tarih ve saat alma işlemi.)
# https://www.w3schools.com/python/python_dictionaries.asp (python sözlükler.)
# https://www.programiz.com/python-programming/nested-dictionary (pythonda iç içe sözlük kullanımı.)
# https://www.geeksforgeeks.org/python-nested-dictionary/
# https://www.programiz.com/python-programming/methods/dictionary/pop (pythonda sözlük)


#   """    201216110  Damla GÖKGÖZ Bilgisayar Programcılığı 1.sınıf    """