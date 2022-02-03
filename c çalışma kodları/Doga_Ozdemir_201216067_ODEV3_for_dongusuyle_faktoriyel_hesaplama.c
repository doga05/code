//Adi Soyadi: Doga Ozdemir
// Numara: 201216067
// Dersin Adi ve Ders Kodu: Temel Programlama - BIL102

#include <stdio.h>

int main()
{
    // Degiskenleri integer olarak atadýk ve fact degiskenini 1 sayisina esitledik.  
    int sayi , x , fact;
    fact = 1 ;
    
    //Kullaniciya sayi sorar ve bu sayiyi yazdirir.
    printf("Lutfen bir sayi girin:");
    scanf("%d",&sayi);
    
    // for dongusu baslar.
    for(x = 1; x <= sayi; x++)
    {
        // Faktoriyel iþlemini yapar.
        fact = fact * x ;
    }
    printf("Faktoriyel sonucu:%d",fact);
}
