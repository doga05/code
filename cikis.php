<?php

session_start();
session_destroy();//açılmış olan oturum bilgilerinin tümünü silmek için

echo "Çıkış işlemi tamamlandı.";
echo "<br> <a href=ziyaretci.php> Anasayfa</a>";


?>