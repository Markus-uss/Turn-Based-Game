import pytest
from hero import Hero
from monster_custom import Wolf
from monster_team import MonsterTeam

@pytest.fixture
def tim():
    return Hero("Tim")

@pytest.fixture
def team():
    # We create a team with just one wolf, level 5
    monster = Wolf(5)
    team = MonsterTeam(1)
    team._monsters = [monster]
    return team

# def test_hero_attack(tim, team):
#     tim.attack(team)

#     assert tim.health == 75     # 100 - 25
#     assert team._monsters[0].health == 10 # 60 - 50

# def test_hero_lethal_attack(tim, team):
#     team._monsters[0].health = 1
#     tim.attack(team)

#     assert team.is_alive is False

# def test_hero_block(tim, team):
#     tim.block(team)
#     assert tim.health == 100 - (25 * 0.3)       # 30% damage from monster
#     assert team._monsters[0].health == 60 - (50 * 0.5)    # 50% damage to monster
