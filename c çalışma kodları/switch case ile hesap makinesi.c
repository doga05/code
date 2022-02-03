#include <stdio.h>


int s1,s2,sonuc;
char islem;

int main()
{
    
    printf("Lütfen birinci sayıyı giriniz: ");
    scanf("%d",&s1);
    printf("Lütfen ikinci sayıyı giriniz: ");
    scanf("%d",&s2);
    printf("Lütfen yapmak istediğiniz işlemi sembolle giriniz: ");
    scanf("%s",&islem);
    
    switch(islem){
        
        case '+':
            sonuc=s1+s2;
            printf("Sonuç: %d",sonuc);break;
        case '-':
            sonuc=s2-s1;
            printf("Sonuç: %d",sonuc);break;
        case '*':
            sonuc=s1*s2;
            printf("Sonuç: %d",sonuc);break;
        case '/':
            sonuc=s2/s1;
            printf("Sonuç: %d",sonuc);break;
    }

    return 0;
}

