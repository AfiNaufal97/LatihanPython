# import tkinter

# hallo = tkinter.Tk()

# def salam():
#     label = tkinter.Label(hallo, text="Assalamualaikum.....")
#     label.pack()


# judul = tkinter.Label(hallo, text="Judul")
# button = tkinter.Button(hallo, text="Saya di tekan", command=salam)

# judul.pack()
# button.pack()
# hallo.mainloop()


import tkinter
# buat nama jendela
hallo = tkinter.Tk()

def sapa():
    label2 = tkinter.Label(hallo, text="assalamualaikum")
    label2.pack()

# buat label
judul = tkinter.Label(hallo, text="Ini Tampilan GUI")
button = tkinter.Button(hallo, text="tekan saya", command= sapa)

# tampilkan jendela
judul.pack()
button.pack()
hallo.mainloop()
