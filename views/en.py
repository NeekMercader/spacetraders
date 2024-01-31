content = {
    "branding_title" : """

███████╗██████╗  █████╗  ██████╗███████╗    ████████╗██████╗  █████╗ ██████╗ ███████╗██████╗ ███████╗
██╔════╝██╔══██╗██╔══██╗██╔════╝██╔════╝    ╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔════╝
███████╗██████╔╝███████║██║     █████╗         ██║   ██████╔╝███████║██║  ██║█████╗  ██████╔╝███████╗
╚════██║██╔═══╝ ██╔══██║██║     ██╔══╝         ██║   ██╔══██╗██╔══██║██║  ██║██╔══╝  ██╔══██╗╚════██║
███████║██║     ██║  ██║╚██████╗███████╗       ██║   ██║  ██║██║  ██║██████╔╝███████╗██║  ██║███████║
╚══════╝╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝       ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝

By Neek Mercader
[Version 0.20 pre-alpha]

""" 		# https://tableconvert.com/ascii-generator
,
    "select_main_legacy" : """

+---------------------------------------------------------------------------------------+
| Type your command:                                                                    |
+---------------------------------------------+-----------------------------------------+
|                                             |                                         |
| 'S' - Enter Ship:                           | 'P' - Player Settings / Dashboard       |
|     'W' - Weapons: Attach / Detach          |     'I' - Player & Ship Info            |
|     'T' - Travel                            |     'C' - Configure                     |
| 'W' - Storage (Transfer Cargo):             | 'I' - Gather Intel (Visit a Bar / Club) |
|     'W' - Move Goods from Warehouse to Ship | 'X' - Exit                              |
|     'S' - Move Goods from Ship to Warehouse |                                         |
| 'M' - Marketplace (Trade):                  |                                         |
|     'B' - Buy                               |                                         |
|     'S' - Sell                              |                                         |
|     'I' - Show Inventory                    |                                         |
| 'B' - Bank (Visit, Deposit, Withdraw):      +-----------------------------------------+
|     'D' - Deposit                           | Stats:                                  |
|     'W' - Withdraw                          +-----------------------------------------+
|     'B' - Make a Loan / Borrow              | Credits: 255,498    |   Bank: 243.85M   |
|     'P' - Pay Loan                          | Ship Health: 100%   |   Shields: 100    |
| 'Y' - Syndicate (Underground):              | Weapons Health:                         |
|     'B' - Make a Loan / Borrow              |     100% (12 slots used of 25 capacity) |
|     'P' - Pay Loan                          | Cargo Capacity:                         |
| 'R' - Maintenance & Repair                  |     2500 of 5000 (2500 available)       |
|                                             |                                         |
+---------------------------------------------+-----------------------------------------+

Command: """,

    "select_main" : """

+-----------------------------------------+-----------------------------------------------+
  Type your command:                      | Info:
+-----------------------------------------+-----------------------------------------------+
  'S' - Enter Ship                        | Location: {gameinfo['location']}
  'W' - Storage (Transfer Cargo)          | Ship: {gameinfo['shipname']}
  'M' - Marketplace (Trade)               |                                                
  'B' - Bank (Visit, Deposit, Withdraw)   +-----------------------------------------------+
  'Y' - Syndicate (Underground)           | Stats:
  'R' - Maintenance & Repair              +-----------------------------------------------+
  'I' - Gather Intel (Visit a Bar / Club) | Credits (On Hand): {gameinfo['credits_on_hand']}
                                          | Bank: {gameinfo['bank_balance']}
+-----------------------------------------+ Ship Health:  {gameinfo['ship_health']}  (Shields:  {gameinfo['ship_shields']})
  'P' - Player Settings / Dashboard       | Weapons: {gameinfo['weapons_slots_used']} slots used of {gameinfo['weapons_max_capacity']} capacity
  'X' - Exit                              | Cargo Capacity: {gameinfo['cargo_used']} of {gameinfo['cargo_capacity']} ({gameinfo['cargo_available']} available)
+-----------------------------------------+-----------------------------------------------+

Command: """,


    "submenu_s" : """

+---------------------------------+--------------------------------+
| Your Order:                                                      |
+---------------------------------+--------------------------------+
   'W' - Weapons: Attach / Detach
   'T' - Travel   
+---------------------------------+--------------------------------+

Command: """,


    "submenu_s_w" : """

+---------------------------------+--------------------------------+
| Enter your destination:                                          |
+---------------------------------+--------------------------------+
   'A' - Attach Weapons from Storage to Ship
   'D' - Detach Weapons from Ship to Storage   
+---------------------------------+--------------------------------+

Command: """,

    "submenu_s_t" : """

+---------------------------------+--------------------------------+
| Enter your destination:         |                                |
+---------------------------------+--------------------------------+
  '1' = Solstra
  '2' = Pulsarion
  '3' = Caelus Prime
  '4' = Draconis
  '5' = Lunaria
  '6' = Stellaria
  '7' = Galaxion
+---------------------------------+--------------------------------+

Command: """,


    "input_endscreen" : """

    ===============
    'R' - Restart
    'X' - Exit
    ===============
    Make a selection: """,



    "invalid_choice" : """

+---------------------------------+--------------------------------+
| Invalid choice. Please enter a letter for your command.          |
+---------------------------------+--------------------------------+

""",


    "main_menu" : """

[Menu]


Command: """,



}



# template:
'''
    "key" : """

[value]

Command: """,

'''
