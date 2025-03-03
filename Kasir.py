from tkinter import *
from tkinter import messagebox

windows = Tk()
windows.title("Mesin Kasir")
bg="#FF1493"
fg="#000000"

# Variable
pulpen= StringVar()
buku = StringVar()
spidol = StringVar()
penggaris = StringVar()
pensil = StringVar()
penghapus = StringVar()
tekstotal = StringVar()
teksapung = StringVar()
total = 0

# Function / Fungsi
def totalbeli():
    global pulpen,buku,spidol,penggaris,pensil,penghapus,tekstotal,total
    h_pulpen = int(pulpen.get()) * 4000
    h_buku = int(buku.get()) * 5000
    h_spidol = int(spidol.get()) * 8000
    h_penggaris = int(penggaris.get()) * 3000
    h_pensil = int(pensil.get()) * 2000
    h_penghapus = int(penghapus.get()) * 1000
    total = h_pulpen+h_buku+h_spidol+h_penggaris+h_pensil+h_penghapus
    tekstotal.set(str(total))

def kembalian():
    global total
    uang = int(teksapung.get())

    if uang >= total:
        kembalian = uang - total
        messagebox.showinfo(message="Kembalian mu sebesar :{}".format(str(kembalian)))
    else:
        messagebox.showerror(message="Uang mu kurang")

def clear():
    pulpen.set("0")
    buku.set("0")
    spidol.set("0")
    penggaris.set("0")
    pensil.set("0")
    penghapus.set("0")
    teksapung.set("0")
    tekstotal.set("0")

windows.geometry("600x600") #Ukuran
windows.resizable(False,False)
windows.configure(bg=bg) #Bground

# Label Title
Label(windows, text="KASIR TOKO BUKU",bg=bg,foreground=fg,font="arial 14 bold").place(x=200,y=30)

# Label menu
Label(windows,text="1. Ball Point",bg=bg,foreground=fg,font="arial 12 bold").place(x=50,y=70)
Label(windows,text="2. Buku",bg=bg,foreground=fg,font="arial 12 bold").place(x=50,y=100)
Label(windows,text="3. Spidol",bg=bg,foreground=fg,font="arial 12 bold").place(x=50,y=130)
Label(windows,text="4. Penggaris",bg=bg,foreground=fg,font="arial 12 bold").place(x=50,y=160)
Label(windows,text="5. Pensil",bg=bg,foreground=fg,font="arial 12 bold").place(x=50,y=190)
Label(windows,text="6. Penghapus",bg=bg,foreground=fg,font="arial 12 bold").place(x=50,y=220)

# Label Harga
Label(windows,text="Rp. 4000",bg=bg,foreground=fg,font="arial 12 bold").place(x=380,y=70)
Label(windows,text="Rp. 5000",bg=bg,foreground=fg,font="arial 12 bold").place(x=380,y=100)
Label(windows,text="Rp. 8000",bg=bg,foreground=fg,font="arial 12 bold").place(x=380,y=130)
Label(windows,text="Rp. 3000",bg=bg,foreground=fg,font="arial 12 bold").place(x=380,y=160)
Label(windows,text="Rp. 2000",bg=bg,foreground=fg,font="arial 12 bold").place(x=380,y=190)
Label(windows,text="Rp. 1000",bg=bg,foreground=fg,font="arial 12 bold").place(x=380,y=220)

# Spinbox
Spinbox(windows,from_=0, to=100, width=7,font="arial 10",textvariable=pulpen,command=totalbeli).place(x=530,y=70)
Spinbox(windows,from_=0,to=100,width=7,font="arial 10",textvariable=buku,command=totalbeli).place(x=530,y=100)
Spinbox(windows,from_=0,to=100,width=7,font="arial 10",textvariable=spidol,command=totalbeli).place(x=530,y=130)
Spinbox(windows,from_=0,to=100,width=7,font="arial 10",textvariable=penggaris,command=totalbeli).place(x=530,y=160)
Spinbox(windows,from_=0,to=100,width=7,font="arial 10",textvariable=penghapus,command=totalbeli).place(x=530,y=190)
Spinbox(windows,from_=0,to=100,width=7,font="arial 10",textvariable=pensil,command=totalbeli).place(x=530,y=220)

# Label Pembayaran
Label(windows,text="Masukkan Uang Anda",bg=bg,foreground=fg,font="arial 12").place(x=50,y=280)

# Entry Uang
Entry(windows,textvariable=teksapung).place(x=53,y=310)

# Label Total
Label(windows,text="Rp. ",bg=bg,foreground=fg,font="arial 12 bold").place(x=380,y=280)
Label(windows,textvariable=tekstotal,bg=bg,foreground=fg,font="arial 12 bold").place(x=410,y=280)

# Tombol / Button
Button(windows,text="Total",bg="#00FF00",foreground="white",font="arial 10",width=10,command=kembalian).place(x=100,y=400)
Button(windows,text="Clear",bg="#FF0000",foreground="white",font="arial 10",width=10,command=clear).place(x=380,y=400)

# Footer
Label(windows,text="Created By Sandy",bg=bg,foreground=fg,font="arial 12").place(x=200,y=500)
windows.mainloop() # Menampilkan App