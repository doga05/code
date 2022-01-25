<?php

include("ayarlar.php");
session_start();

if(($_POST["kadi"]==$kullanici) and ($_POST["parola"]==$parola))
{
	$_SESSION["giris"]=true;
	$_SESSION["kullanici"]=$kullanici;
	$_SESSION["parola"]=$parola;
	
	header("Location:yonetim.php");
}
else {
	echo "Kullanıcı adı veya Şifre yanlış <br>";
	echo "<a href=ziyaretci.php> Geri Dön</a>";
}





?>