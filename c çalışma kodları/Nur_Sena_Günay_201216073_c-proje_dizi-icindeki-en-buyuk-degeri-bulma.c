
// GIRILEN BIR DIZI ICINDEKI EN BUYUK ELEMANI BULMA
#include <stdio.h>

int main()
{
    // Degisken tanimlamalari.
    int i, eleman;
    float array[20];

    // Dizinin icindeki eleman sayisini belirtme ve elemanlarin girilmesi.
    printf("  Toplam eleman sayisini girin (1 ve 50 arasinda): ");
    scanf("%d", &eleman);
    printf("\n");

    // Girilen elemanlari array dizisinin icine yonlendirme.
    for(i=0; i<eleman; ++i)
    {
       printf("--> %d. sayiyi girin : ", i+1);
       scanf("%f", &array[i]);
    }
    // Dizideki elemanlari sirasiyla karsilastirir ve karsilastirmalarda buyuk olan sayiyla bir sonrakini karsilastirir.
    for(i=1; i<eleman; ++i)
    {
       // 0. indeksteki sayi bir sonraki sayidan kucukse, bir sonraki sayi 0. indekse esitlenir ve en buyuk sayi yazdirilir.
       if(array[0] < array[i])
       array[0] = array[i];
    }
    printf("\n> Girdiginiz sayilar icindeki en buyuk eleman = %.2f ", array[0]);

    return 0;
}


