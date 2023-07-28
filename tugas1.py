# variabel  adalah tempat menyimpan data 

a = 10 
x = 5
panjang = 1000

print("Nilai a = ", a)
print("Nilai x = ", x)
print("Nilai panjang = ", panjang)

#penamaan 
nilai_y = 15  #dengan menggunakan underscore 
juta10 = 10000000 #ini boleh 
nilaiZ = 17.5 #ini boleh 

#pemanggilan kedua 
print("Nilai a = ", a)
a = 7 
print("Nilai a = ", a)

#assignment indirect
b = a 
print("Nilai b = ", b)

# a = 10, a adalah variabel dengan nilai 10 

# tipe data:Angka satuan (integer)
data_integer = 11 
print(type(data_integer))
print("data: ", data_integer)
print("- bertipe: ", type(data_integer))

#tipe data: angka dengan koma (float)

data_float = 1.5
print("data: ", data_float)
print("- bertipe: ", type(data_float))

#tipe data: kumpulan karakter (string)

data_string = "ucup"
print("data: ", data_string)
print("- bertipe: ", type(data_string))

#tipe data: biner true/false (boolean)

data_bool = False 
print("data: ", data_bool)
print("- bertipe: ", type(data_bool))

##tipe data khusus

#bilangan kompleks
data_complex = complex(5,6) 
print("data: ", data_complex)
print("- bertipe: ", type(data_complex))

#tipe data dari bahasa C 

from ctypes import c_double

data_c_double = c_double(10.5)
print("data: ", data_c_double)
print("- bertipe: ", type(data_c_double))
