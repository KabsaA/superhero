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
      attackValue = random.randint(0,self.attack_strength)
      # Return an attack value between 0 and the full attack.
      return attackValue

class Weapon(Ability):
    def attack(self):
        return random.randint(self.attack_strength * (0.5), self.attack_strength)
class Team:
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
            for i in self.heroes:
                for j in self.other_team:
                    i.fight(j)

        #    ''' Battle each team against each other.'''
        # TODO: Randomly select a living hero from each team and have
        # them fight until one or both teams have no surviving heroes.
        # Hint: Use the fight method in the Hero class.


        def revive_heroes(self, health=100):
            for hero in self.heroes:
                hero.current_health = health

        def stats(self):
            for hero in self.heroes:
                print(hero.name + "has " + hero.kills + " and " + hero.deaths)

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
    def __init__(self, name, starting_health=100):
          self.abilities = []
          self.armors = []
          self.name = name
          self.current_health = starting_health
          self.deaths = 0
          self.kills = 0

    def add_kill(self, num_kills):
        # This method should add the number of kills to self.kills
        self.kills += num_kills
        return self.kills

    def add_deaths(self, num_deaths):
        ''' Update deaths with num_deaths'''
        # This method should add the number of deaths to self.deaths
        self.deaths += num_deaths
        return self.deaths
      def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        # TODO: This method will append the weapon object passed in as an
        # argument to self.abilities.
        # This means that self.abilities will be a list of
        # abilities and weapons.
        pass
    def add_armor(self, armor):
    '''Add Armor to self.armors
        armor: Armor Object
    '''
    # TODO: This method will add the armor object that is passed in to
    # the list of armor objects defined in the constructor: `self.armors`.
    pass

       # TODO: Initialize instance variables values as instance variables
       # (Some of these values are passed in above,
       # others will need to be set at a starting value)
       # abilities and armors are lists that will contain objects that we can use
    def add_ability(self, ability):
        #abilities = []
        #for i in ability:
        self.abilities.append(ability)
  #''' Add ability to abilities list '''
  # TODO: Add ability object to abilities:List

           # TODO: Add ability object to abilities:List
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
        if opponent.is_alive() == False:
            self.add_kill(1)
            opponent.add_deaths(1)
            print(str(self.name) + " wins!")
        else:
            self.add_kill(1)
            self.add_deaths(1)
            print(str(opponent.name) + " wins!")
class Arena:
    def __init__(self):
        '''Instantiate properties
            team_one: None
            team_two: None
        '''
        # TODO: create instance variables named team_one and team_two that
        # will hold our teams.
     def create_ability(self):
        '''Prompt for Ability information.
            return Ability with values from user Input
        '''
        # TODO: This method will allow a user to create an ability.
        # Prompt the user for the necessary information to create a new ability object.
        # return the new ability object.
        pass
     def create_weapon(self):
        '''Prompt user for Weapon information
            return Weapon with values from user input.
        '''
        # TODO: This method will allow a user to create a weapon.
        # Prompt the user for the necessary information to create a new weapon object.
        # return the new weapon object.
        pass
     def create_armor(self):
        '''Prompt user for Armor information
          return Armor with values from user input.
        '''
        # TODO:This method will allow a user to create a piece of armor.
        #  Prompt the user for the necessary information to create a new armor
        #  object.
        #
        #  return the new armor object with values set by user.
        pass
        def create_hero(self):
        '''Prompt user for Hero information
          return Hero with values from user input.
        '''
        # TODO: This method should allow a user to create a hero.
        # User should be able to specify if they want armors, weapons, and
        # abilities.
        # Call the methods you made above and use the return values to build
        # your hero.
        #
        # return the new hero object
        pass
      def build_team_one(self):
        '''Prompt the user to build team_one '''
        # TODO: This method should allow a user to create team one.
        # Prompt the user for the number of Heroes on team one
        # call self.create_hero() for every hero that the user wants to add to team one.
        #
        # Add the created hero to team one.
        pass

    def build_team_two(self):
        '''Prompt the user to build team_two'''
        # TODO: This method should allow a user to create team two.
        # Prompt the user for the number of Heroes on team two
        # call self.create_hero() for every hero that the user wants to add to team two.
        #
        # Add the created hero to team two.
        pass
    def team_battle(self):
        '''Battle team_one and team_two together.'''
        # TODO: This method should battle the teams together.
        # Call the attack method that exists in your team objects
        # for that battle functionality.
        pass
    def show_stats(self):
        '''Prints team statistics to terminal.'''
        # TODO: This method should print out battle statistics
        # including each team's average kill/death ratio.
        # Required Stats:
        #     Declare winning team
        #     Show both teams average kill/death ratio.
        #     Show surviving heroes.
        pass


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    arena.team_battle()
    arena.show_stats()

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
