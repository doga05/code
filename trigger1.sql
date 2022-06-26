/*trigger: bir tabloda gerçekleþen sorgu sonucuna göre baþka bir sorgunun çalýþmasýný saðlayan sql komutudur.
procedure'dan farký kullanýcý tarafýndan tetiklenmemesidir. execute yazmamýza gerek yok otomatik olur
trigger 2 þekilde çalýþýr.
1: ana sorguyu engellemek(instead of),
2: birlikte çalýþmak(after-for)
*/
--create trigger Deneme on Kitap2
--after insert 
--as
--begin
--select 'Yeni bir kitap kaydý yapýldý'
--end

--insert into Kitap2 values ('Ýnsan ne ile yaþar','hikaye','eeeeee','yeþil',8) --triggerý döndürür

--create trigger Deneme2 on Kitap2
--after insert
--as
--begin
--select Kitapadi, KitapPuan,KitapPuan=KitapPuan+8 from Kitap2 where KitapPuan=10
--end
insert into Kitap2 values('beni seven vikont','roman','ggggg','kýrmýzý',9) --2 ekran gelir çünkü Kitap2 üzerinde 2 tane trigger var. puan artmasý geçicidir