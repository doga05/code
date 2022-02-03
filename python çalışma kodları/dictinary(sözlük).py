'''tuple'a benzer.Gerçek sözlük gibidir. anahtar sözcük vardır ve bir değeri de vardır.Her anahtar elemanın bir değeri vardır.
sözlük={"python":"güzel bir dil","php":"script dili","java":compile edilen dil"} 
print(sözlük["python"]) bu şekilde kullanılır

for i in sözlük.items():
    print(i) yazarsak sözlüğün içindeki her değere ulaşırız.
    
for i in sözlük.items():
    print(i[0] + " " + i[1]) diğeri tuple şeklinde çıktı veriyordu bu ise normal çıktı verir.
for i,j in sözlük.items():
    print(i + " " +j) de farklı bir yazım'''

dersler={"Doğa":["Yapay zeka","Kriptografi"],"Nur":["web tasatım","kriptografi"],"Hazal":["Lineer cebir"]}
isim= input("isim girin: ")
print("{} in aldığı dersler:".format(isim))

for i in (dersler[isim]):
    print(i)

