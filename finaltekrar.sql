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

alter function d�n�s(@c�mle varchar (50))
returns varchar(50)
as
begin
set @c�mle = LOWER(@c�mle)
set @c�mle=REPLACE(@c�mle,'�','u')
set @c�mle=REPLACE(@c�mle,'�','i')
set @c�mle=REPLACE(@c�mle,'�','o')
set @c�mle=REPLACE(@c�mle,'�','g')
set @c�mle=REPLACE(@c�mle, '�','c')
set @c�mle = REPLACE(@c�mle, '�','s')
return @c�mle
end

select dbo.d�n�s('�z�m �ok s�k�ld� D��ar� ��kt�')

--email devam
create function email(@isim varchar(10), @uzanti varchar(15))
returns varchar(50)
as
begin
return dbo.d�n�s(@isim) + '@' + @uzanti
end
 select dbo.email('dogaozdmr', '@gmail.com') as mail


 --mail tablo
 CREATE TABLE Kay�tOlu�turma (
 PersonelNumaras� SMALLINT IDENTITY(1,1) PRIMARY KEY,
 �sim VARCHAR(20) NOT NULL,
 Soyisim VARCHAR(20) NOT NULL,
 mail AS dbo.email(�sim+'.'+Soyisim,'istinye.edu.tr')
 );

 insert into Kay�tOlu�turma (�sim,Soyisim) values ('do�a', '�zdemir')

 select * from Kay�tOlu�turma

 --Employees tablosundan FirstName+LastName as �smim,
 --order details tablosundan OrderID as Sipari�ID,
 --Order Details Tablosundan Quantitiy*UnitPrice as Toplam
 -- Customers tablosundan City as �ehir ve Region as B�lge
 --bilgiler procedur'� alt�nda birle�tir

 create PROCEDURE Sat��BilgileriGenel
as
select (FirstName + ' ' + LastName) �simSoyisim, od.OrderID SiparisID,
avg(od.UnitPrice*Quantity) Ortalama, c.City �ehir, c.Region B�lge from 
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
