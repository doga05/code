<html>
<head> <meta charset="utf-8"> </head>
<body>
<?php

error_reporting(0);//hata varsa ekrana vermez

$baglan=mysqli_connect("localhost","root","","personeldb");//mysql serverinda yarattığımız veritabanına bağlanmak için kullanılan kod kalıbı
mysqli_set_charset($baglan,"utf-8");//girilen değerlerin türkçe karakter olması için


$adi=$_POST["ADI"];//personal.php sayfasından veri alma 
$soyadi=$_POST["SOYADI"];//personal.php veri alma

$sqlekle="INSERT INTO tblpersonel(ADI,SOYADI) VALUES ('$adi','$soyadi')";//sqlekle fonksiyonu yaratıldı db'de bulunan tabloya veri ekleme 
$sonuc=mysqli_query($baglan,$sqlekle);//baglan fonksiyonuyla sqlekle fonks çalışıyor mu diye kontrol eder

if($sonuc==0){//eğer çalışmıyorsa hata veriyor
	echo "<center> Bir hata oluştu, veriler gönderilemedi. </center>";
}
else{//çalışıyorsa ekliyor
	echo "<center> <img src='https://sanalajan.com/wp-content/uploads/2020/05/tik-isareti-nasil-yapilir.jpg' width='100'> </center>";
	echo "<center> Başarıyla kaydedildi </center>";
}

?>
</body>
</html>