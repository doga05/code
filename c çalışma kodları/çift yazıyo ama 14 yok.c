#include <stdio.h>
#include <stdlib.h>

int main()
{
    int i;
    i=2;
    
    while(i<=20)
    {
        if(i%2==0 && 14!=i)
        {
            printf("%d ",i);
        }
        i++;
    }

    return 0;
}

