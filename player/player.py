"""
Aalap Játékos osztály. Absztrakt osztály.
Tényleges játékosoknak ebből kell származnia.
"""
from typing import List


class MPlayer:
    def __init__(self, name:str, id:int):
        """
        Konstruktor
        :param name: Játékos neve
        :param id: Játékos azonosítója
        """
        pass

    def osztottLapotKap(self, lapok: List[str]):
        """
        Bejegyzi, hogy osztáskor milyen lapokat kapott.
        :param lapok: Osztáskor kapott lapok. Lista, melynek tagja kettő hossz stringek, kártyák reprezentálására.
        """
        pass

    def sorrendetKap(self, sorrend: List[int]):
        """
        Ilyen sorrendben következnek az ID-k.
        :param sorrend: egészek rendezett listája. Ilyen sorrendben következnek a játékosok.
        """
        pass

    def korbenLapotAd(self, lapok:List[str]) -> List[str]:
        """
        Egy körben a játékos a következő. Előtte a 'lapok' kártyák vannak az asztalon.4
        Most kell tennie a kezében levő lapok közül.
        Ha lapok is None, akkor azt twaz, amit akar, mert ő az első.
        Az a szabály, hogy annyi darabot kell tennie, amennyi elemű 'lapok', csak nagyobb értékben.
        :param lapok: Lista, melynek tagja kettő hossz stringek, kártyák reprezentálására.
        :return: Lista, melynek tagja kettő hossz stringek
        """
        pass

    def korEsemnytKap(self, jatekos: int, lapok: List[str], befejezte: bool, korVege:bool):
        """
        Játékos regisztrálhatja, hogy mi történt a körben épp most.
        Ha jatekos = self.id, akkor saját magáról van szó, ki kell adnia a kezéből a lapkokat.
        Ha nem magáról van szó, akkor bejegyezheti a történetbe, hogy milyen lapk mentek ki.
        :param jatekos: Játékos ID, aki éppen tett.
        :param lapok: Ezeket a lapokat adta ki. None esetén passzolt.
        :param befejezte: True, épp elfogytak a lapjai
        :param korVege: True, véget ért a kör. Akkor lehet vége, ha az utolsó tétel után n tagú körben volt n-1 pass.
        """
        pass