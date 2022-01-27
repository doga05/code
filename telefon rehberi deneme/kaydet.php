<?php 

$baglan=mysqli_connect("localhost","root","","veridb");
mysqli_set_charset($baglan,"utf-8");


$adi=$_POST["ad"];
$soyadi=$_POST["soyad"];
$telefon=$_POST["tel"];


$sqlekle = ("INSERT INTO tblveri(Ad, Soyad, Telefon) VALUES ($adi, $soyadi, $telefon)");
$sonuc=mysqli_query($baglan,$sqlekle);

if($sonuc==0){
	echo "İşlem gerçekleştirilemedi";
}
else{
	echo "Veriler Başarıyla Kaydedildi";
	header("refresh:5;url=sayfa.php");
}



?>