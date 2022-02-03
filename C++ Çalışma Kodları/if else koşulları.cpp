#include <iostream>

using namespace std;

int main() {
	string password = "nefretediyorumbuevden";
	string input;

	cout << "Lütfen Parolanızı Girin: ";
	cin >> input;

	if(password == input){
		cout<<"Giriş yapıldı.";
	}
	else{
		cout<<"Şifreni Yanlış Girdin Amsalak.";
	}


	return 0;
}
