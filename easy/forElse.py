# kombinasi for break dan else

a = 1
for a in range(1,10):
    if (a == 3 ):
        print("Stop")
        break
    print(a)
    a+=1


for i in range(0, 10):
    if i == 10:
        print("nilai ditemukan")
        break
    print("nilai ke ", i)
else:
    print("nilai tidak ditemukan")
