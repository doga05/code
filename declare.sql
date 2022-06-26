--declare: deðiþken tanýmlarken kullanýlýr.deðiþkenin baþýna @ kullanýlýr. deðiþken ismi ve türü yazýlýr. set ifadesiyle deðer atanýr.
declare @sehir varchar(15)
declare @ilce varchar(15)
set @sehir='Kahramanmaraþ'
set @ilce='elbistan'
--select @sehir -- bu satýr þeklinde tablo gibi getirir.
--mesajlar kýsmýnda normal þekilde gözükmesi için print kullanýrýz
print @sehir + ' / ' + @ilce
print @sehir +' þehrinin ' + @ilce + ' ilçesi.'