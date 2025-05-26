import time

print("Pomodoro App")


#################### Refaire l'exo demain #########################

def compte_rebours(duree):
    for i in range(duree, 0, -1):
        print(f"Travail : {i} secondes restantes", end="\r", flush=True)
        time.sleep(1)

######################################################################################

utilisateur = input(" Quel est le nombre de cycle de travail que tu veux faire ? ")
nombre_cycle = int(utilisateur)
print(f" tu as choisi {nombre_cycle} cycles de travail.")


for i in range(nombre_cycle):
    numero_cycle = i + 1
    print(f" Cycle {numero_cycle} : Travail en cours ... ")
    compte_rebours(300)
    print("Fin de la pause, on enchaîne")

    print("Pause en cours...")
    compte_rebours(300)
    print("Fin de la pause, on enchaîne !")
    print()
print("Bravo ! Tu as terminé tous les cycles Pomodoro !")