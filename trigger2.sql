--update trigger: kayýt güncellendi
--ikinci trigger: sayaç artsýn

--create trigger GuncelleKontrol on Kitap2
--after update 
--as
--begin
--print 'Güncelleme Ýþlemi Gerçekleþti...'
--end
--update Kitap2 set KitapPuan=10 where Kitapadi='Veronika'


--create trigger GuncelleKontrol2 on Kitap2
--after update
--as
--begin
--update Guncelleme set Sayac=Sayac+1
--end
update Kitap2 set KitapPuan=5 where Kitapadi='Beyaz Geceler'