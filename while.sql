--declare @sayi int
--set @sayi=1
--while(@sayi<=10)
--begin
--print @sayi
--set @sayi=@sayi+1
--end
declare @sayac int
set @sayac=1
while (@sayac<=5)
begin
print cast(@sayac as varchar(1)) + '- Merhaba SQL'
set @sayac=@sayac+1
end