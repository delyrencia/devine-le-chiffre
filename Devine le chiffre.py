import random

minVal = 1
maxVal = 100

def nouvellePartie():
    clé = chiffreMystère()
    print(f"\nBienvenue !\n\nEt si je te disais que j'ai choisi un chiffre mystère entre {minVal} et {maxVal} ? Es-tu capable de le deviner ? Tente ta chance !\n")
    nombreTentatives = 0
    contrôle(clé, nombreTentatives)
    
def chiffreMystère():
    return random.randint(minVal,maxVal)

def contrôle(clé, nombreTentatives):
    while True:
        try:
            tentative = int(input("Quel est le chiffre mystère ? ")) if nombreTentatives == 0 else int(input("Essaye encore : "))
            nombreTentatives += 1
        except ValueError:
            print("Hé, est-ce que tu essayes de casser le jeu !? Fais attention !\n")
            continue

        if tentative == clé:
            print(f"\nBien joué ! Tu as trouvé le chiffre mystère {clé} en {nombreTentatives} tentatives !")
            recommencer()
            break
        elif tentative < clé:
            print("\nDommage, c'est trop peu !")
        elif tentative > clé:
            print("\nRaté, c'est beaucoup trop !")       
        
def recommencer():
    while True:
        try:
            décision = input("Tu veux recommencer ? Oui ou non ? Dis oui !\n" )
        except ValueError:
            print("Hé, est-ce que tu essayes de casser le jeu !? Fais attention !\n")
            continue  

        if décision.upper() == "OUI":
            print("\nExcellent ! C'est parti :")
            nouvellePartie()
            break
        else:
            print("\nTu n'as pas compris... J'ai dit : dis OUI !")
            recommencer()
            continue     

if __name__ == "__main__":
    nouvellePartie()