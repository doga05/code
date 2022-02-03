#include <stdio.h>

int main(void)
{
    int fahr, celcius;
    int lower, upper, step;
    
    lower = 300;
    upper = 0;
    step = 20;
    
    celcius = lower;
    while (celcius >= upper)
    {
        fahr = celcius*1.8+32;
        
        printf("%d\t%d\n", celcius, fahr);
        celcius = celcius - step;
    }
}           
     
