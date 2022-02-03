'''fonksiyonlarda varsayılan değerler:
4 parametre alan bir fonksiyon var ama kullanıcı bazı durumlarda 3 parametre girebilsin. 
ÖRNEK FONKSİYON:'''

def kayıtekle(ad="bilgi yok",soyad="bilgi yok",yaş="bilgi yok",meslek="bilgi yok"):
    print("kayıt ekleniyor..")

    print("Ad:{}\nSoyad:{}\nYaş:{}\nMeslek:{}\n".format(ad,soyad,yaş,meslek))

    print("kayıt eklendi")

kayıtekle("Doğa","Özdemir")
#kayıtekle(ad="Doğa,yaş=21") böyle de olabilir
