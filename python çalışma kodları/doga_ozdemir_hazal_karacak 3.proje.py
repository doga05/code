from datetime import datetime
import time
import colored
color = colored.fg(130) 
#çıktılarımızın turuncu olması için yukarıdaki yöntemi kullandık.
Envanter = {"kuşkonmaz": [10,5], "brokoli": [15,6], "havuç": [18,7], "elmalar": [20,5],
"muz":[10, 8], "meyve": [30,3], "yumurta": [50,2], "karışık meyve suyu": [0,18], "balık çubukları":[25,12],
"dondurma": [32,6], "elma suyu": [40,7], "portakal suyu": [30,8], "üzüm suyu":[10,9]}
#üst kısımdaki envanter kısmı sizin vermiş olduğunuz ödev tanıtım dosyasından alınmıştır. 
users = {"ahmet":{"pwd":"İstinye123"},"meryem":{"pwd":"4444"},"doga":{"pwd":"1905"}, "hazal":{"pwd":"1903"}}
#üst kısımda bir sözlük oluşturuldu bu sözlükte kullanıcıların isimm ve şifre bilgilerinin kayıt altında tutulması amaçlanmıştır.
basket = {"ahmet":{},"meryem":{},"doga":{}, "hazal":{}}
#bu kısım isim ve şifredeki gibi sözlük açılarak kullanıcıların sepet bilgirini  tutması için kullanılmıştır .
main_menu_check = False
basket_sum =0.0
total =0.0
product_number = 0
pay = 0
quantity =0
counter = 0
select_product =0 
product_name = ""
username = ""
password = ""
search_product = ""
found_products = []
# üst kısımda e ticaret uygulamamızda çalışıcak olan değişkenlere ilk tip ve değer atamalarını uyguluyoruz.
while True:
    print(color+""">>>>>>>>>> WELCOME TO THE ISTINYE ONLINE MARKET <<<<<<<<<<
  Please enter your username and password:""" )
    time.sleep(1)
    username = input(color+"User Name: ")
    time.sleep(1)
    password = input(color+"Password: ")
    print("Checking your password please wait!!")
    print(">>>>3<<<<")
    time.sleep(1)
    print(">>>>2<<<<")
    time.sleep(1)
    print(">>>>1<<<<")
    if username in users.keys() and users[username]["pwd"] == password:
        print(color+"You have successfully logged in.!")
        print(color+f"Welcome {username}!Please select one of the following options by entering the corresponding menu number.\n")
    else:
        print(color+"Your username and / or password is not correct.Please try again!\n")
        continue
#üst kısımda kullanıcı arayüzü oluşturulmuştur. Girilen isim ve şifre users  kısımda verilen ile eşdeğer durumdaysa kullanıcı sorunsuz giriş yapar . 
#Girilen şifre ve isim users kısmında verilen ile eşleşmemekteyse kullanıcıya uyarı veriri ve geçerli bir isim girmesi istenir .
#kulanıcı geçerli isim girdiğinde program onu ana menü arayüzüne aktarır.
    while True:
        main_menu_check = False
        select = int(input(color+"""Please choose one of the services below:
1. Search product
2. Go to basket
3. Buy
4. Sign Out
5. Log out
"""))
        if select not in [1,2,3,4,5]:
            print(color+"Please select a valid menu number!\n")
# üstteki kısım bize seçebiliceğimiz menü numaralarını verir ve geçersiz bir menü numarası girdiğimizde bizi uyarı verir.
        elif select == 1:  # eğer 1 numaralı menü seçilmişse şunları uygular.
            while True:
                search_product = input(color+"What are you looking for? ")
                if search_product == "0":
                    main_menu_check = True
                    break
                for product in Envanter.keys():
                    if search_product in product :
                        counter += 1
                        found_products.append(product)
                if counter > 0:
                    break
                else:
                    print(color+"Your search did not match any items. Please try something else (Enter 0 for main menu):")
            if main_menu_check == True:
# if search_product == "0": bu kısımda 0'ı tuşladığımızda ana menüye geri döner.
# arama yapmak için girdiğimiz anahtar kelime "Envanter" sözlüğündeki ürün isimleri içerisinde yer alıyorsa bulunan ürünleri "search_product" listesinin içine yollar .
# daha sonnra bulunan ürün sayısını sayan sayaç ekledik .
                continue
            print(color+f"{counter} similar products found:\n")
            for iter in range(len(found_products)):
                print(color+f"{iter+1}. {found_products[iter]} {Envanter[found_products[iter]][1]} $")
            print("\n")
# üst kısımda da bulunan ürünleri ekrana yazdırması için gereken işlemleri yaptık ve bulunan ürünlerden hangisinden kaç tane sepete eklemek istediğimizi seçtiren  yazdıran bir kod girdik .
            while True:
                select_product = int(input(color+"Please select the item you want to add to your basket (Enter 0 for the main menu): "))
                if select_product == 0:
                    counter = 0
                    found_products = []
                    main_menu_check = True
                    break
                if select_product not in range(1,len(found_products)+1):
                    print(color+"Your search did not match any items. Please try something else (Enter 0 for main menu):")
                    continue
                while True:
                    product_number = int(input(color+f"{found_products[select_product-1]} products are being added. How many you want?: "))
                    if product_number> 0:
                        break
                    else:
                        print(color+"Please select at least 1 product!\n")
                        #üst kısımdaki kodlarda ilk seçenek olarak ana menüye dönme kodlanmıştır.Daha sonra  eğer girilen değer bulunan ürünler listesinin uzunuğundan 
                        # fazla ise uyarı cermesini ve tekrardan istemesini sağladık. Daha sonra seçilen ürünü sepete eklemeyi ve kaç adet ekleneceğini  0 dan büyük bir 
                        #değer girmez ise uyarı verip yeni bir değer istemesi gerektiğini yazdırdık.
                while True:
                    if Envanter[found_products[select_product-1]][0] >= product_number:
                        if  found_products[select_product-1] not in basket[username].keys():
                            Envanter[found_products[select_product-1]][0] -= product_number
                            basket[username].update({found_products[select_product-1]:product_number})
                            print(color+f"Your basket {found_products[select_product-1]} added.\nReturning to the main menu ...\n")
                            main_menu_check = True
                            found_products = []
                            counter = 0
                            break
                        else:
                            Envanter[found_products[select_product-1]][0] -= product_number
                            basket[username][found_products[select_product-1]] += product_number
                            print(color+f"Your basket {found_products[select_product-1]} added.\nReturning to the main menu ...\n")
                            main_menu_check = True
                            found_products = []
                            counter = 0
                            break
                    else:
                        print(color+"Sorry! Quantity exceeds limit, Please try again with a smaller amount")
                        product_number = int(input(color+"Quantity (Enter 0 for main menu): "))
                        if product_number == 0:
                            main_menu_check = True
                            break
                if main_menu_check == True:
                    break
            if main_menu_check == True:
                continue
            #üst kısımda ise seçilen ve adedi belirtilen ürünü sepete ekleme, stoktan düşme gibi işlemler için gerekli olanı yaptık. 
            #Eğer seçilen üründen yeteri kadar varsa sepete ekler ve stoktan düşer, ama stokta yeteri kadar yoksa uyarı verir ve miktarı yeniden girmesini ister.
            #Seçilen ürün daha önceden sepete eklenmiş ise ekleme yapar.Daha sonra ana menüye dönüş yapar.
        elif select == 2:
            if len(basket[username]) == 0:
                print(color+"Your basket is empty\n\tTotal 0 $")
                main_menu_check = True
                continue
            else:
                print(color+"Your basket includes:")
                for i in range(len(basket[username])):
                    product_name = list(basket[username].keys())[i]
                    pay = Envanter[list(basket[username].keys())[i]][1]
                    quantity = list(basket[username].values())[i]
                    sum = pay*quantity
                    basket_sum += sum
                    print(color+f"\t{i+1}. {product_name} pay = {pay} $ quantity= {quantity} sum = {sum} $")
                print(color+f"sum {basket_sum} $")
                basket_sum = 0.0
    #üst kısımda eğer sepet boş ise uyarı verip ana menüye çıkmasını , eğer sepet boş değil ise sepetin içeriğini,toplam fiyatını ve sepet menüsünü yazdırması sağlanmıştır .
                while True:
                    basket_select = int(input(color+"""
Choose an option:
1. Update Amount
2. Remove a product
3. Buy
4. Back to main menu
"""))
                    if basket_select not in [1,2,3,4]:
                        print(color+"Please select a valid menu number!\n")
                        continue
            # bu kısımda sepet menüsü oluşturulmuştur .Girilen değer menü üyeleriyle uyuşmuyorsa uyarı verip tekrardan sorması istenmiştir.
            # üst kısımda verilen seçeneklerden 1 numaralı "olan Update Amount"seçildiyse aşağıdaki yol izlenir
                    elif basket_select == 1:
                        for i in range(len(basket[username])):
                            product_name = list(basket[username].keys())[i]
                            pay = Envanter[list(basket[username].keys())[i]][1]
                            quantity = list(basket[username].values())[i]
                            sum = pay*quantity
                            basket_sum += sum
                            print(color+f"\t{i+1}. {product_name} pay = {pay} $ quantity = {quantity} total = {total} $")
                        print(color+f"Total {basket_sum} $")
                        basket_sum = 0
                #Sepetteki içerik ve sepetin toplarm ürün tutarını yazdırılması amaçlanmıştır.Geçerli bir ürün numarası girilmediği takdirde tekrar istenecek şekilde yapılmıştır.
                        while True:
                            basket_select_product = int(input(color+"Please select the product you will change the quantity: "))
                            if basket_select_product in range(1,len(basket[username])+1):
                                break
                            else:
                                print(color+"Please select a valid product number!\n")
            #Şayet girilen ürün numarası sepet listesinin uzunluğundan  büyük değilse uyarı vermesi ve tekrardan girilmesini istemesi amaçlanmıştır . Daha sonra seçilen ürünün yeni miktarı istenir .
                        while True:
                            while True:
                                product_newqty = int(input(color+"Please enter a new amount: "))
                                if product_newqty > 0:
                                    break
                                else:
                                    print(color+"Please select at least 1 product!\n")
                    #üst kısımda şayet girilen yeni miktar 0'dan küçük yahut 0'a eşit ise uyarı vermesi vetekırar girmesini istemesi amaçlanmıştır.
                    #Yeni girilen değer stoktaki seçilen ürün miktarından büyük durumda ise uyarı vermesi ve kullanıcıdan tekrar değer girmesi istenmiştir .
                            if product_newqty <= Envanter[list(basket[username])[basket_select_product-1]][0]:
                                product_oldqty = basket[username][list(basket[username].keys())[basket_select_product-1]]
                                basket[username][list(basket[username].keys())[basket_select_product-1]] = product_newqty
                                Envanter[list(basket[username])[basket_select_product-1]][0] -= product_newqty
                                Envanter[list(basket[username])[basket_select_product-1]][0] += product_oldqty
                                break
                            else:
                                print(color+"Sorry! Quantity exceeds limit, Please try again with a smaller amount")
                        #eski miktarı stoğa geri ekleme ve yeni değeri stoktan geri eksiltme işlemi yapılmıştır.
                        print(color+"Your basket now includes:")
                        for i in range(len(basket[username])):
                            product_name = list(basket[username].keys())[i]
                            pay = Envanter[list(basket[username].keys())[i]][1]
                            quantity = list(basket[username].values())[i]
                            sum = pay*quantity
                            basket_sum += sum
                            print(color+f"\t{i+1}. {product_name} pay = {pay} $ quantity = {quantity} sum = {sum} $")
                        print(color+f"Total {basket_sum} $")
                        basket_sum = 0
                #üst taraftaki kıodlar sepetin yeni halini yazdırmamızı sağlayacaktır.
                    # Eğer "Remove a product" seçildiyse aşagıdaki işlemler takip edilecektir.
                    elif basket_select == 2:
                        for i in range(len(basket[username])):
                            product_name = list(basket[username].keys())[i]
                            pay = Envanter[list(basket[username].keys())[i]][1]
                            quantity = list(basket[username].values())[i]
                            sum = pay*quantity
                            basket_sum += sum
                            print(color+f"\t{i+1}. {product_name} pay = {pay} $ quantity = {quantity} sum = {sum} $")
                        print(color+f"Total {basket_sum} $")
                        basket_sum = 0
                        while True:
                            basket_select_product = int(input(color+"Please select the product you want to delete: "))
                            if basket_select_product in range(1,len(basket[username])+1):
                                break
                            else:
                                print(color+"Please select a valid item number!\n")
                        removed_productqty = basket[username][list(basket[username].keys())[basket_select_product-1]]
                        Envanter[list(basket[username])[basket_select_product-1]][0] += removed_productqty
                        basket[username].pop(list(basket[username].keys())[basket_select_product-1])
                        # Eğer sepet boş kalmışsa uyarı ver
                        #silinmek istenen ürün seçilir ,seçilen ürün sırası listede yoksa uyarı verilmesi ve tekrar seçilmesiniistemesi sağlanır.
                        #silinmek için seçilen ürün miktarı sepete eklendiğinde düştüğü için ürünün miktarı stoğa iade edilir ve sepettenh kalıcı olarak slinir .
                        #Ürün sildikten sonra sepetimiz boş kaldıysa bununla ilgili uyarı vermesi sağlanır.
                        if len(basket[username]) == 0:
                            print(color+"Your basket is empty.\n\tTotal 0 $")
                        #lakin boş değilse sepeti yazdırırız
                        else:
                            for i in range(len(basket[username])):
                                product_name = list(basket[username].keys())[i]
                                pay = Envanter[list(basket[username].keys())[i]][1]
                                quantity = list(basket[username].values())[i]
                                sum = pay*quantity
                                basket_sum += sum
                                print(color+f"\t{i+1}. {product_name} pay = {pay} $ quantity = {quantity} sum = {sum} $")
                            print(color+f"Total {basket_sum} $")
                            basket_sum = 0
                    # Eğer "Buy"  butonu seçildiyse aşağıdaki yollar izlenecektir.
                    elif basket_select == 3:
                        
                        
                        if len(basket[username]) == 0:
                            print(color+"Your basket is empty.\n\tTotal 0 $")
                        else:
                            for i in range(3):
                                time.sleep(1)
                                print("Please wait for your receipt to be printed!!!")
                                print(i)
                           
                            print(color+f"""
Your receipt is  processed ...
*** Istinye Online Market ***
**************
\t0850 283 6000
\tistinye.edu.tr
————————————————————————————————
""")
#Eğer sepet boş ise uyarı verip sepetin boş olduğu bildirilir . Lakin boş değil ise makbuzu yazdırması istenir.
                            for i in range(len(basket[username])):
                                product_name = list(basket[username].keys())[i]
                                pay = Envanter[list(basket[username].keys())[i]][1]
                                quantity = list(basket[username].values())[i]
                                sum = pay*quantity
                                basket_sum += sum
                                print(color+f"\t{i+1}. {product_name} pay = {pay} $ quantity = {quantity} sum = {sum} $")
                            print(color+"————————————————————————————————")
                            print(color+f"Total {basket_sum} $")
                            print(color+"————————————————————————————————")
                            print(color+datetime.now().strftime("%Y/%m/%d %H:%M"))
                            print(color+"Thank you for using our Online Market!")
                            basket_sum = 0
                            main_menu_check = True
                            basket[username] = {}
                             # üst kısımda sepetin son hlinin yazdırılması istenmiştir.
                        if main_menu_check == True:
                            continue
                    elif basket_select == 4:
                        break
                    # ana manüye dönmek için ve eğer "Back to main menu" seçildiyse bu yol izlenir.

        elif select == 3:     # ana menüden "Buy"  seçilirse aşağıdakiler  izlenecektir.
            if len(basket[username]) == 0:
                print(color+"Your basket is empty.\n\tTotal 0 $")

            else:
                for i in range(3):
                    time.sleep(1)
                    print("Please wait for your receipt to be printed!!!")
                    print(i)

                print(color+f"""
Your receipt is  processed ...
*** Istinye Online Market ***
**************
\t0850 283 6000
\tistinye.edu.tr
————————————————————————————————
""")


                for i in range(len(basket[username])):
                    product_name = list(basket[username].keys())[i]
                    pay = Envanter[list(basket[username].keys())[i]][1]
                    quantity = list(basket[username].values())[i]
                    sum = pay*quantity
                    basket_sum += sum
                    print(color+f"\t{i+1}. {product_name} pay = {pay} $ quantity = {quantity} sum = {sum} $")
                    
                print(color+"————————————————————————————————")
                print(color+f"Total {basket_sum} $")
                print(color+"————————————————————————————————")
                print(color+datetime.now().strftime("%Y/%m/%d %H:%M"))
                print(color+"Thank you for using our Online Market!")
                basket_sum = 0
                basket[username] = {}
        # Eğer "sign Out" seçildiyse ana menüden çıkap oturum ana menüsünhe dönmelidir.
        elif select == 4:
            break
        # Eğer "Log Out" seçildiyse alı8şveriş tamamlanmıştır ve artık program sonlandırılabilir demektir.
        elif select == 5:
            quit()



# https://stackoverflow.com/questions/39473297/how-do-i-print-colored-output-with-python-3
# https://stackoverflow.com/questions/73663/how-to-terminate-a-python-script
# https://stackoverflow.com/questions/4843158/check-if-a-python-list-item-contains-a-string-inside-another-string
# https://www.programiz.com/python-programming/nested-dictionary
# https://www.geeksforgeeks.org/python-nested-dictionary/
# https://www.programiz.com/python-programming/methods/dictionary/pop
# https://python-istihza.yazbel.com/standart_moduller/time.html
# https://stackoverflow.com/questions/19184335/is-there-a-need-for-rangelena
# https://www.w3schools.com/python/python_dictionaries.asp
# https://www.tutorialspoint.com/python/python_dictionary.htm
# https://stackoverflow.com/questions/27265322/how-to-print-to-console-in-color
# https://www.geeksforgeeks.org/print-colors-python-terminal/
