'''dosyayı değiştirmek içinden bilgiler okumak yazmak gibi şeyler. Dosya açmak için open fonksiyonu kullanılır ve bir değişkene atanır
sonra dosya ismi ve dosyaya ne yapıcağını söyleyen modu yazarız write modu dosyayı açmamızı ve içine bişeyler yazmamızı sağlar.
dosya bulunduğumuz dizinde varsa eski olan dosyayı siler ve yerine yeni bir dosya açar kullanırken dikkat etmek gerekir.
read moduv olan dosyayı açar ve okumamızı sağlar. son mod ise append modu bu mod olan dosyanın içindeki bilgileri değiştirmemizi
sağlar ve dosya yoksa yeni dosya açarak dosyaya bişeyler yazmamızı sağlar'''

#dosya = open("dosyadeneme.txt","w")# aynısını farklı bir yere açmak için C:/Users/user/Desktop/dosyadeneme.txt olarak yapabiliriz
dosya= open("dosyadeneme.txt","a") # yanına bişey eklemek için append yani a modu
#dosya.write("oha yaptim amk ohaaaa")#dosya içine yazmak için
dosya.write(" yanina ekleme yapmak icin modu degistirir a yapariz")#düzeltmelerde eskisini silmez yanına yenisini yazar 