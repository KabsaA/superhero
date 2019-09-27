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
      damageDone = (self.max_damage - self.attack_strength)
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
        pass
      # TODO: This method should run Ability.attack() on every ability
      # in self.abilities and returns the total as an integer.
class Hero:
    def __init__(self, name, starting_health=100):
          self.abilities = []
          armors: []
          self.name = name
          starting_health: starting_health
          self.current_health = (starting_health - 0)

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
        for i in self.abilities:
            Ability.attack()
        #Calculate the total damage from all ability attacks. return: total:Int
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
        # If you run this file from the terminal
    # this block is executed.
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())
