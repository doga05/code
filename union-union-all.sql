/*bir:turuncu+mor
iki:ye�il+mor
union: birle�tirme i�lemi yaparken iki tabloyu da tamamen birle�tirir. yani turuncu+mor+ye�il yani ortak alan� bir kere al�r yani tekrar eden kay�t yok
union all: turuncu+mor+ye�il+mor ortak alan� iki kere al�r yani tekrar eden kay�tlar vard�r*/
select KitapAd from Kitap union select Kitapadi from Kitap2
select KitapAd from Kitap union all select Kitapadi from Kitap2
