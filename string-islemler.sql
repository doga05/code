use Kitaplik
select * from Kitap

select KitapAd, KitapFiyat, KitapFiyat+3 as 'Yeni Fiyat' from Kitap
select KitapAd + '-' + KitapYazar as 'Kitaplýk' from Kitap

--substring: Bir kayýtta istenilen karakterden baþlayýp istenilen karaktere kadar deðerleri döndürür
select SUBSTRING(KitapAd,1,5) from Kitap--KitapAd sütunundan 1.karakterden baþlar 5.karaktere kadar alýr
select left(KitapAd,7) from Kitap--soldan 7 karakter alýr
select right(KitapAd,7) from Kitap--saðdan 7 karakter alýr
select upper (KitapAd) as 'BÜYÜK HARF', lower(KitapAd) as 'küçük harf' from Kitap
select KitapAd,len(KitapAd) as 'Karakter Sayýsý' from Kitap 
select KitapAd,len(KitapAd) as 'Karakter Sayýsý' from Kitap where len(KitapAd)>15
select KitapAd, Replace(KitapYazar, 'Zülfü Licaneli', 'Z.Livaneli') from Kitap--update olmadýðý için kalýcý bir deðiþiklik olmaz
select REVERSE(KitapAd) from Kitap
