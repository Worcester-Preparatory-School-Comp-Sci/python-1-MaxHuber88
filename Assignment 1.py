def population():
	years = int(input("Years: ")) # user input in years
	seconds = years*365*24*60*60 # convert years to seconds
	pop = 307357870 + (seconds/7) + (seconds/35) - (seconds/13) # calculate population from seconds
	print(int(pop))
	
def oilFacts():
	gal = float(input("Gallons: ")) # user input in gallons
	liters = 3.785*gal # convert gallons to liters
	barrels = gal/19.5 # convert gallons to barrels of oil
	carbonPounds = gal*20 # convert gallons to pounds of carbon dioxide produced
	price = round(gal*3.35,2) # convert gallons to the price in dollars
	print("Liters: ",liters)
	print("Barrels of Oil: ",barrels)
	print("Pounds of Carbon Dioxide: ",carbonPounds)
	print("Price: $",price)
	
def deepWater():
	WATER_VOLUME = 22810 # cubic km
	CONT_US_AREA = 8080464.3 # sq km
	depth = (WATER_VOLUME/CONT_US_AREA)*1000 # calculate depth in meters
	print(depth," meters deep")
	
	#call all functions
	population()
	oilFacts()
	deepWater()
