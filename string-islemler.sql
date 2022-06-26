use Kitaplik
select * from Kitap

select KitapAd, KitapFiyat, KitapFiyat+3 as 'Yeni Fiyat' from Kitap
select KitapAd + '-' + KitapYazar as 'Kitapl�k' from Kitap

--substring: Bir kay�tta istenilen karakterden ba�lay�p istenilen karaktere kadar de�erleri d�nd�r�r
select SUBSTRING(KitapAd,1,5) from Kitap--KitapAd s�tunundan 1.karakterden ba�lar 5.karaktere kadar al�r
select left(KitapAd,7) from Kitap--soldan 7 karakter al�r
select right(KitapAd,7) from Kitap--sa�dan 7 karakter al�r
select upper (KitapAd) as 'B�Y�K HARF', lower(KitapAd) as 'k���k harf' from Kitap
select KitapAd,len(KitapAd) as 'Karakter Say�s�' from Kitap 
select KitapAd,len(KitapAd) as 'Karakter Say�s�' from Kitap where len(KitapAd)>15
select KitapAd, Replace(KitapYazar, 'Z�lf� Licaneli', 'Z.Livaneli') from Kitap--update olmad��� i�in kal�c� bir de�i�iklik olmaz
select REVERSE(KitapAd) from Kitap
