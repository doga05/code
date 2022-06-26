declare @a int
set @a=1
while (@a<=10)
begin
print cast(@a as varchar(10)) + ' Karesi: ' + cast(@a*@a as varchar(3))
set @a = @a+1
end
  --1 ve 10 arasýndan 7yi almadan karelerini alsýn: continue
 declare @x int
 set @x=1
 while(@x<=10)
 begin
 if(@x =7)
 begin
 set @x=@x+1
 continue
 end
 print cast(@x as varchar(2)) + ' Karesi: ' + cast(@x*@x as varchar(3))
 set @x=@x+1
 end
 --goto
 declare @sayac tinyint
 set @sayac=1
 git: --etiket
 print 'Sayaç: ' + cast(@sayac as varchar(1))
 set @sayac=@sayac+1
 while (@sayac <=5)
 goto git

 