declare @sayi1 int, @sayi2 int, @toplam int
set @sayi1=5
set @sayi2=8
set @toplam=@sayi1+@sayi2
print @toplam
--topla: 13 yazmak i�in
print 'Toplam: ' + cast(@toplam as varchar(2))--cast de�i�ken d�n���m� i�in
declare @sayii1 int, @sayii2 int, @toplamm int,
@fark int, @carpim int, @bolum int

set @sayii1=5
set @sayii2=8

set @toplamm = @sayii1+@sayii2
set @fark=@sayii2-@sayii1
set @carpim=@sayii1*@sayii2
set @bolum=@sayii2/@sayii1

print 'Toplam: ' + cast(@toplam as varchar(2))
print 'Fark: ' + cast(@fark as varchar(2))
print '�arp�m: ' + cast(@carpim as varchar(2))
print 'B�l�m: ' + cast(@bolum as varchar(2))

--KARES� K�P� 2x2+4x+5 K�K�
declare @x int, @karesi int,@kupu int,@koku int
set @x=2
set @karesi =@x*@x
set @kupu = @x*@x*@x
set @koku = 2*(@x*@x) + 4*@x+5

print 'Karesi: ' + cast(@karesi as varchar(1))
print 'K�p�: ' + cast(@kupu as varchar(1))
print 'K�k�: ' + cast(@koku as varchar(2)) 