from Arbre import A

""" Paramètres du problème"""
mat = [
    [3, 5, 9, 2],
    [9, 3, 3, 4],
    [1, 4, 2, 6],
    [5, 3, 7, 2]]

n = len(mat)
solutionInit = [1, 2, 3, 4]
scoreInit = sum([mat[i][solutionInit[i] - 1] for i in range(n)])

arbre = A()
arbre.construction(mat)
sol, score = arbre.rechercheSolutionOptimale(solutionInit, scoreInit)
print(f"La solution est: {sol} et de score : {score}")
