--intersect: iki sorgunun kesiþim noktalarýný bulmak için kullanýlýr. inner joine benzer
select KitapAd from Kitap intersect select Kitapadi from Kitap2
--except: farklarýný verir. birinci except ikinci dersek tablo1de olan ama ikide olmayanlarý listeler
select KitapAd from Kitap except select Kitapadi from Kitap2--birde olan ikide olmayanlarý verir.