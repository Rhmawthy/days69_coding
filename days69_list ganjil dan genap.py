#program menmbuat inputan list dengan 2 variabel berbeda antara angka ganjil dan angka genap

ganjil = [ ]
genap = [ ]

while True :
    angka = int(input("masukkan angka : "))

    if angka %2 == 0:
        print("*" *60)
        genap.append(angka)
        print("ini adalah list angka genap \n",genap)
        
    elif angka %2 != 0:
        print("*" *60)
        ganjil.append(angka)
        print ("ini adalah list angka ganjil\n",ganjil)

        
                
