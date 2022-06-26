/*bir:turuncu+mor
iki:yeþil+mor
union: birleþtirme iþlemi yaparken iki tabloyu da tamamen birleþtirir. yani turuncu+mor+yeþil yani ortak alaný bir kere alýr yani tekrar eden kayýt yok
union all: turuncu+mor+yeþil+mor ortak alaný iki kere alýr yani tekrar eden kayýtlar vardýr*/
select KitapAd from Kitap union select Kitapadi from Kitap2
select KitapAd from Kitap union all select Kitapadi from Kitap2
