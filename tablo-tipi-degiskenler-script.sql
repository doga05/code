declare @ogrenciler table(
ogrno varchar(3),
ograd varchar(20),
ogrsoyad varchar(30),
ogrkol varchar(30),
orgmahalle varchar(50))

insert into @ogrenciler values('A25','Baran','Y�ceda�','Sa�l�k','�akirpa�a')
insert into @ogrenciler values('B16','Ali','Y�ld�z','�evre','Ye�ilevler')
insert into @ogrenciler values('A28','Ay�e','Kaya','Trafik','Fezvipa�a')

/*yukardaki bilgler olmasayd� yani yorum sat�r� olsayd� select yazd���m�zda hi� de�er d�nd�rmezdi ��nk� yukarda ol�an tablo sanal bir tablo
yani declare k�sm� hep olmak zorunda yoksa �yle bir tablo bulamaz*/
select * from @ogrenciler