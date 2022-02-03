#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <time.h>
#include <sched.h>
int main() 
{
    FILE *out;
    struct timeval T;
    double baslangic, bitis;
    int N,i,j,k,C;
    cpu_set_t my_set;
    printf("sched_getcpu = %d\n", sched_getcpu());
    printf("Please Insert the Core Number [1-7] odd numbered C: "); 
    scanf("%d",&C);
    CPU_ZERO(&my_set);
    CPU_SET(C, &my_set);
    sched_setaffinity(0, sizeof(cpu_set_t), &my_set);
    printf("Dimension of Matrices N: "); 
    scanf("%d",&N);
    out = fopen ( "./output-ijk.dat", "a");
    
    float **MatrixI = malloc (N*sizeof(float*));
    float **MatrixII = malloc (N*sizeof(float*));
    float **Sonuc = malloc (N*sizeof(float*));

    for (i=0;i<N;i++)
    {
        MatrixI[i] = malloc (N*sizeof(float));
        MatrixII[i] = malloc (N*sizeof(float));
        Sonuc[i] = malloc (N*sizeof(float));
    }
    srand(time(NULL));
    for(i=0; i<N; i++)
    {
        for(j=0; j<N; j++)
        {
            MatrixI[i][j] = (float)rand()/RAND_MAX * 1000; 
            MatrixII[i][j] = (float)rand()/RAND_MAX * 1000;
        }
    }
    printf("sched_getcpu = %d\n", sched_getcpu());
    gettimeofday(&T, 0);
    baslangic = T.tv_sec + T.tv_usec/1000000.0;
    for(i=0; i<N; i++)
    {
        for(j=0; j<N; j++)
        {
            for(k=0; k<N; k++)
            {
                Sonuc[i][j] += MatrixI[i][k] * MatrixII[k][j];
            }
        }
    }
    gettimeofday(&T, 0);
    bitis = T.tv_sec + T.tv_usec/1000000.0;
    printf("wall clock time = %f\n",(bitis - baslangic));
    fprintf(out, "N=%d,\twall clock time=%f,\t ijk \n",N,(bitis - baslangic));
    fclose (out);
    for (j=0;j<N;j++)
    {  
        free(MatrixI[j]);
        free(MatrixII[j]);
        free(Sonuc[j]);
    }     
    free(MatrixI);
    free(MatrixII);
    free(Sonuc);
    
    return 0;
}
