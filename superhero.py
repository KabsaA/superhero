import random
class Ability:
    def __init__(self, name, attack_strength):
      '''Create Instance Variables:
          name:String
          max_damage: Integer
       '''
       # TODO: Instantiate the variables listed in the docstring with then
       # values passed in
      self.name = name
      self.attack_strength = attack_strength
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
        '''Instantiate instance properties.
            name: String
            max_block: Integer
        '''
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
          name: self.name
          starting_health: starting_health
          current_health: 0

       # TODO: Initialize instance variables values as instance variables
       # (Some of these values are passed in above,
       # others will need to be set at a starting value)
       # abilities and armors are lists that will contain objects that we can use
    def add_ability(self, ability):
        abilities = []
           #''' Add ability to abilities list '''

           # TODO: Add ability object to abilities:List
    def attack(self):
        #Calculate the total damage from all ability attacks. return: total:Int
        total = 0
        for i in abilities:
            total += 1
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
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())
    ability = Ability("Great Debugging", 50)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    print(hero.abilities)
