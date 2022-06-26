--get date
--getdate()
select getdate()--içinde bulnduğumuz tarihi getirir

--date part
select datepart(year,getdate()) as 'YIL',
datepart(month,getdate()) as 'AY',
datepart(Day,getdate()) as 'GÜN',
datepart(week,getdate()) as 'HAFTA',--yılın kaçıncı haftası olduğunu hesaplar ayın değil
datepart(quarter,getdate()) as 'ÇEYREK'

select datepart(year,'2000-02-05') as 'YIL'

select * from Kitap where datepart(year,KitapTarih)=2016--2016 yılında basılan kitapları getirir
select * from Kitap where datepart(month,KitapTarih)=12--12.ayda basılan kitapları getirir

--datediff: 3 parametre alır. ilki tarih formatı ikincisi küçük üçünsü büyük tarih.Aralarındaki farkı hesaplar

select datediff(year,'1923-10-29','2022-04-07') as 'Yıl Farkı',
datediff(month,'1923-10-29','2022-04-07')as 'Ay Farkı',
datediff(day, '1923-10-29','2022-04-07') as 'Gün Farkı'

select datediff(year,'1919-05-19',getdate())

--dateadd istenilen tarih formatına zaman ekler.3 parametre alır. birincisi tarif formatı ikinci eklenicek değer üçüncü de nereye eklenicekse o
select dateadd(day,10,getdate()) as 'OnGünSonra'
