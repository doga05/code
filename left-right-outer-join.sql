/*left outer join: soldan birle�me. 1.tablonun tamam�n� al�r ve 2.tablo ile birle�en k�sm�n� da al�r. 
birinci tabloda ikinciyi tabloya denk gelmeyenleri null d�nd�r�r.Yani
Tablo1                      Tablo2
s�r�a k��k                  beyaz geceler             k�rm�z�
and                         su� ve ceza               beyaz
insanc�klar                 insanc�klar               ye�il
�eker portakal�             �eker portakal�           sar�
                            yalnz efe                 gri
Tablo1'i tamamen al�r ve insanc�klar ile �eker portakal�n�n renklerini de getirir ��nk� tablo2de var. Ama di�er iki kitab�n rengi null d�ner.
��nk� tablo2'de de�erleri yok.*/
--use Kitaplik

select KitapAd, KitapRenk from Kitap, Kitap2 --b�t�n de�erleri getirir.
select KitapAd, KitapRenk from Kitap k1 inner join Kitap2 k2 on k1.KitapAd=k2.Kitapadi
select KitapAd, KitapRenk from Kitap k1 left outer join Kitap2 k2 on k1.KitapAd=k2.Kitapadi--do�ru yapt�m :)


/*right outer join: ikinci tabloya g�re i�lem yapar. Yani b�t�n renkleri getirir ama kitapadlar� yoksa katapad de�erini null d�nd�r�r*/

select KitapAd, KitapRenk from Kitap k1 right outer join Kitap2 k2 on k1.KitapAd=k2.Kitapadi --do�ruuu :)