--then: olduktan sonra
select KitapRengi,KitapDerece,'Durum' =
case KitapDerece
when 'a' then '�ok Kaliteli'
when 'b' then 'Kaliteli'
when 'c' then 'eh i�te'
else 'bilinmeyen de�er'
end
from Kitap3 

select KitapRengi, KitapBask�,'Bas�m Oran�'=
case
when KitapBask�<=10 then 'az  bas�m'
when KitapBask� >10 and KitapBask� <=15 then 'orta bas�m'
when KitapBask� >15 and KitapBask� <=20 then 'ideal bas�m'
when KitapBask� >20 then '�ok Bas�m'
end
from Kitap3