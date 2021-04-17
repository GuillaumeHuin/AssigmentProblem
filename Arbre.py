from typing import List


class A:

    def __init__(self, val=[], niv=0, n=0):
        self.val = val
        self.n = n
        self.niveau = niv
        self.e = []
        self.scoreMin = 0
        self.score = 0

    """
    Construction de l'arbre. En deux étapes, on construit l'arbre (construction), puis,
    on écrit les scores de chaque solution.
     - représentation des solutions sous forme d'arbre
     - écriture des scores de chaque solution candidate finale
     - écriture des meilleurs score possible plus haut dans la hiérarchie
    """
    def construction(self, mat: List[List[int]]):
        self.n = len(mat)
        n = self.n

        def loop(arbre: A):
            if arbre.niveau == n:
                pass
            else:
                for i in range(n):
                    arbre.e.append(loop(A(val=arbre.val + [i + 1], niv=arbre.niveau + 1, n=n)))
            return arbre

        def ecritureScores(arbre: A):
            if arbre.val:
                val = arbre.val
                arbre.score = mat[arbre.niveau - 1][val[-1] - 1]
                minimumList = [min(mat[i]) for i in range(arbre.n)]
                minimumList = minimumList[::-1]

                arbre.scoreMin = sum(minimumList[:-arbre.niveau]) + arbre.score + sum(
                    [mat[i][val[i] - 1] for i in range(arbre.niveau - 1)])

            if arbre.e:
                for i in range(arbre.n):
                    ecritureScores(arbre.e[i])

        loop(self)
        ecritureScores(self)
    """
    Recherche de la solution optimale dans l'arbre. On utilise scoreMin pour exclure les
    branches dont la solution optimale est moins bonne que la solution courante.
    Le parcours de l'arbre se réalise en explorant la branche la plus prometteuse en
    utilisant une file d'attente à priorité. Ensuite on réalise le parcours horizontalement.
    """
    def rechercheSolutionOptimale(self, solutionCourante: [], scoreCourant: int, file=[]):
        # action sur le dernier niveau / les feuilles
        if self.niveau == self.n:
            # Au dernier niveau, scoreMin correspond au vrai score du candidat
            if self.scoreMin < scoreCourant and len(self.val) == len(set(self.val)):
                solutionCourante = self.val
                scoreCourant = self.scoreMin

        # Exclusion des solutions non pertinentes
        # Ou plutôt, inclusion des solutions intéressantes uniquement
        if self.e:
            for i in range(self.n):
                if self.e[i].scoreMin < scoreCourant:
                    # Une solution est valide que si [i, j, k, l] tel que i, j, k et l différents deux à deux
                    if len(self.e[i].val) == len(set(self.e[i].val)):
                        file.append(self.e[i])

        if file:
            file = sorted(file, key=lambda a: a.scoreMin)
            file = file[::-1]
            prochaineBranche = file.pop()
            return prochaineBranche.rechercheSolutionOptimale(solutionCourante, scoreCourant, file)
        else:
            return solutionCourante, scoreCourant
