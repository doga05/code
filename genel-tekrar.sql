/*use okulum
create table ogrenci(
ogrno int not null primary key,
ogradi varchar(15),
ogrsoyadi varchar(20),
ogradres varchar (50),
ogrsinif varchar(2),
ogrilce varchar(20) default 'seyhan',
ogrsinav1 tinyint check (ogrsinav1 >0),
ogrsinav2 int,
constraint chks2 check (ogrsinav2 >=0 and ogrsinav2<=100),
ogrkol varchar(20),
constraint chkkol check (ogrkol in ('sa�l�k','k�t�phane','�evre','trafik')))*/

/*alter table ogrenci add devamsizlik tinyint,
ogrkayittarih smalldatetime,
ogrborc tinyint*/

--alter table ogrenci add check (devamsizlik <=20)
--alter table ogrenci alter column ogradres varchar(160)

--alter table ogrenci drop column ogrborc (ogrborc s�tunun siler)
--truncate table ogrenci (i�indeki verileri siler)
--drop table ogrenci tabloyu komple siler