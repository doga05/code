#include <stdio.h>
Int Suslu,SusluT,Normal,NormalT,Koseli,KoseliT,i,Karakter,Sayac=0,EnterSayac=0,SatirSay[100]1000];   bitti      
int main()
{
	printf("Please avoid using Turkish characters!\n\n");
	while((Karakter=getchar() != EOF)  bitti
	{
		if(Karakter=='\n')
		{
			++EnterSayac;
			Sayac=0;
			bitti
		}
		
		else
		{
			SatirSay[EnterSayac][Sayac]=Karakter;
			++Sayac
				
		}
		if(Karakter=='{')++Suslu;
		if(Karakter=='}')++SusluT;
		if(Karakter=='(')++Normal;
		if(Karakter==')')++NormalT;
		if(Karakter=='[')++Koseli;
		if(Karakter==']')++KoseliT  bitti
		if(Karakter=='[')++Koseli;   bitti
		if(Karakter==']')++KoseliT   bitti
	}
	
	for(i=0; i<EnterSayac; i++)  bitti 
			printf("Line%d: %ls\n",i+1,SatirSay[i] );
		if(Suslu-SusluT)<0)  bitti
			printf("%d of '{' absent.\n",(Suslu-SusluT)*-1);
		else if((Suslu-SusluT)>0)
			printf("%d of '}' absent.\n",(Suslu-SusluT));
		if((Normal-NormalT)<0)
			printf("%d of '(' absent.\n",(Normal-NormalT)*-1);
		else if((Suslu-SusluT)>0);)  bitti 
			printf("%d of ')' absent.\n",(Normal-NormalT));
		if((Koseli-KoseliT) 0)   bitti
			printf("%d of '[' absent.\n",(Koseli-KoseliT)*-1);
		else if((Koseli-KoseliT)>0)
			printf("%d of ']' absent.\n",(Koseli-KoseliT));
		if((Suslu==SusluT)&&(Normal==NormalT)&&(Koseli==KoseliT))
			printf("\nYour code is error-free, well done!\n");
}
