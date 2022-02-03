'''dosyaların sonuna başına ve ortasına ekleme yapmak:a modunu kullanırız '''
with open("dosyada okuma.txt","r+") as dosya:
    data = dosya.readlines()#listelerde olan bir özelliği kullanacağımız için dosyayı liste yapıyoruz
    data.insert(1,"php : rasmus lerdorf\n")#sonra eklemek istediğimiz yeri ve şeyi yazıyoruz
    dosya.seek(0)#burda listenin elemanı arttğı için listeyi dosyaya tekrar yazdırmamız gerekiyor o yüzden başına gidiyoruz
    dosya.writelines(data)#ve listemizi dahil ediyoruz

    #dosya.seek(0)#en başa yazmak için yetmez o yüzden yazılı olan tüm veriyi alıp başa eklemek istediğimizle toplarız bunun için hem
    #1.yazma hemde okuma yapmamız gereklidir bunun içinde r+ modunu kullanırız
    #dosya.write("php : rasmus lerdorf")#otomatik olarak dosyanın en sonuna ekler
    #2.data = dosya.read()ilk adım olarak dosyayı okuyup bir değişkene atadık
    #3.dosya.seek(0)sonra dosyanın başına gittik
    #4.data = "php : rasmus lerdorf\n" + data sonra okuduğumuz değişkenin içine başına yazdırmak istediğimizi ve değişkeni topladık string
    #oldukları için toplanabiliyolar
    #5.dosya.write(data)son adım olarak da bunu yazdırdık

#listelerde insert fonksiyonu var indexi ve ne yazmak istediğinizi giriyorsunuz dosyalarda değişiklik yapmak için de bunu kullanıcaz
