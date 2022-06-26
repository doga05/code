/*full outer join: birinci ve ikinci tabloyu komple alýr. yani a+b kadar sonuç verir.
KitapAd				Renk
palto				yeþil
son ada				mavi
insancýklar			yeþil
þeker portakalý		null çünkü ikinci tabloda adý yok
nullbirinci tabloda yok				gri(suç ve ceza) */

select KitapAd,KitapRenk from Kitap k1 full outer join Kitap2 k2 on k1.KitapAd=k2.Kitapadi--21+12 olur ama birden fazla yazýlanlarý 1 kere olur yani doðru

/*cross join: her tarafý her tarafla birleþtirir. yani bütün deðerleri getirir. a*b kadar deðer olur. on kullanýlmaz çünkü her deðeri getirir zaten*/

select KitapAd,KitapRenk from Kitap cross join Kitap2 