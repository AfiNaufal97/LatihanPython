class Mahasiswa3():
    nama = "nama default"
    nim = 123
    alamat = "Alamat default"

    # constructor
    def __init__(self, nama, nim, alamat):
        self.nama = nama
        self.nim = nim
        self.alamat = alamat

    def perkenalan(self):
        print("perkenalan nama saya adalah ", self.nama)


nama3 = Mahasiswa3("Afi", 12345, "Tegal")
nama3.perkenalan()