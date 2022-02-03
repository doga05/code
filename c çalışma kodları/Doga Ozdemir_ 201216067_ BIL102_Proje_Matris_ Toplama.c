/*Adi Syoadi: Doga Ozdemir
Numara: 201216067
Dersin Adi - Dersin Kodu: Temel Programlama C - BIL102
Lab/Odev/Proje: Proje*/

#include <stdlib.h>
#include <stdio.h>

int main()
{
    printf("*.*.*  Matris Toplama Programi *.*.*\n\n");
    
    // Degisken tanimlama
    int i, j,satir,sutun,k,l;
    
    // Kullanicidan A ve B matrisi icin satir ve sutun ister
    printf("A matrisi kac satir ve sutundan olussun: ");
    scanf("%d %d",&satir,&sutun);
    
	printf("B matrisi kac satir ve sutundan olussun: ");
    scanf("%d %d",&satir,&sutun);
    printf("\n\n");
    
    // Matrisleri tanimlama.Koseli parantez icine satir ve sutun yazdik
    //Cunku matrislerin satir ve sutun degeri kullanici tarafindan girilecek ve islem ona gore yapilacak.
    int amatris[satir][sutun],bmatris[satir][sutun],cmatris[satir][sutun];
    
   // A matrisinin satir ve sutunlarini yazma
   printf("*-*-* A matrisinin elemanlarinin yazilmasi *-*-*\n\n"); 
   for(i=0;i<satir;i++)
	{
	    for(j=0;j<sutun;j++)
	    { 
	        printf("A matrisinin %d.satiri ve %d.sutunu [%d][%d]:",i+1,j+1,i+1,j+1);
	        scanf("%d",&amatris[i][j]);     
	           
	    }
	    printf("\n");
	}
	
	// B matrisinin satir ve sutunlarini yazma
    printf("*-*-* B matrisinin elemanlarinin yazilmasi *-*-*\n\n");
	for(i=0;i<satir; i++)
	{  
		for(j=0;j<sutun; j++) 
	    {
	        printf("B matrisinin %d.satiri ve %d.sutunu [%d][%d]:",i+1,j+1,i+1,j+1);
	        scanf("%d",&bmatris[i][j]);
	    }
	    printf("\n");
	}
	
	// Yazdigimiz A matrisini duzgun bir sekilde ekrana bastirma
	printf("Olusan A matrisi\n");
	for(k=0;k<satir;k++)
	{
	    for(l=0;l<sutun;l++)
	    {
	        printf(" %d ",amatris[k][l]);
	    }
	    printf("\n");
	}
	
	// Yazdigimiz B matrisini duzgun bir sekilde ekrana bastirma
	printf("Olusan B matrisi\n");
	for(k=0;k<satir;k++)
	{
	    for(l=0;l<sutun;l++)
	    {
	        printf(" %d ",bmatris[k][l]);
	    }
	    printf("\n");
	}
	printf("*-*-* Matrislerin Toplami Sonucu *-*-*\n\n");
	
	for(i=0;i<satir;i++)
	{
	    for(j=0;j<sutun;j++)
	    {
	        cmatris[i][j] = amatris[i][j] + bmatris[i][j]; // Toplama islemini yapma
	    }
	}
	
	// Yeni matrisi ekrana basma
	for(k=0;k<satir;k++)
	{
	    for(l=0;l<sutun;l++)
	    {
	        printf(" %d ",cmatris[k][l]);
	    }
	    printf("\n");
	}
    return 0;
}
