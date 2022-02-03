#include <stdio.h>
#include <stdlib.h>

int main()
{
    int s1,s2,s3,ort;
    
    printf("Birinci sinav notunu girin: ");
    scanf("%d",&s1);
    
    printf("İkinci sinav notunu girin: ");
    scanf("%d",&s2);
    
    printf("Ucuncu sinav notunu girin: ");
    scanf("%d",&s3);
    
    ort= (s1+s2+s3)/3;
    
    printf("Ortalama: %d\n",ort);
    
    if(ort<50)
    {
        printf("FF:)");
    }
    if(ort>=50 && ort<=60)
    {
        printf("DD!!");
    }
    if(ort>=60 && ort<=70)
    {
        printf("CC");
    }
    if(ort>=70 && ort<=85)
    {
        printf("BB");
    }
    if(ort>=85)
    {
        printf("AA");
    }
    
   
    return 0;
}
