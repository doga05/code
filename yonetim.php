<?php

include("ayarlar.php");
session_start();

if(!isset($_SESSION["giris"]))
{
	echo "Bu sayfayı görüntülemeye yetkiniz yoktur <br>";
	echo "<a href=ziyaretci.php> Giriş Sayfası </a>";
}
else
{
	echo "Admin Paneli <br>";
	echo "<a href=\"cikis.php\"> Çıkış Yap </a>";
}




?>