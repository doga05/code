/*Adi Syoadi: Doga Ozdemir
Numara: 201216067
Dersin Adi - Dersin Kodu: Temel Programlama C - BIL102
Lab/Ödev/Proje: Proje*/

#include <stdio.h>

int main(){

   printf("*-*-* Yazilan Dizideki En Buyuk Sayiyi Bulma Programi*-*-*\n\n");
    
    // Degisken tanimlama
    int i,k;
    
    // Disardan eleman sayisi girme
    printf ("Dizinin Eleman Sayisini Girin: ");
    scanf("%d",&k);

    int a[k];

    printf("\n");
    
    // Kac eleman girildiyse o kadar sayiyi sirayla girmesini ister 
    for(i = 0; i <k ; i++)
    {
        printf("%d. Sayiyi Girin: ", i+1);
        scanf("%d", &a[i]);
    }
    
    printf("\n");
    
    // Girilen sayilari karsilastirir ve buyuk olani yazar
    for(i = 1; i < k; ++i)
    {
 
        if(a[0] < a[i])
        a[0] = a[i];
    }
    
    printf("Girilen Sayilarin En Buyugu: " "%d", a[0]);
}
