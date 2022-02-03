from datetime import datetime
Envanter = {"kuşkonmaz": [10,5], "brokoli": [15,6], "havuç": [18,7], "elmalar": [20,5],
"muz":[10, 8], "meyve": [30,3], "yumurta": [50,2], "karışık meyve suyu": [0,18], "balık çubukları":[25,12],
"dondurma": [32,6], "elma suyu": [40,7], "portakal suyu": [30,8], "üzüm suyu":[10,9]}
#Kullanıcıların şifre ve adlarını tutup kaydetmesi için bir sözlük açıldı.
users = {"ahmet":{"pwd":"İstinye123"},"meryem":{"pwd":"4444"}}
# Kulanıcıların sepetindeki ürünleri tutması için bir sözlük açıldı
basket = {"ahmet":{},"meryem":{}}
# Kullanılan değişkenlerin ilk değerleri verildi ve tip atamaları yapıldı
main_menu_check, basket_total, total, number_item, price, quantity, counter, choose_item, item_name, username, password, search_item, found_items =False, 0.0, 0.0, 0, 0, 0, 0, 0, "", "", "", "", []
# Kullanıcı giriş arayüzü
while True:
    print("""** WELCOME TO THE ISTINYE ONLINE MARKET **
  Please enter your username and password:""")
    # Kullanıcı adı ve şifre girişi
    username = input("User Name: ")
    password = input(color+"Password: ")
    # Eğer girilen kullanıcı adı ve şifre başta açmış olduğumuz "users" sözlüğünde varsa ve birbiriyle uyuşuyorsa giriş yapar
    if username in users.keys() and users[username]["pwd"] == password:
        print(color+"You have successfully logged in.!")
        print(color+f"Welcome {username}!Please select one of the following options by entering the corresponding menu number.\n")
    # Değilse uyarı verir ve bilgilerin tekrar girilmesini ister
    else:
        print(color+"Your username and / or password is not correct.Please try again!\n")
        continue
    # Ana menü arayüzü
    while True:
        main_menu_check = False
        choose = int(input(color+"""Please choose one of the services below:
1. Search product
2. Go to basket
3. Buy
4. Sign Out
5. Log out
"""))
        # Eğer geçersiz menü numarası seçilmişse uyar verir.
        if choose not in [1,2,3,4,5]:
            print(color+"Please select a valid menu number!\n")
        # Eğer "Ürün ara" seçilmişse
        elif choose == 1:
            while True:
                search_item = input(color+"What are you looking for? ")
                # Ana menüye dönüş
                if search_item == "0":
                    main_menu_check = True
                    break
                # Eğer girilen arama kelimesi "Envanter" sözlüğündeki ürün isimleri içerisinde yer alıyorsa
                # bulunan ürünleri "found_items" listesinin içine atar.
                for item in Envanter.keys():
                    if search_item in item:
                        # Bulunan ürün sayısını sayan sayaç
                        counter += 1
                        found_items.append(item)
                # Eğer sayaç 0 ise hiç ürün bulunamamış demektir
                if counter > 0:
                    break
                else:
                    print(color+"Your search did not match any items. Please try something else (Enter 0 for main menu):")
            if main_menu_check == True:
                continue
            # Bulunan ürünleri ekrana yazdırır.
            print(color+f"{counter} similar products found:\n")
            for iter in range(len(found_items)):
                print(color+f"{iter+1}. {found_items[iter]} {Envanter[found_items[iter]][1]} $")
            print("\n")
            # Bulunan ürünlerden hangisinden kaç tane sepete eklemek istendiğini seçme
            while True:
                choose_item = int(input(color+"Please select the item you want to add to your basket (Enter 0 for the main menu): "))
                # Ana menüye dönüş
                if choose_item == 0:
                    counter = 0
                    found_items = []
                    main_menu_check = True
                    break
                # Eğer girilen değer bulunan ürünler listesinin uzunluğundan fazla ise
                # uyarı verir ve tekrar değer girilmesini ister
                if choose_item not in range(1,len(found_items)+1):
                    print(color+"Your search did not match any items. Please try something else (Enter 0 for main menu):")
                    continue
                # Seçilen ürünü sepete ekleme
                while True:
                    # Seçilen üründen kaç adet eklenecek
                    number_item = int(input(color+f"{found_items[choose_item-1]} products are being added. How many you want?: "))
                    # Eğer 0'dan büyük bir değer girilmezse uyar ve tekrar değer girilmesini iste
                    if number_item > 0:
                        break
                    else:
                        print(color+"Please select at least 1 product!\n")
                # Seçilen ve adedi belirtilen ürünü sepete ekleme, stoktan düşme
                while True:
                    # Eğer seçilen üründen istenen miktar stokta yeteri kadar varsa sepete ekler
                    if Envanter[found_items[choose_item-1]][0] >= number_item:
                        # Eğer seçilen ürün daha önceden sepete eklenmemişse
                        if  found_items[choose_item-1] not in basket[username].keys():
                            Envanter[found_items[choose_item-1]][0] -= number_item
                            basket[username].update({found_items[choose_item-1]:number_item})
                            print(color+f"Your basket {found_items[choose_item-1]} added.\nReturning to the main menu ...\n")
                            main_menu_check = True
                            found_items = []
                            counter = 0
                            break
                        # Eğer seçilen ürün daha önceden sepete eklenmişse, adet miktarına ekleme yap
                        else:
                            Envanter[found_items[choose_item-1]][0] -= number_item
                            basket[username][found_items[choose_item-1]] += number_item
                            print(color+f"Your basket {found_items[choose_item-1]} added.\nReturning to the main menu ...\n")
                            main_menu_check = True
                            found_items = []
                            counter = 0
                            break
                    # Eğer seçilen üründen istenen miktarda stokta yoksa miktarı tekrar girmesini ister
                    else:
                        print(color+"Sorry! Quantity exceeds limit, Please try again with a smaller amount")
                        number_item = int(input(color+"Quantity (Enter 0 for main menu): "))
                        # Ana menüye dönüş
                        if number_item == 0:
                            main_menu_check = True
                            break
                if main_menu_check == True:
                    break
            if main_menu_check == True:
                continue
        # Eğer "Sepete git" seçilmişse
        elif choose == 2:
            # Eğer sepet boşsa uyarı ve ana menüye çık
            if len(basket[username]) == 0:
                print(color+"Your basket is empty\n\tTotal 0 $")
                main_menu_check = True
                continue
            # Eğer sepet boş değilse sepetin içeriğini, toplam fiyatı ve sepet menüsünü yazdır
            else:
                print(color+"Your basket includes:")
                for i in range(len(basket[username])):
                    item_name = list(basket[username].keys())[i]
                    price = Envanter[list(basket[username].keys())[i]][1]
                    quantity = list(basket[username].values())[i]
                    total = price*quantity
                    basket_total += total
                    print(color+f"\t{i+1}. {item_name} price = {price} $ quantity= {quantity} total = {total} $")
                print(color+f"Total {basket_total} $")
                basket_total = 0.0
                # Sepet menüsü
                while True:
                    basket_choose = int(input(color+"""
Choose an option:
1. Update Amount
2. Remove a product
3. Buy
4. Back to main menu
"""))
                    # Eğer girilen değer menü ögeleriyle uyuşmuyorsa uyarı verir ve tekrar denenmesini ister
                    if basket_choose not in [1,2,3,4]:
                        print(color+"Please select a valid menu number!\n")
                        continue
                    # Eğer "Tutarı güncelleyin" seçildiyse
                    elif basket_choose == 1:
                        # Sepet içeriğini ve toplam tutarı yazdır
                        for i in range(len(basket[username])):
                            item_name = list(basket[username].keys())[i]
                            price = Envanter[list(basket[username].keys())[i]][1]
                            quantity = list(basket[username].values())[i]
                            total = price*quantity
                            basket_total += total
                            print(color+f"\t{i+1}. {item_name} price = {price} $ quantity = {quantity} total = {total} $")
                        print(color+f"Total {basket_total} $")
                        basket_total = 0
                        # Geçerli ürün numarası girilene kadar ürün numarası iste
                        while True:
                            basket_choose_item = int(input(color+"Please select the product you will change the quantity: "))
                            # Eğer girilen ürün numarası sepet listesinin uzunluğundan büyük değilse uyarı ver
                            # ve tekrar girilmesini iste
                            if basket_choose_item in range(1,len(basket[username])+1):
                                break
                            else:
                                print(color+"Please select a valid product number!\n")
                        # Seçilen ürünün yeni miktarını iste
                        while True:
                            while True:
                                item_new_qty = int(input(color+"Please enter a new amount: "))
                                # Eğer girilene yeni miktar 0'dan küçük veya 0'a eşitse uyarı ver
                                # ve tekrar girilmesini iste
                                if item_new_qty > 0:
                                    break
                                else:
                                    print(color+"Please select at least 1 product!\n")
                            # Eğer yeni girilen değer stoktaki seçilen ürünün miktarından büyükse uyarı ver ve
                            # tekrar değer girilmesini iste
                            if item_new_qty <= Envanter[list(basket[username])[basket_choose_item-1]][0]:
                                # Eski miktarı stoğa geri ekle ve yeni değeri stoktan eksilt
                                item_old_qty = basket[username][list(basket[username].keys())[basket_choose_item-1]]
                                basket[username][list(basket[username].keys())[basket_choose_item-1]] = item_new_qty
                                Envanter[list(basket[username])[basket_choose_item-1]][0] -= item_new_qty
                                Envanter[list(basket[username])[basket_choose_item-1]][0] += item_old_qty
                                break
                            else:
                                print(color+"Sorry! Quantity exceeds limit, Please try again with a smaller amount")
                        # Sepetin yeni halini yazdır
                        print(color+"Your basket now includes:")
                        for i in range(len(basket[username])):
                            item_name = list(basket[username].keys())[i]
                            price = Envanter[list(basket[username].keys())[i]][1]
                            quantity = list(basket[username].values())[i]
                            total = price*quantity
                            basket_total += total
                            print(color+f"\t{i+1}. {item_name} price = {price} $ quantity = {quantity} total = {total} $")
                        print(color+f"Total {basket_total} $")
                        basket_total = 0
                    # Eğer "Bir öğeyi kaldırın" seçildiyse
                    elif basket_choose == 2:
                        # Sepeti yazdır
                        for i in range(len(basket[username])):
                            item_name = list(basket[username].keys())[i]
                            price = Envanter[list(basket[username].keys())[i]][1]
                            quantity = list(basket[username].values())[i]
                            total = price*quantity
                            basket_total += total
                            print(color+f"\t{i+1}. {item_name} price = {price} $ quantity = {quantity} total = {total} $")
                        print(color+f"Total {basket_total} $")
                        basket_total = 0
                        # Silinmek istenen ürünü seç
                        while True:
                            basket_choose_item = int(input(color+"Please select the product you want to delete: "))
                            # Eğer seçilen ürün sırası listede yoksa uyarı ver ve tekrar seçilmesini iste
                            if basket_choose_item in range(1,len(basket[username])+1):
                                break
                            else:
                                print(color+"Please select a valid item number!\n")
                        # Silinmek için seçilen ürünün miktarını stoğa iade et ve sepetten sil
                        removed_item_qty = basket[username][list(basket[username].keys())[basket_choose_item-1]]
                        Envanter[list(basket[username])[basket_choose_item-1]][0] += removed_item_qty
                        basket[username].pop(list(basket[username].keys())[basket_choose_item-1])
                        # Eğer sepet boş kalmışsa uyarı ver
                        if len(basket[username]) == 0:
                            print(color+"Your basket is empty.\n\tTotal 0 $")
                        # Eğer sepet boş değilse sepeti yazdır
                        else:
                            for i in range(len(basket[username])):
                                item_name = list(basket[username].keys())[i]
                                price = Envanter[list(basket[username].keys())[i]][1]
                                quantity = list(basket[username].values())[i]
                                total = price*quantity
                                basket_total += total
                                print(color+f"\t{i+1}. {item_name} price = {price} $ quantity = {quantity} total = {total} $")
                            print(color+f"Total {basket_total} $")
                            basket_total = 0
                    # Eğer "Satın al" seçildiyse
                    elif basket_choose == 3:
                        # Eğer sepet boşsa
                        if len(basket[username]) == 0:
                            print(color+"Your basket is empty.\n\tTotal 0 $")
                        # Eğer sepet boş değilse makbuzu yazdır
                        else:
                            print(color+f"""
Your receipt is being processed ...
*** Istinye Online Market ***
**************
\t0850 283 6000
\tistinye.edu.tr
————————————————————————————————
""")
                            for i in range(len(basket[username])):
                                item_name = list(basket[username].keys())[i]
                                price = Envanter[list(basket[username].keys())[i]][1]
                                quantity = list(basket[username].values())[i]
                                total = price*quantity
                                basket_total += total
                                print(color+f"\t{i+1}. {item_name} price = {price} $ quantity = {quantity} total = {total} $")
                            print(color+"————————————————————————————————")
                            print(color+f"Total {basket_total} $")
                            print(color+"————————————————————————————————")
                            print(color+datetime.now().strftime("%Y/%m/%d %H:%M"))
                            print(color+"Thank you for using our Online Market!")
                            basket_total = 0
                            main_menu_check = True
                            basket[username] = {}
                        # Ana menüye dönüş
                        if main_menu_check == True:
                            continue
                    # Eğer "Ana menüye dön" seçildiyse
                    elif basket_choose == 4:
                        break
        # Eğer ana menüden "Satın al" seçildiyse
        elif choose == 3:
            if len(basket[username]) == 0:
                print(color+"Your basket is empty.\n\tTotal 0 $")
            else:
                print(color+f"""
Your receipt is being processed ...
*** Istinye Online Market ***
**************
\t0850 283 6000
\tistinye.edu.tr
————————————————————————————————
""")
                for i in range(len(basket[username])):
                    item_name = list(basket[username].keys())[i]
                    price = Envanter[list(basket[username].keys())[i]][1]
                    quantity = list(basket[username].values())[i]
                    total = price*quantity
                    basket_total += total
                    print(color+f"\t{i+1}. {item_name} price = {price} $ quantity = {quantity} total = {total} $")
                print(color+"————————————————————————————————")
                print(color+f"Total {basket_total} $")
                print(color+"————————————————————————————————")
                print(color+datetime.now().strftime("%Y/%m/%d %H:%M"))
                print(color+"Thank you for using our Online Market!")
                basket_total = 0
                basket[username] = {}
        # Eğer "Oturumu kapat" seçildiyse ana menüden çıkar ve oturum açma arayüzüne döner
        elif choose == 4:
            break
        # Eğer "Çıkış yap" seçildiyse programı sonlandırır
        elif choose == 5:
            quit()

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