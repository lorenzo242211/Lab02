import translator as tr

t = tr.Translator() #traduttore
t.printMenu()
t.loadDictionary("dictionary.txt")
txtIn = input()

 # Add input control here!
while(txtIn != 4):
    if int(txtIn) == 1: #aggiungi parola se non è già in lista e se non è un numero
        t.handleAdd(input("Inserire parola da aggiungere e relativa traduzione, separata da uno spazio:\n"))

    if int(txtIn) == 2:
        t.handleTranslate(input("Inserisci1 la parola aliena della quale ricevere relative traduzioni:\n "))


    if int(txtIn) == 3:
        t.handleWildCard(input("Inserisci la parola 'wildcard': "))

    if int(txtIn) == 4:
        print(f"sei uscito, hai selezionato: {txtIn}")
        break
    #continuo dopo prima selezione del menù
    t.printMenu()
    txtIn = input()

#prova dizionario per programmazione: print(t.dizionario)