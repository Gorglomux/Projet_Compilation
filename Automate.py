from Sommet import *


class Automate:
    def __init__(self):
        self.commentaire = ''
        self.meta = '#'
        self.vocabEntree = ''
        self.numEtat = 0
        self.vocabSortie = ''
        self.initState = []
        self.finalState = []
        self.sommets = []
        self.transitions = []

    # Définit le commentaire C
    def addComment(self, C):
        self.commentaire = C

    # Définition du Meta Caractère M de l'automate
    def addMeta(self, M):
        self.meta = M

    # Définition d'un vocabulaire d'entrée V
    def addVocabEntree(self, V):
        self.vocabEntree = V

    # Définit le nombre d'état de l'automate E
    def addNumEtat(self, E):
        self.numEtat = E
        if len(self.sommets) < self.numEtat:

            # On recupere le "nom" max de sommet
            maximum = -1
            for s in self.sommets:
                if int(s.nom) > maximum:
                    maximum = int(s.nom)

            toCreate = self.numEtat - len(self.sommets)
            for i in range(toCreate):
                som = Sommet(maximum + i + 1)
                self.sommets.append(som)


    # Définit le vocabulaire de sortie O
    def addVocabSortie(self, O):
        self.vocabSortie = O

    # Définit le ou les états initiaux I
    def addInitState(self, I):
        trouve = False
        for s in self.sommets:
            if s.nom == I:
                trouve = True
                self.initState.append(s)

        if not trouve:
            s = Sommet(I)
            self.initState.append(s)
            self.sommets.append(s)

    # Définit le ou les états finaux F de l'automate.
    def addFinalState(self, F):
        trouve = False
        for s in self.sommets:
            if s.nom == F:
                trouve = True
                self.finalState.append(s)

        if not trouve:
            s = Sommet(F)
            self.finalState.append(s)
            self.sommets.append(s)

    # Permet de définir les transitions T possibles de l'automate
    def addTransition(self, start, end, entree, sortie=''):
        trouve = False
        for s in self.sommets:
            if s.nom == start:
                trouve = True
                s.add_transition(end, entree, sortie)

        if not trouve:
            s = Sommet(start)
            s.add_transition(end, entree, sortie)
            self.sommets.append(s)

    def __str__(self):
        output ="Automate {"
        output +="\nMeta : " + self.meta
        output +="\nVocabulaire en entrée : " + self.vocabEntree
        output +="\nVocabulaire en sortie : " + self.vocabSortie
        output +="\nNombre d'états : " + str(self.numEtat)
        output +="\nSommets : "
        #Affichage des sommets
        for s in self.sommets:
            output += '\n' +str(s)

        output += "\nEtats initaux :"
        #Affichage des etats initiaux
        for s in self.initState:
            output += '\n'+str(s)

        output += "\nEtats finaux :"
        #Affichage des etats finaux
        for s in self.finalState:
            output += '\n'+str(s)
        output += "}"
        return output

    def verify(self):
        if len(self.initState) ==0:
            # On ajoute le sommet 0
            for s in self.sommets:
                if s.nom ==0:
                    self.initState.append(s)
