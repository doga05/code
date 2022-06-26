--get date
--getdate()
select getdate()--i�inde bulndu�umuz tarihi getirir

--date part
select datepart(year,getdate()) as 'YIL',
datepart(month,getdate()) as 'AY',
datepart(Day,getdate()) as 'G�N',
datepart(week,getdate()) as 'HAFTA',--y�l�n ka��nc� haftas� oldu�unu hesaplar ay�n de�il
datepart(quarter,getdate()) as '�EYREK'

select datepart(year,'2000-02-05') as 'YIL'

select * from Kitap where datepart(year,KitapTarih)=2016--2016 y�l�nda bas�lan kitaplar� getirir
select * from Kitap where datepart(month,KitapTarih)=12--12.ayda bas�lan kitaplar� getirir

--datediff: 3 parametre al�r. ilki tarih format� ikincisi k���k ���ns� b�y�k tarih.Aralar�ndaki fark� hesaplar

select datediff(year,'1923-10-29','2022-04-07') as 'Y�l Fark�',
datediff(month,'1923-10-29','2022-04-07')as 'Ay Fark�',
datediff(day, '1923-10-29','2022-04-07') as 'G�n Fark�'

select datediff(year,'1919-05-19',getdate())

--dateadd istenilen tarih format�na zaman ekler.3 parametre al�r. birincisi tarif format� ikinci eklenicek de�er ���nc� de nereye eklenicekse o
select dateadd(day,10,getdate()) as 'OnG�nSonra'
