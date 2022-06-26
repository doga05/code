/*left outer join: soldan birleþme. 1.tablonun tamamýný alýr ve 2.tablo ile birleþen kýsmýný da alýr. 
birinci tabloda ikinciyi tabloya denk gelmeyenleri null döndürür.Yani
Tablo1                      Tablo2
sýrça köþk                  beyaz geceler             kýrmýzý
and                         suç ve ceza               beyaz
insancýklar                 insancýklar               yeþil
þeker portakalý             þeker portakalý           sarý
                            yalnz efe                 gri
Tablo1'i tamamen alýr ve insancýklar ile þeker portakalýnýn renklerini de getirir çünkü tablo2de var. Ama diðer iki kitabýn rengi null döner.
çünkü tablo2'de deðerleri yok.*/
--use Kitaplik

select KitapAd, KitapRenk from Kitap, Kitap2 --bütün deðerleri getirir.
select KitapAd, KitapRenk from Kitap k1 inner join Kitap2 k2 on k1.KitapAd=k2.Kitapadi
select KitapAd, KitapRenk from Kitap k1 left outer join Kitap2 k2 on k1.KitapAd=k2.Kitapadi--doðru yaptým :)


/*right outer join: ikinci tabloya göre iþlem yapar. Yani bütün renkleri getirir ama kitapadlarý yoksa katapad deðerini null döndürür*/

select KitapAd, KitapRenk from Kitap k1 right outer join Kitap2 k2 on k1.KitapAd=k2.Kitapadi --doðruuu :)