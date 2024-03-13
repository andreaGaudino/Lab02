class Dictionary:
    def __init__(self, dizio):
        self.dizionario = dizio
        pass

    def addWord(self, parolaAliena, parolaItaliana):
        #Dictionary(parolaAliena, parolaItaliana)
        if parolaAliena not in self.dizionario:
            self.dizionario[parolaAliena] = [parolaItaliana]
        else:
            self.dizionario[parolaAliena].append(parolaItaliana)
        pass

    def translate(self, parolaAliena):
        for elem in self.dizionario:
            if elem == parolaAliena:
                return (self.dizionario[parolaAliena])
        pass

    def translateWordWildCard(self, parolaAliena):
        parole = parolaAliena.split("?")
        lista = []
        for elem in self.dizionario:
            if len(elem) == len(parolaAliena) and elem[:len(parole[0])] == parole[0] and elem[len(parole[0]) + 1:] == parole[1]:
                for i in self.dizionario[elem]:
                    lista.append(i)
        return lista
    pass

