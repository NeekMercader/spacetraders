class Goods:
	def __init__(self, cat, name, capacity_used, baseprice):
		self.cat = cat				# category (deprecated: self.sku = sku)
		self.name = name
		self.capacity_used = capacity_used	# capacity amount used by this unit
		self.baseprice = baseprice	# suggested retail (standard)
		
	def __repr__(self):
		return str(dir(self))
	
goods_list = {}		# info about goods to trade

# goods_list["Category"] = Goods("Category", "Name", capacity_used, baseprice)

goods_list["minerals"] = Goods("Minerals", "Unobtanium", 10, 1000)
goods_list["raw_materials"] = Goods("Raw Materials", "Nanomaterials", 5, 2)
goods_list["gadgets"] = Goods("Gadgets", "Reality Distortion Field Generator", 2, 500)
goods_list["arms"] = Goods("Arms", "Phasers", 2, 100)
goods_list["food_supplies"] = Goods("Food Supplies", "Rations Block", 5, 2)

'''
goods_list["medical_equipment"] = Goods("Category", "Name", capacity_used, baseprice)
goods_list["luxury"] = Goods("Category", "Name", capacity_used, baseprice)
goods_list["artifacts"] = Goods("Category", "Name", capacity_used, baseprice)
goods_list["precious_metals"] = Goods("Category", "Name", capacity_used, baseprice)
goods_list["energy_crystals"] = Goods("Category", "Name", capacity_used, baseprice)
goods_list["alien_relics"] = Goods("Category", "Name", capacity_used, baseprice)
goods_list["spare_parts"] = Goods("Category", "Name", capacity_used, baseprice)
goods_list["sentient_ai_cores"] = Goods("Category", "Name", capacity_used, baseprice)
goods_list["Category"] = Goods("Category", "Name", capacity_used, baseprice)
goods_list["Category"] = Goods("Category", "Name", capacity_used, baseprice)

'''
