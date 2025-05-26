import tkinter 

cycle = 0

def lancer_cycle():
    global cycle
    if cycle < 4:
        affichage_etat.config(text="Travail en cours...")
        compte_rebours(100,  pause_apres_travail)
    else:
         affichage_etat.config(text="Pomodoro terminé !")
        
        
    
def pause_apres_travail():
    affichage_etat.config(text="Pause bien méritée..")
    global cycle
    cycle +=1
    compte_rebours(100, lancer_cycle)
    

def demarrer_pomodoro():
    lancer_cycle()
    

def compte_rebours(temps, callback=None):
    minutes = temps // 60
    secondes = temps % 60 
    texte = f"temps restant : {minutes:02}:{secondes:02}"
    affichage.config(text=texte)
    if temps > 0:
        affichage.after(1000, compte_rebours, temps -1, callback)
    else:
        if callback:
            callback()
        else:
            affichage.config(text="Fin du cycle !")

    

fenetre = tkinter.Tk()
fenetre.title("Pomodoro")
fenetre.config(bg="white")

affichage_etat = tkinter.Label(fenetre, text="Appuie sur démarrer pour commencer", font=("Helvetica", 18, "normal"), fg="#333", bg="white" )
affichage_etat.pack(pady=(10, 20))

titre = tkinter.Label(fenetre, text=" Bienvenue dans le minuteur Pomodoro", font=("Helvetica", 18, "normal"), )
titre.pack(pady=(20, 20))

bouton = tkinter.Button(fenetre, text="Démarrer Pomodoro", command=demarrer_pomodoro, font=("Arial", 16, "bold"), fg="white", bg="#4CAF50", activebackground="#4CAF50", relief="flat",)
bouton.pack(pady=(20, 40))

affichage = tkinter.Label(fenetre, text="Temps restant : 25:00", font=("Helvetica", 24, "bold"), fg="black", bg="white")
affichage.pack(pady=(20, 50))

fenetre.mainloop()


