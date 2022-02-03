#include <stdio.h>

int main()
{
    int dizi[100],i,sayi,ort,toplam;
    
    printf("Eleman sayısı giriniz: ");
    scanf("%d",&sayi);
    
    for(i=0;i<sayi;i++)
    {
        printf("Dizinin %d. değerini giriniz: ",i+1);
        scanf("%d",&dizi[i]);
    }
    printf("\n\n");
    
    for (i=0;i<sayi;i++)
    {
        toplam+=dizi[i];
    }
    printf("Toplam: %d\n",toplam);
    ort=toplam/sayi;
    printf("Ortalama: %d",ort);
    
    return 0;
}
