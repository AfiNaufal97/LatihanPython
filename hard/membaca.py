import os

place = os.getcwd()

baca = open(place+"/hard/text.txt", "r")

# cetak hanya 4 karakter dari isi yang ada dalam text.txt
# print(baca.read(4))

# membaca 1 baris
print(baca.readline())