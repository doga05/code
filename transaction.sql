/*transaction: 
ATM'den para �ek
Tutar� yaz
giri� tu�una bas
para� al
al�nd� m�(e-h)
e:tutar� toplam hesap bakiyesinden d��
h:paray� atmden geri al ve bakiyeye geri y�kle
son

Begin: i�lem ba�lang�c�
Rollback:i�lemleri geri alma/iptal etme
Commit: ��lemleri kaydet */

Begin transaction --i�lem ba�lang�c�
update Kitap set KitapSayfa=50
update Kitap set KitapFiyat=1
select * from Kitap
rollback --buraya kadar b�t�n kitaplar� 1 lira ve 50 sayfa yapt� ama bu k�z�mda i�lemleri geri ald�k
select * from Kitap -- geri ald���m�z i�in burda eski halini bast�rd�. commit yazsayd�k yapt���m�z �eyleri kaydederdi.
--save transaction'a da bak