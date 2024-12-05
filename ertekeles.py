

def ab_feladat():
    hetnap:str=str(input("Hét napja: "))
    oraneve:str=str(input("Óra neve: "))
    ertekeles:int=int(input("Értékelés (0-5): "))
    
    while not (ertekeles >= 0 and ertekeles <= 5):
        ertekeles:int=int(input("Adj egy értékelés-t 0-5ig: "))
        if ertekeles < 0:
            print("Az értékelés nem lehet negatív")
        elif ertekeles > 5:
            print("Az értékelés nem lehet 5nél nagyobb")
           

    print(f"Összefoglaló: {hetnap},{oraneve},{ertekeles} érték")






    

