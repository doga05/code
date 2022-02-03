
// MATRIS TOPLAMI

#include <stdio.h>

int main()
{
    // Degisken atamalari
    int satir,sutun, matris1[10][10],matris2[10][10],yenimatris[10][10];
    
    // Toplanacak matrisler icin satir,sutun sayilarinin girilmesi.
    printf(" Satir sayisi girin: ");
    scanf("%d",&satir);
    printf(" Sutun sayisi girin: ");
    scanf("%d",&sutun);
    
    //Ilk matris icin satir ve sutun elemanlarinin girilmesi.
    printf("\n-->Ilk matris icin elemanlar-- \n");
    
    //Satir elemanlari i iterasyon degiskenine itare ediliyor.
    for(int i=0;i<satir;i++)
	{
	    // Sutun elemanlari j iterasyon degiskenine itare ediliyor.
	    for(int j=0;j<sutun;j++)
	    { 
	        //Ilk matrisin satir ve sutun elemanlarinin yazdirilmasi. 
	        printf(" matris1[%d][%d]: ",i,j);
	        scanf("%d",&matris1[i][j]);     
	    }
	}
	
	//Ikinci matris icin satir ve sutun elemanlarinin girilmesi.
	printf("\n-->Ikinci matris için elemanlar-- \n") ;
	
	// Satir elemanlari i iterasyon degiskenine itare ediliyor.
	for(int i=0;i<satir; i++)
	{  
	    //Sutun elemanlari j iterasyon degiskenine itare ediliyor.
		for(int j=0;j<sutun; j++) 
	    {
	        //Ikinci matrisin satir ve sutun elemanlarinin yazdirilmasi.
	        printf(" matris2[%d][%d]: ",i,j);
	        scanf("%d",&matris2[i][j]);
	    }
	}
	//Matrislerin toplanmasi
	printf("\n--> Matrislerin toplami: \n");
	
    for(int i=0; i<satir; i++)
	{ 
	   
	   for(int j=0;j<sutun;j++)
	    {
	    	// matris1 ve matris2 degiskeni,toplanarak yenimatris adli degiskene esitleniyor ve yenimatris degiskeni ekrana yazdiriliyor.
	        yenimatris[i][j]= matris1[i][j]+matris2[i][j] ;
	        printf("  %d ",yenimatris[i][j]);
	    }
	    printf(" \n");
	}
	  return 0;
}



