--if else karar yapıları: değişken oluşturulur o değişken sorgu köprüsü olur
declare @kitapsayi tinyint
select @kitapsayi= COUNT(Kitapadi) from Kitap2
if(@kitapsayi>=5)
begin
print 'Yetersiz Kitap: ' + cast(@kitapsayi as varchar(2))
end
else
begin
print 'Yeterli Kitap: ' + cast(@kitapsayi as varchar(2))
end
declare @sayi tinyint
select @sayi =COUNT(KitapTur) from Kitap2 where KitapTur='roman'
if(@sayi<=3)
begin
print 'yetersiz roman: ' + cast(@sayi as varchar(1))
end
else if(@sayi>3 and @sayi <=6)
begin
print 'Orta Sayıda Kitap: ' + cast(@sayi as varchar(1))
end
else
begin
print 'Yeterli Kitap Mevcut: ' + cast(@sayi as varchar(1))
end