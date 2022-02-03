'''liste = ["Alg", "uzmanı",3,5,True]

for i in range(len(liste)):
    print(liste[i])'''
    
başlangıç = input("Başlangıç sayısını girin: ")
bitiş = input("Bitiş sayısını girin: ")

for i in range (int(başlangıç), int(bitiş)+1):
    if i % 2 == 0:
        print("{} sayısı çift sayıdır".format(i))
    else:
        print("{} sayısı tek sayıdır".format(i))

