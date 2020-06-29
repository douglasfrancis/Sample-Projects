pokemon_type = {
"Fire":{
"Strong Against":{"Pokemon_Type":["Grass"], "Damage_To":2}, 
"Weak Against":{"Pokemon_Type":["Water"], "Damage_To":0.5}, 
"Resistant To":{"Pokemon_Type":["Fire", "Grass"], "Damage_From":0.5},
"Vulnerable To":{"Pokemon_Type":["Water"],"Damage_From":2}
},
"Water":{
"Strong Against":{"Pokemon_Type":["Fire"], "Damage_To":2}, 
"Weak Against":{"Pokemon_Type":["Water", "Grass"], "Damage_To":0.5}, 
"Resistant To":{"Pokemon_Type":["Fire", "Water"], "Damage_From":0.5},
"Vulnerable To":{"Pokemon_Type":["Grass"], "Damage_From":2}
} ,
"Grass":{
"Strong Against":{"Pokemon_Type":["Water"], "Damage_To":2}, 
"Weak Against":{"Pokemon_Type":["Fire", "Grass"], "Damage_To":0.5}, 
"Resistant To":{"Pokemon_Type":["Water", "Grass"],"Damage_From":0.5},
"Vulnerable To":{"Pokemon_Type":["Fire"],"Damage_From":2}
} 
}

class Pokemon:
  def __init__(self, name, level, ptype):
    self.name = name
    self.level = level # combat power CP
    self.ptype = ptype
    self.maximum_health = 100 * level
    self.health = 100 * level
    self.knocked_down = False
  
  def __repr__(self):
    if not self.knocked_down:
      return "Pokemon: {name}, Level: {level}, Type: {ptype}, Health: {health} is ready for action".format(name = self.name, level = self.level, ptype = self.ptype, health = self.health)
    return "Pokemon: {name} is Knocked Down!".format(name = self.name)
  
  def knocked_out (self):
    self.knocked_down = True
    print ("{name} has been Knocked Out".format(name = self.name))
    self.heath = 0
  
  def revive (self):
    self.knocked_down = False
    self.health = 20
    print ("{name} has been Revived!!".format(name = self.name))
    print ("{name} current health: {health}".format(name = self.name, health = self.health))

  def lose_health (self, amount):
    self.health -= amount
    if self.health <= 0:
      self.knocked_out()
    print ("{name} has been HIT, Health now: {health}".format(name=self.name, health = self.health))
  
  def gain_health (self, amount):
    self.health += amount
    if self.health <= self.maximum_health:
      print ("{name} recovered health points, Health now: {health}".format(name=self.name, health = self.health))
    else:
      self.health = self.maximum_health
      print ("{name} has achieved Maximum Health: {max_health}".format(name = self.name, max_health = self.health))

  def provide_power_hit (self, enemy):
    my_type = pokemon_type [self.ptype]
    if enemy.ptype in my_type["Strong Against"]["Pokemon_Type"]:
      print ("Strong Against {name}".format(name=enemy.ptype))
      return my_type["Strong Against"]["Damage_To"]
    elif enemy.ptype in my_type["Weak Against"]["Pokemon_Type"]:
      print ("Weak Against {name}".format(name=enemy.ptype))
      return my_type["Weak Against"]["Damage_To"]
    else:
      return 0

  def receive_power_hit (self, enemy):
    my_type = pokemon_type [self.ptype]
    if enemy.ptype in my_type["Resistant To"]["Pokemon_Type"]:
      print ("Resistant To {name}".format(name=enemy.ptype))
      return my_type["Resistant To"]["Damage_From"]
    elif enemy.ptype in my_type["Vulnerable To"]["Pokemon_Type"]:
      print ("Vulnerable To {name}".format(name=enemy.ptype))
      return my_type["Vulnerable To"]["Damage_From"]
    else:
      return 0

  def attack (self, enemy):
    if not self.knocked_down:
      damage = self.provide_power_hit(enemy) * self.level
      print ("Attacking {enemy} with a damage hit of {damage}".format(enemy = enemy.name, damage = damage))
      enemy.lose_health(damage)
    else:
      print ("{name} cannot attack as it's Knocked Down!".format(name=self.name))

class Charmander(Pokemon):
  def __init__(self,level):
    super().__init__("Charmander",level,"Fire")

class Magikarp(Pokemon):
  def __init__(self,level):
    super().__init__("Magikarp",level,"Water")

class Bulbasaur(Pokemon):
  def __init__(self,level):
    super().__init__("Bulbasaur",level,"Grass")

class Trainer:
  def __init__(self, name, pokemons, potions):
    self.name = name
    self.pokemon_list = pokemons
    self.potions = potions
    self.active_pokemon = 0

  def __repr__(self):
    print ("Trainer: {name}".format(name = self.name))
    print ("Pokemon List:")
    for pokemon in self.pokemon_list:
      print (pokemon)
    print ("Number of available Potions:",self.potions)
    return "Active Pokemon: {name}".format(name = self.pokemon_list[self.active_pokemon].name)
  
  def give_potion (self):
    if self.potions > 0:
      self.potions -= 1
      if not self.pokemon_list[self.active_pokemon].knocked_down:
        print("Healing Pokemon {name}".format(name = self.pokemon_list[self.active_pokemon].name))
        self.pokemon_list[self.active_pokemon].gain_health(20)
      else:
        print("Potion will revive Pokemon {name}".format(name = self.pokemon_list[self.active_pokemon].name))
        self.pokemon_list[self.active_pokemon].revive()
    else:
      print ("No more potions left!")

  
  def attack_trainer (self, trainer):
    print ("Attacking trainer {name}".format(name = trainer.name))
    self.pokemon_list[self.active_pokemon].attack(trainer.pokemon_list[trainer.active_pokemon])
  
  def switch_pokemon (self, new_pokemon):
    if new_pokemon >=0 and new_pokemon < len(self.pokemon_list):
      if new_pokemon == self.active_pokemon:
        print("You are trying to switch the same Pokemon!")
      elif not self.pokemon_list[new_pokemon].knocked_down:
        self.active_pokemon = new_pokemon
        print("Switch to Pokemon: ",self.pokemon_list[new_pokemon].name)
      else:
        print("Pokemon {name} is Knocked Down!".format(name = self.pokemon_list[new_pokemon].name))
    else:
      print("No Pokemon available to switch!")

pk1 = Charmander (3)
pk2 = Charmander (7)
pk3 = Magikarp (4)
pk4 = Magikarp (9)
pk5 = Bulbasaur (5)
pk6 = Bulbasaur (7)


tr1 = Trainer ("Ash", [pk1, pk4, pk6], 6)
tr2 = Trainer ("Brock", [pk2, pk3, pk5], 6)

tr2.switch_pokemon(2)

print (tr1)
print (tr2)

pk5.health = 6
tr1.attack_trainer(tr2)
tr2.attack_trainer(tr1)
tr2.give_potion ()
tr2.attack_trainer(tr1)


