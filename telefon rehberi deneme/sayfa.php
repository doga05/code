<html>
<head> <title> Telefon Rehberi </title> </head>
<body background="grey">
<header>
<center>
<p><i><h3> Telefon Rehberi </h3></i></p>
<a href=#listele> <u> Listele </u></a>&nbsp;
<a href=#kayitol> <u> Kayıt Ol </u></a>&nbsp;
<a href=#guncelle> <u> Güncelle </u></a>&nbsp;
<a href=#sil> <u> Sil </u></a>&nbsp;
</center>
</header>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>


<section>
<a name="listele">
<?php 

$baglan=mysqli_connect("localhost","root","","veridb");
mysqli_set_charset($baglan,"utf-8");


$sqlekle = $baglan ->prepare("SELECT * FROM tblveri");
$sqlekle -> execute();
$goster = $sqlekle -> get_result();

while($sonuc = $goster -> fetch_array()){
	echo "Ad: ".$sonuc["Ad"]."<br>";
	echo "Soyad: ".$sonuc["Soyad"]."<br>";
	echo "Telefon Numarası: ".$sonuc["Telefon"]."<br><br><br>";
}
?>
</a>
</section>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

<section>
<a name="kayitol">
<form action="kaydet.php" method="post">
<table border="2" align="center">
<tr><td colspan="2"><h2><b> Telefon Kayıt </b></h2></td></tr>
<tr><td>Adınız:</td><td><input type="text" name="ad"></td></tr>
<tr><td>Soyadınız:</td><td><input type="text" name="soyad"></td></tr>
<tr><td>Telefon Numarası:</td><td><input type="text" name="tel"></td></tr>
<tr><td></td><td><input type="submit" name="kaydet" value="Kaydet"></td></tr>
</table>
</form>
</a>
</section>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

<section>
<a name="guncelle">
<form action="guncelle.php" method="post">
<table border="2" align="center">
<tr><td colspan="2"><h2><b> Telefon Güncelleme </b></h2></td></tr>
<tr><td>Güncellenecek RehberID: </td><td><input type="text" name="id"/></td></tr>
<tr><td>Yeni Ad: </td><td><input type="text" name="gad"></td></tr>
<tr><td>Soyad: </td><td><input type="text" name="gsoyad"></td></tr>
<tr><td>Yeni Numara: </td><td><input type="text" name="gtel"></td></tr>
<tr><td></td><td><input type="submit" value="Güncelle"></td></tr>
</table>
</form>
</a>
</section>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

<section>
<a name="sil">
<form action="silme.php" method="post">
<table border="2" align="center">
<tr><td colspan="2"><h2><b> Telefon Silme </b></h2></td></tr>
<tr><td>Silinecek RehberID: </td><td><input type="text" name="id"/></td></tr>
<tr><td></td><td><input type="submit" value="Sil"></td></tr>
</table>
</form>
</a>
</section>

</body>
</html>