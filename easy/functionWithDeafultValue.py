# function konventional
def id(nama, nim, kelas):
    return ("nama : {}\nnim: {}\nkelas : {}".format(nama, nim, kelas))

# fungsi dengna nilai default
def id2(nama="Afi", nim=1, kelas="5A"):
    return ("nama : {}\nnim: {}\nkelas : {}".format(nama, nim, kelas))

print(id("afi", 2009, "5A"))
print(id2())

# mencetak function dengan nama parameter
print(id2(nim=20092001, nama = "Saya", kelas="5A"))