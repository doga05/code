--stored procedure:

create procedure carpim
(@s1 int,@s2 int,@s3 int,@sonuc int output)
as 
set @sonuc=@s1*@s2*@s3
print 'Sonuç: ' + cast(@sonuc as varchar(3))

declare @a int
exec carpim 4,5,6,@a output

create procedure bolum
(@a int,@b int, @c int, @s int output)
as
set @s=(@a*@b*@c)/3
print 'Ortalama: ' + cast(@s as varchar(2))

declare @b int
exec bolum 4,5,6, @b output

--kitap rengi x olan kitaplarý getirsin istiyorum ve bunun için procedure oluþturucam
create procedure kitaprenk (@renk varchar(10))
as
select * from Kitap2 where KitapRenk = @renk

exec kitaprenk 'yeþil'
exec kitaprenk 'mavi'