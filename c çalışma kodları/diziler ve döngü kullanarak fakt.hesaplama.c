#include <stdio.h>

int main()
{
    int i,sonuc=1,fak[]={1,2,3,4,5,6,7};
    
    for(i=1;i<7;i++)
    {
        sonuc=sonuc*fak[i];
    }
    printf("Faktoriyel: %d",sonuc);
    return 0;
}
