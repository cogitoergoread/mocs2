"""
Kártyák definíciója
"""
from enum import IntEnum, unique
from functools import total_ordering


@unique
class Szinek(IntEnum):
    """
    Francia kártya színek
    """
    KARO = 0
    PIKK = 1
    KOR = 2
    TREFF = 3
    JOKER = 4

    def __str__(self):
        """
        Stringgé alakítja az értéket.
        :return: Szín Unicode karakterként
        """
        return ['\u2662', '\u2660', '\u2661', '\u2663', '*'][self.value]


# Default konstruktor átdefiniálása
# https://stackoverflow.com/questions/24105268/is-it-possible-to-override-new-in-an-enum-to-parse-strings-to-an-instance
def _Szinek_konstruktor(cls, value):
    if not isinstance(value, str):
        # forward call to 'Szinek' superclass (enum.Enum)
        return super(Szinek, cls).__new__(cls, value)
    else:
        # map strings to enum values, default to Unknown
        return {'\u2662': Szinek.KARO,
                '\u2660': Szinek.PIKK,
                '\u2661': Szinek.KOR,
                '\u2663': Szinek.TREFF,
                '*': Szinek.JOKER}.get(value)


setattr(Szinek, '__new__', _Szinek_konstruktor)


@unique
class Ertekek(IntEnum):
    """
    Francia kártya értékek
    """
    C2 = 0  # 2-es lap ....
    C3 = 1
    C4 = 2
    C5 = 3
    C6 = 4
    C7 = 5
    C8 = 6
    C9 = 7
    C0 = 8  # 10
    CJ = 9  # Jumi
    CD = 10  # Dáma
    CK = 11  # Király
    CA = 12  # Ász
    CO = 13  # Joker

    def __str__(self):
        """
        Stringgé alakítja az értéket.
        :return: Szín Unicode karakterként
        """
        return '234567890JDKA*'[self.value]


def _Ertekek_konstruktor(cls, value):
    if not isinstance(value, str):
        # forward call to 'Szinek' superclass (enum.Enum)
        return super(Ertekek, cls).__new__(cls, value)
    else:
        # map strings to enum values, default to Unknown
        return {'234567890JDKA*'[k]: Ertekek(k) for k in range(14)}.get(value)


setattr(Ertekek, '__new__', _Ertekek_konstruktor)


@total_ordering
class Kartya:
    """
    Kártya lapokat reprezentáló osztály
    """
    szin: Szinek
    ertek: Ertekek  # Ez az effektív érték, Kinevezett Joker esetén Joker pl., Körönként változhat
    lap: Ertekek  # Ez a kártya lap megjelenítendő értéke, nem változik

    def __init__(self, krty):
        """
        Egy kártya lapot példányosít
        :param krty: Vagy egy kettő hosszú str ('♣3'), vagy egy két tagú tuple (0,8) Szín, Érték
        """
        # Stringből vagy tuple-ből konstruálunk, ugyanaz!
        self.szin = Szinek(krty[0])
        self.ertek = Ertekek(krty[1])
        self.lap = self.ertek

    def __str__(self) -> str:
        return (self.szin.__str__() + self.lap.__str__())

    def __repr__(self):
        return "Kártya(Szin:{}, Érték:{}, Lap:{})".format(self.szin, self.ertek, self.lap)

    def __eq__(self, other):
        if type(other) is type(self):
            return self.ertek == other.ertek
        return False

    def __lt__(self, other):
        if type(other) is type(self):
            return self.ertek < other.ertek
        return NotImplemented

    def mapJoker(self, ertek: Ertekek):
        """
        Joker átnevezést végez, Ha törölni akarjuk, akkor Ertekek.CJ hívás kell
        :param ertek: ez a kártya lap lesz még Joker
        :type ertek: Ertekek
        """
        if self.lap == ertek:
            # Kell Joker átnevezés, pont ez egy Joker
            self.ertek = Ertekek.CO
        else:
            self.ertek = self.lap
