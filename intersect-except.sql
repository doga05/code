--intersect: iki sorgunun kesi�im noktalar�n� bulmak i�in kullan�l�r. inner joine benzer
select KitapAd from Kitap intersect select Kitapadi from Kitap2
--except: farklar�n� verir. birinci except ikinci dersek tablo1de olan ama ikide olmayanlar� listeler
select KitapAd from Kitap except select Kitapadi from Kitap2--birde olan ikide olmayanlar� verir.