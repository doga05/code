#include <stdio.h>

int main()
{
    int a,fak;
    fak=1;

    printf("Faktoriyelini öğrenmek istediğiniz sayıyı giriniz: ");
    scanf("%d",&a);
    
    while(a>1)
    {
        fak=fak*a;
        a--;
    }
    printf("Faktoriyel: %d",fak);
    return 0;
}

