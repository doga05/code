--fonksiyonlar: procedure mantýðýyla çalýþýr. procedurelerin olduðu yerde fbctions var oraya kkaydedilir
--return: veriyi döndürür
--returns: verinin veri tipini belirleriz

--Kitap3 tablosundaki renkleri büyük yazmak için upper kullanýlabilir ama bunu fonksiyonla yazýcaz yani çaðýrýlan her þeyi büyük yazar
create function buyukharf(@deger as varchar(20))
returns varchar(10)
as
begin
return upper(@deger)
end
select dbo.buyukharf(kitaprengi) from Kitap3

create function kayitsayi(@gelenrenk varchar(10))
returns int
as
begin
declare @sayi int
select @sayi=COUNT(KitapRengi) from Kitap3 where KitapRengi = @gelenrenk
return @sayi
end

select dbo.kayitsayi('yeþil') as 'YEÞÝL'