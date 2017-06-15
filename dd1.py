#	This program is designed to contain all the information

#	of any DnD Character. You can input all your data right

#	from a sheet, save it for later, reload it, change stats,

#	add items, equip gear, roll dice; You name it, this can do it.



#	TODO:

#		Add saveChara() and loadChara() functions



# Dates about this program

begun = "2/4/17"

updated = "2/5/17"

version = 0.3



#Empty Dictionaries for items, skills and abilities

inventory = {}

skills = {}

abilities = {}



#Base values for character stats

stats = {"STR": 0, \

	"bonusSTR": 0, \



	"DEX": 0, \

	"bonusDEX": 0, \



	"CON": 0, \

	"bonusCON": 0, \



	"INT": 0, \

	"bonusINT": 0, \



	"WIS": 0, \

	"bonusWIS": 0, \



	"CHA": 0, \

	"bonusCHA": 0, \



	"fortitude": 0, \

	"reflex": 0, \

	"will": 0, \



	"HPCurrent": 0, \

	"HPMax": 0, \

	"encumberance": 0, \



	"XPCurrent": 0, \

	"XPMax": 0, \

	"level": 0, \



	"money": 0 \

}



#Base character information

info = {"name": "", \

	"class": "", \

	"deity": "", \

	"race": "", \

	"gender": "", \

	"colorEyes": "", \

	"colorHair": "", \

	"currency": "" \

}



#Allows the user to enter new character information

def newInfo():

	info["name"] = str(input("Enter your name: "))

	info["class"] = str(input("Enter your class: "))

	info["deity"] = str(input("Enter your deity: "))



	info["race"] = str(input("Enter your race: "))

	info["gender"] = str(input("Enter your gender: "))



	info["colorEyes"] = str(input("Enter your eye color: "))

	info["colorHair"] = str(input("Enter your hair color: "))



	info["currency"] = str(input("Enter your currency: "))



#Allows the user to change character information

def changeInfo(infoName, infoNew):

	info[infoName] = infoNew



#Allows the user to enter new character stats

def newStats():

	stats["STR"] = int(input("Enter your Strength skill: "))

	stats["bonusSTR"] = int(input("Enter your Strength Bonus: "))



	stats["DEX"] = int(input("Enter your Dexterity skill: "))

	stats["bonusDEX"] = int(input("Enter your Dexterity Bonus: "))



	stats["CON"] = int(input("Enter your Constitution skill: "))

	stats["bonusCON"] = int(input("Enter your Constitution Bonus: "))



	stats["INT"] = int(input("Enter your Intelligence skill: "))

	stats["bonusINT"] = int(input("Enter your Intelligence Bonus: "))



	stats["WIS"] = int(input("Enter your Wisdom skill: "))

	stats["bonusWIS"] = int(input("Enter your Wisdom Bonus: "))



	stats["CHA"] = int(input("Enter your Charisma skill: "))

	stats["bonusCHA"] = int(input("Enter your Charisma Bonus: "))



	stats["fortitude"] = int(stats["CON"] + stats["bonusCON"])

	stats["reflex"] = int(stats["DEX"] + stats["bonusDEX"])

	stats["will"] = int(stats["WIS"] + stats["bonusWIS"])



	stats["HPCurrent"] = int(input("Enter your current HP: "))

	stats["HPMax"] = int(input("Enter your maximum HP: "))



	stats["XPCurrent"] = int(input("Enter your current XP: "))

	stats["level"] = int(input("Enter your level: "))

	stats["XPMax"] = int(100 + (10 * stats["level"]))

	print("Your XP needed for level up is " + str(stats["XPMax"]))



	stats["money"] = int(input("Enter your money: "))



#Changes the stat's value

def changeStat(statName, statNew):

	stats[statName] = int(statNew)



#Changes the stat's bonus value

def changeStatBonus(statName, bonusNew):

	stats["bonus" + statName] = int(bonusNew)



#Automatically updates saving throw stats

def updateSavingThrows():

	stats["fortitude"] = int(stats["CON"] + stats["bonusCON"])

	stats["reflex"] = int(stats["DEX"] + stats["bonusDEX"])

	stats["will"] = int(stats["WIS"] + stats["bonusWIS"])



#Changes the user's HP

def changeHP(HPNew):

	stats["HPCurrent"] = int(HPNew)



#Changes the user's maximum HP

def changeMaxHP(HPMaxNew):

	stats["HPMax"] = int(HPMaxNew)



#Levels up the player

def levelUp(XPRemainder):

	stats["XPCurrent"] = int(XPRemainder)

	stats["level"] += 1

	stats["XPMax"] = int(100 + (10 * stats["level"]))



#Adds to the user's XP

def addXP(XP):

	stats["XPCurrent"] += int(XP)



	if stats["XPCurrent"] >= stats["XPMax"]:

		levelUp(stats["XPMax"] - stats["XPCurrent"])



#Adds money to the user

def addMoney(money):

	stats["money"] += int(money)



#Updates the user's encumberance

def updateEncumberance():

	encumberanceNew = 0



	for item in inventory:

		encumberanceNew += inventory[item]["weight"] * inventory[item]["count"]



	stats["encumberance"] = encumberanceNew



#Adds a new item to the user's inventory

def newItem():

	name = str(input("Enter the item's name: "))

	bonuses = str(input("Does the item have any bonus(es)? [Y/N]: ")).upper()

	if bonuses == 'Y':

		bonuses = str(input("Enter the item's bonus(es) in plain text: "))

	else:

		bonuses = ""

	count = int(input("Enter how many units of the item you have: "))

	weight = float(input("Enter the weight of the item: "))

	

	diceType = str(input("Is the item a weapon? [Y/N]: ")).upper()

	if diceType == 'Y':

		print("(example: for a d4, input \"4\".)")

		diceType = int(input("Enter the type of dice the weapon uses: "))

		diceCount = int(input("Enter how many dice rolls the weapon uses: "))

		

		charges = str(input("Is the weapon charged? [Y/N]: ")).upper()

		if charges == 'Y':

			charges = int(input("Enter how many charges the weapon has: "))

			maxCharges = int(input("Enter how many charges the weapon can have: "))

		else:

			charges = 0

			maxCharges = 0



	else:

		diceType = 0

		diceCount = 0

		charges = 0

		maxCharges = 0



	equipped = str(input("Is this item equipped? [Y/N]: ")).upper()

	if equipped == 'Y':

		equipped = True

	else:

		equipped = False



	inventory[name] = {"name": name, \

		"bonuses": bonuses, \

		"count": count, \

		"weight": weight, \

		"diceType": diceType, \

		"diceCount": diceCount, \

		"charges": charges, \

		"maxCharges": maxCharges, \

		"equipped": equipped \

	}

	updateEncumberance()



#Remove an item from the user's inventory

def removeItem(item):

	del inventory[item]



#Changes the name of an item

def changeItemName(item, nameNew):

	inventory[item]["name"] = nameNew

	inventory[nameNew] = inventory[item]

	del inventory[item]



#Changes the bonus(es) of an item

def changeItemBonus(item, bonusNew):

	inventory[item]["bonuses"] = bonusNew



#Changes how many of an item you have

def changeItemCount(item, countNew):

	inventory[item]["count"] = int(countNew)

	updateEncumberance()



def changeItemWeight(item, weightNew):

	inventory[item]["weight"] = int(weightNew)

	updateEncumberance()



#Changes the dice type of an item

def changeItemDiceType(item, dTypeNew):

	inventory[item]["diceType"] = int(dTypeNew)



#Changes the dice count of an item

def changeItemDiceCount(item, dCountNew):

	inventory[item]["diceCount"] = int(dCountNew)



#Changes the charges of a magic item

def changeItemCharges(item, chargesNew):

	inventory[item]["charges"] = int(chargesNew)



#Changes the max charges of a magic item

def changeItemMaxCharges(item, maxChargesNew):

	inventory[item]["maxCharges"] = int(maxChargesNew)



#Toggles equipment

def toggleEquipped(item):

	inventory[item]["equipped"] = not inventory[item]["equipped"]



#Adds a new skill to the user's list

def newSkill():

	name = str(input("Enter the skill's name: "))

	stat = str(input("Enter which main stat the skill relies on: ")).upper()



	skills[name] = {"name": name, "stat": stat}



#Removes a skill from the user's list

def removeSkill(name):

	del skills[name]



#Changes a skill the user has

def changeSkill(name):

	nameNew = str(input("Enter the skill's new name,\nor hit ENTER to leave it unchanged: "))

	if nameNew != "":

		skills[name]["name"] = nameNew

		skills[nameNew] = skills[name]

		del skills[name]



	statNew = str(input("Enter the skill's new relied stat,\nor hit ENTER to leave it unchanged: ")).upper()

	if statNew != "":

		skills[name]["stat"] = statNew



#Adds a new ability to the user's list

def newAbility():

	name = str(input("Enter the ability's name: "))

	desc = str(input("Describe the ability: "))

	stat = str(input("Enter which main stat the ability relies on: ")).upper()



	abilities[name] = {"name": name, "desc": desc, "stat": stat}



#Removes an ability from the user's list

def removeAbility(name):

	del abilities[name]



#Changes an ability the user has

def changeAbility(name):

	nameNew = str(input("Enter the ability's new name,\nor hit ENTER to leave it unchanged: "))

	if nameNew != "":

		abilities[name]["name"] = nameNew

		abilities[nameNew] = abilities[name]

		del abilities[name]



	descNew = str(input("Enter the ability's new description,\nor hit ENTER to leave it unchanged: "))

	if descNew != "":

		abilities[name]["desc"] = descNew



	statNew = str(input("Enter the ability's new relied stat,\nor hit ENTER to leave it unchanged: ")).upper()

	if statNew != "":

		abilities[name]["stat"] = statNew



#Rolls dice for the player via the random module. 

def rollDice(diceType, diceCount):

	i = 1



	print("\nRolling your dice...")\



	if diceCount >= 10:

		rolls = []



	while i <= diceCount:

		roll = random.randint(1, diceType)

		

		if diceCount >= 10:

			rolls.append(roll)



		if roll <= int(diceType / 2):

			print("\t" + str(roll) + "...")

		elif roll <= int(diceType * 3 / 4):

			print("\t" + str(roll) + ".")

		elif roll <= int(diceType * 9 / 10):

			print("\t" + str(roll) + "!")

		else:

			print("\t" + str(roll) + "!!!")



		i += 1



	if diceCount >= 10:

		print("The average roll was " + str(int(sum(rolls) / len(rolls))) + ".")



#Prints out the contents of the user's info dictionary

def printInfo():

	print("+---" + info["name"] + "'s Information---+")



	for bit in info:

		print("\t+ " + bit + ":\n\t\t+ " + info[bit])



#Prints out the contents of the user's stats dictionary

def printStats():

	print("+---" + info["name"] + "'s Statistics---+")



	for bit in stats:

		print("\t+ " + bit + ":\n\t\t+ " + str(stats[bit]))



#Prints out the contents of the user's inventory dictionary

def printInven():

	print("+---" + info["name"] + "'s Inventory---+")



	for item in inventory:

		print("\t+ " + inventory[item]["name"])



		for bit in inventory[item]:

			if bit != "name" \

			and str(inventory[item][bit]) != "" \

			and str(inventory[item][bit]) != "0" \

			and str(inventory[item][bit]) != "0.0":

				if bit == "equipped":

					if inventory[item]["equipped"]:

						print("\t\t+ Equipped")

					else:

						print("\t\t+ Not Equipped")

				else:

					print("\t\t+ " + bit + "\n\t\t\t+ " + str(inventory[item][bit]))



#Prints out the contents of the user's skills dictionary

def printSkills():

	print("+---" + info["name"] + "'s Skills---+")



	for skill in skills:

		print("\t+ " + skills[skill]["name"] + " (" + skills[skill]["stat"] + ")")



#Prints out the contents of the user's abilities dictionary

def printAbils():

	print("+---" + info["name"] + "'s Abilities---+")



	for abil in abilities:

		print("\t+ " + abilities[abil]["name"] + ": (" + abilities[abil]["stat"] + ")")

		print("\t\t+ " + abilities[abil["desc"]])



#Shortens command input lines

def getCommand():

	return str(input("\nEnter an command (a bracketed word): ")).upper()



#Shortens error message

def printInvalid():

	print("Error: Invalid Command!")



#Main Function

def main():

	print("\tWelcome to C^2's DnD Character Sheet Program")

	print("\t\t[Version " + str(version) + "\t]\n\t\t[Begun " + begun + "\t]\n\t\t[Updated " + updated + "\t]")

	print("\n\t(Tip: Entering the first letter of a command word will suffice)")



	quit = False

	loaded = False



	while not quit:

		print("\n\t[NEW]: Create a new character")

		#print("\t[LOAD]: Load a character from file")



		if loaded:

			#print("\t[SAVE]: Save a character to file")

			print("\n\t[INFO]: Access character info")

			print("\t[STAT]: Access character stats")

			print("\n\t[SKIL]: Access skills")

			print("\t[ABIL]: Access abilities")

			print("\t[INVT]: Access inventory\n")



		print("\t[ROLL]: Roll dice")

		print("\t[QUIT]: Quit program")



		com = getCommand()



		if com == "NEW" or com == "N":

			newInfo()

			newStats()

			loaded = True



		elif com == "ROLL" or com == "R":

			print("\n(Ex. Enter \'20\' for a d20)")

			rollDice(int(input("Enter which type of dice to roll: ")), int(input("Enter how many times to roll: ")))



		elif com == "QUIT" or com == "Q":

			quit = not quit



		elif loaded:

			if com == "INFO":

				print("\n\t[SHOW]: Print all info")

				print("\t[EDIT]: Edit character info")



				com = getCommand()



				if com == "SHOW" or com == "S":

					printInfo()



				elif com == "EDIT" or com == "E":

					for bit in info:

						print("\t+ " + bit)

					changeInfo(input("Enter an above info field: "), input("Enter your new info for the field: "))



				else:

					printInvalid()



			elif com == "STAT":

				print("\n\t[SHOW]: Print all stats")

				print("\t[EDIT]: Edit a stat")



				com = getCommand()



				if com == "SHOW" or com == "S":

					printStats()



				elif com == "EDIT" or com == "E":

					print("\n\t[STAT]: Change main stat")

					print("\t[BONUS]: Change stat bonus")

					print("\t[HP]: Change HP")

					print("\t[MAXHP]: Change maximum HP")

					print("\t[XP]: Add Experience")

					print("\t[COIN]: Add (or remove) Money")



					com = getCommand()



					if com == "STAT" or com == "S":

						for bit in stats:

							if len(bit) == 3:

								print("\t+ " + bit)



						changeStat(input("Enter an above stat: "), input("Enter your new stat value: "))

						updateSavingThrows()

						com = ""



					elif com == "BONUS" or com == "B":

						for bit in stats:

							if len(bit) == 8:

								print("\t+ " + bit)



						changeStat(input("Enter an above bonus stat: "), input("Enter your new bonus stat value: "))

						updateSavingThrows()



					elif com == "HP" or com == "H":

						changeHP(input("Enter your new HP value: "))



					elif com == "MAXHP" or com == "M":

						changeMaxHP(input("Enter your new maximum HP value: "))



					elif com == "XP" or com == "X":

						addXP("Enter how much XP you've just earned: ")



					elif com == "COIN" or com == "C":

						addMoney("Enter how much money you've just earned: ")



				else:

					printInvalid()



			elif com == "SKIL":

				print("\n\t[NEW]: Create a skill")

				print("\t[DEL]: Remove a skill")

				print("\t[EDIT]: Edit a skill")

				print("\t[SHOW]: Print all skills")



				com = getCommand()



				if com == "NEW" or com == "N":

					newSkill()



				elif com == "DEL" or com == "D" or com == "EDIT" or com == "E":

					for bit in skills:

						print("\t+ " + bit)



					if com == "DEL" or com == "D":

						removeSkill(input("Enter an above skill: "))



					elif com == "EDIT" or com == "E":

						changeSkill(input("Enter an above skill: "))



				elif com == "SHOW" or com == "S":

					printSkills()



				else:

					printInvalid()



			elif com == "ABIL":

				print("\n\t[NEW]: Create an ability")

				print("\t[DEL]: Remove an ability")

				print("\t[EDIT]: Edit an abilities")

				print("\t[SHOW]: Print all abilities")



				com = getCommand()



				if com == "NEW" or com == "N":

					newAbility()



				elif com == "DEL" or com == "D" or com == "EDIT" or com == "E":

					for bit in abilities:

						print("\t+ " + bit)



					if com == "DEL" or com == "D":

						removeAbility(input("Enter an above ability: "))



					elif com == "EDIT" or com == "E":

						changeAbility(input("Enter an above ability: "))



				elif com == "SHOW" or com == "S":

					printAbils()					



				else:

					printInvalid()



			elif com == "INVT":

				print("\n\t[NEW]: Create an item")

				print("\t[DEL]: Remove an item")

				print("\t[EDIT]: Edit an item")

				print("\t[SHOW]: Print all items")



				com = getCommand()



				if com == "NEW" or com == "N":

					newItem()



				elif com == "DEL" or com == "D":

					for item in inventory:

						print("\t+ " + item)



					removeItem(input("Enter an above item: "))



				elif com == "SHOW" or com == "S":

					printInven()



				elif com == "EDIT" or com == "E":

					print("\n\t[NAME]: Change item name")

					print("\t[BONUS]: Change item bonus(es)")

					print("\t[EQUIP]: Toggle an equippable item")

					print("\t[AMONT]: Change item amount")

					print("\t[WEGHT]: Change item weight")

					print("\t[DTYPE]: Change item dice type")

					print("\t[ROLLS]: Change item dice rolls")

					print("\t[CHRG]: Change item magic charges")

					print("\t[MAXC]: Change item max charges")



					com = getCommand()



					for item in inventory:

						print("\t+ " + item)



					if com == "NAME" or com == "N":

						changeItemName(input("Enter an above item: "), input("Enter the item's new name: "))



					elif com == "BONUS" or com == "B":

						changeItemBonus(input("Enter an above item: "), input("Enter the item's new bonus(es): "))



					elif com == "EQUIP" or com == "E":

						toggleEquipped(input("Enter an above item: "))



					elif com == "AMONT" or com == "A":

						changeItemCount(input("Enter an above item: "), input("Enter how many of the item you have: "))



					elif com == "WEGHT" or com == "W":

						changeItemWeight(input("Enter an above item: "), input("Enter the item's new weight: "))



					elif com == "DTYPE" or com == "D":

						changeItemDiceType(input("Enter an above item: "), input("Enter the item's new dice type: "))



			import random



