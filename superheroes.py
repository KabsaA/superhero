import random
class Ability:
    def __init__(self, name, attack_strength):
          self.name = name
          self.max_damage = 100
          self.attack_strength = attack_strength
       # TODO: Instantiate the variables listed in the docstring with then
       # values passed in
      #self.attack_strength = attack_strength
    def attack(self):
      #''' Return a value between 0 and the value set by self.max_damage.'''
      # TODO: Use random.randint(a, b) to select a random attack value.
        return random.randint(0,self.max_damage)
      # Return an attack value between 0 and the full attack.


class Weapon(Ability):
    def attack(self):
        return random.randint(self.attack_strength * (0.5), self.attack_strength)

class Armor:
    def __init__(self, name, max_block):
    #Instantiate instance properties.
            self.name = name
            self.max_block = max_block
        # TODO: Create instance variables for the values passed in.
    def block(self):
            #Return a random value between 0 and the initialized max_block strength.
            return (random.randint(0,self.max_block))
      # TODO: This method should run Ability.attack() on every ability
      # in self.abilities and returns the total as an integer.
class Hero:
    def __init__(self, name):
          self.weapons = []
          self.abilities = []
          self.armors = []
          self.name = name
          self.current_health = 100
          self.deaths = 0
          self.kills = 0

    def add_kill(self, numKills):
        # This method should add the number of kills to self.kills
        self.kills += numKills
        return self.kills

    def add_deaths(self, numDeaths):
        #''' Update deaths with num_deaths'''
        # This method should add the number of deaths to self.deaths
        self.deaths += numDeaths
        return self.deaths

    def add_weapon(self, weapon):
        self.weapons.append(weapon)
    def add_ability(self, ability):
        self.abilities.append(ability)
    def attack(self):
        total = 0
        for ability in self.abilities:
            total += Ability.attack(ability)
        return total

    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self,incoming_damage):
        total = 0
        for armor in self.armors:
            total+= int(armor.block())
        return total + incoming_damage


    def take_damage(self,damage):
        newCurrent = self.current_health
        defense = self.defend(damage)
        self.current_health = newCurrent - defense

    def is_alive(self):
        if self.current_health > 0:
            return True
        else:
            return False

    def fight(self,opponent):
        fighting = True
        while fighting:
            if self.is_alive() == True:
                gotHit = self.attack()
                opponent.take_damage(gotHit)
                #print(str(self.name) + " won!")
            else:
                break
            if opponent.is_alive() == True:
                oppAttack = opponent.attack()
                self.take_damage(oppAttack)
                #print(str(self.name) + " won!")
            else:
                break
                fighting = False
        if opponent.is_alive() == False:
            self.add_kill(1)
            opponent.add_deaths(1)
            print(str(self.name) + " wins!")
        else:
            self.add_kill(1)
            self.add_deaths(1)
            print(str(opponent.name) + " wins!")

class Team(Hero,Ability):

        def __init__(self, name):
            self.heroes = []
            self.name = name

        def remove_hero(self, name):
            for item in self.heroes:
                if item.name == name:
                    self.heroes.remove(item)
                    return self.heroes

        def view_all_heroes(self):
            for item in self.heroes:
                print(item.name)

        def add_hero(self, new_hero):
            self.heroes.append(new_hero)

        def attack(self, other_team):
            hero1 = random.choice(self.heroes)
            hero2 = random.choice(other_team.heroes)
            hero1.fight(hero2)


        def revive_heroes(self, health=100):
            for hero in self.heroes:
                hero.current_health = health

        def stats(self):
            for hero in self.heroes:
                print(str(hero.name) + "has " + str(hero.kills) + " and " + str(hero.deaths))
                #print("Hello")

class Arena(Team,Ability):
    def __init__(self):
        self.team_one = None
        self.team_two = None
        self.winning_team = None

    def create_ability(self):
        addedAbility = input("Add ability for hero: ")
        damageAmount = input("Damage amount is : ")
        Ability(addedAbility,damageAmount)

    def create_weapon(self):
        addWeapon = input("Add weapon for hero: ")
        weaponDamage = input("Damage amount is: ")
        return Weapon(addWeapon, weaponDamage)
        return addWeapon
    def create_armor(self):
        whichArmor = input("Add armor for hero: ")
        blockAmount = input("Block amount is: ")
        return Armor(whichArmor, blockAmount)

    def create_hero(self,hero):
        herosName = input("Enter hero's name: ")
        hero = Hero(herosName)

        addAbilities = input("Do you want to add abilities?(Y/N)")
        if addAbilities == "Y" or addAbilities == "y":
            addAbility = self.create_ability()
            hero.add_ability(addAbility)

        addArmors = input("Do you want to add armor?(Y/N)")
        if addArmors == "Y" or addArmors == "y":
            addArmor = self.create_armor()
            hero.add_armor(addArmor)

        addWeapons = input("Do you want to add weapons?(Y/N)")
        if addWeapons == "Y" or addWeapons == "y":
            addWeapon = self.create_weapon()
            hero.add_weapon(addWeapon)
        return hero

	def build_team_two(self):
		team_name = input("Enter a Team 2 name: ")
		num_of_heroes = int(input("Enter a number of heroes: "))

		self.team_two = Team(team_name)

		for i in range(num_of_heroes):
			self.team_two.add_hero(self.create_hero())


	def team_battle(self):
		self.team_one.attack(self.team_two)



	def show_stats(self):

		if self.team_one.is_all_dead():
			print(self.team_one.name + " is the winner!")
			print("The teams ratio was " + str(self.team_one.get_ratio()))
			for hero in self.team_one.get_alive_heroes():
				print(hero.name)
		else:
			self.team_two.name + " is the winner!"
			print("The teams ratio was " + str(self.team_two.get_ratio()))
			for hero in self.team_two.get_alive_heroes():
				print(hero.name)

if __name__ == "__main__":
    # arena = Arena()
    # arena.build_team_one()
    # arena.build_team_two()
    # arena.team_battle()
    # arena.show_stats()
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()

    # hero1 = Hero("Wonder Woman")
    # hero2 = Hero("Dumbledore")
    # ability1 = Ability("Super Speed", 900)
    # print(Weapon.attack(ability1))
    # ability2 = Ability("Super Eyes", 750)
    # ability3 = Ability("Wizard Wand", 2000)
    # ability4 = Ability("Wizard Beard", 2000)
    # hero1.add_ability(ability1)
    # hero1.add_ability(ability2)
    # hero2.add_ability(ability3)
    # hero2.add_ability(ability4)
    # hero2.fight(hero1)
