import pytest
import cards
from pytest_steps import test_steps

@pytest.mark.parametrize('szov, ertek', [
    ('♢', 0),
    ("♠", 1),
    ('♡', 2),
    ('♣', 3),
    ('*', 4)
])
def test_ertek_int(szov, ertek):
    """
    Kártya színek tesztelése int konstruktorral
    """
    karty = cards.Szinek(ertek)
    assert karty.__str__() == szov

@pytest.mark.parametrize('szov, ertek', [
    ('♢', 0),
    ("♠", 1),
    ('♡', 2),
    ('♣', 3),
    ('*', 4)
])
def test_ertek_str(szov, ertek):
    """
    Kártya színek tesztelése str konstruktorral
    """
    karty = cards.Szinek(szov)
    assert karty.value == ertek

@pytest.mark.parametrize('szov, ertek', [('234567890JDKA*'[k], k) for k in range(14)])
def test_szinek_int(szov, ertek):
    """
    Kártya értékek tesztelése int konstruktorral
    """
    karty = cards.Ertekek(ertek)
    assert karty.__str__() == szov

@pytest.mark.parametrize('szov, ertek', [('234567890JDKA*'[k], k) for k in range(14)])
def test_szinek_str(szov, ertek):
    """
    Kártya értékek tesztelése str konstruktorral
    """
    karty = cards.Ertekek(szov)
    assert karty.value == ertek

testdata_init = [
    pytest.param((cards.Szinek.PIKK, cards.Ertekek.C2), '\u26602', "Kártya(Szin:1, Érték:0, Lap:0)", id="Pikk kettes"),
    pytest.param((cards.Szinek.TREFF, cards.Ertekek.C3), '♣3', "Kártya(Szin:3, Érték:1, Lap:1)", id="Treff harmas"),
    pytest.param( '♣3', '♣3', "Kártya(Szin:3, Érték:1, Lap:1)", id="Szinbol Treff harmas")
]
@pytest.mark.parametrize("krty, szoveg, reprez", testdata_init)
def test_init(krty, szoveg, reprez):
    k1 = cards.Kartya(krty)
    if  not isinstance(krty, str):
        assert krty[1] == k1.ertek
        assert krty[0] == k1.szin
    else:
        pass # Ilyenkor nincs tipp, mi lehet.


@pytest.mark.parametrize("krty, szoveg, reprez", testdata_init)
def test_str(krty, szoveg, reprez):
    k1 = cards.Kartya(krty)
    assert szoveg == k1.__str__()


@pytest.mark.parametrize("krty, szoveg, reprez", testdata_init)
def test_repres(krty, szoveg, reprez):
    k1 = cards.Kartya(krty)
    assert reprez == k1.__repr__()

@pytest.mark.parametrize('k1, k2', [((1,'234567890JDKA*'[k]), (2,'234567890JDKA*'[k])) for k in range(14)])
def test_eq(k1, k2):
    assert cards.Kartya(k1) == cards.Kartya(k2)

@pytest.mark.parametrize('k1, k2', [((1,'234567890JDKA*'[k]), (2,'234567890JDKA*'[k+1])) for k in range(13)])
def test_neq_lt(k1, k2):
    kr1, kr2 = cards.Kartya(k1) , cards.Kartya(k2)
    assert kr1 != kr2
    assert kr1 < kr2

@test_steps('Map_elott', 'Mapelve', "Resetelve")
def test_map_eq():
    k1, k2, k3, k4 = (cards.Kartya('♠2'), cards.Kartya('♣3'), cards.Kartya('♡2'), cards.Kartya("**"))
    # Első teszt, map nélküli állapot
    assert k1 == k3 # Map nélkül egyformák
    assert k1 >= k3 # Mivel egyformák
    assert k2 > k3
    assert k4 != k3
    yield

    # Második teszt map
    k3.mapJoker(cards.Ertekek.C2)
    assert k1 != k3 # Nem sima lap
    assert k1 < k3  # Sima lappknál nagyobb a mapelt
    assert k2 < k3
    assert k4 == k3
    yield

    # Hamradik teszt, reset joker map
    # Joker reset, 2-es nem Joker
    k3.mapJoker(cards.Ertekek.CO)  # Reset
    assert k1 == k3 # Map nélkül egyformák
    assert k1 >= k3 # Mivel egyformák
    assert k2 > k3
    assert k4 != k3
    yield