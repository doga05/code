declare @ogrenciler table(
ogrno varchar(3),
ograd varchar(20),
ogrsoyad varchar(30),
ogrkol varchar(30),
orgmahalle varchar(50))

insert into @ogrenciler values('A25','Baran','Yücedað','Saðlýk','Þakirpaþa')
insert into @ogrenciler values('B16','Ali','Yýldýz','Çevre','Yeþilevler')
insert into @ogrenciler values('A28','Ayþe','Kaya','Trafik','Fezvipaþa')

/*yukardaki bilgler olmasaydý yani yorum satýrý olsaydý select yazdýðýmýzda hiç deðer döndürmezdi çünkü yukarda olþan tablo sanal bir tablo
yani declare kýsmý hep olmak zorunda yoksa öyle bir tablo bulamaz*/
select * from @ogrenciler