lude <stdio.h>

int main() {
   int fallen, large, i, flag, temp;  //de�i�ken atamas� yap�l�r.
   
   printf("Enter two numbers(intervals): ");   //kullan�c� say� giri�i yap�l�r.
   
   scanf("%d %d", &fallen, &large);   // �ncelikle b�y�k ve k���k say�lar�n giri�i yap�l�r.

   // Girilen de�er ikinci girilen de�erden b�y�k ise numaralar� de�i�tirin
   if (fallen > large) 
   {
      temp = fallen;
      fallen = large;
      large = temp;
   }

   printf("Prime numbers between %d and %d are: ", fallen, large); //belirlenen say�lar aras�ndaki asal say�lar d���kten b�y��e.
   while (fallen < large) //girilen b�y�k say� k���k say�dan hep b�y�k olur ise devam eden bir d�ng� olur.
   {
      flag = 0;          //girilen de�erler aras�ndaki asal say�lar bulundu�unda boolen de�eri de�i�ir ve 0'a e�itlenir.

      //ignore numbers less than 2
      if (fallen<= 1) 
	  {
         ++fallen;
         continue;
      }

      for (i = 2; i <= fallen / 2; ++i) //fallen de�er elde edilene kadar b�l�n�r.
	  {
         if (fallen % i == 0) //Say�lar tam b�l�n�yor ise de�i�ken=1 olur 
		 {
            flag = 1;
            break; // d�ng�den ��k��
         }
      }
      if (flag == 0)         //Say�lar tam b�l�nm�yor ise flag=0 
      
         printf("%d ", fallen); //bulunan asal say�lar ekrana i�lenir.
      ++fallen;
   }

   return 0;
}
