// MATRIS TRANSPOZU ALMA 

#include <stdio.h>

int main()
{
    // Degisken atamalari.
    int satir,sutun,xmatrisi[10][10],transpoz[10][10];
    
    // 4-9 arasinda satir ve sutun sayisinin girilmesi.
    printf(" Satir sayisi girin(4-9 arasinda): ");
    scanf("%d",&satir);
    
    printf(" Sutun sayisi girin(4-9 arasinda): ");
    scanf("%d",&sutun);
    
     // Satir ve sutun 4-9 degerleri arasında secileceği için daha kucuk ya da buyuk deger girince uyari verir
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
    
    // Matrisin satir ve sutun elemanlarinin, for dongusu ile, i ve j iterasyon degiskenlerine itare edilmesi ve matris elemanlarinin yazdirilmasi.
    printf("\n-> Matris icin elemanlar <-\n");
    for(int i=0;i<satir;i++)
    {
       for(int j=0;j<sutun;j++)
       {
          printf("   xmatrisi[%d][%d] :",i, j);
          scanf("%d",&xmatrisi[i][j]); 
       }
          
    }
    
    // Matris transpozu icin, i degiskenindeki satir elemanlari ile j degiskenindeki sutun elemanlarinin birbirine esitlenmesi, yani yer degistirmesi islemi.
    printf("\n xmatrisi'nin transpozu =\n") ;
    for(int i=0;i<satir;i++) 
  
    {
        for(int j=0;j<sutun;j++)
        {
            // satir ve sutun elemanlarinin yer degistirmesi.
           transpoz[j][i]=xmatrisi[i][j]; 
        }
    }
    // Sutun elemanlarinin i degiskenine, satir elemanlarinin j degiskenine itare edilmesi.
    for(int i=0;i<sutun;i++)
    {
        for(int j=0;j<satir;j++)
        {
            //Olusan yeni matrisin yazdirilmasi.
            printf("  %d  ",transpoz[i][j]);  
        }
        printf("\n");
    }
          
    return 0;
}



