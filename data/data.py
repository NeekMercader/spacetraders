### constants

# player
PLAYER_STARTING_STORAGE = 50000
PLAYER_STARTING_BALANCE = 5000  # cash / credits
DEFAULT_ENEMY_SHIPS = 4 # max
ENEMY_SHIP_HANDICAP = 2000

# ship
STD_SHIP_HEALTH = 10000
STD_SHIP_SHIELDS = 1000
ENEMY_SHIP_HEALTH = 2500
REPAIR_PER_DAMAGE = 2	        # cost per unit damage multiplier
NUMBER_OF_PLAYERS = 4
RANDOM_SHIP_WEAPONS_MAX = 3     # randomize weapons in (usually enemy) ships
RANDOM_SHIP_WEAPONS_MAX_PER = 2 # max quantity of units per item weapon

# finance / bank / syndicate
STD_INTEREST_RATE = 0.1         # (deposit) 10% interest per year (365 turns)
STD_LOANABLE_AMT = 0.5          # Loan at 50% of net worth
STD_LOAN_INTEREST_RATE = 0.15   # loan interest
SYNDICATE_INTEREST_RATE = 1     # 100% interest per year (365 turns)
SYNDICATE_LOANABLE_AMT = 5      # Loan at (up to) 500% of net worth
LOAN_SEVERITY_LEVEL = (1,2,3,4,5)   # similar to DEFCON, Richter, and (storm) Category

# (name, ship_type, ship_class, cargo=500, weapon=100, passenger=1, owner=1, fleet=1)
ship_data = {
    "asteroid miner": ["Asteroid Miner", "AM-22X", 1000, 20, 10, "A specialized spacecraft equipped with mining equipment for extracting valuable resources from asteroids."],
    "asteroid prospector": ["Asteroid Prospector", "AP-5X", 500, 20, 5, "A specialized spacecraft equipped with mining and prospecting tools, used for locating and evaluating valuable resources within asteroids."],
    "battle station": ["Battle Station", "BS-20S", 0, 1000, 0, "A fortified space station equipped with formidable weaponry and defense systems, serving as a defensive stronghold or staging area for military operations."],
    "battlecruiser": ["Battlecruiser", "BC-94", 500, 300, 75, "A hybrid of a battleship and a cruiser, combining firepower with speed and maneuverability."],
    "battleship": ["Battleship", "B-99", 800, 400, 100, "A massive and heavily armed warship, typically the pinnacle of a fleet's offensive capabilities."],
    "boarding craft": ["Boarding Craft", "BC-3E", 0, 50, 20, "A small spacecraft designed for boarding enemy vessels during combat or infiltration missions."],
    "bomber": ["Bomber", "TB-14R", 100, 150, 0, "A heavy attack spacecraft primarily designed to deliver powerful payloads onto enemy targets."],
    "cargo carrier": ["Cargo Carrier", "CC-18S", 2500, 20, 0, "An enormous spacecraft designed for transporting vast quantities of cargo and freight, catering to large-scale logistical operations."],
    "cargo freighter": ["Cargo Freighter", "CF-22", 1500, 20, 10, "Specializing in transporting goods, merchandise, or resources with large storage holds."],
    "cargo hauler": ["Cargo Hauler", "CH-14S", 2000, 20, 0, "A massive spacecraft designed for transporting large quantities of cargo and freight over long distances."],
    "cargo transporter": ["Cargo Transporter", "CT-12S", 1500, 20, 0, "A large spacecraft dedicated to transporting bulk cargo and freight over long distances."],
    "carrier": ["Carrier", "CV-18", 600, 200, 200, "A large spacecraft designed to carry and launch smaller ships, providing air support during battles."],
    "colonial transport": ["Colonial Transport", "CT-22S", 1500, 20, 1000, "A massive spacecraft designed to transport colonists, supplies, and infrastructure to establish colonies on new planets."],
    "colossal carrier": ["Colossal Carrier", "CC-72G", 1500, 100, 500, "An immense carrier capable of carrying numerous smaller spacecraft, including fighters, bombers, and support vessels."],
    "colossal research station": ["Colossal Research Station", "CRS-20X", 0, 20, 1000, "A colossal space station dedicated to scientific research, equipped with advanced laboratories, observatories, and research facilities."],
    "communication satellite": ["Communication Satellite", "CSAT-1", 0, 20, 0, "A satellite designed to bring different ships and entities in a network spanning the galaxy together."],
    "construction ship": ["Construction Ship", "CS-15S", 1000, 20, 50, "A specialized spacecraft equipped with construction and assembly systems for building and repairing space structures and stations."],
    "corvette": ["Corvette", "C-23", 150, 75, 10, "A small, lightly armed and armored warship often used as a patrol vessel or escort."],
    "cruiser": ["Cruiser", "C-72", 400, 250, 50, "A large warship with substantial firepower and crew capacity, often serving as a command ship."],
    "deep space observatory": ["Deep Space Observatory", "DSO-6S", 0, 20, 100, "An orbital observatory stationed in deep space, equipped with powerful telescopes and sensors to study celestial phenomena and gather astronomical data."],
    "deep space probe": ["Deep Space Probe", "DSP-4A", 0, 20, 0, "An unmanned spacecraft designed for long-duration deep space exploration and data collection missions."],
    "deep space research vessel": ["Deep Space Research Vessel", "DSRV-8X", 400, 100, 50, "A specialized research ship designed for long-duration deep space exploration missions, equipped with state-of-the-art scientific instruments and analysis facilities."],
    "destroyer": ["Destroyer", "D-15X", 300, 200, 30, "A heavily armed and armored warship capable of engaging multiple targets simultaneously."],
    "dreadnought": ["Dreadnought", "DN-42", 1000, 500, 150, "The largest and most powerful warship in a fleet, symbolizing overwhelming military might."],
    "exoplanet colony ship": ["Exoplanet Colony Ship", "ECS-5X", 800, 20, 1000, "A massive vessel designed to transport colonists, supplies, and equipment to establish colonies on distant exoplanets."],
    "exploration cruiser": ["Exploration Cruiser", "EC-7C", 600, 200, 100, "A cruiser specifically designed for long-duration deep space exploration missions, equipped with advanced scientific instruments and research facilities."],
    "exploration drone": ["Exploration Drone", "ED-4A", 0, 20, 0, "An autonomous drone deployed for exploratory missions, equipped with sensors and cameras to collect data and images from uncharted territories."],
    "exploration vessel": ["Exploration Vessel", "EV-8M", 300, 50, 50, "A specialized spacecraft equipped for long-distance exploration and scientific research."],
    "explorer shuttle": ["Explorer Shuttle", "ES-3R", 50, 20, 10, "A small and agile spacecraft used for short-range exploration missions, capable of landing on planetary surfaces."],
    "fighter craft": ["Fighter Craft", "XF-7A", 0, 100, 1, "Compact and maneuverable spacecraft built for combat."],
    "frigate": ["Frigate", "F-81", 200, 100, 20, "A medium-sized warship designed for various roles, including escort duty and reconnaissance."],
    "hospital ship": ["Hospital Ship", "HS-3S", 300, 25, 100, "A medical facility in space equipped with state-of-the-art medical facilities and staff."],
    "ice hauler": ["Ice Hauler", "IH-5X", 1200, 20, 0, "A large cargo vessel specialized in transporting and delivering frozen water and ice resources to remote locations."],
    "interceptor cruiser": ["Interceptor Cruiser", "IC-12B", 300, 200, 50, "A cruiser optimized for rapid interception and engagement of enemy vessels, combining firepower and speed for offensive operations."],
    "interceptor": ["Interceptor", "VX-9B", 0, 75, 1, "A fast and nimble spacecraft designed to intercept and destroy enemy vessels."],
    "intergalactic cruiser": ["Intergalactic Cruiser", "IC-25X", 800, 400, 200, "A massive cruiser capable of intergalactic travel, equipped with advanced propulsion and extended-range systems for exploration and defense."],
    "interstellar cargo liner": ["Interstellar Cargo Liner", "ICL-16S", 2000, 20, 200, "A massive cargo vessel specializing in interstellar trade, capable of transporting a vast amount of goods across vast distances."],
    "interstellar cruise liner": ["Interstellar Cruise Liner", "ICL-18E", 1500, 20, 1000, "An extravagant and luxurious spacecraft designed for long-distance interstellar cruises, offering unparalleled comfort and luxury."],
    "interstellar liner": ["Interstellar Liner", "IL-16E", 1000, 20, 500, "A luxurious and spacious spacecraft designed for long-distance interstellar travel, providing comfort and entertainment for passengers."],
    "light freighter": ["Light Freighter", "LF-24B", 300, 150, 50, "A versatile and agile spacecraft designed for fast transportation of cargo, combining speed, maneuverability, and storage capacity."],
    "luxury cruise liner": ["Luxury Cruise Liner", "LCL-14E", 800, 20, 500, "An extravagant and opulent spacecraft designed for luxury cruises, offering lavish amenities and entertainment for passengers."],
    "luxury resort ship": ["Luxury Resort Ship", "LRS-14E", 1000, 20, 500, "A floating paradise in space, offering extravagant amenities, entertainment, and recreational activities for its passengers."],
    "luxury space casino": ["Luxury Space Casino", "LSC-12E", 1000, 20, 500, "A floating entertainment hub in space, offering a wide range of casino games, luxury accommodations, and live performances for its patrons."],
    "luxury yacht": ["Luxury Yacht", "LY-10E", 200, 20, 20, "An extravagant and high-end spacecraft designed for luxury travel and leisure activities in space."],
    "medical transport": ["Medical Transport", "MT-6S", 300, 20, 100, "A specialized spacecraft equipped with state-of-the-art medical facilities to transport patients and provide medical support during emergencies."],
    "mining barge": ["Mining Barge", "MB-8X", 800, 20, 10, "A large spacecraft equipped with advanced mining systems for extracting valuable resources from asteroids and planetary bodies."],
    "mining frigate": ["Mining Frigate", "MF-6B", 300, 20, 5, "A frigate equipped with specialized mining equipment for extracting valuable resources from asteroids and planetary bodies."],
    "mobile command center": ["Mobile Command Center", "MCC-7X", 0, 200, 50, "A self-contained command and control facility capable of coordinating operations and providing situational awareness in remote locations."],
    "mobile repair station": ["Mobile Repair Station", "MRS-7X", 0, 20, 200, "A specialized station equipped with advanced repair facilities, providing on-site repairs and maintenance services for spacecraft and stations."],
    "mobile research lab": ["Mobile Research Lab", "MRL-6X", 200, 25, 50, "A self-contained research facility capable of conducting experiments and analysis while on the move."],
    "orbital defense platform": ["Orbital Defense Platform", "ODP-12S", 0, 500, 0, "A stationary space-based platform armed with powerful weaponry and advanced defense systems, providing protection for strategic locations and assets."],
    "orbital defense satellite": ["Orbital Defense Satellite", "ODS-3S", 0, 500, 0, "A satellite armed with powerful weaponry and defensive systems, positioned in orbit to provide protection for critical assets and installations."],
    "orbital research platform": ["Orbital Research Platform", "ORP-5S", 0, 20, 100, "A space-based research facility positioned in orbit around a celestial body, conducting various scientific experiments and observations."],
    "passenger liner": ["Passenger Liner", "PL-9E", 500, 20, 200, "Luxurious spacecraft built for transporting passengers on long-distance journeys."],
    "planetary assault vessel": ["Planetary Assault Vessel", "PAV-11X", 500, 300, 200, "A heavily armed spacecraft designed for planetary invasion and assault missions, capable of deploying troops and vehicles."],
    "recon drone": ["Recon Drone", "RD-3A", 0, 20, 0, "An autonomous drone designed for reconnaissance missions, equipped with advanced sensors and surveillance technology."],
    "reconnaissance satellite": ["Reconnaissance Satellite", "RSAT-2", 0, 20, 0, "An orbital satellite equipped with advanced sensors and cameras for gathering intelligence and surveillance purposes."],
    "reconnaissance ship": ["Reconnaissance Ship", "RC-8A", 150, 75, 10, "A spacecraft optimized for gathering intelligence and conducting covert reconnaissance missions."],
    "refinery ship": ["Refinery Ship", "RF-9A", 500, 20, 10, "A mobile refinery platform capable of extracting and processing raw materials in space."],
    "refueling tanker": ["Refueling Tanker", "RT-12C", 1500, 20, 100, "A specialized spacecraft equipped with fuel storage and transfer systems, used for refueling other ships during long-distance missions."],
    "repair drone": ["Repair Drone", "RD-5A", 0, 25, 0, "An autonomous drone equipped with repair systems and tools, used for on-site repairs and maintenance of spacecraft and stations."],
    "rescue craft": ["Rescue Craft", "RC-4S", 50, 25, 20, "A spacecraft equipped with medical and search-and-rescue facilities to assist in emergency situations."],
    "research ship": ["Research Ship", "R-6X", 200, 25, 20, "Scientific spacecraft designed for exploration and conducting experiments."],
    "research station": ["Research Station", "RS-18X", 0, 20, 500, "A large space station dedicated to scientific research, equipped with laboratories, observation facilities, and living quarters for researchers."],
    "salvage vessel": ["Salvage Vessel", "SV-5R", 500, 20, 50, "A specialized spacecraft equipped with salvage and recovery systems to collect and salvage valuable materials from wrecked or derelict ships."],
    "scavenger ship": ["Scavenger Ship", "SV-8A", 300, 20, 25, "A spacecraft specialized in salvaging and scavenging valuable materials and components from space debris and wrecks."],
    "science laboratory ship": ["Science Laboratory Ship", "SLS-8X", 300, 50, 50, "A dedicated ship equipped with state-of-the-art scientific laboratories, conducting research and experiments in various scientific fields."],
    "science vessel": ["Science Vessel", "SV-12X", 200, 50, 30, "A dedicated scientific research spacecraft equipped with advanced laboratory and analysis facilities."],
    "scout ship": ["Scout Ship", "RS-12A", 50, 25, 2, "A small and agile spacecraft designed for reconnaissance and exploration missions."],
    "stealth assault ship": ["Stealth Assault Ship", "SAS-12B", 400, 400, 25, "A fast and agile assault ship designed with advanced stealth capabilities, specializing in covert infiltration and surprise attacks."],
    "stealth battleship": ["Stealth Battleship", "SB-18B", 1000, 800, 100, "A battleship designed with advanced stealth technology, combining immense firepower with covert operations capabilities."],
    "stealth bomber": ["Stealth Bomber", "SB-9R", 200, 200, 0, "A heavily armed bomber equipped with advanced stealth capabilities for surprise attacks on enemy targets."],
    "stealth cargo freighter": ["Stealth Cargo Freighter", "SCF-14C", 2000, 20, 50, "A cargo freighter designed with advanced stealth technology, used for covert transportation of goods, resources, or contraband."],
    "stealth cargo ship": ["Stealth Cargo Ship", "SCS-10C", 1500, 20, 20, "A cargo vessel designed with advanced stealth technology, used for covert transport of sensitive or valuable cargo."],
    "stealth command ship": ["Stealth Command Ship", "SCS-9X", 500, 300, 50, "A command ship designed with advanced stealth technology, serving as a mobile headquarters for covert operations and strategic command."],
    "stealth cruiser": ["Stealth Cruiser", "SC-12R", 400, 300, 50, "A cruiser designed with advanced stealth technology, capable of conducting covert operations and surprise attacks."],
    "stealth destroyer": ["Stealth Destroyer", "SD-14X", 500, 400, 40, "A destroyer equipped with advanced stealth technology, combining firepower and covert operations capabilities."],
    "stealth escort": ["Stealth Escort", "SE-9B", 100, 100, 10, "A small and agile spacecraft designed for covert escort missions, providing protection and support while maintaining a low profile."],
    "stealth frigate": ["Stealth Frigate", "SF-9B", 200, 150, 20, "A frigate designed with advanced stealth capabilities, combining agility and firepower for covert operations and hit-and-run tactics."],
    "stealth mining ship": ["Stealth Mining Ship", "SMS-9B", 1000, 20, 10, "A mining vessel equipped with advanced stealth technology for covert resource extraction operations."],
    "stealth research ship": ["Stealth Research Ship", "SRS-8A", 300, 50, 20, "A research vessel equipped with advanced stealth capabilities, used for covert scientific exploration and data gathering."],
    "stealth science vessel": ["Stealth Science Vessel", "SSV-9A", 300, 75, 30, "A dedicated scientific research spacecraft designed with advanced stealth capabilities, used for covert exploration and data gathering."],
    "stealth ship": ["Stealth Ship", "S-27R", 100, 75, 10, "A spacecraft designed with advanced stealth technology for covert operations and infiltration."],
    "stealth supply ship": ["Stealth Supply Ship", "SSS-12R", 800, 50, 50, "A supply ship designed with advanced stealth capabilities, used for covert resupply missions to support operations in hostile territories."],
    "stealth support ship": ["Stealth Support Ship", "SSS-10B", 500, 100, 50, "A support ship designed with advanced stealth capabilities, providing logistical support, repairs, and auxiliary services to other spacecraft."],
    "stealth transport": ["Stealth Transport", "ST-10C", 800, 50, 100, "A covert spacecraft designed for transporting personnel and equipment in secrecy, equipped with advanced stealth technology."],
    "steamer ship": ["Steamer Ship", "ST-7M", 200, 20, 50, "A spacecraft utilizing steam-powered technology, offering a unique blend of retro aesthetics and modern functionality."],
    "steampunk cruiser": ["Steampunk Cruiser", "SP-3R", 400, 200, 100, "A cruiser designed with steampunk-inspired aesthetics, combining retro-futuristic style with advanced technology."],
    "supply ship": ["Supply Ship", "SS-9C", 1000, 20, 50, "A large cargo vessel designed to transport supplies, provisions, and equipment to support remote outposts and space stations."],
    "survey ship": ["Survey Ship", "SS-6B", 150, 25, 15, "A spacecraft equipped with specialized sensors and equipment for surveying and mapping celestial bodies."],
    "terraforming vessel": ["Terraforming Vessel", "TV-10C", 500, 20, 100, "A specialized spacecraft equipped with advanced technologies for terraforming uninhabitable planets, transforming them into habitable environments."],
    "trading vessel": ["Trading Vessel", "TV-11C", 500, 25, 20, "A merchant ship designed for interstellar trade, equipped with trading facilities and storage space."],
    "transport ship": ["Transport Ship", "T-4C", 1000, 20, 50, "Designed to transport cargo, supplies, or personnel between different locations."]
}


weapon_data = {
	"Antimatter Beam": { "Weapon Class": "Energy", "Damage Per Minute": 200, "Hitpoints": 100, "Capacity Used": 10, "Range": "Long Range", "Regeneration Time": 2.5 },
	"Arc Lightning": { "Weapon Class": "Energy", "Damage Per Minute": 140, "Hitpoints": 100, "Capacity Used": 10, "Range": "Medium Range", "Regeneration Time": 1.5 },
	"Arc Rifle": { "Weapon Class": "Energy", "Damage Per Minute": 100, "Hitpoints": 150, "Capacity Used": 10, "Range": "100 meters", "Regeneration Time": 2 },
	"Blaster": { "Weapon Class": "Energy", "Damage Per Minute": 80, "Hitpoints": 150, "Capacity Used": 10, "Range": "80 meters", "Regeneration Time": 1.5 },
	"Cryo Blaster": { "Weapon Class": "Projectile", "Damage Per Minute": 150, "Hitpoints": 100, "Capacity Used": 10, "Range": "Medium Range", "Regeneration Time": 1.5 },
	"Disruptor": { "Weapon Class": "Energy", "Damage Per Minute": 130, "Hitpoints": 180, "Capacity Used": 10, "Range": "150 meters", "Regeneration Time": 2.5 },
	"Energy Sword": { "Weapon Class": "Melee", "Damage Per Minute": 80, "Hitpoints": 100, "Capacity Used": 10, "Range": "Melee Range", "Regeneration Time": -1 },
	"Fusion Blaster": { "Weapon Class": "Energy", "Damage Per Minute": 180, "Hitpoints": 100, "Capacity Used": 10, "Range": "Medium Range", "Regeneration Time": 2 },
	"Fusion Cannon": { "Weapon Class": "Energy", "Damage Per Minute": 200, "Hitpoints": 100, "Capacity Used": 10, "Range": "Medium Range", "Regeneration Time": 2 },
	"Gauss Rifle": { "Weapon Class": "Projectile", "Damage Per Minute": 160, "Hitpoints": 100, "Capacity Used": 10, "Range": "Long Range", "Regeneration Time": 2 },
	"Graviton Beam": { "Weapon Class": "Energy", "Damage Per Minute": 160, "Hitpoints": 100, "Capacity Used": 10, "Range": "Medium Range", "Regeneration Time": 2 },
	"Gravity Well Generator": { "Weapon Class": "Energy", "Damage Per Minute": 200, "Hitpoints": 100, "Capacity Used": 10, "Range": "Medium Range", "Regeneration Time": 2 },
	"Hyper Plasma Cannon": { "Weapon Class": "Energy", "Damage Per Minute": 240, "Hitpoints": 100, "Capacity Used": 10, "Range": "Long Range", "Regeneration Time": 3 },
	"Ion Blaster": { "Weapon Class": "Energy", "Damage Per Minute": 90, "Hitpoints": 120, "Capacity Used": 10, "Range": "100 meters", "Regeneration Time": 1.5 },
	"Ion Cannon": { "Weapon Class": "Energy", "Damage Per Minute": 160, "Hitpoints": 100, "Capacity Used": 10, "Range": "Medium Range", "Regeneration Time": 1.5 },
	"Ionic Pulse Cannon": { "Weapon Class": "Energy", "Damage Per Minute": 220, "Hitpoints": 100, "Capacity Used": 10, "Range": "Medium Range", "Regeneration Time": 2.5 },
	"Laser Cannon": { "Weapon Class": "Energy", "Damage Per Minute": 200, "Hitpoints": 300, "Capacity Used": 10, "Range": "300 meters", "Regeneration Time": 4 },
	"Nanite Swarm Launcher": { "Weapon Class": "Energy", "Damage Per Minute": 180, "Hitpoints": 100, "Capacity Used": 10, "Range": "Medium Range", "Regeneration Time": 2 },
	"Nanomatter Disintegrator": { "Weapon Class": "Energy", "Damage Per Minute": 200, "Hitpoints": 100, "Capacity Used": 10, "Range": "Long Range", "Regeneration Time": 2.5 },
	"Neural Disruptor": { "Weapon Class": "Energy", "Damage Per Minute": 160, "Hitpoints": 100, "Capacity Used": 10, "Range": "Medium Range", "Regeneration Time": 1.5 },
	"Neutron Blaster": { "Weapon Class": "Projectile", "Damage Per Minute": 180, "Hitpoints": 100, "Capacity Used": 10, "Range": "Medium Range", "Regeneration Time": 2 },
	"Nova Bomb": { "Weapon Class": "Projectile", "Damage Per Minute": 280, "Hitpoints": 100, "Capacity Used": 10, "Range": "Long Range", "Regeneration Time": 3.5 },
	"Nuclear Warhead Launcher": { "Weapon Class": "Projectile", "Damage Per Minute": 280, "Hitpoints": 100, "Capacity Used": 10, "Range": "Long Range", "Regeneration Time": 3.5 },
	"Particle Beam": { "Weapon Class": "Energy", "Damage Per Minute": 180, "Hitpoints": 250, "Capacity Used": 10, "Range": "200 meters", "Regeneration Time": 3 },
	"Particle Cannon": { "Weapon Class": "Energy", "Damage Per Minute": 200, "Hitpoints": 100, "Capacity Used": 10, "Range": "Long Range", "Regeneration Time": 2.5 },
	"Phantom Beam": { "Weapon Class": "Energy", "Damage Per Minute": 210, "Hitpoints": 100, "Capacity Used": 10, "Range": "Medium Range", "Regeneration Time": 2.5 },
	"Phase Disruptor": { "Weapon Class": "Energy", "Damage Per Minute": 200, "Hitpoints": 100, "Capacity Used": 10, "Range": "Long Range", "Regeneration Time": 2.5 },
	"Phaser": { "Weapon Class": "Energy", "Damage Per Minute": 100, "Hitpoints": 200, "Capacity Used": 10, "Range": "100 meters", "Regeneration Time": 2 },
	"Photon Torpedo": { "Weapon Class": "Projectile", "Damage Per Minute": 250, "Hitpoints": 350, "Capacity Used": 10, "Range": "1000 meters", "Regeneration Time": 6 },
	"Plasma Blaster": { "Weapon Class": "Energy", "Damage Per Minute": 180, "Hitpoints": 100, "Capacity Used": 10, "Range": "Medium Range", "Regeneration Time": 2 },
	"Plasma Disruptor": { "Weapon Class": "Energy", "Damage Per Minute": 180, "Hitpoints": 100, "Capacity Used": 10, "Range": "Medium Range", "Regeneration Time": 2 },
	"Plasma Gatling": { "Weapon Class": "Energy", "Damage Per Minute": 180, "Hitpoints": 250, "Capacity Used": 10, "Range": "200 meters", "Regeneration Time": 3 },
	"Plasma Launcher": { "Weapon Class": "Energy", "Damage Per Minute": 220, "Hitpoints": 300, "Capacity Used": 10, "Range": "250 meters", "Regeneration Time": 4 },
	"Plasma Pistol": { "Weapon Class": "Energy", "Damage Per Minute": 70, "Hitpoints": 100, "Capacity Used": 10, "Range": "80 meters", "Regeneration Time": 1 },
	"Plasma Rifle": { "Weapon Class": "Energy", "Damage Per Minute": 120, "Hitpoints": 180, "Capacity Used": 10, "Range": "150 meters", "Regeneration Time": 3 },
	"Plasma Torpedo": { "Weapon Class": "Energy", "Damage Per Minute": 180, "Hitpoints": 100, "Capacity Used": 10, "Range": "Long Range", "Regeneration Time": 2.5 },
	"Pulse Cannon": { "Weapon Class": "Energy", "Damage Per Minute": 200, "Hitpoints": 100, "Capacity Used": 10, "Range": "Medium Range", "Regeneration Time": 2 },
	"Pulse Rifle": { "Weapon Class": "Energy", "Damage Per Minute": 110, "Hitpoints": 160, "Capacity Used": 10, "Range": "120 meters", "Regeneration Time": 2 },
	"Quantum Disruptor": { "Weapon Class": "Energy", "Damage Per Minute": 180, "Hitpoints": 100, "Capacity Used": 10, "Range": "Long Range", "Regeneration Time": 2.5 },
	"Quantum Singularity Projector": { "Weapon Class": "Energy", "Damage Per Minute": 220, "Hitpoints": 100, "Capacity Used": 10, "Range": "Long Range", "Regeneration Time": 3 },
	"Radiation Beam": { "Weapon Class": "Energy", "Damage Per Minute": 180, "Hitpoints": 100, "Capacity Used": 10, "Range": "Medium Range", "Regeneration Time": 2 },
	"Railgun": { "Weapon Class": "Projectile", "Damage Per Minute": 150, "Hitpoints": 250, "Capacity Used": 10, "Range": "500 meters", "Regeneration Time": 5 },
	"Singularity Cannon": { "Weapon Class": "Energy", "Damage Per Minute": 250, "Hitpoints": 100, "Capacity Used": 10, "Range": "Long Range", "Regeneration Time": 3 },
	"Sonic Disruptor": { "Weapon Class": "Sound", "Damage Per Minute": 120, "Hitpoints": 100, "Capacity Used": 10, "Range": "Short Range", "Regeneration Time": 1 },
	"Temporal Rift Generator": { "Weapon Class": "Energy", "Damage Per Minute": 300, "Hitpoints": 100, "Capacity Used": 10, "Range": "Long Range", "Regeneration Time": 4 },
}


goods_data = {
    "minerals": { "cat": "Minerals", "name": "Unobtanium", "capacity used": 10, "baseprice": 1000 },
    "raw_materials": { "cat": "Raw Materials", "name": "Nanomaterials", "capacity used": 5, "baseprice": 2 },
    "gadgets": { "cat": "Gadgets", "name": "Reality Distortion Field Generator", "capacity used": 2, "baseprice": 500 },
    "arms": { "cat": "Arms", "name": "Phasers", "capacity used": 2, "baseprice": 100 },
    "food_supplies": { "cat": "Food Supplies", "name": "Rations Block", "capacity used": 5, "baseprice": 2 },
    "contraband": { "cat": "Contraband", "name": "Stardust", "capacity used": 10, "baseprice": 10000 },
    "medical_equipment": { "cat": "Medical Equipment", "name": "Medi-Scanner", "capacity used": 3, "baseprice": 500 },
    "luxury": { "cat": "Luxury", "name": "Exquisite Jewelry", "capacity used": 1, "baseprice": 2000 },
    "artifacts": { "cat": "Artifacts", "name": "Ancient Relics", "capacity used": 1, "baseprice": 5000 },
    "precious_metals": { "cat": "Precious Metals", "name": "Platinum Bars", "capacity used": 5, "baseprice": 500 },
    "energy_crystals": { "cat": "Energy Crystals", "name": "Luminite Crystals", "capacity used": 3, "baseprice": 1500 },
    "alien_relics": { "cat": "Alien Relics", "name": "Xenotech Artifacts", "capacity used": 2, "baseprice": 5000 },
    "spare_parts": { "cat": "Spare Parts", "name": "Fusion Reactor Cores", "capacity used": 2, "baseprice": 1000 },
    "sentient_ai_cores": { "cat": "Sentient AI Cores", "name": "Quantum Neural Processors", "capacity used": 1, "baseprice": 10000 },

    "holovid_disks": { "cat": "Entertainment", "name": "HoloVid Disks", "capacity used": 1, "baseprice": 50 },
    "gravity_boots": { "cat": "Technology", "name": "Gravity Boots", "capacity used": 2, "baseprice": 750 },
    "synthmorphs": { "cat": "Augmentation", "name": "Synthetic Morphs", "capacity used": 3, "baseprice": 3000 },
    "time_crystals": { "cat": "Exotic Matter", "name": "Time Crystals", "capacity used": 1, "baseprice": 5000 },
    "mind_control_implants": { "cat": "Augmentation", "name": "Mind Control Implants", "capacity used": 2, "baseprice": 15000 },
    "psionic_amplifiers": { "cat": "Enhancement", "name": "Psionic Amplifiers", "capacity used": 1, "baseprice": 1000 },
    "nanodrones": { "cat": "Technology", "name": "NanoDrones", "capacity used": 1, "baseprice": 2500 },
    "warp_engines": { "cat": "Propulsion", "name": "Warp Engines", "capacity used": 5, "baseprice": 50000 },
    "cosmic_art": { "cat": "Art", "name": "Cosmic Art", "capacity used": 2, "baseprice": 10000 },
    "quantumputers": { "cat": "Technology", "name": "Quantumputers", "capacity used": 3, "baseprice": 5000 },
}
	


# Event types; Note: Must coincide with EventSystem class list
eventlist = ["nothing", "pirate_attack" ,"alien_attack", "wormhole", "asteroid_shower"]

# events = ["nothing", "pirate_attack", "wormhole", "accident", "asteroid_shower", "angry_loansharks", "space_debris_collision", "engine_malfunction", "alien_encounter", "solar_flare", "cargo_theft", "engine_upgrade_opportunity", "distress_signal", "black_hole_encounter", "trading_opportunity", "navigation_failure", "space_station_malfunction", "planet_exploration", "sabotage_attempt", "mysterious_artifact"]

# Define a list of planets or regions in the known galactic sector
planets = ["Solstra", "Pulsarion", "Caelus Prime", "Draconis", "Lunaria", "Stellaria", "Galaxion"]

# Note: This is intended for future expansion
# Define a dictionary of distances between the planets or regions in the galaxy
# For example: distances["Solstra"]["Pulsarion"] = 100 means the distance between Solstra and Pulsarion is 100 units
# Note: Currently kind of brute-force; can later be refactored to a matrix format with mapped unit coordinates in 3-dimensions 
distances = {
    "Solstra": {"Pulsarion": 100, "Caelus Prime": 200, "Draconis": 300, "Lunaria": 400, "Stellaria": 500, "Galaxion": 600},
    "Pulsarion": {"Solstra": 100, "Caelus Prime": 100, "Draconis": 200, "Lunaria": 300, "Stellaria": 400, "Galaxion": 500},
    "Caelus Prime": {"Solstra": 200, "Pulsarion": 100, "Draconis": 100, "Lunaria": 200, "Stellaria": 300, "Galaxion": 400},
    "Draconis": {"Solstra": 300, "Pulsarion": 200, "Caelus Prime": 100, "Lunaria": 100, "Stellaria": 200, "Galaxion": 300},
    "Lunaria": {"Solstra": 400, "Pulsarion": 300, "Caelus Prime": 200, "Draconis": 100, "Stellaria": 100, "Galaxion": 200},
    "Stellaria": {"Solstra": 500, "Pulsarion": 400, "Caelus Prime": 300, "Draconis": 200, "Lunaria": 100, "Galaxion": 100},
    "Galaxion": {"Solstra": 600, "Pulsarion": 500, "Caelus Prime": 400, "Draconis": 300, "Lunaria": 200, "Stellaria": 100}
}


# names of ships
ship_names = [
    "Bellerophon", "Pegasus", "Widowmaker", "Salamander", "Caesar", "Betelgeuse", "Tomorrow", "Storm", "Coriolis", "Vindelix", "Felix Legion", "Phoenix Legion", "Maximus", "Fulcrum", "Ganymede", "Orion's Buckle", "Farside", "Starlight Express", "Serenity", "Falconia", "Excalibur", "Enterprise", "Defiant", "Galactica", "Nebula's Pride", "Thunderchild", "Valkyrie", "Tempest", "Phoenix", "Vipersword", "Nova's Hope", "Andromeda", "Eclipse", "Shadowrunner", "Dragonfly", "Hyperion", "Stargazer", "Black Pearl", "Astraxis", "Celestion", "Colossa", "Constellus", "Eclipseon", "Eradicon", "Eternus", "Galaxon", "Infinion", "Interstellus", "Leviathus", "Magnia", "Nebulon", "Novacon", "Quantus", "Scourgion", "Singulon", "Solarion", "Spectron", "Stellion", "Stormius", "Supernovacon", "Tempestion", "Thundron", "Titanus", "Vengion", "Vortexium", "Warbringer", "Astradon", "Celestium", "Constellion", "Clysmicon", "Apocalypton", "Armageddus", "Ragnarox", "Thunderion", "Hyperionus", "Catalysmus", "Singularon", "Gravitron", "Cosmon", "Galaxio", "Infinitum", "Void Beast", "Spectral Leviathan", "Quantum Destroyer", "Nebulan", "Nova Tyrant", "Asterion", "Prometheon", "Tartaron", "Typhonus", "Zodiacion", "Pegasion", "Andromedon", "Centaurion", "Velorum", "Carinon", "Puppion", "Lupion", "Vulpes", "Columbon", "Aquilion", "Cetus", "Perseion", "Aurigon", "Ophion", "Sagittarion", "Geminion", "Taurion", "Libron", "Virgon", "Leonis", "Hydron", "Corvion", "Herculeon", "Cygnion", "Lacerton", "Arach", "Triangulum", "Indion", "Pavon", "Grus", "Tucanon", "Horologion", "Torion", "Hadaron", "Procyon", "Canopion", "Altairon", "Aldebaron", "Antares", "Polaris", "Deneb", "Vega", "Altair", "Rigel", "Castor", "Pollux", "Orion's Fury", "Starfire", "Celestial Dawn", "Event Horizon", "Firefly", "Quantum Serpent", "Nebula Star", "Intrepid", "Astral", "Nightshade", "Solar Flare", "Zenith", "Nova's Glory", "Thunderhawk", "Infinity's Edge", "Horizon's Reach", "Nebula Runner", "Starwind", "Hypernova", "Seraphim", "Nova's Embrace", "Valkyrian Flux", "Nebula's Whisper", "Solaris", "Eclipse Raider", "Thunderstrike", "Celestial Wanderer", "Orion's Legacy", "Starblaze", "Spectre's Echo", "Stellar Phoenix", "Crimson Nova", "Quantum Dreamer", "Aurora's Grace", "Nebula Drifter", "Voidbreaker", "Starlancer", "Hyperion's Revenge", "Astral Eclipse", "Orion's Ascendancy", "Nighthawk", "Liberator", "Vanguard", "Peregrine", "Aether", "Mirage", "Galaxy's Crest", "Odyssey", "Avalanche", "Quicksilver", "Etherea", "Thunderclass", "Solaria", "Stardust", "Radiant Ember", "Phoenix Bright", "Luminary Ascendant", "Silvershade", "Nimbus", "Eternal Twilight", "Astrofire", "Stellarion", "Astral Voyager", "Aurora", "Crimson Star", "Solara", "Eclipse's Edge", "Moonshadow", "Lionheart", "Sablefire", "Nebula's Grace", "Voyager's Song", "Celestialis", "Seraph", "Silverwing", "Nebula's Call", "Midnight Serenade", "Novaflare", "Spectra", "Duskblade", "Starshaper", "Zephyr", "Starwind", "Elysian Serenade", "Thunderheart", "Stellaria", "Lunaria", "Marvus", "Jovia", "Saturnia", "Phobiana", "Deimosa", "Iona", "Europia", "Ganyria", "Callistia", "Titania", "Tritonia", "Enceladia", "Mimara", "Tethia", "Diona", "Rheana", "Charona", "Solara", "Astria", "Marvinus", "Saturnalia", "Uranusia", "Neptunia", "Lunaris Prime", "Tritonia Major", "Enceladia Prime", "Mimarina", "Tethoria", "Dionaria", "Rheanus", "Astralis", "Lunaris Minor", "Venaria", "Terranis", "Martis", "Saturnus", "Urania", "Neptunis", "Marsalia", "Deimoria", "Ionus", "Ionara", "Europion", "Ganymedea", "Callistea", "Titanara", "Tritonara", "Encelara", "Tethara", "Dionara", "Rheanis", "Venusia", "Marcellus", "Jovea", "Uranalia", "Neptunalia", "Lunarion", "Marsion", "Charonia",
]

enemy_ship_names = [
    "Stardust", "Nebulon", "Lunaris", "Galacticon", "Quasar", "Warpstrider", "Cosmosis", "Starstruck", "Cometstorm", "Thunderstrike", "Celestial Fury", "Serendipity", "Zenith", "Supernoval", "Polaris", "Moonshadow", "Orion's Bane", "Starmonger", "Warpshifter", "Titan's Wrath", "Lunarchaser", "Meteoric Mayhem", "Infinity's End", "Darklighter", "Starcutter", "Solstice", "Cosmic Crasher", "Blackstar", "Galaxus", "Stardancer", "Quasarion", "Nebula Vanguard", "Warpblade", "Celestialis", "Solar Sovereign", "Lunaris Rex", "Starwhisperer", "Astroshock", "Stellar Eclipse", "Lunaticus", "Cometbane", "Cosmic Laughter", "Meteorion", "Stellarbane", "Nebulon Fury", "Quasarshock", "Celestial Chaos", "Solarian", "Starcrusher", "Galactigor", "Lunarstrike", "Worldbeater", "Warpwalker", "Cosmosplitter", "Sunscorch", "Meteoric Mischief", "Quasarquake", "Nebulord", "Starling", "Lunarloon", "Astrophia", "Orbitalis", "Cometrix", "Lunarion", "Astralia", "Nebulor", "Stardragon", "Celeron", "Astrolynx", "Quasaris", "Aetherion", "Stellarion", "Starlance", "Nebulus", "Cosmostrider", "Galactis", "Lunaveil", "Stargazer", "Voidwalker", "Starstriker", "Cosmic Tempest", "Neutron Star", "Singularity", "Event Horizon", "Supernova", "Galaxy Binder", "Constellation", "Helios", "Terminus", "Infinity", "Oblivion", "Elysium", "Cosmos", "Aurora", "Andromeda", "Cassiopeia", "Cepheus", "Perseus", "Hercules", "Orpheus", "Pegasus", "Odysseus", "Icarus", "Atlas", "Apollo", "Artemis", "Athena", "Ares", "Zeus", "Poseidon", "Hades", "Aether", "Erebus", "Elysium", "Tartarus", "Styx", "Charon", "Matterlock", "Glumpis", "Malagant",
]