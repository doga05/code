#include <stdio.h>

// Adi Syoadi: Doga Ozdemir
//Numara: 201216067
// Ders Adi ve Ders Kodu: Temel Programlama - BIL102
int main()
{

// Degiskenleri integer ve char olarak atadik.
int sayi1,sayi2,sonuc;
char islem;

//Yapmak istenilen islemi ve sayilari kullaniciya sorar ve onlari yazdirir.
printf("Yapmak istediginiz islemi girin( / , * , + , - ):");
scanf("%s",&islem);

printf("Birinci sayiyi girin:");
scanf("%d",&sayi1);

printf("Ikinci sayiyi girin:");
scanf("%d",&sayi2);

//switch case kosulunu baslattik. Girilen isleme gore uygun olan durumu yapar ve sonucu yazdirir.
switch(islem)
{
// Girilen islem bolme ise islemi yapar ve sonucu yazdirir.
    case '/' :
    sonuc= sayi1 / sayi2;
    printf("Sonuc:%d",sonuc); break;
    
// Girilen islem cikartma ise islemi yapar ve sonucu yazdirir.
    case '-' :
    sonuc = sayi1 - sayi2;
    printf("Sonuc:%d",sonuc); break;

// Girilen islem toplama ise islemi yapar ve sonucu yazdirir..   
    case '+' :
    sonuc = sayi1 + sayi2;
    printf("Sonuc:%d",sonuc); break;

// Girilen islem carpma ise islemi yapar ve sonucu yazdirir.    
    case '*' :
    sonuc = sayi1 * sayi2;
    printf("Sonuc:%d",sonuc); break;
    }
}
