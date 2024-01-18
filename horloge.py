# Importation des bibliothèques nécessaires
import tkinter as tk
from time import strftime
from pygame import mixer
from customtkinter import *
import customtkinter as ctk
# Utilisation de la bibliothèque customtkinter
# pour styliser le format traditionnel de l'interphace graphique fournie par tkinter
# pour installer cette bibliothèque : pip install customtkinter

# Création de la fenêtre principale de l'application
fenetre = ctk.CTk()
fenetre.title('Horloge')

# Configuration de l'apparence de la fenêtre
fenetre.configure(fg_color="black")
fenetre.resizable(False, False)
set_default_color_theme("blue")

# Initialisation des variables pour contrôler l'état du programme
heure_actuelle = tk.StringVar()
format_24h = tk.BooleanVar()
pause = tk.BooleanVar()
heure_manuelle = tk.BooleanVar()

# Initialisation des variables pour stocker l'heure de l'alarme
alarme_heure = tk.StringVar()
alarme_minute = tk.StringVar()
alarme_seconde = tk.StringVar()

# Réglage des valeurs initiales des variables
format_24h.set(False)
pause.set(False)
heure_manuelle.set(False)

# Fonction pour basculer entre la saisie manuelle et automatique de l'heure
def changement_heure():
    heure_manuelle.set(not heure_manuelle.get())

    if heure_manuelle.get():
        update_manual_time(int(heure_entry.get()), int(minutes_entry.get()), int(secondes_entry.get()))
    else:
        update_time()

# Fonction pour mettre à jour l'heure manuellement
def update_manual_time(heure_value, minutes_value, secondes_value):
    if heure_manuelle.get():
        secondes_value = (secondes_value + 1) % 60

        if secondes_value == 0:
            minutes_value = (minutes_value + 1) % 60

            if minutes_value == 0:
                heure_value = (heure_value + 1) % 24
            else:
                heure_value = heure_value

        new_time = f'{heure_value:02d}:{minutes_value:02d}:{secondes_value:02d}'
        label.configure(text=new_time + " ")
        heure_actuelle.set(new_time)
        fenetre.after(1000, update_manual_time, heure_value, minutes_value, secondes_value)

# Fonction pour mettre à jour l'heure automatiquement
def update_time():
    if not pause.get():
        if heure_manuelle.get():
            update_manual_time()
        else:
            if format_24h.get():
                current_time = strftime("%H:%M:%S")
            else:
                current_time = strftime("%I:%M:%S %p")

            label.configure(text=current_time + " ")
            heure_actuelle.set(current_time)

            # Vérification correspondance avec l'heure de l'alarme
            if current_time == "{}:{}:{}".format(alarme_heure.get(), alarme_minute.get(), alarme_seconde.get()):
                jouer_sonnerie()

        fenetre.after(1000, update_time)

# Fonction pour jouer le son de l'alarme
def jouer_sonnerie():
    mixer.music.load("iphone_alarm.mp3")
    mixer.music.play()

# Fonction pour arrêter le son de l'alarme
def arreter_sonnerie():
    mixer.music.stop()

# Fonction pour programmer l'heure de l'alarme
def programmer_alarme():
    alarme_heure.set(alarmh_entry.get())
    alarme_minute.set(alarmm_entry.get())
    alarme_seconde.set(alarms_entry.get())

# Fonction pour mettre en pause/reprendre les mises à jour de l'heure
def pause_alarm():
    pause.set(not pause.get())
    if not pause.get():
        update_time()

# Fonction pour basculer entre le format horaire 12 heures et 24 heures
def basculer_format():
    format_24h.set(not format_24h.get())
    update_time()

# Création des composants graphiques

# Étiquettes et champs d'entrée pour la saisie manuelle de l'heure
heure_label = ctk.CTkLabel(fenetre, font=("bahnschrift", 20), text_color="white", text="Heures/Minutes/Secondes suivant le Format 24h :")
heure_label.grid(row=0, column=1, sticky=tk.W)

heure_entry = ctk.CTkEntry(fenetre, font=("bahnschrift", 22), width=62, height=48, border_width=0, corner_radius=18)
heure_entry.grid(row=0, column=2, padx=2 ,pady=2)

minutes_entry = ctk.CTkEntry(fenetre, font=("bahnschrift", 22), width=62, height=48, border_width=0, corner_radius=18)
minutes_entry.grid(row=0, column=3,  padx=2 ,pady=2)

secondes_entry = ctk.CTkEntry(fenetre,font=("bahnschrift", 22), width=62, height=48, border_width=0, corner_radius=18)
secondes_entry.grid(row=0, column=4,  padx=2 ,pady=2)

# Étiquettes et champs d'entrée pour la saisie de l'heure de l'alarme
alarmh_label = ctk.CTkLabel(fenetre,  font=("bahnschrift", 20),text_color="white",text="Heure/Minute/Seconde Alarme suivant le Format 24h :")
alarmh_label.grid(row=2, column=1 ,sticky=tk.W)

alarmh_entry = ctk.CTkEntry(fenetre, font=("bahnschrift", 22), width=62, height=48, border_width=0, corner_radius=18)
alarmh_entry.grid(row=2, column=2,  padx=2,pady=2)

alarmm_entry = ctk.CTkEntry(fenetre, font=("bahnschrift", 22), width=62, height=48, border_width=0, corner_radius=18)
alarmm_entry.grid(row=2, column=3,  padx=2 ,pady=2)

alarms_entry = ctk.CTkEntry(fenetre, font=("bahnschrift", 22), width=62, height=48, border_width=0, corner_radius=18)
alarms_entry.grid(row=2, column=4,  padx=2,pady=2)

# Bouton pour définir l'heure de l'alarme
programmer_bouton = ctk.CTkButton(fenetre, font=("bahnschrift", 15), width=180, height=48, fg_color="white", text_color="black",text="Programmer l'alarme", command=programmer_alarme)
programmer_bouton.grid(row=2, column=5, padx=2 ,pady=2)

# Bouton pour arrêter le son de l'alarme
arreter_bouton = ctk.CTkButton(fenetre, font=("bahnschrift", 15), width=180, height=48,fg_color="white", text_color="black",text="Arrêter la sonnerie", command=arreter_sonnerie)
arreter_bouton.grid(row=2, column=6, padx=2 ,pady=2)

# Boutons pour contrôler les mises à jour de l'heure
regler_bouton = ctk.CTkButton(fenetre, font=("bahnschrift", 15), width=180, height=48, fg_color="white", text_color="black",text="Régler l'heure", command=changement_heure)
regler_bouton.grid(row=0, column=5, padx=2 ,pady=2)

regler_bouton = ctk.CTkButton(fenetre, font=("bahnschrift", 15), width=180, height=48, fg_color="white", text_color="black",text="Revenir à l'heure", command=changement_heure)
regler_bouton.grid(row=0, column=6, padx=2 ,pady=2)

# Bouton pour basculer entre le format horaire 12 heures et 24 heures
format_bouton = ctk.CTkButton(fenetre, font=("bahnschrift", 15), width=180, height=48,fg_color="white", text_color="black",text="Basculer Format", command=basculer_format)
format_bouton.grid(row=4, column=5, padx=2 ,pady=2)

# Bouton pour mettre en pause/reprendre les mises à jour de l'heure
pause_bouton = ctk.CTkButton(fenetre, font=("bahnschrift", 15),width=180, height=48,fg_color="white",text_color="black",text="Pause", command=pause_alarm)
pause_bouton.grid(row=4, column=6, padx=2 ,pady=2)

# Étiquette pour afficher l'heure actuelle
label = ctk.CTkLabel(fenetre, font=("bahnschrift", 70), width=500, fg_color="black", text_color="white")
label.grid(row=9, column=0, columnspan=2)

# Initialisation et démarrage de la bibliothèque pour la lecture du son
mixer.init()
update_time()

# Lancement de la boucle principale pour l'interface graphique
fenetre.mainloop()
