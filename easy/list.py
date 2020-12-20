# list atau array di python
a = ["a", 1, 3.5, True, 'A']
print(a)

# list bisa diakses dengan slicing []
print(a[1])

# slicing dengan :
# mencetak item dalam list mulai dari index ke 0 sampai ke 4(4 tidak masuk kerena hanya sebagai batas)
print(a[0:4])

# print semuanya
print(a[:])

# print semuanya tetapi dimulai dari index -1/ belakang ke depan
print(a[::-1])

# menambhakan data dalam item list dengan 
a.append("good")
print(a)

# extend menambahkan denganmemmecah
a.extend("hallo")
print(a)

# insert menambahkan dengan item ke urutan tertentu
a.insert(1, "Baik")
print(a)