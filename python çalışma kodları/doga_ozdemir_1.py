"""*-*-*-*-*-*-*-*-*-*-**-*-*-* Welcome to the Interest Calculator *-*-*-*-*-*-*-*-*-*-*-*-*-*-*"""

print("*-*-*-*-*-*-*-*-***-*-*-* Welcome to the Interest Calculator *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

name=(input("What is your name?: "))
credit=float(input("Loan Amount: "))
maximum_year=int(input("Maximum Year: "))
maximum_month=int(input("Maximum Month: "))
reiteration=int(input("Reiteration(Month): "))
annual_interest_rate=float(input("Annual Interest_Rate: "))
"""Burda yazılanların hepsi birer değişken yıllık faiz oranı gibi ondalıklı sayıları float olarak
ay ve yıl gibi tam sayıları int olarak tanımlayıp daha sonra fonksiyonların içinde kullanmak
üzere bırakıyoruz"""

def print_duration(maximum_month):
    total_year=int(maximum_month/12)
    remaining_month=maximum_month%12
    print("->Year:" ,total_year, "Month:" ,remaining_month)

print_duration(maximum_month)
""" Burda yaptığımız işlem yılı aya bölmek yani 19 ay yazıyorsak 1 yıl 7 ay şeklinde çıktı
vermemizi sağlıyor."""

def print_money(credit):
    print(format(credit,'.1f'),'$')
print_money(credit)
"""Burda yaptığımız işlemde krediyi float olarak girdiğimiz için .1f sayıda ki noktadan sonra sadece
bir rakamı alıyor.Örneğin 1349.13432 sayısında .1f sayesinde 1349.1 olarak alıyor.$ işareti ise sadece bir para
birimi yani çıktı da paranın dolar cinsinden olduğunu belirtmek için."""

def print_entry(credit,annual_interest_rate,maximum_month):
    total_interest=float(((credit)/100)*(annual_interest_rate/12))*maximum_month
    total_amount=(credit+total_interest)
    monthly_amount=(total_amount/maximum_month)
    print_money(total_amount)
    print("Monthly Amount:")
    print_money(monthly_amount)
print_entry(credit,annual_interest_rate,maximum_month)
""" Burda yaptığımız işlemler aylık ve yıllık miktarı belirlemek için.İşlemi sizin yüklediğiniz ödev pdflerinden
aldım.Total amount ve monthly amountu ben kendim belirledim."""

def print_full_report (credit,annual_interest_rate,maximum_year,maximum_month,reitaretion):
    print('Full report for',name)
    x=reiteration
    while(x<=maximum_year*12+maximum_month):
        print('******************************')
        print_duration(x)
        print_entry(credit,annual_interest_rate,x)
        print('*****************************')
        x+=reiteration

print_full_report(credit,annual_interest_rate,maximum_year,maximum_month,reiteration)
""" Burda yaptığımız işlemler ise çıktının düzgün olması için yaptığımız işlemler.
Değişkenleri yukarıda tanımlamıştık zaten."""

#*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*  KAYNAKÇA *.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*

""" mod alma http://cagrigunay.blogspot.com/2015/06/python-ogreniyorum-ders-7-matematiksel.html 
ve https://www.youtube.com/watch?v=tAZgtqK52HA
.1f http://mcngz.blogspot.com/2018/05/python.html
 http://ahgal.meb.k12.tr/meb_iys_dosyalar/08/03/125513/dosyalar/2018_02/07085232_PYTHON-II.DYNEM.pdf
 https://caylakyazilimci.com/post/python-fonksiyonlar-python-101-5 def fonksiyonu için inceledim
 konuyu daha iyi anlamak için https://www.youtube.com/watch?v=TyRs44XfH5c 
 https://www.youtube.com/watch?v=l70ScGa7 
bileşke faizin nasıl hesaplandığını anlamak için 
https://piyasarehberi.org/yatirim/yatirim-araclari/59-basit-ve-bilesik-faiz
https://www.youtube.com/watch?v=IuGndpLecUk
https://python-istihza.yazbel.com/yorum.html
https://ctrlbizde.com/index.php/egitimler/python-dersleri/item/565-python-da-yorum-satiri-kullanimi-python3-dersleri-ders10
"""