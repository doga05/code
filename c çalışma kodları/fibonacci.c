#include <stdio.h>
#include <stdlib.h>

int main(){
    
    int a,b,c,i;
    a=1;
    b=1;
    
    //fibonacci 10'a kadar yazdırma
    printf("%d\n",a);
    printf("%d\n",b);
    
    for(i=1;i<=10;i++)
    {
        c=a+b;
        a=b;
        b=c;
        printf("%d\n",c);
    }
    

    
    /*printf("Kactan kaca kadar sayilari toplamak istiyorsunuz?: ");
      scanf("%d %d",&a,&b);
      for(i=a;i<=b;i++)
      {
          toplam=toplam+i; 
      }
     printf("Sonuc: %d",toplam);*/
 
 
 return 0;
}

