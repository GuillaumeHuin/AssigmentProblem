from Arbre import A

mat = [
    [3, 5, 9, 2],
    [9, 3, 3, 4],
    [1, 4, 2, 6],
    [5, 3, 7, 2]]

"""
Algo de construction de l'arbre : on encode toutes les solutions de la forme [i, j ,k, l] dans un arbre
"""
def construction(n):
    def loop(arbre):
        if arbre.niveau == n:
            pass
        else:
            for i in range(arbre.n):
                arbre.e.append(loop(A(arbre.val + [i + 1], niv=arbre.niveau + 1)))
        return arbre

    return loop(A([], niv=0))


"""
Ecrit les scores sur chaque noeuds 
Ici on ne le fait pas en POO pur parce qu'on conde en dur les scores minimum, sinon c'est plus lourd
pour traiter le cas général.
args:
scoreMin : cumul des scores min de haut en bas des parents.
"""
def ecritureScores(arbre:A):
    if arbre.val:
        val = arbre.val
        arbre.score = mat[arbre.niveau-1][val[-1]-1]
        minimumList = [min(mat[i]) for i in range(arbre.n)]
        minimumList = minimumList[::-1]

        arbre.scoreMin = sum(minimumList[:-arbre.niveau]) + arbre.score + sum([mat[i][val[i]-1] for i in range(arbre.niveau-1)])

    if arbre.e:
        for i in range(arbre.n):
            ecritureScores(arbre.e[i])

def rechercheSolutionOptimale(arbre:A, solutionCourante:[], scoreCourant:int, file=[]):
    # action sur le dernier niveau / les feuilles
    if arbre.niveau == arbre.n:
        # Au dernier niveau, scoreMin correspond au vrai score du candidat
        if arbre.scoreMin < scoreCourant and len(arbre.val) == len(set(arbre.val)):
            solutionCourante = arbre.val
            scoreCourant = arbre.scoreMin

    # Exclusion des solutions non pertinentes
    # Ou plutôt, inclusion des solutions intéressantes uniquement
    if arbre.e:
        for i in range(arbre.n):
            if arbre.e[i].scoreMin < scoreCourant:
                # Une solution est valide que si [i, j, k, l] tel que i, j, k et l différents deux à deux
                if len(arbre.e[i].val) == len(set(arbre.e[i].val)):
                    file.append(arbre.e[i])

    if file:
        file = sorted(file, key=lambda a: a.scoreMin)
        file = file[::-1]
        prochaineBranche = file.pop()
        return rechercheSolutionOptimale(prochaineBranche, solutionCourante, scoreCourant, file)
    else:
        return solutionCourante, scoreCourant
