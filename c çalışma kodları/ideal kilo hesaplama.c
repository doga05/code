#include <stdio.h>
#include <stdlib.h>

int main()
{
    printf("İdeal kilo hesaplama\n\n");
    // (boy-100+yaş/10)*0.8
    
    float boy,yas,ideal;
    
    printf("Boyunuzu girin: ");
    scanf("%f",&boy);
    
    printf("Yasinizi girin: ");
    scanf("%f",&yas);
    
    ideal=(boy-100+yas/10)*0.8;
    printf("İdeal Kilonuz: %f",ideal);
   
    return 0;
}
