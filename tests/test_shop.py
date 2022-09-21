import pytest
from shop import Shop
from shop_item import SmallHealingPotion, WeaponUpgrade

@pytest.fixture
def shop():
    return Shop("tests/test_shop.txt")

def test_shop_str(shop):
    message = '\n'.join([
        "Welcome to the shop. The following items are available:",
        "1 - small healing potion (1 gold)",
        "2 - big healing potion (3 gold)",
        "3 - small healing potion (1 gold)",
        "4 - small healing potion (1 gold)",
        "5 - weapon upgrade (1 gold)",
    ])
    assert str(shop) == message

def test_shop_init(shop):
    # 3 small potions + 1 large + 1 weapon upgrade
    assert len(shop) == 5

def test_shop_first(shop):
    item = shop.buy(0)
    assert type(item) == SmallHealingPotion

def test_shop_last(shop):
    item = shop.buy(len(shop)-1)
    assert type(item) == WeaponUpgrade

def test_shop_buy_all(shop):
    # Buy all the items
    while len(shop.available_items):
        # We buy the first one every time
        shop.buy(0)

    assert len(shop) == 0

def test_shop_invalid_item(shop):
    with pytest.raises(IndexError):
        shop.buy(10)
