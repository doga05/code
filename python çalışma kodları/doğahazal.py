
import random
import time
from colorama import init 
from colorama import Fore, Back, Style #Bu kısımda çıktıları renkli alabilmek için colorama modülünü,  Fore, Back ve Style ile beraber çağırıyoruz.



init() # init metodu initialize – ilklendirmek, initializer – başlatıcı kavramlarından gelmektedir bu nedenle init () yazarak aktif hale getirdik yani başlattık.
print(Fore.BLUE+Back.RESET)  # fore isimi belirtir ve blue yazdığımızda çıktılar mavi olur . back arka planı temsil eder bunun için Reset dedik çünkü arka planı renklendirmek istemiyoruz

print("        ------------WELCOME TO ISTINYE KOMBAT. HAVE FUN :)------------------      ")
def attack():

	
	attackPoint = int(input("Choose your attack size between 1 and 50:"))# Bu kısımda saldırı için oyunculardan 1 ile 50 arasında bir int ifade girmeleri istenmiştir.
	while (attackPoint > 50 or attackPoint <= 0):                        #girilen ifade 1 den küçük 50 den büyük olursa kabul etmeyip uyarı vermesi ve tekrar sorması istenmiştir.
		attackPoint = int(input("Attack size must be between 1 and 50.\nChoose your attack size between 1 and 50: "))

	
	percentage = 100-attackPoint                      # yan tarafta öncelikle saldırının yüzdesel olara başarı oranı hesaplanıyor karşı tarafa yapılan saldırının başarılı veya başarısız olucağını  belirlemek için 
	luck = random.randint(0, 100)                     #0 ile 100 arasında bir değer seçmesi gerektiğini belirttik . Eğer yüzdesel başarı oranı seçilen sayıdan büyük veya eşit ise saldırı başarılı sayılır küçük veya eşit değil ise 
	isSuccess = True if luck <= percentage else False #saldırı başarısız olur . Bu işlemde başarılı sonucu elde edildikten sonra oyuncudan alınan değer hasar olarak kaydedelmesini istiyorum ama saldırı başarısız olmuşsa hasarın 0 olarak 
	damage = attackPoint if isSuccess else 0          #kaydedilmesini istiyorum 
	return damage                                     #fonksiyonun hasarı bize sayısal olarak bildirmesi için return damage kullanırız


def printInfo(names, healths, turnOn):
                                                                #yan tarafta belirttiğim fonksiyon isim ve can değerleri için gereklidir . 3 parametreli bir fonksiyondur 
                                                                #firstHealthStr = "" bir numaralı oyuncunun can değerlerini sopa olarak hesaplanması işleminin başlangıcıdır
	firstHealthStr = ""                                         #oluşturulan string'e can değerinin yarısı kadar sopa ekliyoruz  aynı işlemi iki numaralı oyuncunun canının sopa 
	for i in range(int(healths[0]/2)):                          #olarak gösterimi için tekrar uygulamamız gerekir . Daha sonra ilk ve ikinci oyuncunun 2.satırda gösterilicek olan 
		firstHealthStr = firstHealthStr+"|"                     #can değerlerinin oluşturulması  işlemi uygulanmıştır .
	secondHealthStr = ""                                        
	for i in range(int(healths[1]/2)):                          
		secondHealthStr = secondHealthStr+"|"                   
	firstStr = "HP[{}]:{}".format(healths[0], firstHealthStr)   
	secondStr = "HP[{}]:{}".format(healths[1], secondHealthStr) 
	if turnOn == 0:                                            # Hamle sırası kimde ise ilk onun isminin ve can değeri yazılacağı için  gerekli if yapısı kullanmamız gerekir .
                                                               
		print('\n{:60s} {:60s}'.format(names[0], names[1]))    # bu kısımda ilk oyuncunun ve ikinci ismini hizalı bir şekilde aynı satırda yazdırmak için gerekli yapıyı yazdık ve kaynak kısmında belirttik 
		print('{:60s} {:60s}'.format(firstStr, secondStr))     # aynı şeyi can çubuklarının hizalı olması için de uyguluyoruz 
	else:
		print('\n{:60s} {:60s}'.format(names[1], names[0]))   
		print('{:60s} {:60s}'.format(secondStr, firstStr))


def game(names):

	healths = [100, 100]                                                                           #names oyuncuların isim bilgilerinin içinde bulunduğu bir string dizisi olarak oluşturulmuştur.
	firstMove = random.randint(0, 1)                                                               #ilk hamleyi hangi oyuncunun yapıcağını belirlemek için  0 veya 1 olarak seçiyoruz bunun için random kullanıyorum 
	print("\nCoin flip result: {} starts first!".format(names[0] if firstMove == 0 else names[1])) #random modülü : çeşitli dağılımlar içn sözde rastgele sayı üreteçleri uygular .
	printInfo(names, healths, firstMove)                                                           
	while (healths[0] > 0 and healths[1] > 0):                                                     
		print("\n———– {} ATTACKS !! ———–".format(names[firstMove]))                                #bu kısımda yapılan işlemleri iki can değerinden bir tanesi sıfır oluncaya dek devam ettiriyorum
		damagePoint = attack()                                                                     #saldırı sırasının hangi oyuncuda olduğunu oyunculara bildiriryorum .
		if damagePoint > 0:                                                                        #oyuncuya verilen hasasr sonucunda can bilgisinin güncellenmesini yazdırıyorum 
			if firstMove == 0:                                                                     #hamle sırası ilk oyuncudaysa ikinci oyuncununcan değerinde azalma meydana gelmesi gerektiğini bildiriyorum 
				healths[1] = healths[1]-damagePoint                                                #can değeri 0'ın altına düştüğü anda 0 a eşitlenmesi ve gerekir ve kimin ne hasar verdiğinin ekranda yazılması gerekir .
				if healths[1] < 0:                                                                 
					healths[1] = 0	                                                              		
			else:                                                                              
				healths[0] = healths[0]-damagePoint
				if healths[0] < 0:
					healths[0] = 0
			print("\n{} {} DAMAGED !!".format(names[firstMove], damagePoint))
			printInfo(names, healths, firstMove)                                        #oyuncu bilgilerinin ekrana yazdırılması gerekir.
		else :
			print("\nOoopsy! {} missed the attack!!".format(names[firstMove]))   #bu kısımda saldırının başarısız olduğu oyunculara bildirilir 
			printInfo(names, healths, firstMove)
		firstMove = 0 if firstMove == 1 else 1
	finalText = "######################### {} WON!!! #########################".format(names[0] if healths[1] <= 0 else names[1])
	finalTextPattern = ""
	for i in range(len(finalText)):
		finalTextPattern = finalTextPattern+"#" 

	print("\n{}\n{}\n{}".format(finalTextPattern, finalText, finalTextPattern))



names = ["", ""]        # uygulamada açılında ilk başlıcağı yer burasıdır.
while True :
    names[0] = input("\n———–——————–– FIRST HERO ———–————–——–\nPlease enter your first hero's name: ")  
    if len(names[0]) > 0:   #bu kısım birinci oyuncun isim bilgilerininin isteniceği ve isim kısmına isim girilmediğinde 
        print (names[0])    #uyarı verip isim girene kadar isim istediği  bölümdür 
        break
    else:
        print ("WARNING! The name of the hero cannot be left blank.")
while True:    
    names[1] = input("\n———–——————- SECOND HERO ——–————–——–\nPlease enter your second hero's name: ")
    if len(names[1]) <= 0:
        print ("WARNING! The name of the hero cannot be left blank.")   # burasıda birinci oyuncunun isim bilgileri için geçerli olan kısmına aynısıdır tek fark 
    elif names[0]==names[1]:                                            # birinci oyuncuya girilen isimle aynı isim girildiğinde uyarı verip farklı bir isim girilene kadar 
        print(names[0] ," is taken, please choose another name!")       #soruyu yineler.
    else:
        
        print 
        
        break
    
print ("The game begins in 5 seconds!" )
time.sleep(1)                           # bu kısım oyunun göze daha güzel gözükmesi için öğrenciler tarafından 
print (">>>>>4<<<<<")                   #isteğe bağlı olarak eklenmiştir. Oyun başlarken 5'ten geriye 1 sn bekleyerek 
time.sleep(1)                           #geri sayan sistemdir .
print (">>>>>3<<<<<")
time.sleep(1)
print (">>>>>2<<<<<")
time.sleep(1)
print (">>>>>1<<<<<")
time.sleep(1)

again = "yes" #bu kısımda belirlenen değişken ile oyunun tekrar oynanıp oynanmayacağını kontrol ediyoruz.

while again == "yes" or again == "Yes": # oyuncular tekrar oynamak istediklerinde belirtilen kelimleri yazdığında oyunu tekrar oynatmak için oluşturulmuş döngüdür.
	game(names) # bunu yazmadığımızda oyun  oynanmamaktadır .

	again = input("\nDo you want to play again(Yes or No)? : ") #tekrar oyanamak için sorulmassı gereken sorudur.

print("\nThanks for playing. See you again!")


"""
RESOURCES
https://www.w3schools.com/python/python_functions.asp
https://stackoverflow.com/questions/11880430/how-to-write-inline-if-statement-for-print
https://docs.python.org/3/tutorial/inputoutput.html
https://stackoverflow.com/questions/33323715/python-evenly-space-output-data-with-varying-string-lengths
https://www.turkhacks.com/konu-python-ekrana-renkli-yazi-yazdirma.html
https://tr.coredump.biz/questions/39718271/python-basic-countdown-timer-amp-function-gt-int
https://www.btkakademi.gov.tr/portal/course/player/s-f-rdan-ileri-seviye-python-programlama-5877?language=tr&token=eyJhbGciOiJSUzUxMiJ9.eyJzdWIiOiI1NTQ0MzEiLCJkb21haW4iOiJCVEsiLCJpc3MiOiJLQiIsIm9pZCI6NTEsImV4cCI6MTYwODIwNzY1OSwidXVpZCI6IjJkNWQ5NDVmLTMwNzctNDk4Ni04ZWY3LTkzNzdkNWQzMWVmZCIsImlhdCI6MTYwODEyMTI1OSwianRpIjoiZGM5ZmUwYTEtYjI5NS00MGQ5LTg4NTctODQ5MTM3NWRjYjZiIn0.JE5Nn2kRJiUBNnQ_PXRodK6ZPg6X-yTFmQa6NowCl7baF4q36uOn2Y_3vgUDLBWs4BxZKMr--eQRSB7L4mJUqSJ_XQxFfRMN0jzQSPooGgEvnSsCQtpC8f_lQJUPNKdUyz_8RwILCeLrsQiX3bpZaKrDk4_63PzsWEMxSCbFUjGWXK-hxe684TUkLZQNWzouAqpRXbDEfneTEatPE_vaew13Lj965MWELZtB0MAu0aXw1zQ4LSq_TuJiLc3U1nSwqlS678yF_P4NfBFiEytlWGrX5dmhcrJ1DE6_12I07qCEzKL1E5pewnydTkWwXaMgzEuRXshme1K3qGHQgDpnAg&examMode=false
https://www.youtube.com/watch?v=XYPNtZZvfMM
https://coding-grace-guide.readthedocs.io/en/latest/guide/lessonplans/beginners-python-text-based-adventure.html"""

"""201216067 Doğa Özdemir Bilgisayar Programcılığı 1. sınıf 
   201216098 Hazal Karacak Bilgisayar Programcılığı 1. sınıf 
   ÖDEVİ İKİ ÖĞRENCİ BİRLİKTE YAPMIŞTIR !"""
