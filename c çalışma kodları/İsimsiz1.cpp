#include <stdio.h>

int main()
{

    int sayi,sayi2,sonuc;
    char islem;
    
    printf("Birinci sayiyi giriniz:");
    scanf("%d",&sayi);
    
    printf("Ikinci sayiyi giriniz:");
    scanf("%d",&sayi2);
    
    printf("Ýslemi girin:");
    scanf("%s",&islem);
    
    switch(islem)
    {
        case '+' : 
        sonuc=sayi+sayi2;
        printf("Sonuc:%d",sonuc);
        break;
        
        case '-' : 
        sonuc=sayi-sayi2;
        printf("Sonuc:%d",sonuc);
        break;
        
        case '*' : 
        sonuc=sayi*sayi2;
        printf("Sonuc:%d",sonuc); 
        break;
        
        case '/' : 
        sonuc=sayi/sayi2;
        printf("Sonuc:%d",sonuc); 
        break;
    }
}
