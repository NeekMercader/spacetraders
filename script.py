### Space Traders ###
'''
	A space trading simulator.
'''

class Species:
	def __init__(self, species_name, home_planet, personality="friendly"):
		self.species_name = species_name
		self.home_planet = home_planet
		self.personality = personality



class Creature:							# lifeform (human, alien, droid)
	def __init__(self, species, name):
		self.species = species			# race
		self.name = name

		self.ship = object()
		self.fleet = {}


class Ship:
	passenger_capacity = 1
	cargo_capacity = 500
	weapon_capacity = 100
  
	def __init__(self, name, ship_type, ship_class, ship_mods=object()):
		self.name = name
		self.ship_type = ship_type		# cargo, fighter, hybrid/mixed, cruiser, capital (ship)
		self.ship_class	= ship_class	# enterprise, starliner, starfighter, x-wing
		self.ship_mods = ship_mods		# modifications like custom phasers, added weapons, expanded cargo holds

		self.utilized_passenger_capacity = 1		# used minimum standard (could be 0 for drones)
		self.utilized_cargo_capacity = 0			# used capacity; usually mass/weight (in "units")
		self.utilized_weapon_capacity = 0			# used weapon capacity

		self.passengers = 1
		self.cargo = {}					# { "identifier (Goods().name)" : capacity}
		self.weapons = []

	def __repr__(self):
		return self.msg("repr_ship")

	def load_cargo(self, goods, qty):
		goods.qty += qty
		goods_capacity = goods.compute_capacity(qty)	# convert 'quantity' and 'space used' by goods into 'capacity'
		if self.cargo_capacity >= self.utilized_cargo_capacity + goods_capacity:	# capacity available?
			self.utilized_cargo_capacity += goods_capacity							# update counters
			if goods.name in self.cargo:			# items already existing in cargo
				# self.cargo[goods.name] += goods_capacity
				self.cargo[goods.name] = self.cargo.get(goods.name) + goods_capacity
			else:									# item doesn't exist; so, append
				self.cargo[goods.name] = goods_capacity	# load goods (cargo)
		print(self.msg("msg_cargo_loaded"))

		
	def remove_cargo(self, goods, qty):
		if goods.qty - qty >= 0:
			goods.qty -= qty
			goods_capacity = goods.compute_capacity(qty)
			self.utilized_cargo_capacity -= goods_capacity
			
			self.cargo[goods.name] = self.cargo.get(goods.name) - goods_capacity
			if self.cargo.get(goods.name) == 0:
				self.cargo.pop(goods.name)		# remove entire item (use only when hitting zero)
			print(sample_ship.msg("msg_cargo_removed"))	# success
		else:
			print("\nCargo not removed! Capacity entered is more than inventory.\n\n")
		
		

	def attach_weapon(self, shipweapon):
		self.weapons.append(shipweapon)

	def remove_weapon(self, shipweapon):
		self.weapons.pop(shipweapon)

	def msg(self, msg_id, lang="en"):
		if lang == "en":
			messages = {
				# regular messages
				"msg_cargo_loaded": "\n----------\n[in msg()] Cargo has been loaded. Stats:\nTotal ship capacity: {one}\nCapacity used: {two} // Remaining capacity: {three}\nCargo inventory: {four}\n----------\n".format(one=self.cargo_capacity,two=self.utilized_cargo_capacity,three=self.cargo_capacity-self.utilized_cargo_capacity,four=self.cargo),
				"msg_cargo_removed": "\n----------\n[in msg()] Cargo has been removed. Stats:\nTotal ship capacity: {one}\nCapacity used: {two} // Remaining capacity: {three}\nCargo inventory: {four}\n----------\n".format(one=self.cargo_capacity,two=self.utilized_cargo_capacity,three=self.cargo_capacity-self.utilized_cargo_capacity,four=self.cargo),

				# console & utility messages
				"repr_ship": "This ship {name} is of type {ship_type} and class {ship_class}, has a passenger capacity now of {passenger_capacity}, cargo capacity of {cargo_capacity}, weapons capacity of {weapons_capacity}. Cargo is {cargo} while weapons is {weapons}.\n\n".format(name=self.name, ship_type=self.ship_type, ship_class = self.ship_class, passenger_capacity = self.utilized_passenger_capacity, cargo_capacity = self.utilized_cargo_capacity, weapons_capacity = self.utilized_weapon_capacity, cargo = self.cargo, weapons = self.weapons), }

		return messages[msg_id]


class Goods:
	def __init__(self, sku, cat, name, capacity_used):
		self.sku = sku
		self.cat = cat 							# category
		self.name = name
		self.capacity_used = capacity_used 		# capacity amount used by this unit

		self.qty = 0
		self.price = 0.0						# suggested retail (standard)
		
	def __repr__(self):
		return dir(self)
	
	def compute_capacity(self, qty):
		return self.capacity_used * qty	# capacity used per unit, times qty
	

class ShipWeapon:
	def __init__(self, weapon_type):
		self.weapon_type = weapon_type

		self.ammunition = 0
		self.hitpoints = 0
		self.damage_per_minute = 0
		self.in_working_condition = True 		# working? destroyed?


class Biome:							# locations like stars, planets, moons, space stations, ports, etc. (calling them all "planets" is inacccurate)
	def __init__(self, name, biome_type, classification="standard"):	# e.g. ()"Moony McMoonFace", "moon", "military")
		self.name = name 
		self.biome_type = biome_type
		self.classification = classification

		self.parent_site = object()
		self.coords = ""
		self.description = ""




#################### (main)


print (\
"""
███████╗██████╗  █████╗  ██████╗███████╗    ████████╗██████╗  █████╗ ██████╗ ███████╗██████╗ ███████╗
██╔════╝██╔══██╗██╔══██╗██╔════╝██╔════╝    ╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔════╝
███████╗██████╔╝███████║██║     █████╗         ██║   ██████╔╝███████║██║  ██║█████╗  ██████╔╝███████╗
╚════██║██╔═══╝ ██╔══██║██║     ██╔══╝         ██║   ██╔══██╗██╔══██║██║  ██║██╔══╝  ██╔══██╗╚════██║
███████║██║     ██║  ██║╚██████╗███████╗       ██║   ██║  ██║██║  ██║██████╔╝███████╗██║  ██║███████║
╚══════╝╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝       ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝

By Neek Mercader
[Version 0.20 pre-alpha]
""")
print("\n")
player_name = input("Enter your name: ")
player_menu_select = input(\
"""

+-------------------------------------------+
| Type your command:                        |
+-------------------------------------------+
|                                           |
| 'N' or 'enter' to board your ship         |
| 'E' or 'exit' to disembark from your ship |
|                                           |
| 'B' or 'buy' to purchase goods (cargo)    |
| 'S' or 'sell' to sell goods (cargo)       |
|                                           |
| 'L' or 'load' cargo                       |
| 'U' or 'unload' cargo                     |
|                                           |
| 'S' or 'shoot' to fire at opponents       |
|                                           |
| 'A' or 'attach' Weapons                   |
| 'D' or 'detach' Weapons                   |
|                                           |
| 'Q' or 'quit' to exit                     |
|                                           |
+-------------------------------------------+

"""
			   ).lower()
print("\nOK,", player_name, ", you selected: '" + player_menu_select + "'.\n\nThis is a pre-alpha version and meant to show you input works and ready to process.\n\n")



sample_goods_01 = Goods("11111", "fruits", "apples", 10)
sample_goods_02 = Goods("11112", "Droid Parts", "Microprocessors", 15)
sample_goods_03 = Goods("11113", "meal kits", "rations #4", 5)

sample_ship = Ship("USS Enterprise", "explorer", "enterprise")
sample_ship.utilized_passenger_capacity = 5

sample_ship.load_cargo(sample_goods_01, 5)
sample_ship.load_cargo(sample_goods_02, 2)
sample_ship.load_cargo(sample_goods_02, 1)
sample_ship.load_cargo(sample_goods_01, 25)
sample_ship.load_cargo(sample_goods_03, 5)
sample_ship.load_cargo(sample_goods_03, 15)
sample_ship.remove_cargo(sample_goods_02, 2)
sample_ship.remove_cargo(sample_goods_02, 1)
sample_ship.load_cargo(sample_goods_02, 5)

print("Hey, " + player_name + ", here's the results from the game: \n", sample_ship)
