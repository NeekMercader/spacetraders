content = {
	
	# input() : UI
	"temp_enter_name" : "Enter your name: ",
    #"temp_print_selection" : "\nOK, " + player_name + ", you selected: '" + player_menu_select + "'.\n\n(Note: This is a pre-alpha version and meant to show you input works and ready to process.)\n\n",
	"temp_print_selection" : "\nOK, {player_name}, you selected: '{player_menu_select}'.\n\n(Note: This is a pre-alpha version and meant to show you input works and ready to process.)\n\n",

	# Player
	"not_enough_balance": "Not enough balance.",

	# Cargo

	"cargo_loaded": "Cargo has been loaded: {four}\n(Qty: {five}, Capacity: {six})\nTotal capacity used: {two} of {one} (Remaining: {three})",
	"cargo_not_loaded": "Cargo was not loaded. Item mismatch or quantity of goods exceed storage capacity.",
	"cargo_removed": "Cargo has been removed: {four}\n(Qty: {five}, Capacity: {six})\nTodal capacity used: {two} of {one} (Remaining: {three})",
	"cargo_not_removed" : "Cargo not removed! Attempting to remove an item that is nonexistent or capacity entered to remove is more than weapon quantity.",
    
	# Weapon

	"weapon_loaded": "Weapon has been loaded to ship: {four}\n(Qty: {five}, Capacity: {six})\nTotal capacity used: {two} of {one} (Remaining: {three})",
	"weapon_not_loaded": "Weapon was not loaded. Item mismatch or quantity of weapons exceed storage capacity.",
	"weapon_removed": "Weapon has been removed from ship: {four}\n(Qty: {five}, Capacity: {six})\nTodal capacity used: {two} of {one} (Remaining: {three})",
	"weapon_not_removed" : "Weapon not removed! Attempting to remove a weapon that is nonexistent or capacity entered to remove is more than weapon quantity.",
    	

	# __repr__
	"repr_ship": "This ship {name} is of type {ship_type} and class {ship_class}, has a passenger capacity now of {passenger_capacity}, remaining cargo capacity of {cargo_capacity}, weapons capacity of {weapons_capacity}. Cargo is {cargo} while weapons is {weapons}.\n\n",

	# utilities
	"thead_labels_cargo": ["Inventory", "Qty", "Capacity", "Total"],
	"thead_labels_weapon": ["Arsenal", "Qty", "Capacity", "Total", "Damage", "Hitpoints"],
    

	# travel: planets
	"label_header_map": "MAP OF GALACTIC SECTOR",
    "label_line_header_map": "----------------------",
    
	# Bank
	"deposited_to_bank": "Deposited {amount} credits into the bank.",
    "invalid_deposit": "Invalid deposit amount.",
    "invalid_withdrawal": "Invalid withdrawal amount or insufficient balance.",
    "loan_paid": "You have paid off your loan.",
    "loan_unpaid": "Insufficient funds to pay off the loan.",
    "loan_overdue": "You have an overdue loan. Please pay it off immediately!",
    "not_loan_overdue": "No overdue loan.",
    
	# Maintenance
	"ship_repair_health": "You repaired your ship by {ship_health} health.",
    "cannot_repair_ship": "You can't repair your ship.",
    
	# CombatSystem
	"ship_destroyed": "Your ship is destroyed. You were defeated!\n",
    "enemy_defeated": "You defeated the enemies!\n",
    "battle_draw": "The battle was a draw!\n",



}