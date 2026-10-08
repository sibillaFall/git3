class Operazione:
    def __init__(self, nome, *valori):
        self.nome = nome
        self.valori = list(valori)

    def esegui(self):
        raise NotImplementedError("Le classi figlie devono implementare esegui()")

    def __str__(self):
        return f"{self.nome}: {self.valori}"


class Somma(Operazione):
    def __init__(self, *valori):
        super().__init__("somma", *valori)

    def esegui(self):
        return sum(self.valori)


class Sottrazione(Operazione):
    def __init__(self, primo, secondo):
        super().__init__("sottrazione", primo, secondo)

    def esegui(self):
        return self.valori[0] - self.valori[1]


class Divisione(Operazione):
    def __init__(self, dividendo, divisore):
        super().__init__("divisione", dividendo, divisore)

    def esegui(self):
        if self.valori[1] == 0:
            raise ValueError("Non si puo dividere per zero")
        return self.valori[0] / self.valori[1]


class Moltiplicazione(Operazione):
    def __init__(self, *valori):
        super().__init__("moltiplicazione", *valori)

    def esegui(self):
        risultato = 1
        for valore in self.valori:
            risultato *= valore
        return risultato


class StoricoOperazioni:
    def __init__(self):
        self.righe = []

    def aggiungi(self, operazione, risultato):
        self.righe.append({
            "operazione": str(operazione),
            "risultato": risultato,
        })

    def ultime(self, quanti=5):
        return self.righe[-quanti:]


class Calcolatore:
    def __init__(self):
        self.storico = StoricoOperazioni()

    def esegui(self, operazione):
        risultato = operazione.esegui()
        self.storico.aggiungi(operazione, risultato)
        return risultato

    def stampa_storico(self):
        for voce in self.storico.righe:
            print(f"{voce['operazione']} = {voce['risultato']}")


if __name__ == "__main__":
    # Esempio pensato per un lavoro di gruppo 2-3 persone:
    # - Studente 1: classi delle operazioni (Somma, Sottrazione, Divisione)
    # - Studente 2: classe Calcolatore e StoricoOperazioni
    # - Studente 3: main/test e gestione Issue/PR su GitHub
    calcolatore = Calcolatore()

    risultato_somma = calcolatore.esegui(Somma(2, 3, 5))
    risultato_sottrazione = calcolatore.esegui(Sottrazione(15, 7))
    risultato_divisione = calcolatore.esegui(Divisione(20, 4))
    risultato_moltiplicazione = calcolatore.esegui(Moltiplicazione(3, 4, 5))

    print("2 + 3 + 5 =", risultato_somma)
    print("15 - 7 =", risultato_sottrazione)
    print("20 / 4 =", risultato_divisione)
    print("3 * 4 * 5 =", risultato_moltiplicazione)

    print("\nStorico operazioni:")
    calcolatore.stampa_storico()