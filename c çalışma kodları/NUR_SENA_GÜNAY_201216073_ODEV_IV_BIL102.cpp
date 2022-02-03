#include <stdio.h>

int main() {

   int small, big, i, flag ;
   // low high degerlerinin, degisim isleminde kullanilmasi icin tam sayý degisken tanýmlama.
   int dummy; 


   printf("Enter two numbers(intervals): ");

   scanf("%d %d", &small, &big);

   printf("Prime numbers between %d and %d are: ", small, big);


   // Dusuk deger, yuksek degerden buyukse sayilari birbiriyle degistir.Olusturdumuz dummy degiskenini burada gecici olarak kullandik.
   if (small > big) 
   {
       
      dummy = small;  small= big;  big = dummy;
      
   }

   // dusuk degerin yuksek degerden kucuk oldugu durumlarda flag 0 olacak.
   while (small < big) 
     {

      flag = 0;

      // Dusuk deger 2 den kucukse, dusuk degeri 1 arttýr ve donguden cik.
      if (small < 2) 
      {
         ++small;
         continue;

      }

 // i=2, i degiskenimiz, low/2 ye kucuk esit oldugunda, i degiskenini 1 arttirir.

      for (i = 2; i <= small/ 2; ++i) 
      {
       
         if (small % i == 0)
         {
             
            flag = 1;
            break;
            
         }

      }

     // flag 0 ise dusuk deger yazdirlacak.
      if (flag == 0)

         printf("%d ", small);

      // Dusuk deger 1 arttirilacak.
      ++small;

   }
      
   return 0;
}
