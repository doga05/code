/*full outer join: birinci ve ikinci tabloyu komple al�r. yani a+b kadar sonu� verir.
KitapAd				Renk
palto				ye�il
son ada				mavi
insanc�klar			ye�il
�eker portakal�		null ��nk� ikinci tabloda ad� yok
nullbirinci tabloda yok				gri(su� ve ceza) */

select KitapAd,KitapRenk from Kitap k1 full outer join Kitap2 k2 on k1.KitapAd=k2.Kitapadi--21+12 olur ama birden fazla yaz�lanlar� 1 kere olur yani do�ru

/*cross join: her taraf� her tarafla birle�tirir. yani b�t�n de�erleri getirir. a*b kadar de�er olur. on kullan�lmaz ��nk� her de�eri getirir zaten*/

select KitapAd,KitapRenk from Kitap cross join Kitap2 