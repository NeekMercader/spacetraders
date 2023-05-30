'''
	### Space Traders ###
	A space trading simulator.
'''
import languages.en as lang
import views.en as views
import data.data as data
import utilities.utilities as util


class Species:
	def __init__(self, species_name, home_planet, personality="friendly"):
		self.species_name = species_name
		self.home_planet = home_planet
		self.personality = personality

class Creature:							# lifeform (human, alien, droid)
	def __init__(self, species, name):
		self.species = species			# race
		self.name = name

		self.type = []					# e.g. "trader", "warlord", "loanshark", "thug", "police", "military"
		self.ship = object()
		self.fleet = {}


class Ship:
  
	def __init__(self, name, ship_type, ship_class, cargo=500, weapon=100, passenger=1):
		self.name = name
		self.ship_type = ship_type		# cargo, fighter, hybrid, cruiser, capital (ship)
		self.ship_class	= ship_class	# enterprise, starliner, starfighter, x-wing
		self.cargo_capacity = cargo
		self.weapon_capacity = weapon
		self.passenger_capacity = passenger

		self.shields = 100				# shield strength (and health)
		self.health = 100				# health (<10 = can't warp; 0 = total damage (scrap) )
		self.ship_mods = object()		# warp boosters, shield boost, custom phasers, expanded cargo holds

		self.utilized_passenger_capacity = 1
		self.utilized_cargo_capacity = 0
		self.utilized_weapon_capacity = 0

		self.passengers = 1
		self.cargo = {}
		self.weapons = {}

	def __repr__(self):
		return self.msg("repr_ship").format(name=self.name, ship_type=self.ship_type, ship_class = self.ship_class, passenger_capacity = self.utilized_passenger_capacity, cargo_capacity = self.utilized_cargo_capacity, weapons_capacity = self.utilized_weapon_capacity, cargo = self.cargo, weapons = self.weapons)

	def load_cargo(self, goods):		# goods = dict (e.g. { "food" : 200, "arms" : 10 })
		goods_capacity = self.compute_capacity(goods)
		if self.cargo_capacity >= self.utilized_cargo_capacity + goods_capacity:
			self.utilized_cargo_capacity += goods_capacity
			for item in goods.keys():
				self.cargo[item] = self.cargo.get(item, 0) + goods[item] # item qty, not capacity 

			print(self.msg("cargo_loaded").format(one=self.cargo_capacity,two=self.utilized_cargo_capacity,three=self.cargo_capacity-self.utilized_cargo_capacity,four=self.cargo))
		else:
			print(lang.content["cargo_not_loaded"])
		
		# print(self.show_cargo_stats(goods))
		print(self.show_cargo_stats(self.cargo))
			
	def remove_cargo(self, goods):			# goods = dict (e.g. { "food" : 200, "arms" : 10 })
		for item in goods.keys():			# check if quantities declared actually exist
			# if (self.cargo[item] < goods[item]):
			if (self.cargo.get(item,0) < goods[item]):
				print(lang.content["cargo_not_removed"], ": [\"", item, "\"].")	# erroneous qty; abort
				return
		for item in goods.keys():			# now that we're safe, do the actual removals
			self.cargo[item] -= goods[item]
			if self.cargo[item] == 0:
				del self.cargo[item]		# if 0, remove entire item
		goods_capacity = self.compute_capacity(goods)		# check total capacity used
		self.utilized_cargo_capacity -= goods_capacity	# update counters

		print(self.msg("cargo_removed"))	# success
		print(self.show_cargo_stats(self.cargo))

		
	def compute_capacity(self, itemlist):			# itemlist = dict of goods
		# return sum( goods[val] for val in goods )
		capacity = 0
		for item in itemlist.keys():
			capacity += data.goods_list[item].capacity_used * itemlist[item]
		return capacity

	def attach_weapon(self, shipweapon):
		self.weapons.append(shipweapon)

	def remove_weapon(self, shipweapon):
		self.weapons.remove(shipweapon)

	def msg(self, msg_id):
		return lang.content[msg_id]
	
	def show_cargo_stats(self, cargo):
		total_capacity = 0
		rows = []
		for item in cargo.keys():
			subtotal_capacity = data.goods_list[item].capacity_used * cargo[item]
			total_capacity += subtotal_capacity

			rows.append([data.goods_list[item].cat, cargo[item], data.goods_list[item].capacity_used, subtotal_capacity ])		# make_table() will do the string-ifying

		print(util.make_table(rows, lang.content["labelwidths"]))
		print(lang.content["inv_capacity_used"] + str(total_capacity))
		

'''
class Goods: ...
'''

class ShipWeapon:
	def __init__(self, weapon_type):
		self.weapon_type = weapon_type

		self.ammunition = 0
		self.hitpoints = 0
		self.damage_per_minute = 0
		self.in_working_condition = True 		# working? destroyed?


class Habitat:							# locations like stars, planets, moons, space stations, ports, etc. (calling them all "planets" is inacccurate)
	def __init__(self, name, habitat_type, classification="standard"):	# e.g. ()"Moony McMoonFace", "moon", "military")
		self.name = name 
		self.habitat_type = habitat_type
		self.classification = classification

		self.parent_site = object()
		self.coords = ""
		self.description = ""


class Bank:
	def __init__(self, location):
		self.location = location 

		bankname = ""
		balance = 0.00
		loan = 0.00


class Warehouse:
	def __init__(self, location, capacity):
		self.locatioin = location
		self.capacity = capacity 




def ui_screens(screen="start"):
	if screen == "start":
		
		print(views.content["branding_title"])

		player_name = input(lang.content["temp_enter_name"])
		player_menu_select = input(views.content["select_main"]).lower()
		print(lang.content["temp_print_selection"].format(player_name=player_name, player_menu_select=player_menu_select))



#################### (main)

ui_screens()					# start

sample_ship = Ship("USS Enterprise", "explorer", "enterprise")

sample_ship.load_cargo( {"minerals": 2, "arms": 5, "gadgets": 2} )
sample_ship.load_cargo( {"food_supplies": 10, "gadgets": 9 } )
sample_ship.load_cargo( {"arms": 10, "raw_materials": 5, "minerals": 5} )
sample_ship.remove_cargo( {"raw_materials": 3, "arms": 2} )
# sample_ship.remove_cargo( {"minerals": 5, "arms": 5, "gadgets": 6} )
# sample_ship.load_cargo( {"raw_materials": 5, "arms": 5} )

print("Here's the results from the game: \n", sample_ship)
