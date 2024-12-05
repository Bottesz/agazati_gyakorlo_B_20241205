from hatoslotto import hatos_lotto_szamok

def fajlbeolvasas():
    fajl = open ('huzasok.txt','r',encoding="utf-8")
    fajl.readline()
    soroklista = fajl.readlines()
    fajl.close()

    huzaslista = []
    for i in range(0,len(soroklista),1):
        aktElem = soroklista[i]
        sorLista = aktElem.strip().split('@')
        huzas = int(sorLista[0])
        ev = int(sorLista[1])
        het = int(sorLista[2])
        szam = float(sorLista[3])

        huzas = (huzas,ev,het,szam)
        huzaslista.append(huzas)
    return huzaslista
   


def HuzasokSzama():
	lista = fajlbeolvasas()
	db = 0
	for huzas in lista:
		db += 1
	return db