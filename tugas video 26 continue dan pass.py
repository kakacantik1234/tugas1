#tugas video 26 continue dan pass

#pass --> dia berfungsi sebagai dummy, tidak akan dieksekusi 

angka = 0 

while angka < 5:

    angka += 1 
    if angka == 3: 
        print("whadaaap!")
        
    print(angka)

#penerapan dengan pass
angka = 0 

while angka < 5:

    angka += 1 
    if angka == 3: 
        pass #ini tidak akan dieksekusi 

    print(angka)

#continue

angka = 0 

print(f"angka sekarang --> {angka}")

while angka < 5:
    angka += 1 
    print(f"angka sekarang --> {angka}")

    if angka == 3:
        print("nice!")

    print("whassup")

print("Pinish!")

#jika dimasukkan continue
angka = 0 

print(f"angka sekarang --> {angka}")

while angka < 5:
    angka += 1 
    print(f"angka sekarang --> {angka}")  #aksi 1

    if angka == 3:
        print("nice!")
        continue #akan membuat loop meloncat ke step selanjutnya 
    print("whassup") #aksi 2

print("Pinish!")