""" Fonksiyonlar için site: https://www.w3schools.com/python/python_functions.asp
 Kodda kullandığım 'inline if' için site: https://stackoverflow.com/questions/11880430/how-to-write-inline-if-statement-for-print
 Kodda kullandığım print türü için site: https://docs.python.org/3/tutorial/inputoutput.html
 Çıktıları hizalamak için kullandığım print için site: https://stackoverflow.com/questions/33323715/python-evenly-space-output-data-with-varying-string-lengths
Çıktıyı renkli almak için: https://www.turkhacks.com/konu-python-ekrana-renkli-yazi-yazdirma.html
Random modülü: https://www.btkakademi.gov.tr/portal/course/player/s-f-rdan-ileri-seviye-python-programlama-5877?language=tr&token=eyJhbGciOiJSUzUxMiJ9.eyJzdWIiOiI1NTQ0MzEiLCJkb21haW4iOiJCVEsiLCJpc3MiOiJLQiIsIm9pZCI6NTEsImV4cCI6MTYwODIwNzY1OSwidXVpZCI6IjJkNWQ5NDVmLTMwNzctNDk4Ni04ZWY3LTkzNzdkNWQzMWVmZCIsImlhdCI6MTYwODEyMTI1OSwianRpIjoiZGM5ZmUwYTEtYjI5NS00MGQ5LTg4NTctODQ5MTM3NWRjYjZiIn0.JE5Nn2kRJiUBNnQ_PXRodK6ZPg6X-yTFmQa6NowCl7baF4q36uOn2Y_3vgUDLBWs4BxZKMr--eQRSB7L4mJUqSJ_XQxFfRMN0jzQSPooGgEvnSsCQtpC8f_lQJUPNKdUyz_8RwILCeLrsQiX3bpZaKrDk4_63PzsWEMxSCbFUjGWXK-hxe684TUkLZQNWzouAqpRXbDEfneTEatPE_vaew13Lj965MWELZtB0MAu0aXw1zQ4LSq_TuJiLc3U1nSwqlS678yF_P4NfBFiEytlWGrX5dmhcrJ1DE6_12I07qCEzKL1E5pewnydTkWwXaMgzEuRXshme1K3qGHQgDpnAg&examMode=false
https://www.youtube.com/watch?v=XYPNtZZvfMM
https://coding-grace-guide.readthedocs.io/en/latest/guide/lessonplans/beginners-python-text-based-adventure.html"""


import random
from colorama import init #colorama modülünü çagrıdık
from colorama import Fore, Back, Style #colorama modülünün Fore, Back, Style çagrıdık

init() #aktif hale getirdik
print(Fore.BLUE+Back.RESET)

""" Saldırı oyun içerisinde ne kadar kullanılacağı bilinmediği için fonksiyon haline getirildi.
 Bu fonksiyon içirisinde: 
 Kullanıcıdan 1 ile 50 arasında bir değer alınıyor.
 Alınan değer 0, 0'dan küçük veya 50'den büyükse tekrardan kullanıcıdan değer alınıyor.
 Saldırının yüzdesel olarak başarısı hesaplanıyor.
 0 ile 100 arasında random bir değer seçiliyor ve yüzdesel başarı seçilen değere eşit ya da daha fazlaysa saldırı başarılı olarak kabul ediliyor.
 Bir önceki maddenin açıklaması:
 yüzdesel başarı = 70 olarak düşünelim yani kullanıcı 30 değerini girmiş olsun
 0 ile 100 arasında random bir sayının 70'den küçük veya 70'e eşit olmasının yüzdesel oranı 70'e eşittir bu yüzden böyle bir yöntem izledim.
 Eğer saldırı başarılıysa fonksiyon verilen hasarı döndürüyor."""

def attack():

	# Kullanıcıdan değer alınması ve sayısal değere dönüştürülmesi
	attackPoint = int(input("Choose your attack size between 1 and 50:"))

	# Alınan değerin 0 ile 50 arasında olup olmadığının kontrolü
	# Eğer 0 ile 50 arasında değilse, hata mesajının yazdırılması ve tekrardan değer alınması
	while (attackPoint > 50 or attackPoint <= 0):
		attackPoint = int(input("Attack size must be between 1 and 50.\nChoose your attack size between 1 and 50: "))

	# Saldırının yüzdesel olarak başarı oranı
	percentage = 100-attackPoint

	# Saldırının başarılı mı başarısız mı olacağını belirlemek için 0 ile 100 arası bir değer seçilmesi
	luck = random.randint(0, 100)

	# Eğer yüzdesel başarı oranı seçilen sayıdan büyük veya seçilen sayıya eşitse saldırının başarılı olarak işaretlenmesi
	isSuccess = True if luck <= percentage else False

	# Eğer saldırı başarılıysa kullanıcıdan alınan değerin hasar olarak kaydedilmesi
	# Eğer saldırı başarısızsa hasarın 0 olarak kaydedilmesi
	damage = attackPoint if isSuccess else 0

	# Fonksiyonun hasarı sayısal olarak geri döndürmesi
	return damage

 #Bu fonksiyon kullanıcıların isim ve can değerlerinin yazdırmak için oluşturulmuştur.
 #Parametreler:
 #names: İsimlerin bulunduğu String dizisi
 #healths: Canların sayısal olarak bulunduğu int dizisi
 #turnOn: saldırı sırasının kimde olduğunu göstermek için tutulan bir int

def printInfo(names, healths, turnOn):

	# İlk kullanıcının can değerini sopa olarak gösterimi için oluşturulmuş string
	firstHealthStr = ""

	# İlk kullanıcının can değerinin sopa olarak hesaplanması:
	# Oluşuturulan string'e can değerinin yarısı kadar sopa ekleniliyor
	for i in range(int(healths[0]/2)):
		firstHealthStr = firstHealthStr+"|"

	# İkinci kullanıcının can değerini sopa olarak gösterimi için oluşturulmuş string
	secondHealthStr = ""

	# İkinci kullanıcının can değerinin sopa olarak hesaplanması:
	# Oluşuturulan string'e can değerinin yarısı kadar sopa ekleniliyor
	for i in range(int(healths[1]/2)):
		secondHealthStr = secondHealthStr+"|" 


	# İlk kullanıcının 2. satırda gözükücek olan can değerlerinin oluşturulması
	firstStr = "HP[{}]:{}".format(healths[0], firstHealthStr)

	# ikinci kullanıcının 2. satırda gözükücek olan can değerlerinin oluşturulması
	secondStr = "HP[{}]:{}".format(healths[1], secondHealthStr)

	# Eğer hamle sırası kimdeyse ilk olarak onun ismi ve can değeri yazılacağı için bir if state'i oluşturuldu
	# Hamle sırası ilk kullanıcıdaysa
	if turnOn == 0:
		# Buradaki {:60s} şu anlama gelmektedir.
		# Eğer ki yazdırılmak istenen text yani names[0] Ali ise Ali'nin yanına 57 tane daha boşluk ekleniyor.

		# İlk kullanıcının ismi ile ikinci kullanıcının isminin aynı satırda yazılması
		print('\n{:60s} {:60s}'.format(names[0], names[1]))

		# İlk Kullanıcının can bilgisi ile ikinci kullanıcının can bilgisinin aynı satırda yazılması
		print('{:60s} {:60s}'.format(firstStr, secondStr))
	else:
		# İkinci kullanıcının ismi ile ilk kullanıcının isminin aynı satırda yazılması
		print('\n{:60s} {:60s}'.format(names[1], names[0]))

		# İkinci kullanıcının can bilgisi ile ilk kullanıcının can bilgisinin aynı satırda yazılması
		print('{:60s} {:60s}'.format(secondStr, firstStr))


# Oyun tekrar oynanılabileceği için kod fazlalığı olmasın diye oyun tamamen fonksiyon haline getirilmiştir.
# Parametre olarak:
# names: Kullanıcıların isimlerinin bulunduğu string dizisi
def game(names):

	# İki oyuncu bulunduğu için oyuncuların can değerlerinin bulunduğu int dizisi oluşturuldu.
	healths = [100, 100]

	# İlk hamleyi hangi oyuncunun yapıcağını belirlemek için random olarak 0 veya 1 seçiyoruz.
	firstMove = random.randint(0, 1) 

	""" İlk hamleyi hangi oyuncunun yapıcağını kullanıcıya belirtmek için konsola yazdırıyoruz.
	 Burada print içerisindeki text'te köşeli parentez kullandığımızda, String sonuna .format() fonksiyonu içerisinde belirttiğimiz değişken'i köşeli parentezle değiştirir
	 Formatın içersinde kullandığım kod ise if fonksiyonun farklı bir kullanımı : 'inline if' """

	print("\nCoin flip result: {} starts first!".format(names[0] if firstMove == 0 else names[1]))

	# Kullanıcıların bilgilerinin ekrana yazılması.
	printInfo(names, healths, firstMove)
	
	# Burada iki can değerinden birisi 0 veya 0'dan daha küçük olana kadar yapılan işlemleri tekrarlıyoruz.
	while (healths[0] > 0 and healths[1] > 0):

		# Saldırı sırası hangi kullanıcıdaysa kullanıcının haberdar olması için ekrana yazılan yazı.
		print("\n———– {} ATTACKS !! ———–".format(names[firstMove]))

		# Kullanıcının yapıcağı saldırı büyüklüğü (en başta açıklanmış olan fonksiyon)
		damagePoint = attack()

		# Eğer verilen hasar 0'dan fazlaysa hasarı alan kullanıcının can değerinin güncellenmesi
		if damagePoint > 0:

			# Eğer hareket sırası ilk kullanıcıdaysa ikinci kullanıcının can değerinin azalması
			if firstMove == 0:
				healths[1] = healths[1]-damagePoint

				# Eğer can değeri 0'ın altına düşerse can değerini 0'a eşitleriz. Çünkü -'ye düşsede 0 olarak gösterilir.
				if healths[1] < 0:
					healths[1] = 0

			# Eğer hareket sırası ikinci kullanıcıdaysa ilk kullanıcının can değerinin azalması					
			else:
				healths[0] = healths[0]-damagePoint

				# Eğer can değeri 0'ın altına düşerse can değerinin 0'a eşitlenmesi.
				if healths[0] < 0:
					healths[0] = 0

			# Kimin ne kadar hasar verdiğinin ekrana yazdırılması.
			print("\n{} {} DAMAGED !!".format(names[firstMove], damagePoint))

			# Kullanıcıların bilgilerinin ekrana yazılması.
			printInfo(names, healths, firstMove)

		# Eğer verilen hasar 0 ise yani saldırı başarısızsa.
		else :
			# Saldırının başarısız olduğunun ekrana yazılması
			print("\nOoopsy! {} missed the attack!!".format(names[firstMove]))
			# Kullanıcıların bilgilerinin ekrana yazılması.
			printInfo(names, healths, firstMove)

		# Sıranın diğer oyuncuya geçmesi
		firstMove = 0 if firstMove == 1 else 1

	# Eğer kullanıcılardan birinin can değeri 1'in altına düşerse kazananın isminin ekrana basılması
	finalText = "######################### {} WON!!! #########################".format(names[0] if healths[1] <= 0 else names[1])
	finalTextPattern = ""
	for i in range(len(finalText)):
		finalTextPattern = finalTextPattern+"#" 

	print("\n{}\n{}\n{}".format(finalTextPattern, finalText, finalTextPattern))


# Uygulama başlatıldığında çalışacak olan ilk satır burasıdır. 
# Kullanıcıların isimlerini tutmak için oluşturulmuş string dizisi
names = ["", ""]

# İlk oyuncu için kullanıcıdan girdi alıp bunu değişken'e atıyoruz
names[0] = input("\n———–——————–– FIRST HERO———–————–——–\nPlease enter your first hero's name: ")

# İkinci oyuncu için kullanıcıdan girdi alıp bunu değişken'e atıyoruz
names[1] = input("\n———–——————- SECOND HERO——–————–——–\nPlease enter your second hero's name: ")

# Eğer iki isimde aynıysa, farklı olana kadar hata mesajı gösterip kullanıcıdan girdi alıp 2. kullanıcının ismine eşitliyoruz
while names[0] == names[1]:
	names[1] = input("\n{} is taken, please choose another name!\n———–——————- SECOND HERO ——–————–——–\nPlease enter your second hero's name:".format(names[0]))

# Oyun ilk defa çalıştırıldığında oyunu oynayabilmek için bu değişken'i evet olarak başlatıyoruz.
# Oyun bittiğinde kullanıcıdan tekrar oynamak isteyip istemediğini sorup bu değişken'e atıyoruz.
# Bu değişken ile oyunun tekrar oynanıp oynanmayacağını kontrol ediyoruz.
again = "yes"

# Kullanıcı 'evet' veya 'Evet' dışında başka bir şey yazana kadar oyunu tekrar oynatmak için oluşturulmuş while loop'u
while again == "yes" or again == "Yes":

	# Oyunun oynanması
	game(names)

	# Kullanıcıların bir tur daha oynamak isteyip istemediklerinin sorulması
	again = input("\nDo you want to play again(Yes or No)? : ")

# Kullanıcı tekrar oynamak istemezse son mesajımızı yazıyoruz.
print("\nThanks for playing. See you again!")
