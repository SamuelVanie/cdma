# Simulation du principe du CDMA

import tkinter as tk
from tkinter import ttk


# Fenetre principale
root = tk.Tk()
#taille de la fenetre


# Cote gauche
emetteur = ttk.Label(text="EMETTEURS")
emetteur.grid(row=0, column=0)
# Configuration des dimensions du rectangle gauche
boxGauche = ttk.Frame(
        root, 
        padding=3,
        relief="flat"
        )
# Placer la grille juste apres le texte
boxGauche.grid(row=1, column=0)
for i in range(4):
    ttk.Label(master=boxGauche, text=f"Chips {i+1}: ").grid(row=i, column=0)
    ttk.Entry(master=boxGauche).grid(row=i, column=1)
    ttk.Label(master=boxGauche, text="      ").grid(row=i, column=2)
    ttk.Label(master=boxGauche, text="      ").grid(row=i, column=4)
    ttk.Label(master=boxGauche, text=f"Bit à transmettre {i+1}: ").grid(row=i, column=5)
    ttk.Entry(master=boxGauche).grid(row=i, column=6)
ttk.Label(master=boxGauche, text="      ").grid(row=4, columnspan=5)
tk.Button(master=boxGauche, justify="left", text="Générer chips", name="generateChips").pack()
tk.Button(master=boxGauche, justify="left", text="Joindre", name="joinChipsBits").pack()


# Centre
# Mettre un espace avant d'ecrire MESSAGES
ttk.Label(text="      ").grid(row=0, column=1)
message = ttk.Label(text="MESSAGES").grid(row=0, column=2)
boxCentre = ttk.Frame(
        root,
        padding=3,
        relief="flat"
        )
# Mettre un espace pour separer les box
ttk.Label(text="      ").grid(row=1, column=1)
boxCentre.grid(row=1, column=2)
#Remplissage de la boxCentre
for i in range(4):
    ttk.Label(master=boxCentre, text="     ")
    ttk.Label(master=boxCentre, text=f"Message {i+1}: ").grid(row=i, column=0)
    ttk.Entry(master=boxCentre).grid(row=i, column=1)


# Cote droit
# Mettre un espace avant d'ecrire RECEPTEURS
ttk.Label(text="      ").grid(row=0, column=3)
reception = ttk.Label(text="RECEPTEURS").grid(row=0, column=4)
boxDroit = ttk.Frame(
        root,
        padding=3,
        relief="flat"
        )
# Separer avant de mettre la box
ttk.Label(text="      ").grid(row=1, column=3)
boxDroit.grid(row=1, column=4)
for i in range(4):
    ttk.Label(master=boxDroit, text="     ")
    ttk.Label(master=boxDroit, text=f"Message {i+1}: ").grid(row=i, column=0)
    ttk.Entry(master=boxDroit).grid(row=i, column=1)

# boucle principale
root.mainloop()
