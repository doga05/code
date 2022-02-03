#include <stdio.h>

int Suslu,SusluT,Normal,NormalT,Koseli,KoseliT,i,Karakter;
int Sayac=0,EnterSayac=0,SatirSay[100][1000];

int main(){
 
   printf("Please avoid using Turkish characters!\n\n");
 
while (Karakter=getchar() != EOF){

    if(Karakter=='\n'){
        ++EnterSayac;
        Sayac=0;}
    else{
        SatirSay[EnterSayac][Sayac]=Karakter;
        ++Sayac;}
    if(Karakter=='{')++Suslu;
    if(Karakter=='}')++SusluT;
    if(Karakter=='(')++Normal;
    if(Karakter==')')++NormalT;
    if(Karakter=='[')++Koseli;
    if(Karakter==']')++KoseliT;
    if(Karakter=='[')++Koseli;
    if(Karakter==']')++KoseliT;
}
}
