# type data dictionary
# key dan value {key:value}
Negara = {"Indonesia":"Jakarta", "Jepang":"Tokyo", "Korea Selatan":"Soul"}
Negara2 = {"Indonesia":"Jakarta", "Jepang":"Tokyo", "Korea Selatan":"Soul"}
print(Negara["Indonesia"])

# mencetak semua keys
print(Negara.keys())
print(Negara.items())

dataNegara = {1:Negara2, 2:Negara}
print(dataNegara[1])