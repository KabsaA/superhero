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

    # Keep all your current code, but add these methods
        def attack(self, other_team):
        #''' Battle each team against each other.'''
        # TODO: Randomly select a living hero from each team and have
        # them fight until one or both teams have no surviving heroes.
        # Hint: Use the fight method in the Hero class.
            pass

        def revive_heroes(self, health=100):
        #''' Reset all heroes health to starting_health'''
        # TODO: This method should reset all heroes health to their
        # original starting value.
            pass

        def stats(self):
        #'''Print team statistics'''
        # TODO: This method should print the ratio of kills/deaths for each
        # member of the team to the screen.
        # This data must be output to the console.
        # Hint: Use the information stored in each hero.
            pass

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
                print(str(self.name) + " won!")
            else:
                break
            if opponent.is_alive() == True:
                oppAttack = opponent.attack()
                self.take_damage(oppAttack)
                print(str(self.name) + " won!")
            else:
                break


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 600)
    print(Weapon.attack(ability1))
    ability2 = Ability("Super Eyes", 2000)
    ability3 = Ability("Wizard Wand", 20)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
