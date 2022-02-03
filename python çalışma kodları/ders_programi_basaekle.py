dosya = open("ders_programi.txt","r+")
data = dosya.read()
dosya.seek(0)
data = "Python Programlama: 2 Ders 3,5 Saat\n" + data
dosya.write(data)
