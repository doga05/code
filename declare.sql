--declare: de�i�ken tan�mlarken kullan�l�r.de�i�kenin ba��na @ kullan�l�r. de�i�ken ismi ve t�r� yaz�l�r. set ifadesiyle de�er atan�r.
declare @sehir varchar(15)
declare @ilce varchar(15)
set @sehir='Kahramanmara�'
set @ilce='elbistan'
--select @sehir -- bu sat�r �eklinde tablo gibi getirir.
--mesajlar k�sm�nda normal �ekilde g�z�kmesi i�in print kullan�r�z
print @sehir + ' / ' + @ilce
print @sehir +' �ehrinin ' + @ilce + ' il�esi.'