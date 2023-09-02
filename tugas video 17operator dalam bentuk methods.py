# operator dalam bentuk methods

## merubah case dari string 

# merubah semua ke upper case 

salam = "bro!"
print("normal = " + salam)
salam = salam.upper()
print("normal = " + salam)

# merubah semua ke lower case 
alay = "aKu KeCe AbieezZzZZZZ"
print("normal = " + alay)
alay = alay.lower()
print("lower = " + alay)

## pengecekan dengan isX method 

# contoh pengecekan lower case 
salam = "sist"
apakah_lower = salam.islower() #hasilnya bool
print(salam + " is lower = " + str(apakah_lower))
apakah_upper = salam.isupper() #hasilnya bool 
print(salam + " is upper = " + str(apakah_upper))

# isalpha() <-- untuk mengecek semuanya huruf 
# isalnum() <-- huruf dan angka 
# isdecimal() <-- angka saja 
# isspace() <-- spasi, tab, newline \n
# istitle() <-- semua kata dimulai dengan huruf besar 

judul = "It Is Okay Not To Be Orkay" #tidak boleh ada ' di it's atau ada huruf kecil di depan--nanti jadi false"
cek_judul = judul.istitle() #hasil bool 

print(judul + " is title = " + str(cek_judul))

## ngecek komponen startswith() endswith() <-- keren
cek_start = "Sangjangnim Oppa".startswith("Sangjangnim")
print("start = " + str(cek_start))

cek_end = "Sangjangnim Oppak".endswith("Oppak")
print("end = " + str(cek_end))

## penggabungan komponen join () split ()
pisah = ['aku','sayang','kamu']
gabungan = ','.join(pisah)
print(pisah)
print(gabungan)

gabungan = ' '.join(pisah)
print(gabungan)

gabungan = ' ehm '.join(pisah)
print(gabungan)

gabungan = "akuehmsayangehmkamu"
print(gabungan.split('ehm'))

# alokasi karakter rjust(), ljust() center()
print(5*"="+"data"+"="*5)
print(5*"="+"lovely"+"="*5)

kanan = "surotong".rjust(10)
print("'"+kanan+"'")

kiri = "surotong".ljust(10)
print("'"+kiri+"'")

tengah = "surotong".center(10)
print("'"+tengah+"'")

tengah = "surotong".center(20,":")
print("'"+tengah+"'")

#kebalikannya --> strip()
tengah = tengah.strip(":") #menghilangkan tanda :
print("'"+tengah+"'")  