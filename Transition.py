class Transition:
    def __init__(self, start, end , entree, sortie = ''):
        self.start = start
        self.end = end
        self.vocEntree = entree
        self.vocSortie = sortie

    def __str__(self):
        output = ""
        output += "Transition {"
        output += "\nStart : " + str(self.start)
        output += "\nEnd : " + str(self.end)
        output += "\nEntree : " + self.vocEntree
        output += "\nSortie : " + self.vocSortie
        output += "\n}"
        return output