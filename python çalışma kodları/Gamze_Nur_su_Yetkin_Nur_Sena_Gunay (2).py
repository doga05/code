from datetime import datetime
import colored
color = colored.fg(130)

# pdf de ki envanter bilgisinin tutulduğu dict tanımlaması.
Envanter = {"kuşkonmaz": [10,5], "brokoli": [15,6], "havuç": [18,7], "elmalar": [20,5],
"muz":[10, 8], "meyve": [30,3], "yumurta": [50,2], "karışık meyve suyu": [0,18], "balık çubukları":[25,12],
"dondurma": [32,6], "elma suyu": [40,7], "portakal suyu": [30,8], "üzüm suyu":[10,9]}
# Kullanıcıların bilgilerini tutan dict tanımlaması.
users = {"ahmet":{"pwd":"İstinye12345"},"meryem":{"pwd":"4444"}}
# Kulanıcıların sepetindeki ürünleri tutan dict tanımlaması.
basket = {"ahmet":{},"meryem":{}}
# Kullanılan değişkenlerin ilk değer ve tip atamaları
anamenu_kontrol, basket_toplam, toplam, item_number, fiyat, miktar, counter, öğe_seç, item_name, username, pwd, ara_item, find_items =False, 0.0, 0.0, 0, 0, 0, 0, 0, "", "", "", "", []
# Kullanıcı girişi
while True:
    print(color+"""* İstinye Online Market'e Hoşgeldiniz *
Lütfen kullanıcı kimlik bilgilerinizi sağlayarak giriş yapın:""")
    # Kullanıcı adı ve şifre girişi
    username = input(color+"Kullanıcı adı: ")
    pwd = input(color+"Şifre: ")
   
    if username in users.keys() and users[username]["pwd"] == pwd:
        print(color+"Başarıyla giriş yapıldı!")
        print(color+f"Hoşgeldiniz {username}! Lütfen ilgili menü numarasını girerek aşağıdaki seçeneklerden birini seçin.\n")
   
    else:
        print(color+"Kullanıcı adınız ve / veya şifreniz doğru değil. Lütfen tekrar deneyin!\n")
        continue
    # Ana menü seçenekleri oluşturuldu.
    while True:
        anamenu_kontrol = False
        seçim = int(input(color+"""Lütfen aşağıdaki hizmetlerden birini seçin:
1. Ürün ara
2. Sepete git
3. Satın al
4. Oturum Kapat
5. Çıkış yap
"""))
        # Geçersiz menü numarası girilirse uyarı ver.
        if seçim not in [1,2,3,4,5]:
            print(color+"Lütfen geçerli bir menü numarası seçiniz!\n")
       
        elif seçim == 1:
            while True:
                ara_item = input(color+"Ne arıyorsunuz? ")
               
                if ara_item == "0":
                    anamenu_kontrol = True
                    break
                # Aratılan kelime envanter dictinin içinde bulunuyor ise bulunan ürünleri find_items listesinin içine at.
                for item in Envanter.keys():
                    if ara_item in item:
                        # Bulunan ürün sayısını sayan sayaç
                        counter += 1
                        find_items.append(item)
                # Sayaç 0 ise hiç ürün bulunamamış demektir
                if counter > 0:
                    break
                else:
                    print(color+"Aramanız hiçbir öğeyle eşleşmedi. Lütfen başka bir şey deneyin (Ana menü için 0 girin):")
            if anamenu_kontrol == True:
                continue
            # Bulunan ürünleri ekrana yazdırmak
            print(color+f"{counter} benzer ürün bulundu:\n")
            for iter in range(len(find_items)):
                print(color+f"{iter+1}. {find_items[iter]} {Envanter[find_items[iter]][1]} $")
            print("\n")
            # Bulunan ürünlerden sepete miktarda eklemek istediğimizi seçmek.
            while True:
                öğe_seç= int(input(color+"Lütfen sepetinize eklemek istediğiniz ürünü seçin (Ana menü için 0 girin): "))
                # Ana menüye dönmek
                if öğe_seç == 0:
                    counter = 0
                    find_items = []
                    anamenu_kontrol = True
                    break
                # Girilen değer bulunan ürünler listesinin uzunluğundan büyük ise uyarı ver ve tekrar giriş iste.
                if öğe_seç not in range(1,len(find_items)+1):
                    print(color+"Aramanız hiçbir öğeyle eşleşmedi. Lütfen başka bir şey deneyin (Ana menü için 0 girin):")
                    continue
                # Seçilen ürünü sepete ekle
                while True:
                    # Sepete seçilen üründen ne miktarda ekleniceği.
                    item_number = int(input(color+f"{find_items[öğe_seç-1]} ekleniyor. Adedi Girin: "))
                    # 0 dan büyük değer girilmezse uyarı ver ve tekrar değer girilmesini iste.
                    if item_number > 0:
                        break
                    else:
                        print(color+"Lütfen en az 1 adet ürün seçiniz!\n")
                # Seçilen ve miktarı belirtilen ürünü sepete eklemek ve stoktan azaltmak.
                while True:
                    # Seçilen üründen istenen miktarda ürün varsa sepete eklenir.
                    if Envanter[find_items[öğe_seç-1]][0] >= item_number:
                        # Seçilen ürün daha önceden sepete eklenmemişse
                        if  find_items[öğe_seç-1] not in basket[username].keys():
                            Envanter[find_items[öğe_seç-1]][0] -= item_number
                            basket[username].update({find_items[öğe_seç-1]:item_number})
                            print(color+f"Sepetinize {find_items[öğe_seç-1]} eklendi.\nAna menüye geri dönülüyor ...\n")
                            anamenu_kontrol = True
                            find_items = []
                            counter = 0
                            break
                        # Seçilen ürün daha önceden sepete eklendiyse, üzerine ekleme yap.
                        else:
                            Envanter[find_items[öğe_seç-1]][0] -= item_number
                            basket[username][find_items[öğe_seç-1]] += item_number
                            print(color+f"Sepetinize {find_items[öğe_seç-1]} eklendi.\nAna menüye geri dönülüyor ...\n")
                            anamenu_kontrol = True
                            find_items = []
                            counter = 0
                            break
                    # Seçilen üründen stokta yeteri kadar yoksa miktarın tekrar girmesini iste.
                    else:
                        print(color+"Üzgünüm! Miktar sınırı aşıyor, Lütfen daha küçük bir miktarla tekrar deneyin")
                        item_number = int(input(color+"Miktar (Ana menü için 0 girin): "))
                        # Ana menüye dönmek
                        if item_number == 0:
                            anamenu_kontrol = True
                            break
                if anamenu_kontrol == True:
                    break
            if anamenu_kontrol == True:
                continue
        # "Sepete gitme"  seçenegi seçilmişse.
        elif seçim == 2:
            # Sepet boşsa uyarı ver ana menüye dön
            if len(basket[username]) == 0:
                print(color+"Sepetiniz boş.\n\tToplam 0 $")
                anamenu_kontrol= True
                continue
            # Sepet boş değilse içeriğini, toplam fiyatı ve sepet menüsünü yazdır.
            else:
                print(color+"Sepetiniz şunları içerir:")
                for i in range(len(basket[username])):
                    item_name = list(basket[username].keys())[i]
                    fiyat = Envanter[list(basket[username].keys())[i]][1]
                    miktar = list(basket[username].values())[i]
                    toplam = fiyat*miktar
                    basket_toplam += toplam
                    print(color+f"\t{i+1}. {item_name} fiyatı = {fiyat} $ Toplam Tutar = {miktar} toplamı= {toplam} $")
                print(color+f"Toplamı {basket_toplam} $")
                basket_toplam = 0.0
                # Sepet menüsü
                while True:
                    basket_seçim = int(input(color+"""
Bir seçeneği seçiniz:
1. Tutarı güncelleyin
2. Bir öğeyi kaldırın
3. Satın al
4. Ana menüye dön
"""))
                    # Girilen değer sayı aralığında yoksa uyarı verir ve tekrar değer girilmesini ister.
                    if basket_seçim not in [1,2,3,4]:
                        print(color+"Lütfen geçerli bir menü numarası seçiniz!\n")
                        continue
                    # "Toplam Tutarı güncelleyin" seçeneği seçildiyse
                    elif basket_seçim == 1:
                        # Sepet içeriği,toplam tutarı yazdır.
                        for i in range(len(basket[username])):
                            item_name = list(basket[username].keys())[i]
                            fiyat = Envanter[list(basket[username].keys())[i]][1]
                            miktar = list(basket[username].values())[i]
                            toplam = fiyat*miktar
                            basket_toplam += toplam
                            print(color+f"\t{i+1}. {item_name} fiyatı = {fiyat} $ Toplam Tutar = {miktar} toplamı = {toplam} $")
                        print(color+f"Toplam {basket_toplam} $")
                        basket_toplam = 0
                        # Geçerli aralıkta ürün numarası girilene kadar tekrar numara girilmesini ister.
                        while True:
                            basket_seçim_item = int(input(color+"Lütfen miktarını değiştireceğiniz öğeyi seçin: "))
                            # Girilen ürün numarası sepet listesinin uzunluğundan küçükse uyarı ver ve tekrar giriş iste.
                            if basket_seçim_item in range(1,len(basket[username])+1):
                                break
                            else:
                                print(color+"Lütfen geçerli bir ürün numarası seçiniz!\n")
                        # Seçilen ürünün yeni miktarı
                        while True:
                            while True:
                                yeni_miktar = int(input(color+"Lütfen yeni miktarı yazın: "))
                                # Girilene yeni miktar 0'dan küçük  veya eşitse uyarı verir ve tekrar girilmesini ister
                                if yeni_miktar > 0:
                                    break
                                else:
                                    print(color+"Lütfen en az 1 adet ürün seçiniz!\n")
                            # Girilen değer stoktaki seçilen ürünün miktarından büyük ise uyarı ver ve yeni değer girilmesini iste.
                            if yeni_miktar <= Envanter[list(basket[username])[basket_seçim_item-1]][0]:
                                # Eski ürünün miktarının stoğa eklenmesi, yeni miktarın stoktan azaltılması.
                                eski_miktar = basket[username][list(basket[username].keys())[basket_seçim_item-1]]
                                basket[username][list(basket[username].keys())[basket_seçim_item-1]] = yeni_miktar
                                Envanter[list(basket[username])[basket_seçim_item-1]][0] -= yeni_miktar
                                Envanter[list(basket[username])[basket_seçim_item-1]][0] += eski_miktar
                                break
                            else:
                                print(color+"Üzgünüm! Miktar sınırı aşıyor, Lütfen daha küçük bir miktarla tekrar deneyin")
                        # Sepetin yeni hali
                        print(color+"Sepetiniz artık şunları içeriyor:")
                        for i in range(len(basket[username])):
                            item_name = list(basket[username].keys())[i]
                            fiyat = Envanter[list(basket[username].keys())[i]][1]
                            miktar = list(basket[username].values())[i]
                            toplam = fiyat*miktar
                            basket_toplam += toplam
                            print(color+f"\t{i+1}. {item_name} fiyatı = {fiyat} $ Toplam Tutarı = {miktar} toplamı = {toplam} $")
                        print(color+f"Toplam Tutarı {basket_toplam} $")
                        basket_toplam = 0
                    # Seçeneklerden "Bir öğeyi kaldırın" seçildiyse.
                    elif basket_seçim == 2:
                        # Sepeti yazdır
                        for i in range(len(basket[username])):
                            item_name = list(basket[username].keys())[i]
                            fiyat= Envanter[list(basket[username].keys())[i]][1]
                            miktar = list(basket[username].values())[i]
                            toplam = fiyat*miktar
                            basket_toplam += toplam
                            print(color+f"\t{i+1}. {item_name} fiyatı = {fiyat} $ Toplam Tutarı = {miktar} toplamı = {toplam} $")
                        print(color+f"Toplam {basket_toplam} $")
                        basket_toplam = 0
                        # Sepettenn çıkarılmak istenen ürünü seç.
                        while True:
                            basket_seçim_item = int(input(color+"Lütfen silmek istediğiniz öğeyi seçin: "))
                            # Girilen ürün numarası  listede yoksa uyarı ver ve tekrar değer girilmesini iste.
                            if basket_seçim_item in range(1,len(basket[username])+1):
                                break
                            else:
                                print(color+"Lütfen geçerli bir ürün numarası seçiniz!\n")
                        # Sepete eklendikten sonra, sepetten çıkarılan ürünü stoğa geri eklemek.
                        kaldırılan_öğe= basket[username][list(basket[username].keys())[basket_seçim_item-1]]
                        Envanter[list(basket[username])[basket_seçim_item-1]][0] += kaldırılan_öğe
                        basket[username].pop(list(basket[username].keys())[basket_seçim_item-1])
                        # Ürün çıkartıldıktan sonra sepet boş kalmışsa uyarı ver.
                        if len(basket[username]) == 0:
                            print(color+"Sepetiniz boş.\n\tToplam 0 $")
                        # Sepet boş değilse sepeti yazdır.
                        else:
                            for i in range(len(basket[username])):
                                item_name = list(basket[username].keys())[i]
                                fiyat = Envanter[list(basket[username].keys())[i]][1]
                                miktar = list(basket[username].values())[i]
                                toplam = fiyat*miktar
                                basket_toplam += toplam
                                print(color+f"\t{i+1}. {item_name} fiyatı = {fiyat} $ Toplam Tutarı= {miktar} toplamı = {toplam} $")
                            print(color+f"Toplam Tutarı {basket_toplam} $")
                            basket_toplam = 0
                    # Seçeneklerden "Satın al" seçildiyse.
                    elif basket_seçim == 3:
                        # Sepet boşsa uyarı ver.
                        if len(basket[username]) == 0:
                            print(color+"Sepetiniz boş.\n\tToplam 0 $")
                        # Sepet boş değilse fişi yazdır.
                        else:
                            print(color+f"""
Makbuzunuz işleniyor ...
* İstinye Online Market *
******
\t0850 283 6000
\tistinye.edu.tr
————————————————————————————————
""")
                            for i in range(len(basket[username])):
                                item_name = list(basket[username].keys())[i]
                                fiyat = Envanter[list(basket[username].keys())[i]][1]
                                miktar = list(basket[username].values())[i]
                                toplam = fiyat*miktar
                                basket_toplam += toplam
                                print(color+f"\t{i+1}. {item_name} fiyatı = {fiyat} $ Toplam Tutarı = {miktar} toplamı = {toplam} $")
                            print(color+"————————————————————————————————")
                            print(color+f"Toplam Tutarı{basket_toplam} $")
                            print(color+"————————————————————————————————")
                            print(color+datetime.now().strftime("%Y/%m/%d %H:%M"))
                            print(color+"Online Market’imizi kullandığınız için teşekkür ederiz!")
                            basket_toplam = 0
                            anamenu_kontrol = True
                            basket[username] = {}
                        # Ana menüye dönmek.
                        if anamenu_kontrol == True:
                            continue
                    # Seçeneklerden "Ana menüye dön" seçildiyse.
                    elif basket_seçim == 4:
                        break
        # Ana menüdeki seçeneklerden "Satın al" seçildiyse.
        elif seçim == 3:
            if len(basket[username]) == 0:
                print(color+"Sepetiniz boş.\n\tToplam 0 $")
            else:
                print(color+f"""
Makbuzunuz işleniyor ...
* İstinye Online Market *
******
\t0850 283 6000
\tistinye.edu.tr
————————————————————————————————
""")
                for i in range(len(basket[username])):
                    item_name = list(basket[username].keys())[i]
                    fiyat = Envanter[list(basket[username].keys())[i]][1]
                    miktar = list(basket[username].values())[i]
                    toplam = fiyat*miktar
                    basket_toplam += toplam
                    print(color+f"\t{i+1}. {item_name} fiyatı = {fiyat} $ Toplam Tutar = {miktar} toplamı = {toplam} $")
                print(color+"————————————————————————————————")
                print(color+f"Toplam Tutar {basket_toplam} $")
                print(color+"————————————————————————————————")
                print(color+datetime.now().strftime("%Y/%m/%d %H:%M"))
                print(color+"Online Market’imizi kullandığınız için teşekkür ederiz!")
                basket_toplam = 0
                basket[username] = {}
        # Seçeneklerden "Oturumu kapat" seçildiyse ana menüden çık ve oturum açmaya dön.
        elif seçim == 4:
            break
        # Seçeneklerden "Çıkış yap" seçildiyse programı sonlandır.
        elif seçim == 5:
            quit()



           
            #NUR SENA GÜNAY 201216073
            #GAMZE NUR SU YETKİN 201216083

 
 
 
 #KAYNAKÇA          

# https://stackoverflow.com/questions/27265322/how-to-print-to-console-in-color
# https://www.geeksforgeeks.org/print-colors-python-terminal/
# https://stackoverflow.com/questions/39473297/how-do-i-print-colored-output-with-python-3
# https://ozzmaker.com/add-colour-to-text-in-python/#:~:text=To%20make%20some%20of%20your,right%20into%20the%20print%20statement.
# https://stackoverflow.com/questions/73663/how-to-terminate-a-python-script
# https://stackoverflow.com/questions/4843158/check-if-a-python-list-item-contains-a-string-inside-another-string
# https://www.programiz.com/python-programming/methods/built-in/iter
# https://www.programiz.com/python-programming/datetime/current-datetime
# https://www.w3schools.com/python/python_dictionaries.asp
# https://www.programiz.com/python-programming/nested-dictionary
# https://www.geeksforgeeks.org/python-nested-dictionary/
# https://www.programiz.com/python-programming/methods/dictionary/pop