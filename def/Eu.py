""" 
csatlakozas.txt
Ausztria;1995.01.01
Belgium;1958.01.01
Bulgária;2007.01.01
"""

#1. Az Eu osztály létrehozása:

class Eu:
  def __init__(self, sor):
    orszag, datum = sor.strip().split(";")
    self.orszag = orszag
    self.datum = datum
    self.ev = int(datum[:4]) 
    self.honap = int(datum[5:7])
    self.nap = datum[8:10]

print(f"1. Osztály létrehozása Eu: néven")
# -------------------------------------------------------
# 2. Forrast fált megnyit, beolvas, feldolgoz, listaval visszater. Bemenő paraméter a fájl neve.
def forrast_beolvas_feldolgoz_listaval_visszater(fname):
  with open(fname, encoding="UTF-8") as f:
    lista = [Eu(sor) for sor in f]
  return lista

lista = forrast_beolvas_feldolgoz_listaval_visszater("csatlakozas.txt")

print(f"2. A 'csatlakozas.txt' fájl beolvasása, a lista létrehozása.")
# -------------------------------------------------------
# 3. A tagállamok száma 2018-ban a BREXIT előtt, tehát Az Egyesült királyság még tag.
def tagallamok_szama_2018(lista):
  return len(lista)

tagallamok_szama = tagallamok_szama_2018(lista)
print(f"3. A tagállamok száma 2018-ban: {tagallamok_szama}")
#--------------------------------------------------------


# 4. Csatlakozások száma az adott évben (bemenő paraméter az adatokat tartalmazó lista  és az adott év)
def csatlakozasok_szama_az_evben(lista, ev):
  return len([sor for sor in lista if sor.ev == ev])
  """
  csatlakozasok = 0
  for sor in lista:
    if sor.ev == ev:
      csatlakozasok += 1
  return csatlakozasok
  """
csatlakozasok_2007 = csatlakozasok_szama_az_evben(lista, 2007)
print(f"4. Csatlakozások száma 2007-ben: {csatlakozasok_2007} ")
#--------------------------------------------------------


# 5. Csatlakozások száma az adott hónapban (bemenő paraméter az adatokat tartalmazó lista  és a adott hónap)
def csatlakozasok_szama_a_honapban(lista, honap):
    return len([sor for sor in lista if sor.honap == honap]) 

csatlakozasok_majus = csatlakozasok_szama_a_honapban(lista, 5)
print(f"5. Csatlakozások száma májusban: {csatlakozasok_majus} ")
#--------------------------------------------------------


# 6. Egy adott ország csatlakozási dátuma. (Bemenő paraméter az adatokat tartalmazó lista  és az adott ország.)
def orszag_csatlakozasi_datuma(lista, orszag):
  return [sor.datum for sor in lista if sor.orszag == orszag][0]
  
magyarorszag_datuma = orszag_csatlakozasi_datuma(lista, 'Magyarország')
print(f"6. Magyarország csatlakozási dátuma: {magyarorszag_datuma}")
#--------------------------------------------------------
# 7. Melyik ország csatlakozott utoljára?
def utoljara_csatlakozott_orszag(lista):
  szamlalo = ""
  orszag = ""
  for sor in lista:
    if sor.datum > szamlalo:
      szamlalo = sor.datum
      orszag = sor.orszag
  return orszag


  
print(
    f"7. Utoljára csatlakozott ország neve: {utoljara_csatlakozott_orszag(lista)} "
)
#--------------------------------------------------------


# 8. Mely hónapban csatlakozott a legtöbb ország? (Bemenő paraméter az adatokat tartalmazó lista, visszatérési érték a hónap integer típusként.)
def legtobb_csatlakozas_honapja(lista):
   stat = dict()

   for sor in lista:
     stat[sor.honap] = stat.get(sor.honap, 0) + 1
   return max(stat, key=stat.get)



print(
    f"8. A legtöbb ország a következő hónapban csatlakozott: {legtobb_csatlakozas_honapja(lista)}"
)
#--------------------------------------------------------


# 9. A megadott évben hány tagállama volt az Eu-nak?
def tagallamok_szama_az_adott_evben(lista, ev):
  tagok =  0
  for sor in lista:
    if sor.ev <= ev:
      tagok += 1
  return tagok


  
print(
    f"9. A tagállamok száma 2000-ben: {tagallamok_szama_az_adott_evben(lista, 2000)}"
)
