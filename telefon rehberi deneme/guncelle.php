<?php 

$baglan=mysqli_connect("localhost","root","","veridb");
mysqli_set_charset($baglan,"utf-8");

$id=$_POST["id"];
$adi=$_POST["gad"];
$soyadi=$_POST["gsoyad"];
$telefon=$_POST["gtel"];

$sqlekle = ("UPDATE tblveri SET Ad=$adi, Soyad=$soyadi, Telefon=$telefon WHERE RehberID=$id ");


	echo "Veriler Başarıyla Güncellendi";
	header("refresh:5;url=sayfa.php");


?>