from monster import Monster


class Hero:
    # The HP percents that the hero wil gain back - 50%
    HEALING_PERCENTS = 1.5
    # The damage points that the hero wil gain back - 20%
    DAMAGE_PERCENTS = 1.5
    # The power by which the coin level grows in order to level up- times 3
    UPGRADE_COIN_POWER = 2
    # Reduces damage when hero chooses to defend- 80%
    PROTECTION_PERCENTS = 0.8

    def __init__(self, hero_name: str) -> None:
        """
        Initializes hero character
        """
        self.hero_name = hero_name
        self.hp = 10
        self.damage = 2
        self.level = 1
        self.coins = 0

    def heal(self) -> None:
        """
        The function raises the hero's hp by the defined healing percents
        """
        self.hp = self.hp * Hero.HEALING_PERCENTS
        print(
            f"Just like magic, you have gained back your strength. You now have {self.hp} lives"
        )

    def level_up(self) -> None:
        """
        The function checks if the hero can level up based on their coins
        If so, the function upgrades the hero
        """
        if (self.level + 1) ** Hero.UPGRADE_COIN_POWER < self.coins:
            self.damage = self.damage * Hero.DAMAGE_PERCENTS
            self.hp = self.hp * Hero.HEALING_PERCENTS
            print(
                f"Successful level up! Upgrade stats: {self.hp} lives left and {self.damage} damage points"
            )
            self.level += 1

    def attack(self, current_monster: Monster):
        """
        The function attacks the monster and reduces its lives
        If it has no more lives, the function creates and returns a new monster
        Else, it returns none
        """
        monster_lives = current_monster.reduce_health(self)
        print(f"Amazing! The monster has {current_monster.hp} lives left")
        if monster_lives == 0:
            self.increase_coins(self.level)
            return Monster(f"Monster {current_monster.level + 1}", self.level)
        else:
            return None

    def defend(self, received_damage: int) -> None:
        """
        The function receives a certain amount of damage points
        The function reduces the damage points to the hero's stash
        """
        self.hp -= received_damage * Hero.PROTECTION_PERCENTS

    def increase_coins(self: object, received_coins: int) -> None:
        """
        The function receives a certain amount of coins
        The function adds the coins to the hero's stash
        """
        self.coins += received_coins

    def reduce_health(self, current_monster: Monster, chosen_action: int):
        """
        The function receives the playing hero, monster, and the hero's action
        The function reduces the hero's hp according to the monster's damage and hero's action
        The function returns the hero's life count
        """
        if chosen_action == 2:
            Hero.defend(self, current_monster.damage)
            if self.hp <= 0:
                print("Seems like you don't have any more lives")
            else:
                print(f"\nWonderful defense! You now have {self.hp} lives left")
        else:
            self.hp -= current_monster.damage
            if self.hp < 0:
                self.hp = 0
            print(
                f"\nWatch out, you're under attack! You now have {self.hp} lives left"
            )
        return self.hp

    def to_str(self, current_monster: Monster) -> None:
        """
        Function receives a hero and monster
        The function prints all the relevant details for this round
        """
        print(
            f"You have {self.hp} lives, {self.coins} coins, and you're at level {self.level}.\
        \nPrepare to face {current_monster.monster_name}\
        \n\nMonster stats: \
        \nName: {current_monster.monster_name}\
        \nLevel: {current_monster.level}\
        \nDamage: {current_monster.damage}\
        \nHP: {current_monster.hp} "
        )
