"""
3.feladat:
Az UTF-8_as karakterkodolású "solsys.txt" állomány (file) tartalmazza naprendszerünk bolygóinak néhány adatát. A sorok azonos szerkezetűek, az adattagok pontosvesszővel vannak elválasztva. Az állomány egy sora például:

            Mars;2;0.151

Ahol az adattagok jelentése rendre a következő:
  - A bolygó neve: [Mars]
  - A holdjainak száma: [2]
  - A bolygó térfogatának aránya a Földéhez képest: [0.151]

Hozz létre egy osztályt (class) létrehozása NEM KÖTELEZŐ DE több pontot lehet kapni. Osztály használata esetén, ami reprezentálja egy bolygó példányait (object) istance. Az osztály konstruktora (constructor) paraméterként kapja meg a beolvasott sort, és ebből határozza meg az adott attribútomokat (property). 

3.0 Olvasd be az állomány tartalmát, és tárold le egy homogén listában. Ennek a listának a felhasználásával oldd meg az alábbi feladatokat, a kiírás legyen a mintának megfelelő!

3.1: Írd ki a terminálra, hogy hány bolygó adatai szerepelnek az állományban!

3.2: Írd ki a terminálra, hogy a listában szereplő bolygóknak hány holdja van átlagosan!

3.3: Írd ki a terminálra a legnagyobb térfogatú bolygó nevét.

3.4: Kérj be a terminálról egy karakterláncot! Határozd meg, hogy van-e ilyen nevű bolygó a listában!

3.5: Kérj be egy pozitiv egész számot a terminálról! Írd ki azon bolygók neveit, melyeknek több holdja van, mint a beírt szám!

Minta/output: _____________________________________________________

3. feladat:
     3.1: 8 bolygó van a naprendszerben
     3.2: a naprendszerben egy bolygónak átlagosan 25.75 holdja van
     3.3:a legnagyobb térfogatú bolygó a Jupiter
     3.4: írd be a keresett bolygó nevét: Plútó
             sajnos nincs ilyen nevű bolygó a naprendszer
     3.5: Írj be egy egész számot: 10
     a következő bolygókank 10-nál/nél több holdja:
     ['Jupiter', 'Szaturnusz', 'Uránusz', 'Neptunusz']

___________________________________________________________________


"""
#0
# Merkúr;0;0.0562
class Bolygok:
  def __init__(self,sor):
    nev,holdszam,terfogat_arany = sor.strip().split(";")
    self.nev = nev
    self.holdszam = int(holdszam)
    self.terfogat_arany = float(terfogat_arany)

with open("solsys.txt","r",encoding="UTF-8") as f:
  lista = [Bolygok(sor) for sor in f]

#1
  
print("3. feladat:")
print(f"     3.1: {len(lista)} bolygó van a naprendszerben")

