/* Adi Soyadi: Doga Ozdemir
   Numara: 201216067
   Dersin Adi - Dersin Kodu: Temel Programlama C - BIL102
   Lab/Odev/Proje: Odev IV*/
   
#include <stdio.h>

int main() {
    
    // Kendi olusturdugumuz 'blank' degiskenini tanimladik.
   int low, high, i, blank, flag;
   
   // Klavyeden sayi girisi ve bu sayilari ekrana yazdirma.
   printf("Enter two numbers(intervals): ");
   scanf("%d %d", &low, &high);
   printf("Prime numbers between %d and %d are: ", low, high);
   
   // Dusuk deger, yuksek degerden buyukse sayilari birbiriyle degistir.
    if (low > high) {
      blank = low;
      low = high;
      high = blank;
   }
   
   // low high'dan kucuk oldugu sure boyunca dongu doner.
   while (low < high) {
      flag = 0;
      // 2'den kucuk sayilari gormez.
      if (low <= 1) {
         ++low;
         continue;
      }
      
      // low asal olmayan bir sayi ise flag 1 olur ve donguden cikar.
      for (i = 2; i <= low / 2; ++i) {
         if (low % i == 0) {
            flag = 1;
            break;
         }
      }
      
      // Tam bolunmuyosa flag 0 olur.
      if (flag == 0)
         printf("%d ", low); // ve o sayiyi ekrana yazdirir.
      // low'a 1 ekler.
      ++low;
   }
   
   return 0;
}
