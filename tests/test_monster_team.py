import pytest
from monster_team import MonsterTeam
from monster_custom import Wolf, Giant, Magician

@pytest.fixture
def typical_team():
    """ Creates a custom team for test purposes
    2x wolf, level 5: 60 health, 25 power
    1x giant, level 4: 25 health, 40 power
    1x magician: 20 health, 0 power
    """
    wolf_1 = Wolf(5)
    wolf_2 = Wolf(5)
    giant = Giant(4)
    magician = Magician(1)
    team = MonsterTeam(1)
    team._monsters = [wolf_1, wolf_2, giant, magician]

    return team

def test_team_level_1():
    team = MonsterTeam(1)
    assert len(team) == 1

def test_team_level_1():
    team = MonsterTeam(1)
    assert type(team._monsters[0]) == Wolf

def test_alive_monsters():
    team = MonsterTeam(1)
    assert len(team.alive_monsters) == 1
    assert type(team.alive_monsters[0]) is Wolf

def test_sorted_team():
    team = MonsterTeam(1)
    monster = Giant(10)
    team._monsters.append(monster)
    first_sorted = team.alive_monsters[0]
    assert type(first_sorted) == Giant
    assert first_sorted.health == 55

def test_team_healthiest_monster():
    team = MonsterTeam(1)
    monster = Wolf(10)
    team._monsters.append(monster)
    assert team.healthiest_monster == monster

def test_weakest_monster():
    team = MonsterTeam(1)
    monster = Wolf(1)
    monster.power = 0
    team._monsters.append(monster)
    assert team.weakest_monster == monster

def test_team_health(typical_team):
    assert typical_team.health == 165

def test_team_power(typical_team):
    assert typical_team.power == 90

    typical_team._monsters[0].health = 0
    assert typical_team.power == 65

def test_team_str(typical_team):
    output = "\n".join([
        "4/4 monsters:",
        "Wolf (60.00 health, 25.00 power)",
        "Wolf (60.00 health, 25.00 power)",
        "Giant (25.00 health, 40.00 power)",
        "Magician (20.00 health, 0.00 power)",
    ])
    assert str(typical_team) == output

def test_team_str_dead(typical_team):
    typical_team._monsters[0].health = 0
    typical_team._monsters[3].health = 0

    output = "\n".join([
        "2/4 monsters:",
        "Wolf (60.00 health, 25.00 power)",
        "Giant (25.00 health, 40.00 power)",
        "Wolf (DEAD)",
        "Magician (DEAD)",
    ])
    assert str(typical_team) == output

def test_team_is_alive(typical_team):
    assert typical_team.is_alive is True

    for m in typical_team._monsters:
        m.health = 0

    assert typical_team.is_alive is False

def test_team_next_turn(typical_team):
    typical_team.next_turn()
    assert typical_team._monsters[0].power == 27        # 25 + 2 (2 wolves)
    assert typical_team._monsters[1].power == 27
    assert typical_team._monsters[0].health == 66       # 60 + 10% (magician)
    assert typical_team._monsters[1].health == 66
    assert typical_team._monsters[2].health == 27.5     # 25 + 10% (magician)
    assert typical_team._monsters[3].health == 20       # magician stays the same

def test_team_next_turn_dead_magician(typical_team):
    # Kill one wolf
    typical_team._monsters[0].health = 0
    # Kill the magician
    typical_team._monsters[3].health = 0

    typical_team.next_turn()
    # No health from dead magician
    assert typical_team._monsters[1].health == 60
    # No boost from wolves (only 1 in the team)
    assert typical_team._monsters[1].power == 25

def test_team_next_turn_dead_monster(typical_team):
    # Kill a wolf
    typical_team._monsters[0].health = 0
    typical_team.next_turn()

    # Make sure the magician did not revive a dead monster
    assert typical_team._monsters[0].is_alive is False