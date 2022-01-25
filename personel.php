<html>
<?php

$baglan=mysqli_connect("localhost","root","","personeldb");//fonksiyon yaratıp bağladık
mysqli_set_charset($baglan,"utf-8");
?>
<head> <meta charset="utf-8"> </head>
<body>

<form action="personelkaydet.php" method="Post">
<table border="5" align="center">

<tr> <td colspan="2"> <h2> PERSONEL KAYIT </h2> </td></tr>
<tr><td> Adı:</td> <td><input type="text" name="ADI"></td></tr>
<tr><td> Soyadı:</td> <td><input type="text" name="SOYADI"></td></tr>
<tr><td></td> <td> <input type="submit" name="kaydet" value="KAYDET"> </td></tr>
</table>
</form>

</body>
</html>