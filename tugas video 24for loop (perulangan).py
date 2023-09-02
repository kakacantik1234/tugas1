#for loop (perulangan)

# angka = 1 
# print(angka)
# angka = angka + 1 
# print(angka)
# angka = angka + 1 
# print(angka)

from tkinter.simpledialog import askstring


# for kondisi:
#     aksi

#ini dengan list
angka2 = [0,1,2,3,4] #ini adalah list 
print(angka2)

for i in angka2:
    print(f"i sekarang --> {i}")

print("akhir dari program 1a")

angka3 = [0,5,12,43,48]
print(angka3)

for i in angka3:
    print(f"i sekarang --> {i}")

print("akhir dari program 1b")

# ini dengan range 
angka2_range = range(5)

for i in angka2_range:
    print(f"i sekarang --> {i}")

print("akhir dari program 2")

angka2_range = range(1,15)

for i in angka2_range:
    print(f"i sekarang --> {i}")

print("akhir dari program 3")

#menggunakan string 
data_str = "saya ganteng abiees"

for huruf in data_str:
    print(huruf)

print("akhir dari program 4 \n")

for i in angka2:
    print("saya keren")


