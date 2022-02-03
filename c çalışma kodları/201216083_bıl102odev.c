lude <stdio.h>

int main() {
   int fallen, large, i, flag, temp;  //deðiþken atamasý yapýlýr.
   
   printf("Enter two numbers(intervals): ");   //kullanýcý sayý giriþi yapýlýr.
   
   scanf("%d %d", &fallen, &large);   // öncelikle büyük ve küçük sayýlarýn giriþi yapýlýr.

   // Girilen deðer ikinci girilen deðerden büyük ise numaralarý deðiþtirin
   if (fallen > large) 
   {
      temp = fallen;
      fallen = large;
      large = temp;
   }

   printf("Prime numbers between %d and %d are: ", fallen, large); //belirlenen sayýlar arasýndaki asal sayýlar düþükten büyüðe.
   while (fallen < large) //girilen büyük sayý küçük sayýdan hep büyük olur ise devam eden bir döngü olur.
   {
      flag = 0;          //girilen deðerler arasýndaki asal sayýlar bulunduðunda boolen deðeri deðiþir ve 0'a eþitlenir.

      //ignore numbers less than 2
      if (fallen<= 1) 
	  {
         ++fallen;
         continue;
      }

      for (i = 2; i <= fallen / 2; ++i) //fallen deðer elde edilene kadar bölünür.
	  {
         if (fallen % i == 0) //Sayýlar tam bölünüyor ise deðiþken=1 olur 
		 {
            flag = 1;
            break; // döngüden çýkýþ
         }
      }
      if (flag == 0)         //Sayýlar tam bölünmüyor ise flag=0 
      
         printf("%d ", fallen); //bulunan asal sayýlar ekrana iþlenir.
      ++fallen;
   }

   return 0;
}
