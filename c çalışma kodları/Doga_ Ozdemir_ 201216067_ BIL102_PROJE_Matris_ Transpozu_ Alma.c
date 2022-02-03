/*Adi Syoadi: Doga Ozdemir
Numara: 201216067
Dersin Adi - Dersin Kodu: Temel Programlama C - BIL102
Lab/Ödev/Proje: Proje*/

#include <stdlib.h>
#include <stdio.h>

int main()
{
    printf("*.*.*  Matrisin Transpozunu Alma Programi *.*.*\n\n");
    
    // Degisken tanımlama
    int i, j,k,l,satir,sutun;
    
     // Kullanicidan transpozu alinicak matrisi icin satir ve sutun ister
    printf("Matris satiri icin 4-9 arasi bir deger giriniz: ");
    scanf("%d",&satir);
    printf("Matris sutunu icin 4-9 arasi bir deger giriniz: ");
    scanf("%d",&sutun);
    
    // Satir ve sutun 4-9 degerleri arasında secilecegi icin daha kucuk ya da buyuk deger girince uyari verir
    if(satir<4 || satir>9)
    {
        printf("Lutfen satir icin 4-9 arası bir deger girin: \n");
        scanf("%d",&satir);
    }
    if(sutun<4 || sutun>9)
    {
        printf("Lutfen sutun icin 4-9 arası bir deger girin: \n");
        scanf("%d",&sutun);
    }
    
    // Matrisleri tanimlama.Koseli parantez icine satir ve sutun yazdik
    //Cunku matrislerin satir ve sutun değeri kullanici tarafindan girilecek ve islem ona gore yapilacak.
    int matris[satir][sutun],tmatris[satir][sutun];
    
     // Matrisin satir ve sutunlarini yazma
   printf("***** Matrisin elemanlarinin yazilmasi*****\n\n"); 
   for(i=0;i<satir;i++)
	{
	    for(j=0;j<sutun;j++)
	    { 
	            printf(" Matrisin %d.satiri ve %d.sutunu [%d][%d]:",i+1,j+1,i+1,j+1);
	            scanf("%d",&matris[i][j]);     
	           
	    }
	    printf("\n");
	}
	
	// Yazdigimiz matrisi duzgun bir sekilde ekrana bastirma
	printf("*****Girdiginiz matris*****\n");
	for(k=0;k<satir;k++)
	{
	    for(l=0;l<sutun;l++)
	    {
	        printf(" %d ",matris[k][l]);
	    }
	    printf("\n");
	}
	
	printf("\n");
	printf("*****Girdiğiniz matrisin transpozu*****\n");
	
	//Matrisin transpozunu alma
	for(i=0;i<satir;i++)
	{
	    for(j=0;j<sutun;j++)
	    {
	        tmatris[j][i] = matris[i][j];// Transpoz islemi
	    }
	}
	// Transpozu alinan matrisi ekrana basma
	for(k=0;k<satir;k++)
	{
	    for(l=0;l<sutun;l++)
	    {
	        printf(" %d ",tmatris[k][l]);
	    }
	    printf("\n");
	}
	
    return 0;
}
