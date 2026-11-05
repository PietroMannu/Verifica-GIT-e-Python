from componente import Componente

class Robot:
    def __init__(self, codice: str, modello: str, applicazione: str, peso_massimo_componenti_kg: float, stato: str) -> None:
        self.codice = codice
        self.modello = modello
        self.applicazione = applicazione
        peso_max = peso_massimo_componenti_kg
        
        if (peso_max <= 0 or peso_max <= self.componente.peso_kg):
            raise ValueError("Il peso non può essere negativo o minore del pso del componente")
        else:
            self.peso_max = peso_massimo_componenti_kg    
        self.componenti = []
        
    def aggiungiComponente(componente: Componente)->None:
        codice_attuale = self.componente.codice
        a = 0
        for componente in componenti():
            if (codice_attuale == codice_duplicato):
                raise ValueError("Il codice del componente è gia presente")
                a = 1
                break
            else:
                a = 0
        if (a == 1):
            print (f"Codice già presente")
        else:
            print (f"Codice non ancora presente")
            if(componente.peso_kg > peso_massimo_componenti_kg ):
                raise ValueError("Il componente pesa troppo")
            else:
                self.componenti.append(componente)
            
        codice_duplicato = self.componente.codice
            

        
        
        
            
        
    