// 201216067 Doğa Özdemir
// 201216073 Nur Sena Günay 

#include <iostream>
#include <locale.h>
using namespace std;

void sifrele(int sayi) { // Girilen 4 basamaklı sayıyı şifrelemek için bir fonksiyon oluşturduk.
    int dizi[4], gecici; // 4 elemanlı bir dizi ve gerekli değişken tanımladık.
    dizi[0]=sayi/1000; // Girilen sayının basamak değerini elde etmek için ve diziye atamak için basamak çözümleme yaptık. 
    dizi[1]=(sayi%1000)/100;
    dizi[2]=(sayi%100)/10;
    dizi[3]=(sayi%10);
    
    for(int i=0; i<4; i++) { //Dizi elemanlarını alır
        dizi[i]=(dizi[i]+7)%10; // Her elemana 7 ekleyerek mod 10 işlemi yapar ve sayının şifreli değerini bulur.
    }
    gecici=dizi[0];
    dizi[0]=dizi[2];
    dizi[2]=gecici;
    gecici=dizi[1];
    dizi[1]=dizi[3];
    dizi[3]=gecici; //Şifreleme için gerekli işlemler yapıldı.
        
    cout << "--> Oluşturulan şifre: ";
    for(int j=0; j<4; j++) { // Oluşturulan şifreyi bastırmak için for döngüsü kullandık.
        cout << dizi[j];
    }
    cout<< endl;
} 



void sifrecoz(int sayi2) { // Şifrelenmiş 4 basamaklı sayıyı çözmek için bir fonksiyon oluşturduk.
    int dizi2[4],gecici; // Gerekli dizi ve değişken tanımlandı.
    dizi2[0]= sayi2/1000; 
    dizi2[1]=(sayi2%1000)/100;
    dizi2[2]=(sayi2%100)/10;
    dizi2[3]=(sayi2%10);
    
    for(int i=0; i<4; i++) {
        dizi2[i]=((dizi2[i]+10)-7)%10;// Burada şifreyi çözmek için şifreleme işleminin tersi yapıldı.
    }
    gecici= dizi2[0];
    dizi2[0]=dizi2[2];
    dizi2[2]=gecici;
    gecici= dizi2[1];
    dizi2[1]=dizi2[3];
    dizi2[3]=gecici;
        
    cout << "--> Çözülen Şifre: ";
    for(int j=0; j<4; j++) { // Çözümlenen şifre bastırıldı.
        cout << dizi2[j];
    }
    cout << endl;
}


// Kodun içinde seçenekler sunduğumuz için bu işlemleri her seferinde yazmamak için bununla ilgili fonksiyonlar oluşturduk.

void secenekSayiSifrele() { //İlk seçeneği gerçekleştiren sayı şifreleme fonksiyonu
    int veri;
    cout << "--> Şifrelemek istediğiniz 4 haneli sayıyı giriniz: ";
    cin >> veri;
    sifrele(veri);// Sayı şifreleme seçeneği olduğu için şifreleme fonksiyonunu yazdırması için bu fonksiyonun içine ekledik.
    cout<<endl;
}



void secenekSayiCoz() { // İkinci seçeneği gerçekteştiren sayı çözümleme fonksiyonu
    int veri;
    cout << "--> Çözümlemek istediğiniz 4 haneli sayıyı giriniz: ";
    cin >> veri;
    sifrecoz(veri);// Şifre çözme seçeneğinde çözümlenmiş şifreyi yazdırmak için çözümleme fonksiyonunu seçenek fonksiyonuna ekledik
    cout<<endl;
}

/*Sezar Şifreleme: Girilen metnin her bir karakterini belirtilen öteleme anahtarı miktarı kadar öteleyerek ortaya şifreli bir 
metin çıkarır. Anahtarı kişi kendi belirleyebilir.*/

void sezar(char mesaj[100], int anahtar){// Sezar şifreleme için bir şifreleme fonksiyonu oluşturduk.
    for(int i = 0; mesaj[i] != '\0'; ++i){
        char karakter = mesaj[i];//Metindeki harfleri kontrol etmek için karakter değişkenine atar.
       
        if(karakter>= 'a' && karakter <= 'z'){// Girilen karakterler alfabe aralığındaysa 
            karakter = karakter + anahtar;// Karakter değişkenini anahtar ile toplar ve tekrar kendine eşitler.
           
            if(karakter > 'z'){// Eğer z harfinden büyükse ekleme işleminin alfabenin başına dönmesi için kontrol yapar.
                karakter = karakter - 'z' + 'a' - 1;
            }
           
            mesaj[i] = karakter;//Girilen mesaj indexlerini karakter değişkeni ile şifrelenmiş harflere eşitler.
        }
        else if(karakter >= 'A' && karakter <= 'Z'){// Yukardaki bütün işlemleri büyük harflere göre yapar.
            karakter = karakter + anahtar;
            if(karakter > 'Z'){
                karakter = karakter - 'Z' + 'A' - 1;
            }
            mesaj[i] = karakter;
        }
    }
    cout << "--> Şifreli mesaj: " << mesaj << endl;
}


void seceneksezarSifrele() {//Üçüncü seçeneği gerçekleştiren Sezar Şifreleme fonksiyonu.
	char mesaj[100];
	int ilerleme;
	cout<< "--> Anahtarı giriniz:";
	cin>>ilerleme;
	cout << "--> Şifrelemek istediğiniz metni giriniz: ";
	cin.ignore();
	cin.getline(mesaj,100);// Girilen şifreleme metninin tamamını alması için getline fonksiyonu kullandık.
	sezar(mesaj,ilerleme);
	cout<< endl;
} 




void sezarcoz(char line[100],int key){//Sezar Şifre Çözme fonksiyonu
    for(int i = 0; line[i] != '\0'; ++i){
        char karakter = line[i];
       
        if(karakter >= 'a' && karakter <= 'z'){//Şifreleme işlemi için yapılan işlemlerin tersini yapar.
            karakter = karakter - key;
           
            if(karakter > 'z'){
                karakter = karakter - 'z' > 'a' + 1;
            }
           
            line[i] = karakter;
        }
        else if(karakter >= 'A' && karakter <= 'Z'){//Aynı işlemleri büyük harflere göre yapar.
            karakter = karakter - key;
            if(karakter > 'Z'){
                karakter = karakter - 'Z' - 'A' + 1;
            }
            line[i] = karakter;
        }
    }
    cout << "--> Şifresiz mesaj: " << line << endl;
   
}


void secenekSezarSifreCoz() {// Dördüncü seçeneği gerçekleştiren Sezar Şifre Çözme fonksiyonu. 
	char line[100];
	int gerileme;
	cout<<"--> Anahtarı giriniz:";
	cin>>gerileme;
    cout<< "--> Çözmek istediğiniz metni giriniz: ";
    cin.ignore();
	cin.getline(line,100);
	sezarcoz(line,gerileme);
	cout<<endl;
}


int main() {
    
    setlocale(LC_ALL,"Turkish"); // Türkçe karakter desteği
    
    cout << "**********************************************************"<<endl;
    cout<<  "***** ŞİFRELEME VE ÇÖZÜMLEME PROGRAMINA HOS GELDİNİZ *****"<<endl;
    cout << "**********************************************************"<<endl<<endl;
            
    int secim;
    cout << "--> İşlem numarası giriniz: "<<endl<<"\t1.Sayı Şifreleme\n\t2.Sayı Çözümleme\n\t3.Sezar Şifreleme\n\t4.Sezar Çözümleme\n\t5.Çıkış"<<endl;
    cout<<endl<<"--> Seçim:";
    cin >> secim;
    
    switch(secim) {// Girilen seçim numarasına göre işlem yapar ve doğru fonskiyonları uygular.
        
        case 1: 
        secenekSayiSifrele();
        break;
        cout << endl;
        
        case 2:
        secenekSayiCoz();
        break;
        cout << endl;
        
        case 3: 
        seceneksezarSifrele();
        break;
        cout << endl;
        
        case 4:
        secenekSezarSifreCoz();
        break;
        cout<< endl;
        
        case 5:
        cout << "Programdan Çıkıldı.";
        return 0;
        break;
        
        default:
        cout << "!Geçersiz işlem numarası girdiniz!";
        break;
        cout << endl;
    }
    return main();
}