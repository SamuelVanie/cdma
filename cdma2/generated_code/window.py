from tkinter import *
from tkinter import messagebox
from CDMA_FUNCTIONS import *


window = Tk()

def btn_clicked():
    print("btn cliked")
    return

# Declaration des fonctions
def generer_chips():
    # Genere les chips et les insèrent dans les champs
    global entry0
    global entry1
    global entry2
    global entry3

    chips = Generer_code()

    # Ecriture dans le champs 1
    entry0.delete(0, END)
    entry0.insert(0, chips[0])

    # Ecriture dans le champs 2
    entry1.delete(0, END)
    entry1.insert(0, chips[1])

    # Ecriture dans le champs 3
    entry2.delete(0, END)
    entry2.insert(0, chips[2])

    # Ecriture dans le champs 4
    entry3.delete(0, END)
    entry3.insert(0, chips[3])

    return

def join():

    global entry0
    global entry1
    global entry2
    global entry3

    global entry4
    global entry5
    global entry6
    global entry7


    global entry8
    global entry9
    global entry10
    global entry11

    chips = [entry0.get(), entry1.get(), entry2.get(), entry3.get()]
    mess = [entry4.get(), entry13.get(), entry14.get(), entry15.get()]

    message = Calcul(chips, mess)
    
    # Ecriture dans le champs 1
    entry5.delete(0, END)
    entry5.insert(0, message[0])

    # Ecriture dans le champs 2
    entry10.delete(0, END)
    entry10.insert(0, message[1])

    # Ecriture dans le champs 3
    entry11.delete(0, END)
    entry11.insert(0, message[2])

    # Ecriture dans le champs 4
    entry12.delete(0, END)
    entry12.insert(0, message[3])

    return

def transmit():
    global entry5
    global entry10
    global entry11
    global entry12

    global entry6
    global entry7
    global entry8
    global entry9

    entry6.delete(0, END)
    entry6.insert(0, entry5.get())

    entry7.delete(0, END)
    entry7.insert(0, entry10.get())

    entry8.delete(0, END)
    entry8.insert(0, entry11.get())

    entry9.delete(0, END)
    entry9.insert(0, entry12.get())

    return

def decode():
    global entry0
    global entry1
    global entry2
    global entry3

    global entry6
    global entry7
    global entry8
    global entry9

    chips = [entry0.get(), entry1.get(), entry2.get(), entry3.get()]
    messCrypt = [entry6.get(), entry7.get(), entry8.get(), entry9.get()]

    result = Decoder(messCrypt, chips)

    entry6.delete(0, END)
    entry6.insert(0, result[0])

    entry7.delete(0, END)
    entry7.insert(0, result[1])

    entry8.delete(0, END)
    entry8.insert(0, result[2])

    entry9.delete(0, END)
    entry9.insert(0, result[3])

    return


window.geometry("1000x600")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

# Fenetre pop-up d'aide
messagebox.showinfo("Welcome", """
Les emetteurs envoient des messages, les messages sont cryptés à l'aide des séquences de chips qui
peuvent être générées et envoyés aux recepteurs. Ceux-ci à leur tour peuvent décoder les messages
à l'aide des codes de chips 
""")

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    499.5, 285.0,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    120.5, 286.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry0.place(
    x = 73.0, y = 269,
    width = 95.0,
    height = 32)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    120.5, 344.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry1.place(
    x = 73.0, y = 327,
    width = 95.0,
    height = 32)

entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvas.create_image(
    120.5, 403.0,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry2.place(
    x = 73.0, y = 386,
    width = 95.0,
    height = 32)

entry3_img = PhotoImage(file = f"img_textBox3.png")
entry3_bg = canvas.create_image(
    120.5, 461.0,
    image = entry3_img)

entry3 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry3.place(
    x = 73.0, y = 444,
    width = 95.0,
    height = 32)

entry4_img = PhotoImage(file = f"img_textBox4.png")
entry4_bg = canvas.create_image(
    243.5, 286.0,
    image = entry4_img)

entry4 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry4.place(
    x = 196.0, y = 269,
    width = 95.0,
    height = 32)

entry5_img = PhotoImage(file = f"img_textBox5.png")
entry5_bg = canvas.create_image(
    499.5, 277.5,
    image = entry5_img)

entry5 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry5.place(
    x = 400.0, y = 260,
    width = 199.0,
    height = 33)

entry6_img = PhotoImage(file = f"img_textBox6.png")
entry6_bg = canvas.create_image(
    817.5, 269.5,
    image = entry6_img)

entry6 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry6.place(
    x = 718.0, y = 252,
    width = 199.0,
    height = 33)

entry7_img = PhotoImage(file = f"img_textBox7.png")
entry7_bg = canvas.create_image(
    817.5, 330.5,
    image = entry7_img)

entry7 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry7.place(
    x = 718.0, y = 313,
    width = 199.0,
    height = 33)

entry8_img = PhotoImage(file = f"img_textBox8.png")
entry8_bg = canvas.create_image(
    817.5, 391.5,
    image = entry8_img)

entry8 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry8.place(
    x = 718.0, y = 374,
    width = 199.0,
    height = 33)

entry9_img = PhotoImage(file = f"img_textBox9.png")
entry9_bg = canvas.create_image(
    817.5, 452.5,
    image = entry9_img)

entry9 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry9.place(
    x = 718.0, y = 435,
    width = 199.0,
    height = 33)

entry10_img = PhotoImage(file = f"img_textBox10.png")
entry10_bg = canvas.create_image(
    499.5, 338.5,
    image = entry10_img)

entry10 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry10.place(
    x = 400.0, y = 321,
    width = 199.0,
    height = 33)

entry11_img = PhotoImage(file = f"img_textBox11.png")
entry11_bg = canvas.create_image(
    499.5, 399.5,
    image = entry11_img)

entry11 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry11.place(
    x = 400.0, y = 382,
    width = 199.0,
    height = 33)

entry12_img = PhotoImage(file = f"img_textBox12.png")
entry12_bg = canvas.create_image(
    499.5, 460.5,
    image = entry12_img)

entry12 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry12.place(
    x = 400.0, y = 443,
    width = 199.0,
    height = 33)

entry13_img = PhotoImage(file = f"img_textBox13.png")
entry13_bg = canvas.create_image(
    243.5, 344.0,
    image = entry13_img)

entry13 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry13.place(
    x = 196.0, y = 327,
    width = 95.0,
    height = 32)

entry14_img = PhotoImage(file = f"img_textBox14.png")
entry14_bg = canvas.create_image(
    243.5, 403.0,
    image = entry14_img)

entry14 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry14.place(
    x = 196.0, y = 386,
    width = 95.0,
    height = 32)

entry15_img = PhotoImage(file = f"img_textBox15.png")
entry15_bg = canvas.create_image(
    243.5, 461.0,
    image = entry15_img)

entry15 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry15.place(
    x = 196.0, y = 444,
    width = 95.0,
    height = 32)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:generer_chips(),
    relief = "flat")

b0.place(
    x = 145, y = 496,
    width = 72,
    height = 21)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:join(),
    relief = "flat")

b1.place(
    x = 225, y = 495,
    width = 75,
    height = 23)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:transmit(),
    relief = "flat")

b2.place(
    x = 536, y = 492,
    width = 72,
    height = 22)

img3 = PhotoImage(file = f"img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:decode(),
    relief = "flat")

b3.place(
    x = 853, y = 491,
    width = 73,
    height = 23)

window.resizable(False, False)
window.mainloop()
