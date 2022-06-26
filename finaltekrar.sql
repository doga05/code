--fibo
create function fibo(@sayi int)
returns @numbers table (number int)
as
begin
	declare @n1 int =1, @i int=0, @n2 int =1, @temp int
	insert into @numbers values (@n1),(@n2)
	while(@i<=@sayi)
	begin
	insert into @numbers values (@n2+@n1)
	set @temp = @n2
	set @n2= @n2+@n1
	set @n1=@temp
	set @i +=1
	end
	return
end
select * from dbo.fibo(5)


--faktoriyel
create function fakt(@s int)
returns int
as
begin
declare @i int =1, @sonuc int=1
while(@i<=@s)
begin
set @sonuc *= @i
set @i +=1
end
return @sonuc
end

select dbo.fakt (5)

--email

alter function dönüs(@cümle varchar (50))
returns varchar(50)
as
begin
set @cümle = LOWER(@cümle)
set @cümle=REPLACE(@cümle,'ü','u')
set @cümle=REPLACE(@cümle,'ı','i')
set @cümle=REPLACE(@cümle,'ö','o')
set @cümle=REPLACE(@cümle,'ğ','g')
set @cümle=REPLACE(@cümle, 'ç','c')
set @cümle = REPLACE(@cümle, 'ş','s')
return @cümle
end

select dbo.dönüs('Üzüm çok sıkıldı Dışarı çıktı')

--email devam
create function email(@isim varchar(10), @uzanti varchar(15))
returns varchar(50)
as
begin
return dbo.dönüs(@isim) + '@' + @uzanti
end
 select dbo.email('dogaozdmr', '@gmail.com') as mail


 --mail tablo
 CREATE TABLE KayıtOluşturma (
 PersonelNumarası SMALLINT IDENTITY(1,1) PRIMARY KEY,
 İsim VARCHAR(20) NOT NULL,
 Soyisim VARCHAR(20) NOT NULL,
 mail AS dbo.email(İsim+'.'+Soyisim,'istinye.edu.tr')
 );

 insert into KayıtOluşturma (İsim,Soyisim) values ('doğa', 'özdemir')

 select * from KayıtOluşturma

 --Employees tablosundan FirstName+LastName as İsmim,
 --order details tablosundan OrderID as SiparişID,
 --Order Details Tablosundan Quantitiy*UnitPrice as Toplam
 -- Customers tablosundan City as Şehir ve Region as Bölge
 --bilgiler procedur'ü altında birleştir

 create PROCEDURE SatışBilgileriGenel
as
select (FirstName + ' ' + LastName) İsimSoyisim, od.OrderID SiparisID,
avg(od.UnitPrice*Quantity) Ortalama, c.City Şehir, c.Region Bölge from 
Employees e inner join Orders o on
e.EmployeeID = o.EmployeeID inner join [Order Details] od on od.OrderID = o.OrderID
inner join Customers c on c.CustomerID = o.CustomerID 
inner join Products p on 
p.ProductID = od.ProductID
group by FirstName, LastName, od.OrderID, p.UnitPrice, Quantity, c.City, c.Region

 --script
 DECLARE @I AS INT=0
WHILE @I<100000
BEGIN
DECLARE @isim AS VARCHAR(100)
DECLARE @cinsiyet AS VARCHAR(1)
DECLARE @soyisim AS VARCHAR(100)
DECLARE @sehir AS VARCHAR(100)
DECLARE @ilce AS VARCHAR(100)
DECLARE @dogumtarihi AS DATETIME

DECLARE @RAND AS INT
SET @RAND= RAND()*609 
 
SELECT @isim=isim,@cinsiyet=cinsiyet FROM isimler WHERE ID=@RAND 

SET @RAND= RAND()*16000 
SELECT @soyisim=soyisim FROM soyisimler WHERE ID=@RAND 

SET @RAND= RAND()*900 
SELECT @sehir=sehir, @ilce=ilce  FROM SehirBilgileri WHERE ID=@RAND 

SET @RAND=RAND()*365*80
SET @dogumtarihi=GETDATE()-@RAND 
 
INSERT INTO musteriler ( isim, soyisim, dogumtarihi, sehir, ilce , cinsiyet)
VALUES ( @isim, @soyisim, @dogumtarihi, @sehir, @ilce,@cinsiyet)

SET @I=@I+1
END
SELECT * FROM musteriler
