import random
class Ability:
    def __init__(self, name, attack_strength):
          self.name = name
          self.attack_strength = attack_strength
       # TODO: Instantiate the variables listed in the docstring with then
       # values passed in
      #self.attack_strength = attack_strength
    def attack(self):
      #''' Return a value between 0 and the value set by self.max_damage.'''
      # TODO: Use random.randint(a, b) to select a random attack value.
      # Return an attack value between 0 and the full attack.
      # Hint: The constructor initializes the maximum attack value.
        pass
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
        pass
      # TODO: This method should run Ability.attack() on every ability
      # in self.abilities and returns the total as an integer.
class Hero:
    def __init__(self, name, starting_health=100):
          self.abilities = Hero.add_ability(ability)
          armors: []
          self.name = name
          starting_health: starting_health
          self.current_health = (starting_health - 0)

       # TODO: Initialize instance variables values as instance variables
       # (Some of these values are passed in above,
       # others will need to be set at a starting value)
       # abilities and armors are lists that will contain objects that we can use
    def add_ability(self, ability):
        abilities = []
        #for i in ability:
        abilities.append(ability)
  #''' Add ability to abilities list '''
  # TODO: Add ability object to abilities:List

           # TODO: Add ability object to abilities:List
    def attack(self):
        #Calculate the total damage from all ability attacks. return: total:Int
        pass
    def defend(self,incoming_damage):
        pass
    def take_damage(self,damage):
        pass
    def is_alive(self):
        pass
    def fight(self,opponent):
        pass





if __name__ == "__main__":
        # If you run this file from the terminal
    # this block is executed.
    ability = Ability("Great Debugging", 50)
    ability2 = Ability("Grging", 70)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    hero.add_ability(ability2)
    print(hero.abilities)
