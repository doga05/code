/*alter table Kitap
alter column KitapTarih date --veri tipi güncelleme*/

/*select * from Kitap where KitapAd='Palto'
select * from Kitap where KitapSayfa>150
select * from Kitap where KitapYazar='Reþat Nuri Güntekin'*/

select * from Kitap where KitapYayýnEvi='Güneþ' and KitapFiyat>8

select * from Kitap where KitapSayfa >200 or KitapFiyat>12 or KitapYazar='Charles Dickens'

select * from Kitap where KitapSayfa in(200,300,220)--220 300 ya da 200 sayfa olan kitap varsa getirir
select * from Kitap where KitapAd like '%a%'--içinde a harfi geçen kitaplar 
select * from Kitap where KitapAd like 'a%' -- adý a harfi ile baþlayanlar
