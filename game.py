#Author: Markus Lu A01224733

from monster_team import MonsterTeam
from hero import Hero
from monster import Monster
from shop import Shop
from story import get_lvl_message

def main():
    #Receive hero name, and create new hero.
    name = input("\nWhat is your hero's name? ")
    hero = Hero(name)
    shop = Shop()
    repeated_dialogue = False

    lvl = 1 #Preps monster level for loop

    #While the hero is alive, a new monster will appear, increasing in level each time
    while hero.is_alive != False and lvl < 9:

        #Gives user story to read, waits for any input before continuing.
        if hero.obtained_token == False and repeated_dialogue == False:
            get_lvl_message(lvl)
            continue_confirmation = input('Enter any key to continue: ')
            repeated_dialogue = True

        #Level 1 is repeated until token is bought.
        elif hero.obtained_token == True:
            lvl += 1
            get_lvl_message(lvl)
            continue_confirmation = input('Enter any key to continue: ')

        #Loop ends after reaching level 9.
        if lvl < 9:
            print(f'\n[LEVEL {lvl}]' + '-'*40)
            print('\nA monster appears!')
            monsters = MonsterTeam(lvl)

            #Loops the fight between hero and monster until one dies(0 health points).
            while monsters.is_alive != False and hero.is_alive != False:
                print(f'\n[Hero] {hero.get_description()}\n')
                print(str(monsters))

                #User inputs action, attack(a), block(b), dodge(d) shop(s), monster responds accordingly.
                print(f'\n[A]ttack ({hero.power} DMG), [B]lock ({int(round((hero.power*0.5),1))} DMG), [D]odge ({100-(10*hero.dodge_stack)}%), [S]hop')
                action = input('Choose your action: ')
                if action.lower() == 'a':
                    hero.attack(monsters)
                    monsters.next_turn()
                elif action.lower() == 'b':
                    hero.block(monsters)
                    monsters.next_turn()
                elif action.lower() == 'd':
                    hero.dodge(monsters)
                    monsters.next_turn()

                #Shop interaction
                elif action.lower() == 's':
                    buy_option = 'Pending'
                    while str(buy_option).lower() != 'e':
                        print(f'\n[LEVEL {lvl}]' + '-'*40)
                        if len(shop) > 0:
                            print('\n' + str(shop))
                        else:
                            print("\nI'm out of stock. ;(")
                        print(f"\nYou have {hero.gold} gold.")
                        buy_option = input('\nChoose your action: [1-5]Buy item, [E]xit: ')
                        if buy_option.isdigit() == True and 0 < int(buy_option) <= len(shop):
                            buy_option = int(buy_option) - 1
                            if hero.gold >= shop.items[buy_option].price:
                                shop_item = shop.buy(buy_option)
                                hero.gold -= shop_item.price
                                shop_item.change(hero)
                                print('\nThank you for your patronage. :-)')
                            else:
                                print(f"You only have {hero.gold} gold?! Give me my gold, and I'll give you business!")
                        elif buy_option.lower() == 'e':
                            print('\nCome back soon. >:-)')
                        else:
                            print("Excuse me?")
                else:
                    print('\nInvalid action.')
            
            #Gold earned after killing all the monsters on a floor.
            hero.gold += len(monsters._monsters)

    #Prints the user score.
    if lvl == 9:
        print('\n[WINNER]' + '-'*40)
        print('\nYou have successfully beat all 9 circles and rescued your wife from Hades.')
        print('\nYou and your wife live happily ever after. ;-)\n')

    else:
        print('\n[GAME OVER]' + '-'*40)
        print('\nThe hero collapses!\n')
        print(f'Your hero has survived {lvl} circles')

main()