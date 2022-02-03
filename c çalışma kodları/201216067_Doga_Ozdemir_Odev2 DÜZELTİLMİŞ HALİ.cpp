#include <stdio.h>
int Suslu,SusluT,Normal,NormalT,Koseli,KoseliT,i,Karakter,Sayac=0,EnterSayac=0,SatirSay[100][1000];
int main()
{
    printf("Please avoid using Turkish characters!\n\n");
    while((Karakter=getchar()) != EOF)
    {
       if(Karakter=='\n')
        {
            EnterSayac++;
            Sayac=0;
            break;
        }
        else
        {
            SatirSay[EnterSayac][Sayac]=Karakter;
            Sayac++;
        }
        if(Karakter=='{')++Suslu;
        if(Karakter=='}')++SusluT;
        if(Karakter=='(')++Normal;
        if(Karakter==')')++NormalT;
        if(Karakter=='[')++Koseli;
        if(Karakter==']')++KoseliT;
       
    }
    for(i=0; i<EnterSayac; i++)
    {
            printf("Line%d: %ls\n",i+1,SatirSay[i] );
        if((Suslu-SusluT)<0)
            printf("%d of '{' absent.\n",(Suslu-SusluT)*-1);
        else if((Suslu-SusluT)>0)
            printf("%d of '}' absent.\n",(Suslu-SusluT));
        if((Normal-NormalT)<0)
            printf("%d of '(' absent.\n",(Normal-NormalT)*-1);
        else if((Normal-NormalT)>0)
            printf("%d of ')' absent.\n",(Normal-NormalT));
        if((Koseli-KoseliT)<0)
            printf("%d of '[' absent.\n",(Koseli-KoseliT)*-1);
        else if((Koseli-KoseliT)>0)
            printf("%d of ']' absent.\n",(Koseli-KoseliT));
        if((Suslu==SusluT)&&(Normal==NormalT)&&(Koseli==KoseliT))
            printf("\nYour code is error-free, well done!\n");
    }
}



