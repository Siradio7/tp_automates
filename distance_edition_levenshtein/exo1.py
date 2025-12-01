def create_tab(n, m):
    L = []

    for i in range(n):
        L.append([0] * m)

    return L

def subst(x, y):
    if x == y:
        return 0
    
    return 1

def levenshtein_table(word_1, word_2):
    word_1_len = len(word_1)
    word_2_len = len(word_2)
    T = create_tab(word_1_len + 1, word_2_len + 1)

    for i in range(word_1_len + 1):
        T[i][0] = i

    for i in range(word_2_len + 1):
        T[0][i] = i

    for i in range(word_1_len):
        for j in range(word_2_len):
            insert = T[i+1][j] + 1
            delete = T[i][j+1] + 1
            subs = T[i][j] + subst(word_1[i], word_2[j]) 

            T[i+1][j+1] = min(insert, delete, subs)

    return T
    
def distance(word_1, word_2):
    tab = levenshtein_table(word_1, word_2)
    word_1_len = len(word_1)
    word_2_len = len(word_2)

    return tab[word_1_len][word_2_len]

print(distance("cellulaire", "automate"))

def chemin(x, y):
    T = levenshtein_table(x, y)
    i, j = len(x), len(y)
    path = []
    
    while i > 0 or j > 0:
        val_actuelle = T[i][j]
        
        val_diag = T[i-1][j-1] if (i > 0 and j > 0) else float('inf')
        val_haut = T[i-1][j] if i > 0 else float('inf')
        val_gauche = T[i][j-1] if j > 0 else float('inf')
        
        cout_subst = 0 if (i > 0 and j > 0 and x[i-1] == y[j-1]) else 1
        
        if i > 0 and j > 0 and val_actuelle == val_diag + cout_subst:
            path.append((x[i-1], y[j-1]))
            i -= 1
            j -= 1
        elif i > 0 and val_actuelle == val_haut + 1:
            path.append((x[i-1], '-'))
            i -= 1
        else:
            path.append(('-', y[j-1]))
            j -= 1
            
    return path[::-1]

print(chemin("05122022", "01012023"))
print(chemin("maison", "maçon"))

def tous_chemins(x, y):
    T = levenshtein_table(x, y)
    solutions = []
    
    def parcours(i, j, chemin_courant):
        if i == 0 and j == 0:
            solutions.append(chemin_courant[::-1])
            return

        val_actuelle = T[i][j]
        cout_subst = 0 if (i > 0 and j > 0 and x[i-1] == y[j-1]) else 1
        
        if i > 0 and j > 0:
            if val_actuelle == T[i-1][j-1] + cout_subst:
                parcours(i-1, j-1, chemin_courant + [(x[i-1], y[j-1])])
                
        if i > 0:
            if val_actuelle == T[i-1][j] + 1:
                parcours(i-1, j, chemin_courant + [(x[i-1], '-')])
                
        if j > 0:
            if val_actuelle == T[i][j-1] + 1:
                parcours(i, j-1, chemin_courant + [('-', y[j-1])])

    parcours(len(x), len(y), [])

    return solutions
    
tous_les_chemins = tous_chemins("rame", "marin")

for chemin in tous_les_chemins:
    print(chemin)