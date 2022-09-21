import pytest
from hero import Hero
from monster import Monster

@pytest.fixture
def tim():
    return Hero("Tim")

def test_hero_attributes(tim):
    assert tim.name == "Tim"
    assert tim.power == 50
    assert tim.health == 100

    # Remove these attributes
    assert not hasattr(tim, "heal")
    assert not hasattr(tim, "prestige")

def test_hero_is_alive(tim):
    assert tim.is_alive

    tim.health = 0
    assert tim.is_alive is False

def test_attack_invalid_type(tim):
    with pytest.raises(TypeError):
        tim.attack(Monster(1))

def test_block_invalid_type(tim):
    with pytest.raises(TypeError):
        tim.block(Monster(1))
