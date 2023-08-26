#Bon fini les conneries on est pas sur git pour faire des truc moisis et avoir des pseudos claqués, en avant le vrai code XD

"""Vous êtes un détective de police, vous avez la réputation d'employer des méthodes douteuses pour parvenir à boucler vos affaires .
Le Commissaire vous a placé sur une enquête très intriguante impliquant un tueur en série au mode opératoire surprenant"""

def clean():
    print("\n"*1000)

def choix():
    print("""taper aide pour consulter les actions disponibles, taper indice pour avancer dans le scénario""")
    choix = input("Que faites vous ?")
    return choix

#
quitter = False
#
Listevide = ["Rien"]
item = []
#
est_I = True
choixI = None

voi_I = ["regarder","demander","prendre","utiliser","marcher","TOPOLOGIE","QUITTER (l'enquete)"]
voi_Ireg = ["placeholder"]
#voi_Idem = ["RIEN"] ==> liste vide
voi_Ipre = ["donuts","clé_voiture","cigarette","briquet"]

voi_Imar =["parking intérieur","parking extérieur","commissariat accueil","commissariat service"]
lieu = "voi_I"



#













nom =input("Choisissez un nom de détective :")
prenom=input("Choisissez votre prénom :")

if nom == "":
    nom = "Dian"
if prenom == "":
    prenom = "James"

#introduction jour = 26 août 2012, ville de Sagrasne
clean()
print('''26 août 2012, 8h00''','''ville de Sagrasne :''','''Commissariat de Police Centre Nord''','''''',sep="\n")
input('press enter')

clean()
print("""Vous arrivez en voiture devant le Commissariat centre nord,""",""" l'endroit où l'élite de la brigade des stups de cette ville perdue de campagne possède son QG.""","""Alors que vous êtes arrêtés sur le parking vous contemplez les Donuts achetés tous frais du jour,""","""vous vous demandez si cett achat vallait bien les 20 Euros dépensés pour les acquérirs""","""C'est difficile de réparer son image quand tout le monde pense que vous êtes un homme malhonnète,""","""surtout dans la police, les gens sont de nature méfiante et très enclins à écouter les bruits qui courrent.""","""En repensant cela, vous vous dîtes que ce n'est pas plus mal que les gens soient méfiant :""","""on n'a pas besoin de freins, ni de boulets administratifs, surtout dans un milieu où l'officier doit montrer l'exemple""",sep="\n")



while est_I == True:

    if lieu == "voi_I":
        print("""La voiture tourne encore. vous êtes garés dans le parking sécurisé.""")
        choixI = choix()
        if choixI == "aide":
            print("""actions disponibles :""",voi_I)


        if choixI == "indice":
            print("""Vous devriez aller au commissariat, le boulot a déjà commencé.""")
    
        if choixI == "topologie":
            print("ce lieu possède les pièces suivantes :", voi_Imar )
        
        if choixI == "quitter":
            break









































exit(0)