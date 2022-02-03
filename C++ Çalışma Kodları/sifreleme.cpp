// 201216067 Doğa Özdemir
// 201216073 Nur Sena Günay 


#include <iostream>
using namespace std;

void sifrele(int sayi) {
    int dizi[4], gecici;
    dizi[0]=sayi/1000;
    dizi[1]=(sayi%1000)/100;
    dizi[2]=(sayi%100)/10;
    dizi[3]=(sayi%10);
    
    for(int i=0; i<4; i++) {
        dizi[i]=(dizi[i]+7)%10;
    }
    gecici=dizi[0];
    dizi[0]=dizi[2];
    dizi[2]=gecici;
    gecici=dizi[1];
    dizi[1]=dizi[3];
    dizi[3]=gecici;
        
    cout << " Olusturulan sifre: ";
    for(int j=0; j<4; j++) {
        cout << dizi[j];
    }
}   



void sifrecoz(int sayi2) {
    int dizi2[4],gecici;
    dizi2[0]= sayi2/1000;
    dizi2[1]=(sayi2%1000)/100;
    dizi2[2]=(sayi2%100)/10;
    dizi2[3]=(sayi2%10);
    
    for(int i=0; i<4; i++) {
        dizi2[i]=((dizi2[i]+10)-7)%10;
    }
    gecici= dizi2[0];
    dizi2[0]=dizi2[2];
    dizi2[2]=gecici;
    gecici= dizi2[1];
    dizi2[1]=dizi2[3];
    dizi2[3]=gecici;
        
    cout << " Cozulen sifre: ";
    for(int j=0; j<4; j++) {
        cout << dizi2[j];
    }
}



void secenekSayiSifrele() {
    int veri;
    cout << " Sifrelemek istediginiz 4 haneli sayiyi giriniz: ";
    cin >> veri;
    sifrele(veri);
}



void secenekSayiCoz() {
    int veri;
    cout << " Cozumlemek istediginiz 4 haneli sayiyi giriniz: ";
    cin >> veri;
    sifrecoz(veri);
}


void sezar(char mesaj[100], int anahtar){
    for(int i = 0; mesaj[i] != '\0'; ++i){
        char karakter = mesaj[i];
       
        if(karakter>= 'a' && karakter <= 'z'){
            karakter = karakter + anahtar;
           
            if(karakter > 'z'){
                karakter = karakter - 'z' + 'a' - 1;
            }
           
            mesaj[i] = karakter;
        }
        else if(karakter >= 'A' && karakter <= 'Z'){
            karakter = karakter + anahtar;
            if(karakter > 'Z'){
                karakter = karakter - 'Z' + 'A' - 1;
            }
            mesaj[i] = karakter;
        }
    }
    cout << "Şifreli mesaj: " << mesaj;
}


void seceneksezarSifrele() {
	char mesaj[100];
	int ilerleme;
	cout<< " Anahtarı giriniz:";
	cin>>ilerleme;
	cout << " Sifrelemek istediginiz metni giriniz: ";
	cin.ignore();
	cin.getline(mesaj,100);
	sezar(mesaj,ilerleme);
} 




void sezarcoz(char line[100],int key){
    for(int i = 0; line[i] != '\0'; ++i){
        char karakter = line[i];
       
        if(karakter >= 'a' && karakter <= 'z'){
            karakter = karakter - key;
           
            if(karakter > 'z'){
                karakter = karakter - 'z' > 'a' + 1;
            }
           
            line[i] = karakter;
        }
        else if(karakter >= 'A' && karakter <= 'Z'){
            karakter = karakter - key;
            if(karakter > 'Z'){
                karakter = karakter - 'Z' - 'A' + 1;
            }
            line[i] = karakter;
        }
    }
    cout << "Şifresiz mesaj: " << line;
   
}


void secenekSezarSifreCoz() {
	char line[100];
	int gerileme;
	cout<<" Anahtarı giriniz:";
	cin>>gerileme;
    cout<<endl<< " Cozmek istediginiz metni giriniz: ";
    cin.ignore();
	cin.getline(line,100);
	sezarcoz(line,gerileme);
}


int main() {
    
    cout << "****************"<<endl;
    cout<<"** SIFRELEME PROGRAMINA HOS GELDİNİZ **"<<endl;
    cout << "****************"<<endl<<endl;
            
    int secim;
    char mesaj; 
    int ilerleme;
    cout << "--> Islem numarasi giriniz: "<<endl<<"\t1.Sayi Sifreleme\n\t2.Sayi Cozumleme\n\t3.Sezar Sifreleme\n\t4.Sezar Cozumleme\n\t5.Çıkış"<<endl;
    cout<<endl<<"--> Secim:";
    cin >> secim;
    
    switch(secim) {
        
        case 1: 
        secenekSayiSifrele();
        break;
        
        case 2:
        secenekSayiCoz();
        break;
        
        case 3: 
        seceneksezarSifrele();
        break;
        
        case 4:
        secenekSezarSifreCoz();
        break;
        
        case 5:
        return 0;
        break;
        
        default:
        cout << "Geçersiz işlem numarası girdiniz!";
        break;
        cout<<endl;
    }
    return main();
    
}

