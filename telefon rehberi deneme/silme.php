<?php 

$baglan=mysqli_connect("localhost","root","","veridb");
mysqli_set_charset($baglan,"utf-8");


$id=$_POST["id"];

$sqlekle =$baglan -> query("DELETE from tblveri WHERE RehberID = $id");
$sonuc=mysqli_query($baglan,$sqlekle);

echo "İşlem Başarı İle Gerçekleşti.. 2 saniye içinde Anasayfaya yönlendirileceksiniz.";
header("refresh:2;url=sayfa.php");

?>