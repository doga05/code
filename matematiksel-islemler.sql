select abs(KitapFiyat) as 'KitapFiyatlar�' from Kitap--mutlak
select CEILING(KitapFiyat) as 'KitapFiyatlar�', KitapFiyat, KitapAd from Kitap--noktal� say�larda �ste yuvarlar
select CEILING(KitapFiyat) as '�st',KitapFiyat, FLOOR(KitapFiyat) as 'Alt', KitapAd from Kitap--noktal� say�larda alta yuvarlar
select KitapAd, KitapFiyat, round(KitapFiyat,2) from Kitap -- virg�lden sonra ka� basamak gelir
select power(2,5) as '�s' -- �s al�r ilki taban ikincisi �s
select sqrt(36) as 'K�k'--karek�k

---TOPLAMA

select sum(KitapFiyat) as 'TOPLAM', sum(Vergi) as 'TOPLAM VERG�' from Kitap
select sum(KitapFiyat) as 'TOPLAM' from Kitap where KitapTarih between '2015-01-01' and '2016-03-31'
select KitapAd, KitapFiyat from Kitap where KitapTarih between '2015-01-01' and '2016-03-31'
select avg(KitapFiyat) as 'ORTALAMA' from Kitap--ortalama
select sum(KitapFiyat) as 'toplam' from Kitap
select max(KitapFiyat) as 'MAX', min(KitapFiyat) as 'Min' from Kitap
select count(KitapAd) from Kitap--ka� kitap oldu�unu sayar