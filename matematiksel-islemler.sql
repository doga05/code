select abs(KitapFiyat) as 'KitapFiyatlarý' from Kitap--mutlak
select CEILING(KitapFiyat) as 'KitapFiyatlarý', KitapFiyat, KitapAd from Kitap--noktalý sayýlarda üste yuvarlar
select CEILING(KitapFiyat) as 'Üst',KitapFiyat, FLOOR(KitapFiyat) as 'Alt', KitapAd from Kitap--noktalý sayýlarda alta yuvarlar
select KitapAd, KitapFiyat, round(KitapFiyat,2) from Kitap -- virgülden sonra kaç basamak gelir
select power(2,5) as 'Üs' -- üs alýr ilki taban ikincisi üs
select sqrt(36) as 'Kök'--karekök

---TOPLAMA

select sum(KitapFiyat) as 'TOPLAM', sum(Vergi) as 'TOPLAM VERGÝ' from Kitap
select sum(KitapFiyat) as 'TOPLAM' from Kitap where KitapTarih between '2015-01-01' and '2016-03-31'
select KitapAd, KitapFiyat from Kitap where KitapTarih between '2015-01-01' and '2016-03-31'
select avg(KitapFiyat) as 'ORTALAMA' from Kitap--ortalama
select sum(KitapFiyat) as 'toplam' from Kitap
select max(KitapFiyat) as 'MAX', min(KitapFiyat) as 'Min' from Kitap
select count(KitapAd) from Kitap--kaç kitap olduðunu sayar