'''
	### Space Traders ###
	A space trading simulator.
'''
import languages.en as lang
import views.en as views
import data.data as data
import utilities.utilities as util

import time
import random


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

		self.type = []					# e.g. "trader", "warlord", "loanshark", "thug", "police", "military"
		self.ship = object()
		self.fleet = {}

class Location:							# Places like stars, biomes/planets, moons, space stations, ports, etc. (calling them all "planets" is inacccurate)
	def __init__(self, name, location_type, classification="standard"):	# e.g. ()"Moony McMoonFace", "moon", "military")
		self.name = name 
		self.location_type = location_type
		self.classification = classification

		self.parent_site = object()
		self.coords = ""
		self.description = ""

'''

class Player:
	def __init__(self, player_id=1, player_username="SirLootALot", initial_balance=0):	# balance = money
		self.player_id = player_id
		self.player_username = player_username
		self.balance = initial_balance

		self.curr_location = "Solstra"
		self.reputation = 0
		self.storage = {}	# dict of Storage instances based on location; e.g. { "Solstra": Storage("Solstra", 50000), }

	# Check if player has sufficient balance for a given amount
	def check_balance(self, amount):
		return self.balance >= amount

	# Add amount to player's balance
	def add_balance(self, amount):
		self.balance += amount

	# Remove amount from player's balance
	def remove_balance(self, amount):
		if self.check_balance(amount):
			self.balance -= amount
		else:
			print("Not enough balance.")


class Ship:
	@staticmethod
	def init_ship(shipname="Bellerophon", shiptype="light freighter", owner = 1, fleet = 1):	# automator for object definition; used in constructor
		# shipdata = [str(x) if isinstance(x, int) else "\"" + x + "\"" for x in data.ship_data[shiptype][:-1]]
		shipdata = [x for x in data.ship_data[shiptype][:-1]]
		shipdata.insert(0, shipname)
		shipdata.append(owner)
		shipdata.append(fleet)
		return shipdata
	
	@staticmethod
	def msg(msg_id):
		return lang.content[msg_id]

	# def __init__(self, name, ship_type, ship_class, cargo=500, weapon=100, passenger=1, owner=1, fleet=1):
	def __init__(self, *argslist):
		name, ship_type, ship_class, cargo, weapon, passenger, owner, fleet = argslist
		self.name = name
		self.ship_type = ship_type		# cargo, fighter, hybrid, cruiser, capital (ship)
		self.ship_class	= ship_class	# enterprise, starliner, starfighter, x-wing
		self.cargo_capacity = cargo
		self.weapon_capacity = weapon
		self.passenger_capacity = passenger
		self.owner = owner if owner in range(4) else len(player_list)				# player ID (and company name) (default: #1)
		self.fleet = fleet				# fleet ID# (not qty) (default: #1)
		self.player = player_list[self.owner - 1]	# player_list = list of Player instances. [self.owner + 1] = NPC

		self.shields = 100				# shield strength (and health) (in %)
		self.health = 10000 if owner > 0 else 2500				# health (<10 = can't warp; 0 = total damage (scrap) )
		self.ship_mods = object()		# warp boosters, shield boost, custom phasers, expanded cargo holds

		self.utilized_passenger_capacity = 1
		self.utilized_cargo_capacity = 0
		self.utilized_weapon_capacity = 0

		self.passengers = 1
		self.cargo = {}
		self.weapons = {}

		print("\n\n%%%%%%%%%%%%%%%%\n", name, ship_type, ship_class, cargo, weapon, passenger, owner, fleet, "SHIP HEAlth = ", self.health, "OWNER = ", self.owner, "\n\%%%%%%%%%%%%%%%%%%%\n\n")
	
	def __repr__(self):
		return Ship.msg("repr_ship").format(name=self.name, ship_type=self.ship_type, ship_class = self.ship_class, passenger_capacity = self.passenger_capacity, cargo_capacity = self.utilized_cargo_capacity, weapons_capacity = self.utilized_weapon_capacity, cargo = self.cargo, weapons = self.weapons)

	def set_curr_location(self, location):
		self.player.curr_location = location
		self.curr_location = location

	def load_cargo(self, goods):		# goods = dict (e.g. { "food" : 200, "arms" : 10 })
		goods_capacity = self.compute_capacity(goods)
		if self.cargo_capacity >= self.utilized_cargo_capacity + goods_capacity:
			self.utilized_cargo_capacity += goods_capacity
			for item in goods.keys():
				self.cargo[item] = self.cargo.get(item, 0) + goods[item] # item qty, not capacity 

			print(Ship.msg("cargo_loaded").format(one=self.cargo_capacity,two=self.utilized_cargo_capacity,three=self.cargo_capacity-self.utilized_cargo_capacity,four=goods,five=sum(goods.values()),six=goods_capacity))
		else:
			print(lang.content["cargo_not_loaded"])
			return False
		# print(self.show_cargo_stats(goods))
		print(self.show_cargo_stats(self.cargo))
		return True
			
	def remove_cargo(self, goods):			# goods = dict (e.g. { "food" : 200, "arms" : 10 })
		for item in goods.keys():			# check if quantities declared actually exist
			# if (self.cargo[item] < goods[item]):
			if (self.cargo.get(item,0) < goods[item]):
				print(lang.content["cargo_not_removed"], ": [\"", item, "\"].")	# erroneous qty; abort
				return False
		for item in goods.keys():			# now that we're safe, do the actual removals
			self.cargo[item] -= goods[item]
			if self.cargo[item] == 0:
				del self.cargo[item]		# if 0, remove entire item
		goods_capacity = self.compute_capacity(goods)		# check total capacity used
		self.utilized_cargo_capacity -= goods_capacity	# update counters
		print(Ship.msg("cargo_removed").format(one=self.cargo_capacity,two=self.utilized_cargo_capacity,three=self.cargo_capacity-self.utilized_cargo_capacity,four=goods,five=sum(goods.values()),six=goods_capacity))
		print(self.show_cargo_stats(self.cargo))
		return True


	def attach_weapon(self, shipweapon):	# shipweapon = dict (e.g. { "Pulse Cannon" : 2, "Railgun" : 1 })
		weapon_capacity = self.compute_capacity(shipweapon, "weapons")
		if self.weapon_capacity >= self.utilized_weapon_capacity + weapon_capacity:
			self.utilized_weapon_capacity += weapon_capacity
			for item in shipweapon.keys():
				self.weapons[item] = self.weapons.get(item, 0) + shipweapon[item]	# qty, not capacity
			print(Ship.msg("weapon_loaded").format(one=self.weapon_capacity,two=self.utilized_weapon_capacity,three=self.weapon_capacity-self.utilized_weapon_capacity,four=shipweapon,five=sum(shipweapon.values()),six=weapon_capacity))
		else:
			print(lang.content["weapon_not_loaded"])
			return False
		print(self.show_weapon_stats(self.weapons))
		return True

	def remove_weapon(self, shipweapon):	# { "Pulse Cannon" : 2, "Railgun" : 1 })
		for item in shipweapon.keys():
			if (self.weapons.get(item,0) < shipweapon[item]):
				print(lang.content["weapon_not_removed"], ": [\"", item, "\"].")	# erroneous qty; abort
				return False
		for item in shipweapon.keys():
			self.weapons[item] -= shipweapon[item]
			if self.weapons[item] == 0:
				del self.weapons[item]
		weapon_capacity = self.compute_capacity(shipweapon, "weapons")
		self.utilized_weapon_capacity -= weapon_capacity
		print(Ship.msg("weapon_removed").format(one=self.weapon_capacity,two=self.utilized_weapon_capacity,three=self.weapon_capacity-self.utilized_weapon_capacity,four=shipweapon,five=sum(shipweapon.values()),six=weapon_capacity))
		print(self.show_weapon_stats(self.weapons))
		return True

	# return item (goods/cargo or weapons) qty
	def check_item_qty(self, item):
		return self.cargo[item] if item in self.cargo else self.weapons[item]

	def compute_capacity(self, itemlist, itemtype="goods"):			# itemlist = dict of goods (e.g. { "food" : 200, "arms" : 10 }) (if weapons, itemtype="weapons")
		# return sum( goods[val] for val in goods )
		capacity = 0
		for item in itemlist.keys():
			capacity += (data.goods_data[item].capacity_used if itemtype == "goods" else data.weapons_list[item].capacity_used ) * itemlist[item]
		return capacity

	def show_cargo_stats(self, cargo):
		total_capacity = 0
		rows = []
		for item in cargo.keys():
			subtotal_capacity = data.goods_data[item].capacity_used * cargo[item]
			total_capacity += subtotal_capacity

			rows.append([data.goods_data[item].cat, cargo[item], data.goods_data[item].capacity_used, subtotal_capacity ])	# format_table() will string-ify; cargo[item] = qty
		return(util.format_table(rows, lang.content["thead_labels_cargo"]))
		
	def show_weapon_stats(self, weapon):
		total_capacity = 0
		rows = []
		for item in weapon.keys():
			subtotal_capacity = data.weapons_list[item].capacity_used * weapon[item]
			total_capacity += subtotal_capacity

			# rows.append([item, weapon[item], data.weapons_list[item].capacity_used, subtotal_capacity ])	# format_table() will string-ify; weapon[item] = qty
			rows.append([item, weapon[item], data.weapons_list[item].capacity_used, subtotal_capacity, data.weapons_list[item].damage_per_minute, data.weapons_list[item].hitpoints ])	# format_table() will string-ify; weapon[item] = qty
		return(util.format_table(rows, lang.content["thead_labels_weapon"]))
	
	def take_damage(self, damage):
		self.shields -= damage
		if self.shields < 0:
			self.health += self.shields
			self.shields = 0
		if self.health <= 0:
			self.health = 0
			print(f"Ship {self.name} has been destroyed!")
			return 
		# print(f"{self.name} takes {damage} damage. {self.name} health is {self.health}.")
	

'''
# transferred to data.py
class Goods: ...
class Weapon: ...
'''


class Bank:

	STD_INTEREST_RATE = 0.1  # 10% interest per year (365 turns)
	LOANABLE_AMT = 0.5  # Loan at 50% of net worth

	def __init__(self, player_id=1, location="Solstra"):
		self.player_id = player_id
		self.location = location
		self.balance = 0.0
		self.loan = 0.0
		self.interest_rate = STD_INTEREST_RATE

	# Deposit money into the bank.
	def deposit(self, amount):
		if amount > 0:
			self.balance += amount
			print(f"Deposited ${amount:.2f} into the bank.")
		else:
			print("Invalid deposit amount.")

	# Withdraw money from the bank.
	def withdraw(self, amount):
		if amount > 0 and self.balance >= amount:
			self.balance -= amount
			print(f"Withdrawn ${amount:.2f} from the bank.")
		else:
			print("Invalid withdrawal amount or insufficient balance.")

	# Loan money to the player.
	def loan_money(self, player):
		loan_amount = player.balance * LOANABLE_AMT
		self.loan = loan_amount
		player.balance += loan_amount
		print(f"You have borrowed ${loan_amount:.2f} from the bank.")

	# Pay off the loan.
	def pay_loan(self, player):
		if player.balance >= self.loan:
			player.balance -= self.loan
			self.loan = 0.0
			print("You have paid off your loan.")
		else:
			print("Insufficient funds to pay off the loan.")

	# Calculate and apply interest on the loan.
	def calculate_interest(self):
		interest = self.loan * self.interest_rate
		self.loan += interest
		print(f"Interest applied: ${interest:.2f}")

	# Harass the player if the loan is past due.
	def harass_player(self, player):
		if self.loan > 0 and player.balance < self.loan:
			print("You have an overdue loan. Please pay it off immediately!")
		else:
			print("No overdue loan.")




class Storage:
	def __init__(self, location, capacity, player_id=1):
		self.location = location
		self.capacity = capacity
		self.player_id = player_id

		self.utilized_capacity = 0
		
		self.items = {}  # Dictionary to hold item names and quantities

	# Check the remaining storage capacity.
	def get_remaining_capacity(self):
		return self.capacity - self.utilized_capacity

	# Convert qty to capacity
	def qty_to_capacity(self, item, qty):
		# get capacity multiplier for the item from the item dict
		if item not in data.goods_data and item not in data.weapon_data:
			return -1
		return (data.goods_data[item].capacity_used * qty) if item in data.goods_data else (data.weapon_data[item]["Capacity Used"]) * qty

	# Check the qty of a specific item in storage.
	def check_item_qty(self, item):
		return self.items.get(item, 0)


	# Add a qty of an item to storage.
	def add_item(self, item, qty):
		curr_capacity = self.qty_to_capacity(item, qty)
		if (curr_capacity != -1) and self.utilized_capacity + curr_capacity <= self.capacity:
			self.items[item] = self.items.get(item, 0) + qty  # add item qty
			self.utilized_capacity += curr_capacity
			print(f"Added {qty} units ({curr_capacity} capacity) of {item} to storage. (Total: {self.items} units at {self.utilized_capacity} capacity)\n")
		else:
			print(f"Insufficient storage capacity to add {qty} units of {item}.")

	# Remove a qty of an item from storage.
	def remove_item(self, item, qty):
		curr_capacity = self.qty_to_capacity(item, qty)
		if self.items.get(item, 0) >= qty:
			self.items[item] -= qty
			if self.items[item] == 0:
				del self.items[item]  # delete key if no more of this item
			self.utilized_capacity -= curr_capacity
			print(f"Removed {qty} units ({curr_capacity} capacity) of {item} from storage.")
		else:
			print(f"Insufficient quantity to remove {qty} units of {item}.")

	# Transfer a qty of an item from storage to a ship. (items can be of itemtype "cargo" or other (e.g. "weapons"))
	def transfer_to_ship(self, ship, item, qty):	# , itemtype="cargo"
		print(\
'''
###############################################
# INITIATING TRANSFER FROM STORAGE TO SHIP... #
###############################################
'''
		)
		if self.items.get(item, 0) >= qty:
			# ship.load_cargo({item: qty})  # assumes ship's load_cargo method takes a dict
			if ( ship.load_cargo({item: qty}) if item in data.goods_data else ship.attach_weapon({item: qty}) ):
				self.remove_item(item, qty)
				print("\n\nATTACHed ITEM TO SHIP, REMOVED FROM STORAGE!")
				print(f"\n-----\nItems ({item}: {qty}) moved from storage to ship.\nShip inventory:\n\t{ship.cargo} (cargo)\n\t{ship.weapons} (weapons)\nStorage inventory: {self.items}\n-----\n")
		else:
			print(f"Insufficient qty to transfer {qty} units of {item}.")

	# Transfer a qty of an item from a ship to storage. (items can be of itemtype "cargo" or other (e.g. "weapons"))
	def receive_from_ship(self, ship, item, qty):	# , itemtype="cargo"
		print(\
'''
###############################################
# INITIATING TRANSFER FROM SHIP TO STORAGE... #
###############################################
'''
		)
		if ship.check_item_qty(item) >= qty:
			# ship.remove_cargo({item: qty})  # assumes ship's remove_cargo method takes a dict
			if ( ship.remove_cargo({item: qty}) if item in data.goods_data else ship.remove_weapon({item: qty}) ):
				self.add_item(item, qty)
				print("\n\nMOVED ITEM FROM SHIP TO STORAGE!")
				print(f"\n-----\nItems ({item}: {qty}) moved from ship to storage.\nShip inventory:\n\t{ship.cargo} (cargo)\n\t{ship.weapons} (weapons)\nStorage inventory: {self.items}\n-----\n")
			else:
				print("\nSOMETHING WENT WRONG.\n\n")
		else:
			print(f"Insufficient quantity to receive {qty} units of {item} from ship.")


class TradingMarketplace:

	def __init__(self, player, location):		# player = Player object
		self.player = player
		self.location = location
		self.market = {
			"goods": {},
			"weapons": {},
			"assets": {}
		}

	# Buy an item from the marketplace
	def buy_item(self, item_type, item_id, qty):
		item_dict = self.get_item_dict(item_type)
		if item_id in item_dict and item_dict[item_id]['qty'] >= qty:
			cost = item_dict[item_id]['price'] * qty
			if self.player.check_balance(cost):
				item_dict[item_id]['qty'] -= qty
				self.player.remove_balance(cost)
				self.player.storage[self.player.curr_location].add_item(item_id, qty)  # Add item directly to player's storage at the current location
			else:
				print (f"Insufficient funds to buy {qty} units of item {item_id}.")
			print(f"##########\nCHECKPOINT: Bought Item: {item_id}\n##########\nitem_type: {item_type} / qty: {qty} / item_dict: {item_dict} @ cost: {cost} / new_item_dict: {self.get_item_dict(item_type)} \nplayer balance: {self.player.balance}\n##########\n")
		else:
			print (f"Insufficient qty or item does not exist: {qty} units of item {item_id}.")

	# Sell an item to the marketplace
	def sell_item(self, item_type, item_id, qty):
		item_dict = self.get_item_dict(item_type)
		if self.player.storage[self.player.curr_location].check_item_qty(item_id) >= qty:  # Check qty in player's storage
			earnings = item_dict[item_id]['price'] * qty
			self.player.add_balance(earnings)
			self.player.storage[self.player.curr_location].remove_item(item_id, qty)  # Remove item directly from player's storage
			if item_id in item_dict:
				item_dict[item_id]['qty'] += qty	# marketplace stock/inventory
			else:
				item_dict[item_id] = {'qty': qty, 'price': self.player.get_item_price(item_type, item_id)}
			print(f"##########\nCHECKPOINT: Sold Item: {item_id}\n##########\nitem_type: {item_type} / qty: {qty} / item_dict: {item_dict} @ earnings: {earnings} / new_item_dict: {self.get_item_dict(item_type)} \nmarketplace contents: {self.market}\nplayer balance: {self.player.balance}\nStorage inventory: {self.player.storage[self.player.curr_location].items}\n##########\n")
		else:
			print (f"Insufficient qty to sell {qty} units of item {item_id}.")

	# Load an item to the marketplace
	def add_item(self, item_type, item_id, qty, price):
		item_dict = self.get_item_dict(item_type)
		if item_id in item_dict:
			item_dict[item_id]['qty'] += qty
			item_dict[item_id]['price'] = price
		else:
			item_dict[item_id] = {'qty': qty, 'price': price}
		print(f"##########\nCHECKPOINT: ADDED Item: {item_id}\n##########\nitem_type: {item_type} / qty: {qty} / item_dict: {item_dict} / new_item_dict: {self.get_item_dict(item_type)} \n##########\n")

	# get item info dict 
	def get_item_dict(self, item_type):
		return self.market.get(item_type, {})
	'''
	def get_item_dict(self, item_type):
		if item_type in self.market:
			return self.market[item_type]
		else:
			print ("Invalid item type: {item_type}.".format())
	'''

	# Get the qty of a specific item in the marketplace
	def get_item_qty(self, item_type, item_id):
		item_dict = self.get_item_dict(item_type)
		return item_dict[item_id]['qty'] if item_id in item_dict else 0

	# Get the price of a specific item in the marketplace
	def get_item_price(self, item_type, item_id):
		item_dict = self.get_item_dict(item_type)
		return item_dict[item_id]['price'] if item_id in item_dict else 0


class Maintenance:
	def __init__():
		pass 

	# repairs the ship's health by a certain amount based on player money and availability of parts
	def repair_ship(self, ship, damage, repair_percentage=1.00):	# percentage: 100%
		self.ship = ship
		self.owner = self.ship.owner

		# REPAIR_CONST = .20		  # percentage to compute
		REPAIR_PER_DAMAGE = 100	 # cost per unit damage

		money_needed = int(damage * repair_percentage * REPAIR_PER_DAMAGE)

		if self.owner.balance >= money_needed:	  # do we have enough money available?
			self.owner.balance -= money_needed
			ship_health += int(repair_percentage * damage)
			print("You repaired your ship by", repair_percentage * damage, "health.")
		else:
			print("You can't repair your ship.")


class TravelSystem:

	@staticmethod
	def expand_selection(input_char):
		return planets[int(input_char) - 1]	# convert input char to planet name string (based on index #)

	def __init__(self, ship):		# player = Player object; provides Ship and location info
		self.ship = ship

	def travel_start(self):
		selection = TravelSystem.expand_selection(UISystem.ui_screens("travel"))
		print(f"Traveling to {selection}...\n")

		# EventSystem()
		print(f"Arriving in {selection}...\n")
		self.ship.set_curr_location(selection)


		

	def travel_arrival(self):
		
		selection = TravelSystem.expand_selection(UISystem.ui_screens("main"))

		# set player location



'''

class EventSystem:
	def __init__(self, ship):
		self.ship = ship	# Ship instance
		
		event = data.eventlist[random.randint(1, len(eventlist))]
		print(f"\nInside EventSystem, current event is {event}.\n")

		if event == "nothing":
			pass
		elif event == "pirate_attack":
			pass
		elif event == "alien_attack":
			pass
		elif event == "wormhole":
			pass
		elif event == "asteroid_shower":
			pass
'''



class CombatSystem:
    def __init__(self, player_ship, enemy_ships):
        self.player_ship = player_ship
        self.enemy_ships = enemy_ships
        self.player_ship.attack_roll_bonus = self.calculate_attack_roll_bonus(player_ship)
        for enemy_ship in self.enemy_ships:
            enemy_ship.attack_roll_bonus = self.calculate_attack_roll_bonus(enemy_ship)
        self.player_ship.critical_hit_chance = 0.20  # Give the player a higher critical hit chance
        self.player_ship.critical_hit_damage_multiplier = 2  # Set the multiplier for critical hits

    # Calculate the total damage a ship can inflict
    def calculate_attack_roll_bonus(self, ship):
        total_bonus = 0
        for weapon, count in ship.weapons.items():
            total_bonus += data.weapons_list[weapon].damage_per_minute * count  # weapon.damage_per_minute * count
        return total_bonus

    # Get attack damage of a ship from a random weapon it has
    def get_attack_damage(self, ship):
        damage = 0
        for weapon, count in ship.weapons.items():
            damage += random.randint(1, data.weapons_list[weapon].damage_per_minute) * count
        return damage

    def delay_with_dots(self, seconds):
        for _ in range(seconds):
            time.sleep(1)
            print(".", end='')

	# The fight method in the CombatSystem class

    def fight(self):
        while self.player_ship.health > 0 and any(enemy_ship.health > 0 for enemy_ship in self.enemy_ships):
            for enemy_ship in self.enemy_ships:
                if enemy_ship.health > 0:  # Ensure that enemy_ship can attack only if it is not destroyed
                    enemy_damage = self.get_attack_damage(enemy_ship)
                    print(f"Enemy ship {enemy_ship.name} deals {enemy_damage} damage! ", end='')
                    self.player_ship.take_damage(enemy_damage)

                if self.player_ship.health <= 0:  # Check after each attack if the player ship's health is zero
                    print("Your ship is destroyed. You were defeated!")
                    return  # Exit the function as soon as player's health reaches zero

                if enemy_ship.health > 0:  # Ensure that player_ship can attack only if the enemy_ship is not destroyed
                    player_damage = self.get_attack_damage(self.player_ship)
                    print(f"Your ship {self.player_ship.name} deals {player_damage} damage to enemy ship {enemy_ship.name}! ", end='')
                    enemy_ship.take_damage(player_damage)
		    
                    print(f"\nYour ship {self.player_ship.name}'s health is {self.player_ship.health}. Enemy ship {enemy_ship.name}'s health is {enemy_ship.health}.\n")

        print()
        if self.player_ship.health > 0 and not any(enemy_ship.health > 0 for enemy_ship in self.enemy_ships):
            print("You defeated the enemies!")
        elif self.player_ship.health <= 0 and any(enemy_ship.health > 0 for enemy_ship in self.enemy_ships):
            print("You were defeated!")
        else:
            print("The battle was a draw!")






class UISystem:
	@staticmethod
	def ui_screens(screen="start"):
		if screen == "start":
			print(views.content["branding_title"])
			player_name = input(lang.content["temp_enter_name"])
			player_menu_select = input(views.content["select_main"]).lower()
			print(lang.content["temp_print_selection"].format(player_name=player_name, player_menu_select=player_menu_select))
		elif screen == "main":
			player_menu_select = input(views.content["select_main"]).lower()
		elif screen == "travel":
			player_menu_select = input(views.content["select_travel"]).lower()
		return player_menu_select



#################### (main)

# UISystem.ui_screens()					# start


# initialize player
player_01 = Player()	# player_id=1, player_username="SirLootALot", initial_balance=0)

player_list = []
player_list.append(player_01)

player_01.storage.update( {"Solstra": Storage("Solstra", 50000)} )	# test only; can be instantiated by other means
player_01.balance = 50000
player_01.storage["Solstra"].add_item("Pulse Cannon",5)	# later "Solstra" changed to curr_loc
player_01.storage["Solstra"].add_item("Railgun",7)
player_01.storage["Solstra"].remove_item("Pulse Cannon",2)
player_01.storage["Solstra"].add_item("Graviton Beam",2)


# init_ship converts strings to fully-formed list for Ship object declaration
sample_ship = Ship(*Ship.init_ship("Prometheus", "light freighter"))
sample_ship.load_cargo( {"arms": 2, "gadgets": 5, "minerals": 2} )
sample_ship.load_cargo( {"food_supplies": 10, "gadgets": 9 } )
sample_ship.load_cargo( {"arms": 10, "raw_materials": 5, "minerals": 5} )
sample_ship.remove_cargo( {"raw_materials": 3, "arms": 2} )
sample_ship.remove_cargo( {"minerals": 5, "arms": 5, "gadgets": 6} )
sample_ship.load_cargo( {"raw_materials": 5, "arms": 5} )

sample_ship.attach_weapon( {"Pulse Cannon": 2, "Railgun": 1} )
sample_ship.attach_weapon( {"Plasma Blaster": 2, "Railgun": 1} )
sample_ship.remove_weapon( {"Pulse Cannon": 1, "Plasma Blaster": 1})

# transfer weapons between ship and storage
player_01.storage["Solstra"].transfer_to_ship(sample_ship, "Railgun", 3)
player_01.storage["Solstra"].receive_from_ship(sample_ship, "Railgun", 2)

# test combat system
# combat_01 = CombatSystem(sample_ship, [enemy_ship]) # Note the brackets around enemy_ship

enemy_ship = Ship(*Ship.init_ship("Vindelix", "light freighter", -1, -1))	# last two parameters at zero or below indicate NPC enemy ships
enemy_ship.attach_weapon( {"Pulse Cannon": 2, "Railgun": 1} )
enemy_ship.attach_weapon( {"Plasma Blaster": 2, "Railgun": 1} )
enemy_ship.remove_weapon( {"Pulse Cannon": 1, "Plasma Blaster": 1})
# combat_01 = CombatSystem(sample_ship, enemy_ship)

enemy_ship_02 = Ship(*Ship.init_ship("Foobar", "stealth cruiser", -2, -2)); enemy_ship_02.attach_weapon( {"Pulse Cannon": 1, "Railgun": 1} )
enemy_ship_03 = Ship(*Ship.init_ship("Widowmaker", "orbital defense platform", -3, -3)); enemy_ship_03.attach_weapon( {"Pulse Cannon": 2, "Railgun": 2} )
enemy_ship_04 = Ship(*Ship.init_ship("Betelgeuse", "mining frigate", -4, -4)); enemy_ship_04.attach_weapon( {"Pulse Cannon": 1, "Railgun": 1} )
enemy_ship_05 = Ship(*Ship.init_ship("Bellerophon", "battlecruiser", -5, -5)); enemy_ship_05.attach_weapon( {"Pulse Cannon": 1, "Railgun": 2} )

enemy_ships = [enemy_ship, enemy_ship_02, enemy_ship_03, enemy_ship_04, enemy_ship_05]
combat_01 = CombatSystem(sample_ship, enemy_ships)


combat_01.fight()

# trading marketplace
print(\
"""

.
.
.


>>>>>>>>>>>>>>>>>>>>>>>>>>>>
> STARTING Trading Process >
>>>>>>>>>>>>>>>>>>>>>>>>>>>>

""")
mkt = TradingMarketplace(player_01, "Solstra")
mkt.add_item("weapons", "Railgun", 58, 300)
mkt.add_item("goods", "food_supplies", 100, 12)
mkt.add_item("weapons", "Plasma Blaster", 50, 2500)
mkt.sell_item("weapons", "Railgun", 1)
mkt.buy_item("weapons", "Plasma Blaster", 3)

'''
sell_item(self, item_type, item_id, qty):
'''


'''
sample_storage = Storage("Solstra", 50000)
sample_storage.add_item("Pulse Cannon",5)
sample_storage.add_item("Railgun",7)
sample_storage.remove_item("Pulse Cannon",2)
sample_storage.add_item("Graviton Beam",2)

sample_storage.transfer_to_ship(sample_ship, "Railgun", 3)
sample_storage.receive_from_ship(sample_ship, "Railgun", 2)

print("Here's the results from the game: \n", sample_ship)

util.display_map()
'''

