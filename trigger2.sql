--update trigger: kay�t g�ncellendi
--ikinci trigger: saya� arts�n

--create trigger GuncelleKontrol on Kitap2
--after update 
--as
--begin
--print 'G�ncelleme ��lemi Ger�ekle�ti...'
--end
--update Kitap2 set KitapPuan=10 where Kitapadi='Veronika'


--create trigger GuncelleKontrol2 on Kitap2
--after update
--as
--begin
--update Guncelleme set Sayac=Sayac+1
--end
update Kitap2 set KitapPuan=5 where Kitapadi='Beyaz Geceler'