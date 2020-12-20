a = ["satu", "Dua", "Tiga"]

for i in a:
    print(i)

# menambahkan nomer atau index pada for looping
b = 0
c = ["satu", "Dua", "Tiga"]
for i in c:
    print("Nilai index ke-{} dibaca {}".format(b+1, i))
    b+=1

# dengan enumerate
data = ["armada",
        "anji",
        "virgoun",
        "fiersa Besari",
        "mawar"]

no = 0
for index, item in enumerate(data):
    print("index ke {} = {}". format(index,item))

lagu = ["asal kau bahagia",
        "dia",
        "bukti",
        "celengan rindu",
        "lebih dari egoku"]

# mencetak pasangan list dengan zip
for penyannyi, lagu in zip(data, lagu):
    print("{} menyanyikan lagu {}". format(penyannyi, lagu))


# mencetak for dari data dictionari
pasangan = {"anji":"dia", "fiersa besari":"celnegn rindu", "mawar":"lebih dari egoku"}
for penyannyi, lagu in pasangan.items():
    print("{} menyanyikan lagu {}". format(penyannyi, lagu))


