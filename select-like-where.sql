/*alter table Kitap
alter column KitapTarih date --veri tipi g�ncelleme*/

/*select * from Kitap where KitapAd='Palto'
select * from Kitap where KitapSayfa>150
select * from Kitap where KitapYazar='Re�at Nuri G�ntekin'*/

select * from Kitap where KitapYay�nEvi='G�ne�' and KitapFiyat>8

select * from Kitap where KitapSayfa >200 or KitapFiyat>12 or KitapYazar='Charles Dickens'

select * from Kitap where KitapSayfa in(200,300,220)--220 300 ya da 200 sayfa olan kitap varsa getirir
select * from Kitap where KitapAd like '%a%'--i�inde a harfi ge�en kitaplar 
select * from Kitap where KitapAd like 'a%' -- ad� a harfi ile ba�layanlar
