#include <stdio.h>

int main()
{
    /*int i=5;
    
    for(i=0;i<=5;i++)
    {
        printf("******\n"); dikdörtgen şeklinde yapar
    }*/
    
    int i,j;
    
    for (i=1;i<=5;i++)
    {
        for(j=1;j<=i;j++)
        {
            printf("*");
        }
        printf("\n");
    }

    return 0;
}
