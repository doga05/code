--then: olduktan sonra
select KitapRengi,KitapDerece,'Durum' =
case KitapDerece
when 'a' then 'Çok Kaliteli'
when 'b' then 'Kaliteli'
when 'c' then 'eh iþte'
else 'bilinmeyen deðer'
end
from Kitap3 

select KitapRengi, KitapBaský,'Basým Oraný'=
case
when KitapBaský<=10 then 'az  basým'
when KitapBaský >10 and KitapBaský <=15 then 'orta basým'
when KitapBaský >15 and KitapBaský <=20 then 'ideal basým'
when KitapBaský >20 then 'Çok Basým'
end
from Kitap3