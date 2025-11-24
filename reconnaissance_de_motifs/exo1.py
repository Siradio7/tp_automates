############################################################
#  Automates & Langages - L3 Info / L3 Math-Info - 2025/26 #
#  TP 3  - Algorithmes de recherche de motif (suite)       #
############################################################

      

print('------------------------------------ TP 3 ---------------------------------------------')



#  Algorithme de Boyer Moore
############################


print('### Exercice 1 ###')   

def dicoDerOcc(motif) :         # retourne le dictionnaire des dernières occurrences
    last_occ_dic = {}

    for i in range(0, len(motif)):
        last_occ_dic[motif[i]] = i

    return last_occ_dic
    
print(dicoDerOcc("abracadabra"))
    
    




print('### Exercice 2 ###')

def rechercheBMH(motif, texte) : #   version simplifiée de BM -> BM Horspool 
    lm = len(motif)
    lt = len(texte)   
    i = lm - 1                 #  indice motif
    j = i                      #  indice texte
    dico = dicoDerOcc(motif)
    
    while (j < lt) :
        d = -1

        if texte[j] in dico:
            d = dico[texte[j]] 

        if motif[i] == texte[j]:
            if i == 0:
                return j

            i = i - 1
            j = j - 1
        elif motif[i] != texte[j] and d == -1:
            i = lm - 1
            j = j + i
        elif motif[i] != texte[j] and d < i:
            i = lm - 1
            j = j + i - d
        else:
            i = lm - 1
            j = j - i + lm
        
    return -1


 
 
 
 
 
 
 

def RechercheBMH(fichier,motif) :

    f_in = open(fichier,'r',encoding='utf-8')
    texte = f_in.read()
    f_in.close()

    position = rechercheBMH(motif, texte)
    if position == -1 :
        print('Le motif',motif,'n''apparaît pas dans le fichier',fichier)
    else :
        print('Le motif',motif,'apparaît en position',position,'dans le fichier',fichier)


# print(RechercheBMH('horla.txt','Rouen'))



    
#   Algorithme de Rabin-Karp
#############################


print('### Exercice 3.1 ###')


def str2int(s) :
    for i in range(1, len(s) + 1):
        print(2)

    return sum(ord(s[-i]) * 256 ** (i-1) for i in range(1,len(s)+1))

def hash(s) :
    return str2int(s) % 101
    
print(str2int("abar"))
    

print('### Exercice 3.2 ###')

def rechercheRK(motif,texte) :   
    hm = hash(motif)
    lm = len(motif)
    lt = len(texte)
    
    for i in range(lt):
        if i == 0:
            ht = hash(texte[0:lm])
        else:
            ht = update(ht, lm, texte[i-1], texte[i + lm - 1])

        if ht == hm:
            if motif == texte[i:i+lm]:
                return i
        
    return -1

def update(h,n,s_i,s_j) :
    return (256 * (h - ord(s_i) * 256 ** (n-1)) + ord(s_j)) % 101

print(rechercheRK("eui", "abeuicah"))


def RechercheRK(fichier,motif) :

    f_in = open(fichier,'r',encoding='utf-8')
    texte = f_in.read()
    f_in.close()
    
    position = rechercheRK(motif, texte)
    if position == -1 :
        print('RK : Le motif',motif,'n''apparaît pas dans le fichier',fichier)
    else :
        print('RK : Le motif',motif,'apparaît en position',position,'dans le fichier',fichier)


# print(RechercheRK('horla.txt','admirable'))




print('### Exercice 4 ###')

# calcul amorti de l'empreinte en fonction de celle du facteur précédent


def update(h,n,s_i,s_j) :
    return (256 * (h - ord(s_i) * 256 ** (n-1)) + ord(s_j)) % 101

