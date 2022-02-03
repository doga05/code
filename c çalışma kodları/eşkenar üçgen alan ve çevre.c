#include <stdio.h>
#include <math.h>

int main()
{
    int kenar,alan,cevre;
    kenar=3;
    cevre=3*kenar;
    alan=sqrt(kenar)/4*(kenar*kenar);
    printf("Alan: %d\n",alan);
    printf("Cevre: %d",cevre);

    return 0;
}
