class Componente:
    def __init__(self, codice: str, nome: str, peso_kg: float):
        self.cod = codice
        self.nome = nome
        pesoX = peso_kg
        if (pesoX <= 0):
            raise ValueError("Il peso non può essere negativo")
        else:
            self.pesoX = peso_kg
            

            
        
    
        