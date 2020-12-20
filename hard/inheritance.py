class Hewan():
    nama = "default hewan"
    makan = "daging"
    isCarnivora = True

    def cetak(self):
        print(self.nama, self.makan, self.isCarnivora)



# class turunan Hewan
class Kucing(Hewan):
    def cetak(self):
       super.cetak()
       print("meong")



persia = Kucing()
persia.cetak()
    