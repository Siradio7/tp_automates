def creerDT(n):
    dico = []

    for i in range(32, 127):
        dico.append(chr(i))

    for i in range(n):
        dico.append("")

    return (dico, 95)

dico, t = creerDT(12)

def estPlein(dico):
    return len(dico) == t

def ajout(dico, mot):
    if estPlein(dico):
        return dico
    else:
        d, t = dico
        d[t] = mot

        return (d, t+1)

def indice(dico, mot):
    d, t = dico
    
    for i in range(t):
        if d[i] == mot:
            return i
        
    return None

def encodeLZW(texte):
    code = []
    dico = creerDT(50)
    mot = texte[0]

    for lettre in texte[1:]:
        suivant = mot + lettre
        i = indice(dico, suivant)

        if i == None:
            code.append(indice(dico, mot))
            dico = ajout(dico, suivant)
            mot = lettre
        else:
            mot = suivant
        
    code.append(indice(dico, mot))

    return code

print(encodeLZW("blablabla"))
print(encodeLZW("babar"))

def lire_dico(dico, i):
    d, b = dico
    
    return d[i]

def decodeLZW(code):
    dico = creerDT(50)

    premier_code = code[0]
    texte = lire_dico(dico, premier_code)
    mot = lire_dico(dico, premier_code)

    for i in code[1:]:
        if i < len(dico[0]) and lire_dico(dico, i) != "":
            entree = lire_dico(dico, i)
        else:
            entree = mot + mot[0]

        texte += entree
        dico = ajout(dico, mot + entree[0])
        mot = entree

    return texte

print(decodeLZW(encodeLZW("blablabla")))
print(decodeLZW(encodeLZW("babar")))
    