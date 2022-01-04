# Simulation du principe du CDMA

import sys

if sys.version_info >= (3,):
    import tkinter as tk
    from tkinter import messagebox
else:
    import Tkinter as tk
    import tkMessageBox


# Fenetre principale
root = tk.Tk()
#taille de la fenetre

# Fenetre pop-up d'aide
messagebox.showinfo("Welcome in CDMA SIMULATION", """
       Bienvenue dans notre application de simulation du fonctionnement de l'algorithme CDMA


        1. EMETTEURS

        Au niveau de cette partie de l'interface, vous pouvez:
            - Générer les chips qui vont servir à la création du message codé
            - Ecrire les messages à transmettre(bits)

        2. MESSAGES

        Ici, vous pouvez voir les messages qui seront transmis aux recepteurs

        3. RECEPTEURS

        Les recepteurs reçoivent les messages qui peuvent être ensuite décodé
        """)

# Cote gauche
emetteur = tk.Label(text="EMETTEURS", font=("", 14))
emetteur.grid(row=1, column=0)
# Configuration des dimensions du rectangle gauche
boxGauche = tk.Frame(
        root, 
        relief="flat"
        )
# Placer la grille juste apres le texte dans la grille root
boxGauche.grid(row=2, column=0, padx=20, sticky="E")
for i in range(4):
    tk.Label(master=boxGauche, text=f"Chips {i+1}: ").grid(row=i, column=0, sticky="E")
    tk.Entry(master=boxGauche).grid(row=i, column=1, sticky="E")
    tk.Label(master=boxGauche, text="   ").grid(row=i, column=2)
    tk.Label(master=boxGauche, text=f"Bit à transmettre {i+1}: ").grid(row=i, column=3, sticky="E")
    tk.Entry(master=boxGauche).grid(row=i, column=4, ipadx=12, sticky="E")
# Placer le bouton dans la derniere colonne, et dernière ligne occupées
tk.Button(master=boxGauche, justify="left", text="Générer chips", name="generateChipsBtn").grid(row=5, column=4, sticky="W")
tk.Button(master=boxGauche, justify="left", text="Joindre", name="joinChipsBitsBtn").grid(row=5, column=4, sticky="E")


# Centre
# mettre un espace pour séparer les messages sur la première colonne root
tk.Label(text="     ").grid(row=1, column=1)
message = tk.Label(text="MESSAGES", font=("", 14)).grid(row=1, column=2)
boxCentre = tk.Frame(
        root,
        relief="flat"
        )
boxCentre.grid(row=2, column=2, padx=20, sticky="E")
#Remplissage de la boxCentre
for i in range(4):
    tk.Label(master=boxCentre, text=f"Message {i+1}: ").grid(row=i, column=0)
    tk.Entry(master=boxCentre).grid(row=i, column=1)
# Ajout des boutons
tk.Button(master=boxCentre, justify="left", text="Envoyer", name="sendMessageBtn").grid(row=5, column=1, sticky="E")


# Cote droit
# Mettre un espace pour séparer les messages sur la première colonne root
tk.Label(text="      ").grid(row=1, column=3)
reception = tk.Label(text="RECEPTEURS", font=("", 14)).grid(row=1, column=4)
boxDroit = tk.Frame(
        root,
        relief="flat"
        )
# 
boxDroit.grid(row=2, column=4, padx=20, sticky="E")
for i in range(4):
    tk.Label(master=boxDroit, text=f"Message {i+1}: ").grid(row=i, column=0)
    tk.Entry(master=boxDroit).grid(row=i, column=1)
# Ajout des boutons
tk.Button(master=boxDroit, justify="left", text="Decoder", name="decodeMessageBtn").grid(row=5, column=1, sticky="E")

# boucle principale
root.mainloop()
