#dörtgen alanı kısa kenar*uzun kenar
def dortgen_alan_hesapla_v1():
	alan = x*y
	print("Dörtgeninizin alanı =", alan)

x = int(input("uzun kenari giriniz: "))
y = int(input("kısa kenari giriniz: "))	
	
dortgen_alan_hesapla_v1()

#daire alanı pi.r**2

def daire_alan_hesapla_v1():
	pi = 3
	alan = pi*r**2
	print("Dairenin alanı:",alan)

r=int(input("Dairenin alanını hesaplamak için bir yarıçap değeri giriniz:"))

daire_alan_hesapla_v1()


def dortgen_alanı_hesapla_v2():
	alan = (x**2)*(y**2)
	print("Dörtgeninizin alanı =", alan)

x = int(input("uzun kenari giriniz: "))
y = int(input("kısa kenari giriniz: "))	

dortgen_alanı_hesapla_v2()

def daire_alanı_hesapla_v2():
	pi = 3
	alan = (pi**2)*((r**2)**2)
	print("Dairenin alanı:",alan)

r=int(input("Dairenin alanını hesaplamak için bir yarıçap değeri giriniz:"))

daire_alanı_hesapla_v2()
