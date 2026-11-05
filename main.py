from componenti import Componente
from robot import Robot

if __name__ == "__main__":
    print("=== GESTIONE ROBOT ===")    
    while True:
        print(f"\n--- PANNELLO DI CONTROLLO ---")
        print("1. registra_robot")
        print("2. cerca_robot")
        print("3. riepilogo_robot")
        print("4. Esci dal programma")
        
        scelta = input("Seleziona un'opzione (1-4): ")
        
        if scelta == "1":
            robot_prodotti: list[Robot], robot: Robot -> None
            try:
            
                except ValueError as e:
            
                
        elif scelta == "2":
            for robot in robot_prodotti():
            
                
        elif scelta == "3":
           
            
        elif scelta == "4":
            print(f"\n Arrivederci")
            break
            
        else:
            print("❌ Scelta non valida. Inserisci un numero da 1 a 4.")
