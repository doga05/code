#kullanıcı girişi doğrulama
import time 

print(""" 
*************
** Kullanıcı Girişi Ekranı **
*************
""")
      


def GirisHakki():

    kullanıcıAdı= input("Kullanıcı Adı: ")
    parola= input("Parola: ")
    
SystemUsername = "AdminGiriş"
SystemPasswd = "0AdminParola0"
giriş_hakkı = 3

while True:


    if (SystemUsername != kullanıcıAdı and SystemPasswd == parola):
        print("Kullanıcı Adı Hatalı \n")
        giriş_hakkı -= 1
        
    elif (SystemPasswd != parola and SystemUsername == kullanıcıAdı):
        print("Parola Hatalı \n")
        giriş_hakkı -= 1 
        
    elif(SystemUsername != kullanıcıAdı and SystemPasswd != parola):
        print("Kullanıcı Adı ve Parola Hatalı \n")
        giriş_hakkı -= 1

    elif(giriş_hakkı == 0):
        print("Giriş Hakkınız Geçici Olarak Kısıtlandı\n10 Dakika Sonra Tekrar Deneyiniz.\nYönlendiriliyor...")
        time.sleep(2)
        return GirisHakki()
            
    else:
        print("Sisteme Başarıyla Giriş Yaptınız.\n")
        giriş_hakkı -= 1
        time.sleep(2)
