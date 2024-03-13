import dictionary as dc
class Translator:

    def __init__(self):
        pass

    def printMenu(self):
        # 1. Aggiungi nuova parola
        # 2. Cerca una traduzione
        # 3. Cerca con wildcard
        # 4. Exit
        menu = ""
        menu+="-"*30+"\n"+"Translator Alien-Italian\n"+"-"*30

        menu+= "\n1. Aggiungi nuova parola\n2. Cerca una traduzione\n3. Cerca con wildcard\n4. Exit"
        print(menu)
        pass

    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        d = {}
        dizio = dc.Dictionary(d)
        with open(dict, "r") as dizionario:
            righe = dizionario.readlines()
            for elem in righe:
                parole = elem.strip("\n").split(" ")
                dizio.addWord(parole[0], parole[1])

        return dizio
        pass

    def handleAdd(self, entry, dizio):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        traduzioni = entry[1]
        for i in traduzioni:
            dizio.addWord(entry[0].lower(), i.lower())

        pass

    def handleTranslate(self, query, dizio):
        # query is a string <parola_aliena>
        return (dizio.translate(query.lower()))
        pass

    def handleWildCard(self,query, dizio):
        # query is a string with a ? --> <par?la_aliena>
        return dizio.translateWordWildCard(query.lower())

        pass