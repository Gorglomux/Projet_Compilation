from Transition import *


class Sommet:
    def __init__(self, nom):
        self.nom = nom
        self.transitions = []

    def add_transition(self, end, entree, sortie= ''):
        self.transitions.append(Transition(self.nom, end, entree, sortie))

    def get_vocEntree(self):
        vocEntree = ""
        for t in self.transitions:
            vocEntree += t.vocEntree

        # Enlever les doublons
        return vocEntree

    def get_vocSortie(self):
        vocSortie = ""
        for t in self.transitions:
            vocSortie += t.vocSortie

        # Enlever les doublons
        return vocSortie

    def __str__(self):
        output = ""
        output += "Sommet { \nnom : "+str(self.nom) + "\nTransitions :"
        for t in self.transitions:
            output += "\n"+str(t)
        output += "\n}"
        return output