/*trigger: bir tabloda ger�ekle�en sorgu sonucuna g�re ba�ka bir sorgunun �al��mas�n� sa�layan sql komutudur.
procedure'dan fark� kullan�c� taraf�ndan tetiklenmemesidir. execute yazmam�za gerek yok otomatik olur
trigger 2 �ekilde �al���r.
1: ana sorguyu engellemek(instead of),
2: birlikte �al��mak(after-for)
*/
--create trigger Deneme on Kitap2
--after insert 
--as
--begin
--select 'Yeni bir kitap kayd� yap�ld�'
--end

--insert into Kitap2 values ('�nsan ne ile ya�ar','hikaye','eeeeee','ye�il',8) --trigger� d�nd�r�r

--create trigger Deneme2 on Kitap2
--after insert
--as
--begin
--select Kitapadi, KitapPuan,KitapPuan=KitapPuan+8 from Kitap2 where KitapPuan=10
--end
insert into Kitap2 values('beni seven vikont','roman','ggggg','k�rm�z�',9) --2 ekran gelir ��nk� Kitap2 �zerinde 2 tane trigger var. puan artmas� ge�icidir