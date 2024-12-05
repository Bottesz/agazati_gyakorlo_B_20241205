import random

global rlista 
rlista = []
i:int = 0

def abc():
    i:int=0
    while i < 8:
        rsz:int=random.randint(-100,859)
        rlista.append(rsz)
        i += 1

    i=0
    while i < len(rlista):
        if i < len(rlista) -1 :
            print(f"\t {rlista[i]}", end="; ")
        else:
            print(f"{rlista[i]}", end=" ")

        i += 1




def tizzeloszt():
    szamlalo:int=0
    for rsz in rlista:
        if rsz % 10 == 0:
            szamlalo += 1
    return szamlalo



def konzol_ir():
    eredmeny = tizzeloszt()
    print(f"10zel oszhatoak szama {eredmeny}. ")




def fajlba_ir():
    szam=tizzeloszt()
    f = open('vegeredmeny.txt', 'w') 
    f.write(f"\t A tizzel osztahtoak szama {szam}.")
    f.close()