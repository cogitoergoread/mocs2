# Visegrádi jegyzetek

## Asztal

-  Hány játékos van, és hány kártyalap
- Leoszt a játékosoknak kártyát
- Levezényli a köröket
- Adminisztrálja az eredményt
- Két üzemmódja van:
   1. Koordinálja a játékot
   2. Fogadja kivülről az infromációkat
- Algoritmusa:
    - Amíg vant kint kártya
        - Játékosokra, sorrendben lép
            - Lapot kér a játékostól, amíg jót nem ad
            - Kiértékeli, ellenőrzi az adott lapot.
            - Megnézi, kiment-e a játékos
            - Megnézi, vége van-e a körnek
 - Mentse le a játszmát. FÁjlba. Json.
    - ordered list, játékosok
    - dict: játékos, kártya
    - ordered list: játékosok sorrendje
    - List: lerakott lapok
        - \# sorszám
        - játékos
        - kártáyák
        - Játékosnak elfogyott?
        - Kör vége?
 
 ## GUI
 - Fogadja a játékosokat, sorrendet
 - Fogadja a kártyákat
 - Fogadja a lap publikációt az asztaltól
 - Mondjuk History fájlból le tud játszani egy partit.
 - PyGame
     - Meg kellene nézni a Python - pygame - pygame cards képességeit
     - 1-4 játékosra jó.
     - Ha nehéz, akkor az egyszerűbb, nem pyGame, kártyákat forgatni kell esetleg
     - Mondjuk Enterre tovább megy
  - Json fájl az IF, definiálni kell, és lehet függetlenedni.
## Játékos
- Képességek:
    - n-tuple bontás
    - jokerrel bővítés
    - Nem kell magassal ütni, ha utána biztos ütő van
    - Esetleg ezek valószínűségei
- Szintek:
    - Naive, ha tud, üt. Hívja a legkisebbet
    - History + MiniMax
    - Monte Carlo
    - Reinforcement Learning
- MiniMax lépések
    - Ha ismertek a lapok, akkor tudjon végjátékot játszani
    - Nem ismert lapokra valószínűségekkel megadni
- History megvalósítása
    - Kiment lapot le kell venni a játékostól.
    - Ha x lappal ütött, de x-1 lappal is lehetett volna:
        - nincs x-1 lapja
        - van x-1 lapja, de nem ilyen tuple tagja
        - direkt nem azt tette.
        - Biztosan ütni akart magassal
    - Adat ábrázolás: {játékos ID: cards in hand}
    - Én lapjaim, kiment lapok, hátralévő lapok 


# Körös feladat
- r sugar körök, 6r oldalú négyzet csúcsában 4 körlap
- kb 20 körlap eldobálva véleteln koordinátákkal
- 2 körlap lehet alatta - felette relációban
- Mi a körlapok sorrendje?