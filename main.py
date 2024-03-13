import translator as tr
#import dictionary as dc


t = tr.Translator()
t.__init__()
dizio = t.loadDictionary("dictionary.txt")


while(True):

    t.printMenu()
    #s="ciao"
    #print(s[0:1]+s[2:4])

    txtIn = input("-")

    # Add input control here!

    if int(txtIn) == 1:
        print()
        txtIn = input("Quale parola devo aggiungere? ")
        parole = txtIn.split(" ")
        tupla = (parole[0], parole[1:])
        t.handleAdd(tupla, dizio)
        pass
    elif int(txtIn) == 2:
        txtIn = input("Inserisci la parola da tradurre: ")
        for i in t.handleTranslate(txtIn, dizio):
            print(i, end=" ")
        print()
        pass
    elif int(txtIn) == 3:
        txtIn = input("Inserisci la parola da tradurre con wildcard: ")
        for i in t.handleWildCard(txtIn, dizio):
            print(i, end=" ")
        print()

        pass
    elif int(txtIn) == 4:
        break
