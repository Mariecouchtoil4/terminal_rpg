pv = 6
advance = 0
is_over = False
is_a_win = False

item = []
utiliser = None
possede = False
entree = None
e = None
menu = None
is_menu = True

def clean():
    print("","","","","","","","","","","","","","","","","", sep="\n")

def menu(is_menu):
    while is_menu == True:
        clean()
        print('''Covid Fighter : A Jean Marie Bigard text odyssee''','''''','''1)parameters''','''2)enter game''')
        menu = int(input('Choose an option'))
        if menu == 1:
            input('''Only Language available : "Langage grossier de Bigard"''')
        elif menu == 2:
            print('''Commencing adventure...''')
            is_menu = False
    



menu(True)



while is_over != True and entree != "quitter":
    
    clean()

    if advance == 0:
        print('Tu es Jean Marie Bigard, un humoriste reconnu et une personnalité publique importante.',"Mais aujourd'hui, l'heure est grave, l'heure n'est pas à la détente ou à la franche rigolade car je cite :'Nous sommes en guerre !'",'tels étaient les mots prononcés par le président de la République','''En entendant ces mots prononcés par un homme détesté de tous et pourri jusqu'à la moile''','Votre décision est prise, il vous faut intervenir', sep="\n")
        advance += 1

    if advance == 1:
        print('','''indice : tapez aide''',sep="\n")
        entree = input('''QUE SOUHAITEZ-VOUS FAIRE ?''')
        if entree == "prendre voiture":
            print("Vous sortez de votre appartement pour prendre votre voiture")
            advance += 1
        elif entree == "aide":
            input('''il n'y a qu'une seule chose à faire quand on entend la connerie humaine à l'état pure : aller à la maison de la radio''')
            advance = 0

            
        else:
            print('''avancée''', advance)

    
    if advance == 2:
        print('''Vous êtes désormais devant votre voiture, juste à la sortie de votre appartement''')
        entree = input("QUE SOUHAITEZ-VOUS FAIRE ?")
        if entree == "utiliser":
            print('liste des items',item)
            utiliser = input("Quel item utiliser ?")
            if utiliser == "clé_bagnole":
                for i in range(len(item)):
                    if utiliser == item[i]:
                        possede = True

                if possede == True:
                    print('''Vous ouvrez la caisse avec la clé''')
                    advance += 1
                else:
                    print('''Tu nas pas pris tes clés''')
            elif utiliser == "Le_doigt":
                print('''Tu mets les doigts dans la serrure et la voiture s'ouvre ''')
                advance += 1
            else:
                print('''L'objet''', utiliser, '''possède une quantité de qualités incroyables mais pascelle d'ouvrir ta voiture.''')



    if advance == 3:
        is_over = True
        print('''Vous êtes en route pour la Maison de la Radio afin de répondre à une connasse de journaliste''','''Dans un sens, c'est pas de sa faute : c'est une femme''')



if entree == 'quitter':
    clean()
    print('Vous avez abandonné le peuple Françis à son sort .','''Le peuple a besoin de vous pour résister à l'oppression''')