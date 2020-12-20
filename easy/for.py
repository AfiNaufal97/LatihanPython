# loping hampir mirip seperti di kotlin
a = [1, 2, 3, 4, 5]
for i in a:
    print(i)

# nested for
# for dalam for
namaBuah = ["Apel", "Rambutan", "Mangga", "Anggur", "Strowberry"]
gorengan  = ["tempe", "tahu", "pisang"]
sayur     = ["kangkung", "bayam", "wortel"]
keranjang = [namaBuah, gorengan, sayur]

for item in keranjang:
    print(item)
    for nama in item :
        print(nama)
