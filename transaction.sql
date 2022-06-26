/*transaction: 
ATM'den para çek
Tutarý yaz
giriþ tuþuna bas
paraý al
alýndý mý(e-h)
e:tutarý toplam hesap bakiyesinden düþ
h:parayý atmden geri al ve bakiyeye geri yükle
son

Begin: iþlem baþlangýcý
Rollback:iþlemleri geri alma/iptal etme
Commit: Ýþlemleri kaydet */

Begin transaction --iþlem baþlangýcý
update Kitap set KitapSayfa=50
update Kitap set KitapFiyat=1
select * from Kitap
rollback --buraya kadar bütün kitaplarý 1 lira ve 50 sayfa yaptý ama bu kýzýmda iþlemleri geri aldýk
select * from Kitap -- geri aldýðýmýz için burda eski halini bastýrdý. commit yazsaydýk yaptýðýmýz þeyleri kaydederdi.
--save transaction'a da bak