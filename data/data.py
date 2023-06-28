class Goods:
	def __init__(self, cat, name, capacity_used, baseprice):
		self.cat = cat				# category (deprecated: self.sku = sku)
		self.name = name
		self.capacity_used = capacity_used	# capacity amount used by this unit
		self.baseprice = baseprice	# suggested retail (standard)
		
	def __repr__(self):
		return str(dir(self))


class Weapon:
    
	def __init__(self, weapon_dict):	# e.g. { "Railgun": { "Weapon Class": "Projectile", "Damage Per Minute": 150, "Hitpoints": 250, "Capacity Used": 10, "Range": "500 meters", "Regeneration Time": 5 } }
		self.weapon_name = (*weapon_dict,)		
		self.in_working_condition = True 		# working? destroyed?
		self.capacity_used = weapon_dict["Capacity Used"]
		self.damage_per_minute = weapon_dict["Damage Per Minute"]
		self.hitpoints = weapon_dict["Hitpoints"]
		print("WEAPON class CHECK:\n",\
			"self.weapon_name =", self.weapon_name,\
			"self.capacity_used =", self.capacity_used, \
			"self.damage_per_minute =", self.damage_per_minute, \
			"self.hitpoints", self.hitpoints, \
			"\n\n")
		return
        

# (name, ship_type, ship_class, cargo=500, weapon=100, passenger=1, owner=1, fleet=1)
ship_data = {
    "asteroid miner": ["Asteroid Miner", "AM-22X", 1000, 0, 10, "A specialized spacecraft equipped with mining equipment for extracting valuable resources from asteroids."],
    "asteroid prospector": ["Asteroid Prospector", "AP-5X", 500, 0, 5, "A specialized spacecraft equipped with mining and prospecting tools, used for locating and evaluating valuable resources within asteroids."],
    "battle station": ["Battle Station", "BS-20S", 0, 1000, 0, "A fortified space station equipped with formidable weaponry and defense systems, serving as a defensive stronghold or staging area for military operations."],
    "battlecruiser": ["Battlecruiser", "BC-94", 500, 300, 75, "A hybrid of a battleship and a cruiser, combining firepower with speed and maneuverability."],
    "battleship": ["Battleship", "B-99", 800, 400, 100, "A massive and heavily armed warship, typically the pinnacle of a fleet's offensive capabilities."],
    "boarding craft": ["Boarding Craft", "BC-3E", 0, 50, 20, "A small spacecraft designed for boarding enemy vessels during combat or infiltration missions."],
    "bomber": ["Bomber", "TB-14R", 100, 150, 0, "A heavy attack spacecraft primarily designed to deliver powerful payloads onto enemy targets."],
    "cargo carrier": ["Cargo Carrier", "CC-18S", 2500, 0, 0, "An enormous spacecraft designed for transporting vast quantities of cargo and freight, catering to large-scale logistical operations."],
    "cargo freighter": ["Cargo Freighter", "CF-22", 1500, 0, 10, "Specializing in transporting goods, merchandise, or resources with large storage holds."],
    "cargo hauler": ["Cargo Hauler", "CH-14S", 2000, 0, 0, "A massive spacecraft designed for transporting large quantities of cargo and freight over long distances."],
    "cargo transporter": ["Cargo Transporter", "CT-12S", 1500, 0, 0, "A large spacecraft dedicated to transporting bulk cargo and freight over long distances."],
    "carrier": ["Carrier", "CV-18", 600, 200, 200, "A large spacecraft designed to carry and launch smaller ships, providing air support during battles."],
    "colonial transport": ["Colonial Transport", "CT-22S", 1500, 0, 1000, "A massive spacecraft designed to transport colonists, supplies, and infrastructure to establish colonies on new planets."],
    "colossal carrier": ["Colossal Carrier", "CC-72G", 1500, 100, 500, "An immense carrier capable of carrying numerous smaller spacecraft, including fighters, bombers, and support vessels."],
    "colossal research station": ["Colossal Research Station", "CRS-20X", 0, 0, 1000, "A colossal space station dedicated to scientific research, equipped with advanced laboratories, observatories, and research facilities."],
    "communication satellite": ["Communication Satellite", "CSAT-1", 0, 0, 0, "A satellite designed to bring different ships and entities in a network spanning the galaxy together."],
    "construction ship": ["Construction Ship", "CS-15S", 1000, 0, 50, "A specialized spacecraft equipped with construction and assembly systems for building and repairing space structures and stations."],
    "corvette": ["Corvette", "C-23", 150, 75, 10, "A small, lightly armed and armored warship often used as a patrol vessel or escort."],
    "cruiser": ["Cruiser", "C-72", 400, 250, 50, "A large warship with substantial firepower and crew capacity, often serving as a command ship."],
    "deep space observatory": ["Deep Space Observatory", "DSO-6S", 0, 0, 100, "An orbital observatory stationed in deep space, equipped with powerful telescopes and sensors to study celestial phenomena and gather astronomical data."],
    "deep space probe": ["Deep Space Probe", "DSP-4A", 0, 0, 0, "An unmanned spacecraft designed for long-duration deep space exploration and data collection missions."],
    "deep space research vessel": ["Deep Space Research Vessel", "DSRV-8X", 400, 100, 50, "A specialized research ship designed for long-duration deep space exploration missions, equipped with state-of-the-art scientific instruments and analysis facilities."],
    "destroyer": ["Destroyer", "D-15X", 300, 200, 30, "A heavily armed and armored warship capable of engaging multiple targets simultaneously."],
    "dreadnought": ["Dreadnought", "DN-42", 1000, 500, 150, "The largest and most powerful warship in a fleet, symbolizing overwhelming military might."],
    "exoplanet colony ship": ["Exoplanet Colony Ship", "ECS-5X", 800, 0, 1000, "A massive vessel designed to transport colonists, supplies, and equipment to establish colonies on distant exoplanets."],
    "exploration cruiser": ["Exploration Cruiser", "EC-7C", 600, 200, 100, "A cruiser specifically designed for long-duration deep space exploration missions, equipped with advanced scientific instruments and research facilities."],
    "exploration drone": ["Exploration Drone", "ED-4A", 0, 10, 0, "An autonomous drone deployed for exploratory missions, equipped with sensors and cameras to collect data and images from uncharted territories."],
    "exploration vessel": ["Exploration Vessel", "EV-8M", 300, 50, 50, "A specialized spacecraft equipped for long-distance exploration and scientific research."],
    "explorer shuttle": ["Explorer Shuttle", "ES-3R", 50, 0, 10, "A small and agile spacecraft used for short-range exploration missions, capable of landing on planetary surfaces."],
    "fighter craft": ["Fighter Craft", "XF-7A", 0, 100, 1, "Compact and maneuverable spacecraft built for combat."],
    "frigate": ["Frigate", "F-81", 200, 100, 20, "A medium-sized warship designed for various roles, including escort duty and reconnaissance."],
    "hospital ship": ["Hospital Ship", "HS-3S", 300, 25, 100, "A medical facility in space equipped with state-of-the-art medical facilities and staff."],
    "ice hauler": ["Ice Hauler", "IH-5X", 1200, 0, 0, "A large cargo vessel specialized in transporting and delivering frozen water and ice resources to remote locations."],
    "interceptor cruiser": ["Interceptor Cruiser", "IC-12B", 300, 200, 50, "A cruiser optimized for rapid interception and engagement of enemy vessels, combining firepower and speed for offensive operations."],
    "interceptor": ["Interceptor", "VX-9B", 0, 75, 1, "A fast and nimble spacecraft designed to intercept and destroy enemy vessels."],
    "intergalactic cruiser": ["Intergalactic Cruiser", "IC-25X", 800, 400, 200, "A massive cruiser capable of intergalactic travel, equipped with advanced propulsion and extended-range systems for exploration and defense."],
    "interstellar cargo liner": ["Interstellar Cargo Liner", "ICL-16S", 2000, 0, 200, "A massive cargo vessel specializing in interstellar trade, capable of transporting a vast amount of goods across vast distances."],
    "interstellar cruise liner": ["Interstellar Cruise Liner", "ICL-18E", 1500, 0, 1000, "An extravagant and luxurious spacecraft designed for long-distance interstellar cruises, offering unparalleled confort and luxury."],
    "interstellar liner": ["Interstellar Liner", "IL-16E", 1000, 0, 500, "A luxurious and spacious spacecraft designed for long-distance interstellar travel, providing comfort and entertainment for passengers."],
    "light freighter": ["Light Freighter", "LF-24B", 300, 150, 50, "A versatile and agile spacecraft designed for fast transportation of cargo, combining speed, maneuverability, and storage capacity."],
    "luxury cruise liner": ["Luxury Cruise Liner", "LCL-14E", 800, 0, 500, "An extravagant and opulent spacecraft designed for luxury cruises, offering lavish amenities and entertainment for passengers."],
    "luxury resort ship": ["Luxury Resort Ship", "LRS-14E", 1000, 0, 500, "A floating paradise in space, offering extravagant amenities, entertainment, and recreational activities for its passengers."],
    "luxury space casino": ["Luxury Space Casino", "LSC-12E", 1000, 0, 500, "A floating entertainment hub in space, offering a wide range of casino games, luxury accommodations, and live performances for its patrons."],
    "luxury yacht": ["Luxury Yacht", "LY-10E", 200, 0, 20, "An extravagant and high-end spacecraft designed for luxury travel and leisure activities in space."],
    "medical transport": ["Medical Transport", "MT-6S", 300, 0, 100, "A specialized spacecraft equipped with state-of-the-art medical facilities to transport patients and provide medical support during emergencies."],
    "mining barge": ["Mining Barge", "MB-8X", 800, 0, 10, "A large spacecraft equipped with advanced mining systems for extracting valuable resources from asteroids and planetary bodies."],
    "mining frigate": ["Mining Frigate", "MF-6B", 300, 0, 5, "A frigate equipped with specialized mining equipment for extracting valuable resources from asteroids and planetary bodies."],
    "mobile command center": ["Mobile Command Center", "MCC-7X", 0, 200, 50, "A self-contained command and control facility capable of coordinating operations and providing situational awareness in remote locations."],
    "mobile repair station": ["Mobile Repair Station", "MRS-7X", 0, 0, 200, "A specialized station equipped with advanced repair facilities, providing on-site repairs and maintenance services for spacecraft and stations."],
    "mobile research lab": ["Mobile Research Lab", "MRL-6X", 200, 25, 50, "A self-contained research facility capable of conducting experiments and analysis while on the move."],
    "orbital defense platform": ["Orbital Defense Platform", "ODP-12S", 0, 500, 0, "A stationary space-based platform armed with powerful weaponry and advanced defense systems, providing protection for strategic locations and assets."],
    "orbital defense satellite": ["Orbital Defense Satellite", "ODS-3S", 0, 500, 0, "A satellite armed with powerful weaponry and defensive systems, positioned in orbit to provide protection for critical assets and installations."],
    "orbital research platform": ["Orbital Research Platform", "ORP-5S", 0, 0, 100, "A space-based research facility positioned in orbit around a celestial body, conducting various scientific experiments and observations."],
    "passenger liner": ["Passenger Liner", "PL-9E", 500, 0, 200, "Luxurious spacecraft built for transporting passengers on long-distance journeys."],
    "planetary assault vessel": ["Planetary Assault Vessel", "PAV-11X", 500, 300, 200, "A heavily armed spacecraft designed for planetary invasion and assault missions, capable of deploying troops and vehicles."],
    "recon drone": ["Recon Drone", "RD-3A", 0, 10, 0, "An autonomous drone designed for reconnaissance missions, equipped with advanced sensors and surveillance technology."],
    "reconnaissance satellite": ["Reconnaissance Satellite", "RSAT-2", 0, 0, 0, "An orbital satellite equipped with advanced sensors and cameras for gathering intelligence and surveillance purposes."],
    "reconnaissance ship": ["Reconnaissance Ship", "RC-8A", 150, 75, 10, "A spacecraft optimized for gathering intelligence and conducting covert reconnaissance missions."],
    "refinery ship": ["Refinery Ship", "RF-9A", 500, 0, 10, "A mobile refinery platform capable of extracting and processing raw materials in space."],
    "refueling tanker": ["Refueling Tanker", "RT-12C", 1500, 0, 100, "A specialized spacecraft equipped with fuel storage and transfer systems, used for refueling other ships during long-distance missions."],
    "repair drone": ["Repair Drone", "RD-5A", 0, 25, 0, "An autonomous drone equipped with repair systems and tools, used for on-site repairs and maintenance of spacecraft and stations."],
    "rescue craft": ["Rescue Craft", "RC-4S", 50, 25, 20, "A spacecraft equipped with medical and search-and-rescue facilities to assist in emergency situations."],
    "research ship": ["Research Ship", "R-6X", 200, 25, 20, "Scientific spacecraft designed for exploration and conducting experiments."],
    "research station": ["Research Station", "RS-18X", 0, 0, 500, "A large space station dedicated to scientific research, equipped with laboratories, observation facilities, and living quarters for researchers."],
    "salvage vessel": ["Salvage Vessel", "SV-5R", 500, 0, 50, "A specialized spacecraft equipped with salvage and recovery systems to collect and salvage valuable materials from wrecked or derelict ships."],
    "scavenger ship": ["Scavenger Ship", "SV-8A", 300, 0, 25, "A spacecraft specialized in salvaging and scavenging valuable materials and components from space debris and wreckages."],
    "science laboratory ship": ["Science Laboratory Ship", "SLS-8X", 300, 50, 50, "A dedicated ship equipped with state-of-the-art scientific laboratories, conducting research and experiments in various scientific fields."],
    "science vessel": ["Science Vessel", "SV-12X", 200, 50, 30, "A dedicated scientific research spacecraft equipped with advanced laboratory and analysis facilities."],
    "scout ship": ["Scout Ship", "RS-12A", 50, 25, 2, "A small and agile spacecraft designed for reconnaissance and exploration missions."],
    "stealth assault ship": ["Stealth Assault Ship", "SAS-12B", 400, 400, 25, "A fast and agile assault ship designed with advanced stealth capabilities, specializing in covert infiltration and surprise attacks."],
    "stealth battleship": ["Stealth Battleship", "SB-18B", 1000, 800, 100, "A battleship designed with advanced stealth technology, combining immense firepower with covert operations capabilities."],
    "stealth bomber": ["Stealth Bomber", "SB-9R", 200, 200, 0, "A heavily armed bomber equipped with advanced stealth capabilities for surprise attacks on enemy targets."],
    "stealth cargo freighter": ["Stealth Cargo Freighter", "SCF-14C", 2000, 0, 50, "A cargo freighter designed with advanced stealth technology, used for covert transportation of goods, resources, or contraband."],
    "stealth cargo ship": ["Stealth Cargo Ship", "SCS-10C", 1500, 0, 20, "A cargo vessel designed with advanced stealth technology, used for covert transport of sensitive or valuable cargo."],
    "stealth command ship": ["Stealth Command Ship", "SCS-9X", 500, 300, 50, "A command ship designed with advanced stealth technology, serving as a mobile headquarters for covert operations and strategic command."],
    "stealth cruiser": ["Stealth Cruiser", "SC-12R", 400, 300, 50, "A cruiser designed with advanced stealth technology, capable of conducting covert operations and surprise attacks."],
    "stealth destroyer": ["Stealth Destroyer", "SD-14X", 500, 400, 40, "A destroyer equipped with advanced stealth technology, combining firepower and covert operations capabilities."],
    "stealth escort": ["Stealth Escort", "SE-9B", 100, 100, 10, "A small and agile spacecraft designed for covert escort missions, providing protection and support while maintaining a low profile."],
    "stealth frigate": ["Stealth Frigate", "SF-9B", 200, 150, 20, "A frigate designed with advanced stealth capabilities, combining agility and firepower for covert operations and hit-and-run tactics."],
    "stealth mining ship": ["Stealth Mining Ship", "SMS-9B", 1000, 0, 10, "A mining vessel equipped with advanced stealth technology for covert resource extraction operations."],
    "stealth research ship": ["Stealth Research Ship", "SRS-8A", 300, 50, 20, "A research vessel equipped with advanced stealth capabilities, used for covert scientific exploration and data gathering."],
    "stealth science vessel": ["Stealth Science Vessel", "SSV-9A", 300, 75, 30, "A dedicated scientific research spacecraft designed with advanced stealth capabilities, used for covert exploration and data gathering."],
    "stealth ship": ["Stealth Ship", "S-27R", 100, 75, 10, "A spacecraft designed with advanced stealth technology for covert operations and infiltration."],
    "stealth supply ship": ["Stealth Supply Ship", "SSS-12R", 800, 50, 50, "A supply ship designed with advanced stealth capabilities, used for covert resupply missions to support operations in hostile territories."],
    "stealth support ship": ["Stealth Support Ship", "SSS-10B", 500, 100, 50, "A support ship designed with advanced stealth capabilities, providing logistical support, repairs, and auxiliary services to other spacecraft."],
    "stealth transport": ["Stealth Transport", "ST-10C", 800, 50, 100, "A covert spacecraft designed for transporting personnel and equipment in secrecy, equipped with advanced stealth technology."],
    "steamer ship": ["Steamer Ship", "ST-7M", 200, 0, 50, "A spacecraft utilizing steam-powered technology, offering a unique blend of retro aesthetics and modern functionality."],
    "steampunk cruiser": ["Steampunk Cruiser", "SP-3R", 400, 200, 100, "A cruiser designed with steampunk-inspired aesthetics, combining retro-futuristic style with advanced technology."],
    "supply ship": ["Supply Ship", "SS-9C", 1000, 0, 50, "A large cargo vessel designed to transport supplies, provisions, and equipment to support remote outposts and space stations."],
    "survey ship": ["Survey Ship", "SS-6B", 150, 25, 15, "A spacecraft equipped with specialized sensors and equipment for surveying and mapping celestial bodies."],
    "terraforming vessel": ["Terraforming Vessel", "TV-10C", 500, 0, 100, "A specialized spacecraft equipped with advanced technologies for terraforming uninhabitable planets, transforming them into habitable environments."],
    "trading vessel": ["Trading Vessel", "TV-11C", 500, 25, 20, "A merchant ship designed for interstellar trade, equipped with trading facilities and storage space."],
    "transport ship": ["Transport Ship", "T-4C", 1000, 0, 50, "Designed to transport cargo, supplies, or personnel between different locations."],
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




	
goods_data = {}		# test info about goods to trade
# goods_data["Category"] = Goods("Category", "Name", capacity_used, baseprice)
goods_data["minerals"] = Goods("Minerals", "Unobtanium", 10, 1000)
goods_data["raw_materials"] = Goods("Raw Materials", "Nanomaterials", 5, 2)
goods_data["gadgets"] = Goods("Gadgets", "Reality Distortion Field Generator", 2, 500)
goods_data["arms"] = Goods("Arms", "Phasers", 2, 100)
goods_data["food_supplies"] = Goods("Food Supplies", "Rations Block", 5, 2)
'''
goods_data["medical_equipment"] = Goods("Category", "Name", capacity_used, baseprice)
goods_data["luxury"] = Goods("Category", "Name", capacity_used, baseprice)
goods_data["artifacts"] = Goods("Category", "Name", capacity_used, baseprice)
goods_data["precious_metals"] = Goods("Category", "Name", capacity_used, baseprice)
goods_data["energy_crystals"] = Goods("Category", "Name", capacity_used, baseprice)
goods_data["alien_relics"] = Goods("Category", "Name", capacity_used, baseprice)
goods_data["spare_parts"] = Goods("Category", "Name", capacity_used, baseprice)
goods_data["sentient_ai_cores"] = Goods("Category", "Name", capacity_used, baseprice)
goods_data["Category"] = Goods("Category", "Name", capacity_used, baseprice)
goods_data["Category"] = Goods("Category", "Name", capacity_used, baseprice)
'''


weapons_list = {}      # test weapons loaded
weapons_list["Pulse Cannon"] = Weapon(weapon_data["Pulse Cannon"])
weapons_list["Plasma Blaster"] = Weapon(weapon_data["Plasma Blaster"])
weapons_list["Railgun"] = Weapon(weapon_data["Railgun"])



events_space_travel = ["nothing", "pirate_attack" ,"alien_attack", "wormhole", "asteroid_shower"]

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
