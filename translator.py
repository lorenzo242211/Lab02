class Translator:

    def __init__(self):
        self.dizionario = dict()

    def printMenu(self):
        print("1. Aggiungi nuova parola")
        print("2. Cerca una traduzione")
        print("3. Cerca con wildcard")
        print("4. Exit")

        pass

    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        with open(dict, 'r', encoding="utf-8") as file:
            righe = file.readlines()
            for r in righe:
                r = r.split(" ")
                r[1] = r[1].replace("\n", "")
                self.dizionario[r[0]] = [r[1]]


    #operatore extend di phyton per versare contenuto lista 2 in lista 1
    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        traduzione = entry.lower().split(" ")
        for parola in traduzione:
            parola = parola.replace("\n", "")
            if not parola.isalpha():
                print("Inserire parola valida (no numeri) ! \n")
                return
        if (traduzione[0] not in self.dizionario):
                print(traduzione[0] + " non era presente, l'ho aggiunto al dizionario con la sua rispettiva traduzione/i ")
                #print("-".join(traduzione)[1]) STAMPO LISTA CON SEPARATORE
                print(traduzione[1:])
                self.dizionario[traduzione[0]] = list() #associo lista di un solo elemento
                self.dizionario[traduzione[0]].extend(traduzione[1:])
        elif traduzione[0] in self.dizionario: #caso parola è già nel dizionario
             #aggiungo ulteriore significato alla parola
            for s in traduzione[1:]:
                if s not in self.dizionario[traduzione[0]]:
                    print(f"la parola {s} è aggiunta come significato di {traduzione[0]}\n")
                    self.dizionario[traduzione[0]].append(s)
                if s in self.dizionario[traduzione[0]]:
                    print(s + f", traduzione di '{traduzione[0]}', non è aggiunta poichè era già inserita!\n")
        else:
            print("ERRORE \n")
            return



    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        self.query = query.lower()
        if self.query not in self.dizionario:
            print(f"'{query}' non è nel dizionario!")
        if self.query in self.dizionario:
            print("la traduzione di " + query + " è/sono:")
            for trad in self.dizionario[self.query]:
                print(trad)
        print("\n")

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        risultati = dict()
        for chiave in self.dizionario:
            if len(chiave) == len(query):
                check = True #a prescindere sarà vero, ora verifichiamo
                i = 0
                for letteraAlienaChiave in chiave:
                    if query[i] != "?" and query[i] != letteraAlienaChiave:
                        check = False #se viene trovata una sola lettera che non sia ?, diversa allora parola non valida
                        break #esco dal for (lettera chiave), non ha senso continuare su questa parola
                    i = i + 1
                if check:
                    risultati[chiave] = self.dizionario[chiave] #assoccio valori chiave a nome chiave stesso

        #stampo
        for k in risultati:
            print("Parola: " + k + ", traduzione/i associate: ")
            for trad in risultati[k]:
                print("-" + trad)
            print("\n")