--fonksiyonlar: procedure mant���yla �al���r. procedurelerin oldu�u yerde fbctions var oraya kkaydedilir
--return: veriyi d�nd�r�r
--returns: verinin veri tipini belirleriz

--Kitap3 tablosundaki renkleri b�y�k yazmak i�in upper kullan�labilir ama bunu fonksiyonla yaz�caz yani �a��r�lan her �eyi b�y�k yazar
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

select dbo.kayitsayi('ye�il') as 'YE��L'