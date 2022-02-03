#include <stdio.h>

int main()
{
    /*int i,sayilar[]={10,20,30,40,50,60,70};
    
    for(i=0;i<7;i++){
        printf("%d\n",sayilar[i]);
    }*/
    
    int i,toplam=0,sayilar[]={10,15,20,35};
    
    for(i=0;i<4;i++)
    {
        toplam=toplam+sayilar[i];
        printf("Toplam: %d\n",toplam);
    }
    return 0;
}
