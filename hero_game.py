from monster import Monster
from hero import Hero

hero_name = input("Welcome to the Hero Game! What is your heroine's name? ")
heroine = Hero(hero_name)
fighting_monster = Monster(f"Monster 1", heroine.level)
heroine.to_str(fighting_monster)
while heroine.hp > 0:
    chosen_action = Monster.choose_action()
    match chosen_action:
        case 1:
            attack_outcome = heroine.attack(fighting_monster)
            if attack_outcome is not None:
                fighting_monster = attack_outcome
                # Heroine receives another coin every round
                heroine.increase_coins(1)
                heroine.to_str(fighting_monster)
                continue
        case 3:
            heroine.level_up()
        case 4:
            heroine.heal()
        case -1:
            continue
    fighting_monster.attack(heroine, chosen_action)
    # Heroine receives another coin every round
    heroine.increase_coins(1)
print(f"You have lost the game. Your level was {heroine.level}. Try again!")
