content = {
	
	# input() : UI
	"temp_enter_name" : "Enter your name: ",
    #"temp_print_selection" : "\nOK, " + player_name + ", you selected: '" + player_menu_select + "'.\n\n(Note: This is a pre-alpha version and meant to show you input works and ready to process.)\n\n",
	"temp_print_selection" : "\nOK, {player_name}, you selected: '{player_menu_select}'.\n\n(Note: This is a pre-alpha version and meant to show you input works and ready to process.)\n\n",



	# Cargo

	"cargo_loaded": "\n----------\nCargo has been loaded. Stats:\nTotal ship capacity: {one}\nCapacity used: {two} // Remaining capacity: {three}\nCargo inventory: {four}\n----------\n",
	"cargo_not_loaded": "Cargo was not loaded. Item mismatch or quantity of goods exceed storage capacity.",
	"cargo_removed": "\n----------\nCargo has been removed. Stats:\nTotal ship capacity: {one}\nCapacity used: {two} // Remaining capacity: {three}\nCargo inventory: {four}\n----------\n",
	"cargo_not_removed" : "Cargo not removed! Capacity entered is more than inventory.\n",
    "inv_capacity_used": " Total capacity used: ",
    

	# __repr__
	"repr_ship": "This ship {name} is of type {ship_type} and class {ship_class}, has a passenger capacity now of {passenger_capacity}, cargo capacity of {cargo_capacity}, weapons capacity of {weapons_capacity}. Cargo is {cargo} while weapons is {weapons}.\n\n",

	# utilities
	"labelwidths": ["Inventory", "Qty", "Capacity", "Total"],
}