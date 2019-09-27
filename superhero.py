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
      # Hint: The constructor initializes the maximum attack value.
      #my_dog = Dog("Rex", "SuperDog")
      #my_dog.bark()


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
          self.starting_health = starting_health
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
        pass





if __name__ == "__main__":
    hero = Hero("Grace Hopper", 200)
    hero.take_damage(150)
    print(hero.is_alive())
    hero.take_damage(15000)
    print(hero.is_alive())
