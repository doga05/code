#include <stdio.h>

int main() {
	
	char Kitapadi[20], Yazari[30], Sayfasayisi[4], Basimtarihi[4], Turu[20];
	
	printf("Kitap Adi: ");
	scanf("%s", Kitapadi);
	
	printf("Yazar: ");
	scanf("%s", Yazari);
	
	printf("Sayfa Sayisi: ");
	scanf("%s", Sayfasayisi);
	
	printf("Basim Tarihi:" );
	scanf("%s", Basimtarihi);
	
	printf("Kitabin Turu: ");
	scanf("%s", Turu);
	
	printf("Kitap Adi: %s\n",Kitapadi);
	printf("Yazar: %s",Yazari);
	printf("\n");
	printf("Sayfa Sayisi:%s\nBasim Tarihi:%s\nKitabin Turu:%s\n",Sayfasayisi,Basimtarihi,Turu);
}