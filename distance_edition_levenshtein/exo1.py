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
    dist = 0
    tab = levenshtein_table(word_1, word_2)
    word_1_len = len(word_1)
    word_2_len = len(word_2)
    i = word_1_len
    j = word_2_len
    
    

    return dist

print(distance("rame", "marin"))

def chemin(word_1, word_2):
    T = levenshtein_table(word_1, word_2)

    return chemin_rec(word_1, word_2)

def chemin_rec(word_1, word_2, T):
    if word_1 == "" and word_2 == "":
        return []
    
    if word_1 == "":
        L = chemin_rec("", word_2[:-1], T)
        L.append("-", word_2[-1])
        
        return L
    
    if word_2 == "":
        L = chemin_rec(word_1[:-1], "-", T)
        L.append(word_1[-1], "-")

        return L

    