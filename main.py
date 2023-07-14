'''
    ### Space Traders ###
    A space trading simulator.
'''

import time
import random

from typing import Any

import languages.en as lang
import views.en as views
import data.data as data
import utilities.utilities as util


'''

import os
import sys     # for sys.exit()

class Species:
    def __init__(self, species_name, home_planet, personality="friendly"):
        self.species_name = species_name
        self.home_planet = home_planet
        self.personality = personality

class Creature:                            # lifeform (human, alien, droid)
    def __init__(self, species, name):
        self.species = species            # race
        self.name = name

        self.type = []                    # e.g. "trader", "warlord", "loanshark", "thug", "police", "military"
        self.ship = object()
        self.fleet = {}

class Location:                            # Places like stars, biomes/planets, moons, space stations, ports, etc. (calling them all "planets" is inacccurate)
    def __init__(self, name, location_type, classification="standard"):    # e.g. ()"Moony McMoonFace", "moon", "military")
        self.name = name 
        self.location_type = location_type
        self.classification = classification

        self.parent_site = object()
        self.coords = ""
        self.description = ""

class Weapon:
    def __init__(self, weapon_dict):    # e.g. { "Railgun": { "Weapon Class": "Projectile", "Damage Per Minute": 150, "Hitpoints": 250, "Capacity Used": 10, "Range": "500 meters", "Regeneration Time": 5 } }
        self.weapon_name = (*weapon_dict,)        
        self.in_working_condition = True         # working? destroyed?
        self.capacity_used = weapon_dict["Capacity Used"]
        self.damage_per_minute = weapon_dict["Damage Per Minute"]
        self.hitpoints = weapon_dict["Hitpoints"]
        return

class Goods:
    def __init__(self, cat, name, capacity_used, baseprice):
        self.cat = cat                # category (deprecated: self.sku = sku)
        self.name = name
        self.capacity_used = capacity_used    # capacity amount used by this unit
        self.baseprice = baseprice    # suggested retail (standard)
        
    def __repr__(self):
        return str(dir(self))
    

'''

class Player:

    player_list = []    # for multiple player system; later for multiplayer gameplay

    def __init__(self, player_id=1, player_username="SirLootALot", initial_balance=0, initial_bank_balance=0):    # balance = money
        self.player_id = player_id
        self.player_username = player_username
        self.balance = initial_balance    # money (cash) on hand
        self.bank_balance = initial_bank_balance    # bank deposit
        self.loan = 0
        self.syndicate_loan = 0
        self.hit_order = 0    # at level 2, thugs; at 3, kill order; at 4, all-out (John Wick style)
        self.no_repeat_switch = False    # don't repeat harassing or adding to hit_order from method 

        self.curr_location = "Solstra"
        self.reputation = 0
        self.storage = {}    # dict of Storage instances based on location; e.g. { "Solstra": Storage("Solstra", 50000), }

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
            print(util.msg("not_enough_balance"))

    def add_to_playerlist(self):
        self.__class__.player_list.append(self)        # Player.player_list.append(self)



class Ship:
    @staticmethod
    def init_ship(shipname="Bellerophon", shiptype="light freighter", owner = 1, fleet = 1):    # automator for object definition; used in constructor
        # shipdata = [x for x in data.ship_data[shiptype][:-1]]
        shipdata = list(data.ship_data[shiptype][:-1])
        shipdata.insert(0, shipname)
        shipdata.append(owner)
        shipdata.append(fleet)
        return shipdata

    # def __init__(self, name, ship_type, ship_class, cargo=500, weapon=100, passenger=1, owner=1, fleet=1):
    def __init__(self, *argslist):
        name, ship_type, ship_class, cargo, weapon, passenger, owner, fleet = argslist
        self.name = name
        self.ship_type = ship_type        # cargo, fighter, hybrid, cruiser, capital (ship)
        self.ship_class    = ship_class    # enterprise, starliner, starfighter, x-wing
        self.cargo_capacity = cargo
        self.weapon_capacity = weapon
        self.passenger_capacity = passenger
        self.fleet = fleet                # fleet ID# (not qty) (default: #1)

        player_list = Player.player_list
        self.owner = owner if owner in range(data.NUMBER_OF_PLAYERS) else len(player_list)                # (default: #1) above NUMBER_OF_PLAYERS means (enemy) NPC
        self.player = player_list[self.owner - 1]    # player_list = list of Player instances. [len(self.owner) + 1] = NPC

        self.shields = data.STD_SHIP_SHIELDS                # shield strength (and health)
        self.health = data.STD_SHIP_HEALTH if owner > 0 else data.ENEMY_SHIP_HEALTH        # health standard: player: 10000 / enemy: 2500 )
        self.ship_mods = {}        # warp boosters, shield boost, custom phasers, expanded cargo holds

        self.utilized_passenger_capacity = 1
        self.utilized_cargo_capacity = 0
        self.utilized_weapon_capacity = 0

        self.passengers = 1
        self.cargo = {}
        self.weapons = {}

    def __repr__(self):
        return util.msg("repr_ship").format(name=self.name, ship_type=self.ship_type, ship_class = self.ship_class, passenger_capacity = self.passenger_capacity, cargo_capacity = self.utilized_cargo_capacity, weapons_capacity = self.utilized_weapon_capacity, cargo = self.cargo, weapons = self.weapons)

    def set_curr_location(self, location):
        self.player.curr_location = location
        self.curr_location = location

    def load_cargo(self, goods, show_stats=False):        # goods = dict (e.g. { "food" : 200, "arms" : 10 })
        goods_capacity = self.compute_capacity(goods)
        if self.cargo_capacity >= self.utilized_cargo_capacity + goods_capacity:
            self.utilized_cargo_capacity += goods_capacity
            for item in goods.keys():
                self.cargo[item] = self.cargo.get(item, 0) + goods[item] # item qty, not capacity 

            print(util.msg("cargo_loaded").format(one=self.cargo_capacity,two=self.utilized_cargo_capacity,three=self.cargo_capacity-self.utilized_cargo_capacity,four=goods,five=sum(goods.values()),six=goods_capacity))
        else:
            print(util.msg("cargo_not_loaded"))
            return False
        # print(self.show_cargo_stats(goods))
        if show_stats == True: print(self.show_cargo_stats())    # .show_cargo_stats(self.cargo))
        return True
            
    def remove_cargo(self, goods, show_stats=False):            # goods = dict (e.g. { "food" : 200, "arms" : 10 })
        for item in goods.keys():            # check if quantities declared actually exist
            # if (self.cargo[item] < goods[item]):
            if (self.cargo.get(item,0) < goods[item]):
                print(util.msg("cargo_not_removed"), ": [\"", item, "\"].")    # erroneous qty; abort
                return False
        for item in goods.keys():            # now that we're safe, do the actual removals
            self.cargo[item] -= goods[item]
            if self.cargo[item] == 0:
                del self.cargo[item]        # if 0, remove entire item
        goods_capacity = self.compute_capacity(goods)        # check total capacity used
        self.utilized_cargo_capacity -= goods_capacity    # update counters
        print(util.msg("cargo_removed").format(one=self.cargo_capacity,two=self.utilized_cargo_capacity,three=self.cargo_capacity-self.utilized_cargo_capacity,four=goods,five=sum(goods.values()),six=goods_capacity))
        if show_stats == True: print(self.show_cargo_stats())        # .show_cargo_stats(self.cargo))
        return True
    
    def attach_weapon(self, shipweapon):    # shipweapon = dict (e.g. { "Pulse Cannon" : 2, "Railgun" : 1 })
        weapon_capacity = self.compute_capacity(shipweapon, "weapons")
        if self.weapon_capacity >= self.utilized_weapon_capacity + weapon_capacity:
            self.utilized_weapon_capacity += weapon_capacity
            for item in shipweapon.keys():
                self.weapons[item] = self.weapons.get(item, 0) + shipweapon[item]    # qty, not capacity
            print(util.msg("weapon_loaded").format(one=self.weapon_capacity,two=self.utilized_weapon_capacity,three=self.weapon_capacity-self.utilized_weapon_capacity,four=shipweapon,five=sum(shipweapon.values()),six=weapon_capacity))
        else:
            for item in shipweapon.keys():    # fit weapons individually
                print("\n\n\n$$$$$$$$$$\nATTACH_WEAPON'S ITEM =", str(item), "\nSHIPWEAPON = ", str(shipweapon), "\nSHIPWEAPON(KEYS) = ", shipweapon.keys(), "\n\n\n")    # TEST
                item_dict = {}
                item_dict[item] = 1
                weapon_capacity_single = self.compute_capacity(item_dict, "weapons")
                if self.utilized_weapon_capacity + weapon_capacity_single >= 0:
                    self.weapons[item] = self.weapons.get(item, 0) + shipweapon[item]
                else:
                    print(util.msg("weapon_not_loaded"))
                    return False
        print(self.show_weapon_stats(self.weapons))
        return True
    
    '''
    # enemy_ship.attach_weapon({item: random.randint(1,data.RANDOM_SHIP_WEAPONS_MAX_PER)})
    def attach_weapon(self, shipweapon):    # shipweapon = dict (e.g. { "Pulse Cannon" : 2, "Railgun" : 1 })
        weapon_capacity = self.compute_capacity(shipweapon, "weapons")
        if self.weapon_capacity >= self.utilized_weapon_capacity + weapon_capacity:
            self.utilized_weapon_capacity += weapon_capacity
            for item in shipweapon.keys():
                self.weapons[item] = self.weapons.get(item, 0) + shipweapon[item]    # qty, not capacity
            print(util.msg("weapon_loaded").format(one=self.weapon_capacity,two=self.utilized_weapon_capacity,three=self.weapon_capacity-self.utilized_weapon_capacity,four=shipweapon,five=sum(shipweapon.values()),six=weapon_capacity))
        else:
            for item in shipweapon.keys():    # .keys()    # fit weapons individually
                util.debug_checkpoint("INSIDE ATTACH_WEAPON'S ELSE: CLAUSE. Shipweapon = ", shipweapon)
                weapon_capacity_single = self.compute_capacity(shipweapon, "weapons")
            
                if self.utilized_weapon_capacity + weapon_capacity_single >= 0:
                    util.debug_checkpoint("INSIDE ATTACH_WEAPON'S ELSE then IF: CLAUSE. Item = " + item + " item = ", item)
                    self.weapons[item] = self.weapons.get(item, 0) + shipweapon[item]
                else:
                    print(util.msg("weapon_not_loaded"))
                    return False
        print(self.show_weapon_stats(self.weapons))
        return True    
        """    
        else:
            print(util.msg("weapon_not_loaded"))
            return False
        print(self.show_weapon_stats(self.weapons))
        return True
        """
    '''

    def remove_weapon(self, shipweapon):    # { "Pulse Cannon" : 2, "Railgun" : 1 })
        for item in shipweapon.keys():
            if (self.weapons.get(item,0) < shipweapon[item]):
                print(util.msg("weapon_not_removed"), ": [\"", item, "\"].")    # erroneous qty; abort
                return False
        for item in shipweapon.keys():
            self.weapons[item] -= shipweapon[item]
            if self.weapons[item] == 0:
                del self.weapons[item]
        weapon_capacity = self.compute_capacity(shipweapon, "weapons")
        self.utilized_weapon_capacity -= weapon_capacity
        print(util.msg("weapon_removed").format(one=self.weapon_capacity,two=self.utilized_weapon_capacity,three=self.weapon_capacity-self.utilized_weapon_capacity,four=shipweapon,five=sum(shipweapon.values()),six=weapon_capacity))
        print(self.show_weapon_stats(self.weapons))
        return True

    # return item (goods/cargo or weapons) qty
    def check_item_qty(self, item):
        return self.cargo[item] if item in self.cargo else self.weapons[item]

    def compute_capacity(self, itemlist, itemtype="goods"):            # itemlist = dict of goods (e.g. { "food" : 200, "arms" : 10 }) (if weapons, itemtype="weapons")
        capacity = 0
        print("\n\n\n$$$$$$$$$$\nITEMLIST = ", str(itemlist), "\n$$$$$$$$$$\n\n\n\n")
        for item in itemlist.keys():
            capacity += (data.goods_data[item]["capacity used"] if itemtype == "goods" else data.weapon_data[item]["Capacity Used"] )     # * itemlist[item]
        return capacity

    def show_cargo_stats(self):
        cargo = self.cargo
        total_capacity = 0
        rows = []
        for item in cargo.keys():
            subtotal_capacity = data.goods_data[item]["capacity used"] * cargo[item]
            total_capacity += subtotal_capacity

            rows.append([data.goods_data[item]["cat"], cargo[item], data.goods_data[item]["capacity used"], subtotal_capacity ])    # format_table() will string-ify; cargo[item] = qty
        return(util.format_table(rows, lang.content["thead_labels_cargo"]))
    
    def show_weapon_stats(self, weapon):
        total_capacity = 0
        rows = []
        for item in weapon.keys():
            subtotal_capacity = data.weapon_data[item]["Capacity Used"] * weapon[item]
            total_capacity += subtotal_capacity

            # rows.append([item, weapon[item], data.weapon_data[item]["Capacity Used"], subtotal_capacity ])    # format_table() will string-ify; weapon[item] = qty
            rows.append([item, weapon[item], data.weapon_data[item]["Capacity Used"], subtotal_capacity, data.weapon_data[item]["Damage Per Minute"], data.weapon_data[item]["Hitpoints"] ])    # format_table() will string-ify; weapon[item] = qty
        return(util.format_table(rows, lang.content["thead_labels_weapon"]))
    
    def take_damage(self, damage):
        if self.shields > 0:
            print(util.msg("take_damage_shields").format(name=self.name, health=self.health, shields=self.shields))
        self.shields -= damage
        if self.shields < 0:
            self.health += self.shields
            self.shields = 0
        if self.health <= 0:
            self.health = 0
            print(f"Ship {self.name} has been destroyed!")
            return 
        # print(f"{self.name} takes {damage} damage. {self.name} health is {self.health} (shields: {self.shields}).")
        print(util.msg("take_damage").format(name=self.name, damage=damage, health=self.health, shields=self.shields))
    
    @staticmethod
    def random_ships_and_weapons(quantity, name_type="player"):        # which list? "player" (default) or "enemy"
        names = []
        if name_type == "player":
            random_names = data.ship_names
        elif name_type == "enemy":
            random_names = data.enemy_ship_names
        elif name_type == "ship_types":
            random_names = list(data.ship_data.keys())
        elif name_type == "weapon_types":
            random_names = list(data.weapon_data.keys())
        else:
            pass

        # indices = random.sample(range(len(random_names)), quantity)    # Generate random indices without duplicates
        shiplist = random.sample(random_names, quantity)
        for shipitem in shiplist:    # Get names corresponding to the random indices
            # names.append(random_names[idx])
            names.append(shipitem)
        return names


class LoanSystem:

    def __init__(self, player, loan_source="bank"):
        self.player = player
        self.loan_source = loan_source
        # pass


    # Loan money to the player
    def loan_money(self, player):
        loanable_amt = data.STD_LOANABLE_AMT if loan_source == "bank" else data.SYNDICATE_LOANABLE_AMT
        loan_amount = (self.player.balance + self.player.bank_balance) * loanable_amt
        self.player.loan = loan_amount
        self.player.balance += loan_amount
        print(f"You have borrowed ${loan_amount:.2f} from the bank.")

    # Pay off the loan.
    def pay_loan(self, player):
        print(util.msg("player_balance").format(balance=self.player.balance))
        if self.player.loan == 0: return    # there is no loan balance to begin
        amt = int(input(util.msg("how_much_to_pay").format(player_loan=self.player.loan)))
        while (amt > self.player.balance) or (amt > self.player.loan) or (amt <= 0):
            print(util.msg("amount_out_of_range"))
            amt = int(input(util.msg("how_much_to_pay").format(player_loan=self.player.loan)))
        self.player.balance -= amt
        self.player.loan -= amt

        if self.player.loan == 0:
            print(util.msg("loan_paid"))
        elif self.player.loan > 0:
            print(util.msg("loan_partially_paid").format(outstanding_loan=self.player.loan))
        else:
            print(util.msg("loan_amt_invalid"))

    # Calculate and apply interest on the loan.
    def calculate_interest(self, player):
        interest_rate = data.STD_INTEREST_RATE if loan_source == "bank" else data.SYNDICATE_INTEREST_RATE
        interest = self.player.loan * interest_rate
        self.player.loan += interest
        print(f"Interest applied: ${interest:.2f}")

    # Harass the player if the loan is past due.
    def remind_of_loan(self, player, severity):
        if self.player.loan > 0:
            print(util.msg("loan_overdue"))
            if severity >= data.LOAN_SEVERITY_LEVEL[2]:    # if over threshold, player is marked
                self.player.hit_order = severity
        return


class Bank(LoanSystem):
    def __init__(self, player, location="Solstra"):    # loan_source: "bank", "syndicate"
        self.location = location
        super().__init__(player, "bank")    # access  loan engine superclass parent
        
    # Deposit money into the bank.
    def deposit(self, player, amount):
        if amount > 0:
            player.bank_balance += amount
            # print(f"Deposited ${amount:.2f} into the bank.")
            print(util.msg("deposited_to_bank").format(amount=amount))
        else:
            print(util.msg("invalid_deposit"))

    # Withdraw money from the bank.
    def withdraw(self, player, amount):
        if amount > 0 and player.balance >= amount:
            player.bank_balance -= amount
            print(f"Withdrawn ${amount:.2f} from the bank.")
        else:
            print(util.msg("invalid_withdrawal"))

class Syndicate(LoanSystem):
    def __init__(self, player, location="Solstra"):
        super().__init__(player, "syndicate")

    def compel_meeting():
        print(util.msg("compel_meeting"))    # separate from ArrivalRoutine that activates visit
        return
    
    @staticmethod
    def add_hit_order(player):
        if player.no_repeat_switch == False:
            player.no_repeat_switch = True    # no need to keep repeating
            player.hit_order += 1
        print(f"\n\n@@@\nTEST: Balance: {player.balance} | Hit order: {player.hit_order} | No repeat switch: {player.no_repeat_switch} \n@@@\n\n")

    @staticmethod
    def remove_hit_order(player):
        if player.no_repeat_switch == True:
            player.no_repeat_switch = False
            player.hit_order -= 1 

    @staticmethod
    def do_favor(player):
        donation_amt = random.randint(int(player.balance * .05), int(player.balance * .30))    # currently set between 5% - 30% of player's cash on hand
        print(util.msg("do_favor").format(donation_amt=donation_amt))
        favor = input("Will you donate? ").lower()
        if favor == 'y' or favor == lang.content["yes"]:
            player.balance -= donation_amt
            player.hit_order -= 1 if player.hit_order > 0 else 0    # not zero, in case there are multiple hit ordrers
            player.no_repeat_switch = False    # no need to keep repeating invitation to meet Syndicate
            print(f"\n\n@@@\nTEST: Balance: {player.balance} | Hit order: {player.hit_order} | No repeat switch: {player.no_repeat_switch} \n@@@\n\n")
            return True
        else:
            Syndicate.add_hit_order(player)
        return False

    @staticmethod
    def delinquency():
        print(util.msg("delinquency"))
        return

    @staticmethod
    def beatdown(player):
        print(util.msg("beatdown"))
        player.balance = 0        # all carryon cash is stolen
        return


class ArrivalRoutines:    # note: call standard_routines()
    def __init__(self):
        self.days = 0

    def standard_routines(self, player, ship):
        self.days += 1        # add a routine day

        self.update_interest(player)
        # self.check_ship_health(ship)
        # self.syndicate_visit(player)
        self.police_raid(player, ship)

    def update_interest(self, player):                                    # update counters
        player.bank_balance *= int(data.STD_INTEREST_RATE / 365)            # bank interest
        player.loan *= int(data.STD_LOAN_INTEREST_RATE / 365)                # bank's loan's interest (opporesive!)
        player.syndicate_loan *= int(data.SYNDICATE_INTEREST_RATE / 365)    # syndicate's loan's interest (opporesive!)

    # check if repairs or maintenance needed
    def check_ship_health(self, ship):
        if ship.health < data.STD_SHIP_HEALTH:
            repair = input(util.msg("ask_repair_ship")).lower()
            if repair == 'y':
                Maintenance.repair_ship(ship)

    def syndicate_visit(self, player):
        Syndicate.compel_meeting()
        decision = input(util.msg("ask_visit_syndicate")).lower()
        if decision == 'y':
            print(util.msg("visiting_syndicate"))
            time.sleep(1)
            Syndicate.do_favor(player)
        else:
            Syndicate.add_hit_order(player)
        return
        
    # police_raid
    def police_raid(self, player, ship):
        if "contraband" in ship.cargo:
            if 1: # if (random.randint(1, 5) == 1):        # 20% odds, 1 in 5
                fine = ship.cargo["contraband"] * (player.balance * 0.05)     # fine = contraband * (5% of cash balance)
                del ship.cargo["contraband"]
                player.balance -= int(fine)
                print(util.msg("police_confiscation").format(fine=fine, balance=player.balance))




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
        return (data.goods_data[item]["capacity used"] * qty) if item in data.goods_data else (data.weapon_data[item]["Capacity Used"]) * qty

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
    def transfer_to_ship(self, ship, item, qty):    # , itemtype="cargo"
        if self.items.get(item, 0) >= qty:
            # ship.load_cargo({item: qty})  # assumes ship's load_cargo method takes a dict
            if ( ship.load_cargo({item: qty}) if item in data.goods_data else ship.attach_weapon({item: qty}) ):
                self.remove_item(item, qty)
                print(f"\n-----\nItems ({item}: {qty}) moved from storage to ship.\nShip inventory:\n\t{ship.cargo} (cargo)\n\t{ship.weapons} (weapons)\nStorage inventory: {self.items}\n-----\n")
        else:
            print(f"Insufficient qty to transfer {qty} units of {item}.")

    # Transfer a qty of an item from a ship to storage. (items can be of itemtype "cargo" or other (e.g. "weapons"))
    def receive_from_ship(self, ship, item, qty):    # , itemtype="cargo"
        if ship.check_item_qty(item) >= qty:
            # ship.remove_cargo({item: qty})  # assumes ship's remove_cargo method takes a dict
            if ( ship.remove_cargo({item: qty}) if item in data.goods_data else ship.remove_weapon({item: qty}) ):
                self.add_item(item, qty)
                print(f"\n-----\nItems ({item}: {qty}) moved from ship to storage.\nShip inventory:\n\t{ship.cargo} (cargo)\n\t{ship.weapons} (weapons)\nStorage inventory: {self.items}\n-----\n")
            else:
                print(f"\nError. Something went wrong.\n\n")
        else:
            print(f"Insufficient quantity to receive {qty} units of {item} from ship.")


class TradingMarketplace:

    def __init__(self, player, location):        # player = Player object
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
                item_dict[item_id]['qty'] += qty    # marketplace stock/inventory
            else:
                item_dict[item_id] = {'qty': qty, 'price': self.player.get_item_price(item_type, item_id)}
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
    # get item info dict 
    def get_item_dict(self, item_type):
        return self.market.get(item_type, {})

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
    def repair_ship(ship):    # percentage: 100%
        # ship = ship
        player = ship.player

        damage = data.STD_SHIP_HEALTH - ship.health

        money_needed = int(damage * data.REPAIR_PER_DAMAGE)    # money_needed = int(damage * repair_percentage * REPAIR_PER_DAMAGE)

        if player.balance >= money_needed:      # do we have enough money available?
            player.balance -= money_needed
            ship.health += int(damage)    # . += int(repair_percentage * damage)
            print(util.msg("ship_repair_health").format(ship_health=ship.health))
        else:
            print(util.msg("cannot_repair_ship"))


class TravelSystem:

    @staticmethod
    def expand_selection(input_char):
        return data.planets[int(input_char) - 1]    # convert input char to planet name string (based on index #)

    def __init__(self, ship):        # player = Player object; provides Ship and location info
        self.ship = ship

    def ship_travel(self):
        selection = TravelSystem.expand_selection(Game.ui_screens("travel"))    # departure
        print(f"Traveling to {selection}...\n")

        # time.sleep(1)
        EventSystem(self)
        # time.sleep(1)

        
        print(f"Arriving in {selection}...\n")
        self.set_curr_location(selection)        # set ship location; later, fleet can have different locations
        self.player.curr_location = selection    # player location; fleet ships can be scattered in diff locations
        # selection = TravelSystem.expand_selection(Game.ui_screens("main"))        # arrival



class EventSystem:
    def __init__(self, ship):
        # self.ship = ship    # Ship instance
        
        event = data.eventlist[random.randint(1, len(data.eventlist) - 1)]  # could also be: event = random.choice(data.eventlist)
        
        print("\n\n\n\n\n#################################")
        print(f"\nInside EventSystem, current event is {event}.\n")
        print("#################################\n\n\n\n\n")

        # enemy_ships = CombatSystem.get_enemy_ships()
        enemy_ships = CombatSystem.initialize_enemies()
        combat_01 = CombatSystem(ship, enemy_ships)    # sample_ship
        combat_01.fight()
        '''
        if event == "nothing":
            pass
        elif event == "pirate_attack" or event == "alien_attack":
            # CombatSystem(self.ship)

            enemy_ships = CombatSystem.get_enemy_ships()
            combat_01 = CombatSystem(sample_ship, enemy_ships)
            combat_01.fight()



        elif event == "wormhole":
            pass
        elif event == "asteroid_shower":
            pass
        '''
        return



class CombatSystem:
    def __init__(self, player_ship, enemy_ships):
        self.player_ship = player_ship
        self.enemy_ships = enemy_ships
        self.player_ship.attack_roll_bonus = self.calculate_attack_roll_bonus(self.player_ship)
        for enemy_ship in self.enemy_ships:
            enemy_ship.attack_roll_bonus = self.calculate_attack_roll_bonus(enemy_ship)
        self.player_ship.critical_hit_chance = 0.20  # Give the player a higher critical hit chance
        self.player_ship.critical_hit_damage_multiplier = 2  # Set the multiplier for critical hits

    # Calculate the total damage a ship can inflict
    def calculate_attack_roll_bonus(self, ship):
        total_bonus = 0
        for weapon, count in ship.weapons.items():
            total_bonus += data.weapon_data[weapon]["Damage Per Minute"] * count  # weapon.damage_per_minute * count
        return total_bonus

    # Get attack damage of a ship from a random weapon it has
    def get_attack_damage(self, ship):
        damage = 0
        for weapon, count in ship.weapons.items():
            damage += random.randint(1, data.weapon_data[weapon]["Damage Per Minute"]) * count
        return damage

    def delay_with_dots(self, seconds):
        for _ in range(seconds):
            time.sleep(1)
            print(".", end='')

    # The fight method in the CombatSystem class

    def fight(self):
        enemy_qty = len(self.enemy_ships)
        selected = input(util.msg("run_or_fight").format(enemy_qty=enemy_qty,is_are=("ship is" if enemy_qty == 1 else "ships are")))
        while self.player_ship.health > 0 and any(enemy_ship.health > 0 for enemy_ship in self.enemy_ships):
            for enemy_ship in self.enemy_ships:
                # option to outrun
                chance = random.randint(1,10)    # 1 in 10 chance of outrunning
                if chance == 1 and selected.lower() == 'r':
                    print(util.msg("outran_enemy_ships"))
                    return
        
                if enemy_ship.health > 0:  # Ensure that enemy_ship can attack only if it is not destroyed
                    enemy_damage = self.get_attack_damage(enemy_ship)
                    print(f"Enemy ship {enemy_ship.name} deals {enemy_damage} damage! ")     # , end='')
                    self.player_ship.take_damage(enemy_damage)

                if self.player_ship.health <= 0:  # Check after each attack if the player ship's health is zero
                    print(util.msg("ship_destroyed"))
                    # Game.endscreen()
                    return  # Exit the function as soon as player's health reaches zero

                if enemy_ship.health > 0:  # Ensure that player_ship can attack only if the enemy_ship is not destroyed
                    player_damage = self.get_attack_damage(self.player_ship)
                    print(f"Your ship {self.player_ship.name} is dealing {player_damage} damage to enemy ship {enemy_ship.name}! ")     # , end='')
                    enemy_ship.take_damage(player_damage)
            
                    print(f"\nYour ship {self.player_ship.name}'s health is {self.player_ship.health}. ", end='')
                    print(f"Enemy ship {enemy_ship.name}'s health is {enemy_ship.health}.\n") if enemy_ship.health > 0 else print()    

        print()
        if self.player_ship.health > 0 and not any(enemy_ship.health > 0 for enemy_ship in self.enemy_ships):
            print(util.msg("enemy_defeated"))
        else:
            print(util.msg("battle_draw"))
        # Game.endscreen()
        return

    @staticmethod
    def initialize_enemies(mode="random", ship_qty=0, player_ship_health=data.STD_SHIP_HEALTH):    # modes: default / random / specific qty
        if ship_qty > 0:    # specific qty
            qty = ship_qty
        elif mode == "default":        
            qty = data.DEFAULT_ENEMY_SHIPS
        else:    # mode: random
            qty = random.randint(1, int(player_ship_health / data.ENEMY_SHIP_HANDICAP)) # base it on player ship as advantage for playability
        # compute relative health of player ship, to set matched enemy ship fleet health
        # qty = ship_qty if ship_qty > 0 else random.randint(1, int(self.player_ship.health / 2000))

        ship_names = Ship.random_ships_and_weapons(qty, "enemy")
        ship_types = Ship.random_ships_and_weapons(qty, "ship_types")
        ship_weapons = Ship.random_ships_and_weapons(qty, "weapon_types")    # important: check if qty matches ship capacity
    
        # util.debug_checkpoint("ship_weapons[]", ship_weapons)    # TEST
    
        enemy_ships = []
        for q in range(qty):
            enemy_ship = Ship(*Ship.init_ship(ship_names[q], ship_types[q], data.NUMBER_OF_PLAYERS+1, data.NUMBER_OF_PLAYERS+1))
            for item in ship_weapons:
                enemy_ship.attach_weapon({item: random.randint(1,data.RANDOM_SHIP_WEAPONS_MAX_PER)})
            enemy_ship.shields = 0
            enemy_ship.health = data.ENEMY_SHIP_HEALTH
        
            enemy_ships.append(enemy_ship)
        return enemy_ships


class Game:
    def __init__():
        pass

    @staticmethod
    def ui_screens(screen="start"):
        if screen == "start":
            print(views.content["branding_title"])
            player_name = input(lang.content["temp_enter_name"])
            player_menu_select = input(views.content["select_main"]).lower()
            print(util.msg("temp_print_selection").format(player_name=player_name, player_menu_select=player_menu_select))
        elif screen == "main":
            player_menu_select = input(views.content["select_main"]).lower()
        elif screen == "travel":
            player_menu_select = input(views.content["select_travel"]).lower()
        return player_menu_select
    
    @staticmethod
    def endscreen():
        choice = input(util.msg("input_endscreen", "view")).lower()
        if choice == 'x':    # choice 'x' (or anything else)
            print(util.msg("exit_msg"))
        return choice       

    @staticmethod
    def play_game():

        player_menu_select = Game.ui_screens()   # start the game

        while (player_menu_select != 'x') and (player_menu_select != lang.commands["exit"]): # to exit, user can press 'x' or type 'exit'
            
            # initialize player
            player_01 = Player()    # player_id=1, player_username="SirLootALot", initial_balance=0)

            player_01.add_to_playerlist()

            player_01.storage.update( {"Solstra": Storage("Solstra", data.PLAYER_STARTING_STORAGE)} )    # test only; can be instantiated by other means
            player_01.balance = data.PLAYER_STARTING_BALANCE
            player_01.storage["Solstra"].add_item("Pulse Cannon",5)    # later "Solstra" changed to curr_loc
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

            # test
            time_passage = ArrivalRoutines()
            # sample_ship.health = 5000    # test
            sample_ship.cargo["contraband"] = 10
            # time_passage.police_raid(player_01, sample_ship)
            time_passage.standard_routines(player_01, sample_ship)

            TravelSystem.ship_travel(sample_ship)

            player_01.loan = 12000    # testing
            # player_01.balance = 1000    # testing
            testbank = Bank(player_01)    # self, player, location="Solstra"
            testbank.pay_loan(player_01)

            '''
            # trading marketplace

            mkt = TradingMarketplace(player_01, "Solstra")
            mkt.add_item("weapons", "Railgun", 58, 300)
            mkt.add_item("goods", "food_supplies", 100, 12)
            mkt.add_item("weapons", "Plasma Blaster", 50, 2500)
            mkt.sell_item("weapons", "Railgun", 1)
            mkt.buy_item("weapons", "Plasma Blaster", 3)

            sell_item(self, item_type, item_id, qty):

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
            util.debug_checkpoint("Last player_menu_select")
            player_menu_select = Game.endscreen()



if __name__ == '__main__':
    Game.play_game()
