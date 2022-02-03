// Adi Soyadi: Doga Ozdemir
//Numara: 201216067
// Dersin Adi ve Dersin Kodu: Temel Programlama - BIL102

#include <stdio.h>

int main()
{
    // Sayý degiskenini integer olarak atadik ve fact degiskenini 1 sayisina esitledik.
    int sayi,fact;
    fact = 1;
    
    // Kullanicidan bir sayi ister ve o sayiyi yazdirir. 
    printf("Lutfen bir sayi giriniz:");
    scanf("%d",&sayi);
    
    //while dongusu baslar.
    while(sayi >= 1)
    {
        // Faktoriyel islemini yapar.
        fact = fact * sayi;
        sayi--;
    }
    //Sonucu ekrana yazdirir.
    printf("Faktoriyel Sonucu:%d",fact);
}
