#include <stdio.h>

int main()
{
    int a,toplam;
    toplam=0;
    
    for(a=1;a<=41;a+=4)
    {
        toplam=toplam+a;
        printf("%d\n",a);
    }
    printf("Toplama Sonucu: %d\n",toplam);

    return 0;
}

