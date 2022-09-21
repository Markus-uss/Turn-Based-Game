import pytest
from hero import Hero
from shop_item import ShopItem, BigHealingPotion, SmallHealingPotion, WeaponUpgrade

@pytest.fixture
def tim():
    hero = Hero("Tim")
    hero.health = 10
    return hero

def test_small_healing_potion(tim):
    potion = SmallHealingPotion()
    assert isinstance(potion, ShopItem)
    potion.change(tim)
    assert tim.health == 20

def test_big_healing_potion(tim):
    potion = BigHealingPotion()
    assert isinstance(potion, ShopItem)
    potion.change(tim)
    assert tim.health == 60

def test_weapon_upgrade(tim):
    item = WeaponUpgrade()
    assert isinstance(item, ShopItem)
    item.change(tim)
    assert tim.power == 52.5