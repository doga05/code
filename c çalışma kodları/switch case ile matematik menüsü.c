#include <stdio.h>

int main()
{
    int s1,s2,sonuc,secim;
    
    printf("***** MATEMATİK MENÜSÜ *****\n");
    printf("1 - Karede alan ve çevre hesabı\n");
    printf("2 - Girilen Sayının Küpü\n");
    printf("3 - Çemberde Alan ve Çevre Hesabı\n");
    printf("4 - 5x^2+7x+9 x'e göre işlemin sonucu\n");
    printf("5 - Dikdörtgende Alan ve Çevre Hesabı\n");
    printf("Lütfen İşlem Seçiniz: ");
    scanf("%d",&secim);
    
    switch(secim)
    {
        case 1:
            printf("Lütfen bir kenar uzunluğu giriniz: ");
            scanf("%d",&s1);
            printf("Karenin Alanı: %d\n",(s1*s1));
            printf("Karenin Çevresi: %d",(s1*4));
            break;
        case 2:
            printf("Küpünü Almak İstediğiniz Sayıyı Giriniz: ");
            scanf("%d",&s1);
            printf("Girilen Sayının Küpü: %d",(s1*s1*s1));
            break;
        case 3:
            printf("Lütfen Çemberin Yarıçapını Giriniz: ");
            scanf("%d",&s1);
            printf("Çemberin Alanı: %f\n",(s1*3.14));
            printf("Çemberin Çevresi: %f",(2*s1*3.14));
            break;
        case 4:
            printf("Bir x Değeri Giriniz: ");
            scanf("%d",&s1);
            printf("5x**2+7x+9'un Değeri: %d",(5*s1+7*s1+9));
            break;
        case 5:
            printf("Kısa Kenarın Değerini Giriniz: ");
            scanf("%d",&s1);
            printf("Uzun Kenarın Değerini Giriniz: ");
            scanf("%d",&s2);
            printf("Dikdörtgenin Alanı: %d\n",(s1*s2));
            printf("Dikdörtgenin Çevresi: %d",(2*(s1+s2)));
            break;
    }
    

    return 0;
}
