import pytest
from monster_custom import Wolf, Giant, Magician

def test_wolf_level():
    monster = Wolf(0)
    assert monster.health == 10
    assert monster.power == 0

    monster = Wolf(2)
    assert monster.health == 30
    assert monster.power == 10

def test_magician_level():
    monster = Magician(10)
    assert monster.health == 20
    assert monster.power == 0

def test_giant_level():
    monster = Giant(2)
    assert monster.health == 15
    assert monster.power == 20

def test_monster_invalid_level():
    with pytest.raises(AttributeError):
        Wolf("1")
    with pytest.raises(AttributeError):
        Magician("1")
    with pytest.raises(AttributeError):
        Giant("1")

def test_wolf_is_alive():
    monster = Wolf(0)
    assert monster.is_alive

    monster.health = 0
    assert monster.is_alive is False

def test_wolf_str():
    monster = Wolf(2)
    assert str(monster) == "Wolf (30.00 health, 10.00 power)"

def test_giant_str():
    monster = Giant(2)
    assert str(monster) == "Giant (15.00 health, 20.00 power)"

def test_giant_str_dead():
    monster = Giant(2)
    monster.health = 0
    assert str(monster) == "Giant (DEAD)"

def test_wolf_lt():
    wolf1 = Wolf(1)
    wolf2 = Wolf(2)

    assert wolf1 < wolf2

def test_wolf_giant_lt():
    wolf = Wolf(2)
    giant = Giant(2)

    assert giant < wolf

def test_magician_lt_invalid_type():
    magician = Magician(1)
    with pytest.raises(TypeError):
        magician < 10

    with pytest.raises(TypeError):
        magician < list()
