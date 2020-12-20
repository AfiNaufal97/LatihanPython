# menentukan scope global dan lokal

nama = "Saya"

# local
def tambahNama(namaBaru):
    nama = namaBaru
    print(nama)


# eksekusi function
tambahNama(" Keren")
print(nama)

# global
def ubahNama(namaBaru):
    global nama
    nama = namaBaru
    print(nama)


ubahNama("keren")
print(nama)