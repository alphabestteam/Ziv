import random
#The hero module could not be imported due to circular import issues

class Monster:
    # The ration between the life and level of the monster is 1:2
    PROPORTION_CONSTANT = 2

    def __init__(self, monster_name: str, hero_level: int):
        """
        Initializes monster
        """
        self.monster_name = monster_name
        if hero_level == 1:
            self.level = random.randint(1, 2)
        else:
            self.level = hero_level + random.randint(-1, 1)
        self.hp = self.level * Monster.PROPORTION_CONSTANT
        self.damage = self.level * Monster.PROPORTION_CONSTANT

    def attack(self, game_hero, chosen_action: int) -> int:
        """
        The function receives the playing monster, hero, and the hero's action
        The function calls on reduce_health from Hero class
        The function returns the hero's life count
        """
        hero_lives = game_hero.reduce_health(self, chosen_action)
        return hero_lives

    def reduce_health(self, game_hero) -> int:
        """
        The function receives the playing hero and monster
        The function reduces the monsters's hp according to the hero's damage
        The function returns the monster's life count
        """
        self.hp -= game_hero.damage
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def choose_action() -> int:
        """ 
        Hero enters input based on his choice of action
        The function returns a digit code signifying that action 
        """
        chosen_action = (
            input("What will you do now? Attack, defend, level up or heal?")
        ).upper()
        if chosen_action == "ATTACK":
            return 1
        elif chosen_action == "DEFEND":
            return 2
        elif chosen_action == "LEVEL UP":
            return 3
        elif chosen_action == "HEAL":
            return 4
        else:
            print("No such action exists. Try again")
            return -1
