import random

def tab_to_text(tab):
    first = True
    res = ""
    for i in range(len(tab)):
        if(first):
            first = False
            res += str(tab[i])
        else:
            res += ", " + str(tab[i])
    return res

def answer_number_only():
    while(True):
        answer = input()
        try:
            answer_n = int(answer)
            return answer_n
        except ValueError:
            # Handle the exception
            print('Mauvaise valeur')

def answer_number(text, num_min, num_max):
    while(True):
        print(text)
        answer = input()
        try:
            answer_n = int(answer)
            if(answer_n >= num_min and answer_n <= num_max):
                return answer_n
            else:
                 print('Mauvaise valeur')
        except ValueError:
            # Handle the exception
            print('Mauvaise valeur')

def answer_number_tab(text, tab):
    while(True):
        print(text)
        answer = input()
        try:
            answer_n = int(answer)
            if(answer_n in tab):
                return answer_n
            else:
                 print('Mauvaise valeur')
        except ValueError:
            # Handle the exception
            print('Mauvaise valeur')

#Items : Calculatrice, tri de balles

pv_guerrier = 20
pv_tireur = 20

cnt_sort_guerrier = 0
cnt_sort_tireur = 0

cap_sort_guerrier = 12
cap_sort_tireur = 10

guerrier_mort = False
tireur_mort = False

#règles

print("====== REGLES ======")
print()
print("Vous allez combattre un monstre avec vos deux personnages : un guerrier et un tireur.")
print()
print("=== LE GUERRIER ===")
print()
print("Le guerrier peut faire une attaque qui retire 1, 3 ou 5 PV au monstre.")
print("Dès que le guerrier a fait 12 dégâts ou plus au monstre, il peut utiliser sa super attaque.")
print("Il faudra résoudre correctement un calcul. Le nombre de dégâts est égal au résultat du calcul.")
print()
print("=== LE TIREUR ===")
print()
print("Le tireur peut diviser le nombre de PV du monstre par 2, 3, 4, 5, 6 ou 7.")
print("Attention, si la division ne donne pas un nombre entier (sans virgule), le coup est râté.")
print("A chaque coup réussi, sa super-jauge augmente de 20%")
print("A 100%, il peut désormais diviser par 10.")
print("Contre 50% de votre super-jauge, vous pouvez trier vos balles pour ne garder que celles effectives.")
print()
print("=== LE MONSTRE ===")
print()
print("L'attaque du monstre est égale à son dernier nombre de PV. Si le dernier nombre est un 0, le monstre attaque de 10 PV.")
print()
print("--------")

rejouer = True
garde_pv = False
while(rejouer):
    phrase = "Choisissez votre niveau : 1, 2, 3, 4, 6"
    niveau = answer_number(phrase, 1, 5)

    if(not garde_pv):
        pv_guerrier = 20
        pv_tireur = 20
        
    pv_ennemi_min = 10
    pv_ennemi_max = 99
    while(niveau > 1):
        pv_ennemi_min *= 10
        pv_ennemi_max *= 10
        pv_ennemi_max += 9

        if(not garde_pv):
            pv_guerrier += 5
            pv_tireur += 5
        niveau -= 1
    pv_ennemi = random.randint(pv_ennemi_min,pv_ennemi_max)

    print("Très bien, c'est parti !")

    nb_tour = 1
    while(pv_ennemi > 0):
        print("---- TOUR",nb_tour,"----")
        print()
        print("PV ennemi :",pv_ennemi)
        print()
        print("PV guerrier :",pv_guerrier)
        
        super_jauge_guerrier = round(cnt_sort_guerrier / cap_sort_guerrier * 100)
        if(super_jauge_guerrier > 100):
            super_jauge_guerrier = 100
        print("Super jauge guerrier:",super_jauge_guerrier,"%")
        print()
        print("PV tireur :",pv_tireur)
        super_jauge_tireur = round(cnt_sort_tireur / cap_sort_tireur * 100)
        if(super_jauge_tireur > 100):
            super_jauge_tireur = 100
        print("Super jauge tireur:",super_jauge_tireur,"%")
        print()
        print("--------")
        print()

        first_player = 1
        if(not guerrier_mort and not tireur_mort):
            #On choisit l'ordre
            phrase = "Qui joue en premier ? 1 - Guerrier, 2 - Tireur"
            answer = answer_number(phrase, 1, 2)
            first_player = answer
            order = [1,2]
            if(answer == 2):
                order = [2,1]
        elif(guerrier_mort):
            first_player = 2
            order = [2]
        elif(tireur_mort):
            first_player = 1
            order = [1]
            
        #Attaque des personnages
        for i in range(0,len(order)):
            if(pv_ennemi > 0):
                #Guerrier
                if(order[i] == 1 and not guerrier_mort):

                    #Utilise sa super attaque si possible ?
                    superattaque = False
                    if(super_jauge_guerrier == 100):
                        phrase = "Utiliser la super-attaque du guerrier ? oui / non"
                        print(phrase)
                        answer = input()
                        if(answer.lower() == "oui"):
                            cnt_sort_guerrier = 0
                            superattaque = True
                    
                    if(superattaque):
                        sa_base = 100
                        sa_sous = random.randint(10,50)
                        sa_add = random.randint(50,100)
                        sa_mult = 2
                        sa_res = 0
                        sa_order = random.randint(1,4)
                        if(sa_order == 1):
                            sa_res = ((sa_base - sa_sous) + sa_add) * sa_mult
                            print("((",sa_base,"-",sa_sous,")","+",sa_add,")","*",sa_mult,"= ?")
                        elif(sa_order == 2):
                            sa_res = ((sa_base + sa_add) * sa_mult) - sa_sous
                            print("((",sa_base,"+",sa_add,")","*",sa_mult,")","-",sa_sous,"= ?")
                        elif(sa_order == 3):
                            sa_res = ((sa_base * sa_mult) + sa_add) - sa_sous
                            print("((",sa_base,"*",sa_mult,")","+",sa_add,")","-",sa_sous,"= ?")
                        else:
                            sa_res = ((sa_base - sa_sous) * sa_mult) + sa_add
                            print("((",sa_base,"-",sa_sous,")","*",sa_mult,")","+",sa_add,"= ?")

                        answer = answer_number_only()
                        if(answer == sa_res):
                            print("Attaque réussie.")
                            pv_ennemi -= answer
                        else:
                            print("Attaque ratée.")
                    else:
                        phrase = "Combien de dégâts fait l'attaque du guerrier ? 1, 3, 5 ?"
                        answer = answer_number_tab(phrase, [1,3,5])

                        pv_ennemi -= answer
                        cnt_sort_guerrier += answer
                #Tireur
                elif(order[i] == 2 and not tireur_mort):
                    if(pv_ennemi == 1):
                         phrase = "Le tireur achève l'ennemi."
                         print(phrase)
                         pv_ennemi = 0
                    else:

                        #trier ses balles
                        if(super_jauge_tireur >= 50):
                            phrase = "Utiliser 50% de votre super-jauge pour trier les balles ? oui / non"
                            print(phrase)
                            answer = input()
                            if(answer.lower() == "oui"):
                                cnt_sort_tireur -= 5
                                balles = [2,3,4,5,6,7]
                                balles_triees = []
                                for i_balle in range(len(balles)):
                                    if(pv_ennemi%balles[i_balle] == 0):
                                        balles_triees.append(balles[i_balle])
                                print("Les balles efficaces sont : " + tab_to_text(balles_triees) + ".")
                            
                            
                        #Si super-attaque possible
                        if(super_jauge_tireur == 100):
                            phrase = "Quel diviseur le tireur doit-il utiliser ? 2, 3, 4, 5, 6, 7, 10 ?"
                            answer = answer_number_tab(phrase, [2,3,4,5,6,7,10])
                        else:
                            phrase = "Quel diviseur le tireur doit-il utiliser ? 2, 3, 4, 5, 6, 7 ?"
                            answer = answer_number_tab(phrase, [2,3,4,5,6,7])

                        #Super-attaque
                        if(answer == 10):
                            print("Vous utilisez votre super-attaque : LE DIVISEUR PAR 10 !")
                            cnt_sort_tireur = 0

                        if(pv_ennemi%answer == 0):
                            pv_ennemi //= answer
                            cnt_sort_tireur += 2
                        else:
                            print("L'attaque râte")

                #Minimum à zéro
                if(pv_ennemi <= 0):
                    print("L'ennemi est mort.")
                    pv_ennemi = 0
                else:
                    print("L'ennemi a",pv_ennemi,"PV.")
                print()
            #fin si pv ennemi > 0
        #fin for
                
        #l'ennemi choisit sa cible et l'attaque

        if(pv_ennemi > 0):
            target_ennemi = first_player

            #l'attaque de l'ennemi vaut le dernier nombre de ses pv. Si 0, atk = 10
            atk_ennemi = pv_ennemi%10
            if(atk_ennemi == 0):
                atk_ennemi = 10

            if(guerrier_mort):
                target_ennemi = 2
            elif(tireur_mort):
                target_ennemi = 1
            
            if(target_ennemi == 1):
                pv_guerrier -= atk_ennemi
                print("L'ennemi inflige",atk_ennemi,"dégâts au guerrier.")
            elif(target_ennemi == 2):
                pv_tireur -= atk_ennemi
                print("L'ennemi inflige",atk_ennemi,"dégâts au tireur.")

            #Minimum à zéro
            if(pv_guerrier <= 0 and not guerrier_mort):
                pv_guerrier = 0
                guerrier_mort = True
                print("Le guerrier est mort.")
            else:
                print("Le guerrier a",pv_guerrier,"PV.")
                
            if(pv_tireur <= 0 and not tireur_mort):
                pv_tireur = 0
                tireur_mort = True
                print("Le tireur est mort.")
            else:
                print("Le tireur a",pv_tireur,"PV.")

            if(guerrier_mort and tireur_mort):
                print("GAME OVER")
                break
            print()
            
        nb_tour+=1

    print("Bravo, vous avez battu l'ennemi.")
    phrase = "Rejouer ? oui / non"
    print(phrase)
    answer = input()
    if (answer != "oui"):
        rejouer = False
    else:
        phrase = "Voulez-vous garder vos PV actuels ? oui / non"
        print(phrase)
        answer = input()
        if (answer == "oui"):
            garde_pv = True
            
print("Merci d'avoir joué !")
    
