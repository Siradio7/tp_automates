###############################################################
#  Automates & Langages  -  L3 Info / L3 Math-Info  - 2025/26 #
#  TP 2  - Algorithmes de recherche de motif - I              #                                    
###############################################################


print('------------------------------------ TP 2 ---------------------------------------------')



#  Préliminaires
################

#  jeu de 95 caractères Unicode latin de base (hors commandes)

for i in range(95) :
    print(hex(i+32),' : ',chr(i+32))
    
print()

# pour visualiser la lettre i d'une chaîne

def marque(chaineCar,i) :
    return '{}[{}]{}'.format(chaineCar[:i],chaineCar[i],chaineCar[i+1:])

print(marque('blabla',1))
print()


# pour visualiser la comparaison entre la lettre i du motif et la lettre i+j du texte

def compare(motif,texte,i,j) :
    print('{}\n{}{}\n'.format(marque(texte,i+j),' '*j,marque(motif,i)))

compare('blabla','lalablablère',5,4)


def comparePlus(motif,texte,i,j) :
    if texte[i+j] != motif[i] :
        print('{} : ! \n{}{}\n'.format(marque(texte,i+j),' '*j,marque(motif,i)))
    else :
        print('{}\n{}{}\n'.format(marque(texte,i+j),' '*j,marque(motif,i)))

comparePlus('blabla','lalablablère',5,4)




#  Algorithme de recherche naif
###############################

print('### Exercice 1 ###')    

def recherche(motif,texte) :
    lm = len(motif)
    lt = len(texte)

    for i in range(lt - lm + 1) :
        if texte[i:i+lm] == motif :
            return i
            
    return -1

print(recherche("bla", "blibla"))



#  Algorithme KMP : pré-traitement du motif
###########################################

print('### Exercice 2 ###') 


def table(motif) :            # table[i] = longueur du plus long suffixe de motif[i] aussi préfixe du motif
    lm = len(motif)
    T = [0] * lm
    i = -1 
    T[0] = i 

    for j in range(1,lm) :
        while (i != -1) and (motif[i] != motif[j-1]) :
            i = T[i]

        i = i+1
        T[j] = i  

    return T

print(table("abracadabra"))

#  Algorithme KMP : début d'implantation
########################################

print('### Exercice 3 ###')

def rechercheMP(motif, texte):
    T = table(motif) 
    n = len(texte)
    m = len(motif)
    i = 0
    j = 0
    
    while i < n:
        if texte[i] == motif[j]:
            i += 1
            j += 1
            
            if j == m:
                return i - j
        else:
            if j > 0: 
                j = T[j]
            else:
                i += 1
                
    return -1

print(rechercheMP("bla", "blibla"))
    
    

def RechercheMP(fichier,motif) :

    f_in = open(fichier,'r',encoding='utf-8')
    texte = f_in.read()
    f_in.close()
    
    position = rechercheMP(motif, texte)
    if position == -1 :
        print('Recherche MP : Le motif',motif,'n''apparaît pas dans le fichier.',fichier)
    else :
        print('Recherche MP : Le motif',motif,'apparaît en position',position,'dans le fichier :',fichier)

# remarque : sans redondance dans le motif, KMP perd de son intérêt ... Imaginons son exécution plutôt sur du binaire !



#  Algorithme KMP : finalisation de l'implantation
##################################################

print('### Exercice 4 ###')

def rechercheKMP(motif, texte):
    m = len(motif)
    n = len(texte)
    T = table(motif)
    i = 0
    j = 0
    
    while i < n:
        if motif[j] == texte[i]:
            i += 1
            j += 1

            if j == m:
                return i - j
        else:
            if T[j] > -1:
                j = T[j]
            else:
                i += 1
                j = 0
                
    return -1

print(rechercheKMP("bla", "blibla"))
        
        
        
        
        
        
        

def RechercheKMP(fichier,motif) :

    f_in = open(fichier,'r',encoding='utf-8')
    texte = f_in.read()
    f_in.close()

    position = rechercheKMP(motif, texte)
    if position == -1 :
        print('Recherche KMP : Le motif',motif,'n''apparaît pas dans le fichier.',fichier)
    else :
        print('Recherche KMP : Le motif',motif,'apparaît en position',position,'dans le fichier.',fichier)



        


#  Algorithme de Aho-Corasick : construction
############################################

print('### Exercice 5 --> sur papier ###')

def construire_automate(motif, alphabet):
    m = len(motif)
    automate = [{}] 
    
    for char in alphabet:
        automate[0][char] = 0
        
    etat_terminal = 0
    
    for i in range(m):
        a = motif[i]
        nouvel_etat = i + 1
        automate.append({})
        etat_repli = automate[etat_terminal][a]
        automate[etat_terminal][a] = nouvel_etat

        for b in alphabet:
            automate[nouvel_etat][b] = automate[etat_repli][b]
            
        etat_terminal = nouvel_etat
        
    return automate


#  Algorithme de Aho-Corasick : implantation de l'automate
##########################################################

print('### Exercice 6 ###')

def recherche_automate(motif, texte, alphabet):
    automate = construire_automate(motif, alphabet)
    etat = 0
    m = len(motif)
    
    for i, char in enumerate(texte):
        if char not in alphabet:
            etat = 0
            continue
            
        etat = automate[etat][char]
    
        if etat == m:
            return i - m + 1
            
    return -1

print(recherche_automate("bla", "blibla", [chr(i) for i in range(32, 127)]))