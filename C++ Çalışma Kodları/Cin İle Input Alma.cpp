#include <iostream>

using namespace std;

int main(){
	/*int x;
	cout << "Bir sayı giriniz: ";
	cin >> x;
	cout << "Girdiğiniz Sayı: "<< x<< endl;*/

	int a,b,c;
	cout << "Birinci Sayıyı Giriniz: ";
	cin >> a;

	cout <<"İkinci Sayıyı Giriniz: ";
	cin >> b;

	cout << "Üçüncü Sayıyı Girin: ";
	cin >> c;

	// cout <<"Sayıları girin: ";
	//cin>> a>> b>> c; şeklinde de olabilir.Tek satır halinde alır
	cout << "Toplamları: "<< a+b+c<<endl;

	return 0;
}
