import sys, math, os

### Globals
programRan = False

## Dictionaries
population = {
	#This is the key.
				#This is the data inside the key.
	#To call a dictionary variable you use dictionary["key"], which brings out the value.
	"juvenile" : 1000,
	"adult"    : 2000,
	"senile"   : 500
}

survivalRate = {
	"juvenile" : 0.75,
	"adult"    : 0.5,
	"senile"   : 0.25
}

other = {
	"birth rate"  : 3,
	"generations" : 10,
	"disease"     : 100000,
	"dis mod"     : 0.2
}

### Main Program
def main():
	#Menu system, all on one line for shortening of the code, \n makes a new line.
	choice = int(input("1) Set the Generation 0 values\n2) Display the Generation 0 values\n3) Run the model\n4) Export Data\n5) Quit\n"))
	if   choice == 1:
		print("\nSetting Gen 0 values")
		print("--------------------")
		set()
	elif choice == 2:
		print("\nDisplaying Gen 0 values")
		print("------------------------")
		display()
	elif choice == 3:
		print("\nRunning the model")
		print("-----------------")
		#Run the model using parameters, since I will be changing a version of them in the model.
		run(population["juvenile"], population["adult"], population["senile"], survivalRate["juvenile"], survivalRate["adult"], survivalRate["senile"])
	elif choice == 4:
		print("\nExporting data to a file")
		print("------------------------")
		export()
	elif choice == 5:
		print("Exiting Program...")
		sys.exit()
	else:
		print("Please type in one of the possible numbers.")
	
## Setting	
def set():
	#settings menu, lets people go to each area separately, in case they only want to edit them individually.
	print("What would you like to edit?")
	choice2 = str(input("1) Populations\n2) Survival Rates\n3) Birth Rate\n4) Generations\n5) Disease Modifications\nOr type B to go Back\n"))
	choice2 = choice2.lower()
	if   choice2 == "1":
		set_population()
	elif choice2 == "2":
		set_sr()
	elif choice2 == "3":
		set_br()
	elif choice2 == "4":
		set_gen()
	elif choice2 == "5":
		set_disease()
	elif choice2 == "b" or choice2 == "back":
		print("Sending back to the menu...\n")
		#this clears the console, only works in console, not the IDLE run.
		os.system("cls")
		#sends back to the main menu system.
		main()

#these are the different parts of the settings section, so if an error occurs, I can loop.
def set_population():
	newValue = int(input("\nWhat would you like to set the population of juveniles to? "))
	if newValue <= 0:
		print("It must be greater than 0.")
		set_population()
	else:
		population["juvenile"] = newValue
		
		#to loop through a section in a secondary area, I have used a while
		x = True
	while x == True:
		newValue = int(input("What would you like to set the population of adults to? "))
		if newValue <= 0:
			print("It must be greater than 0.")
			#if there is an area, I don't give it any details and it should loop.
		else:
			population["adult"] = newValue
			#change x so I can escape the while loop.
			x = False
	
	#since this is the end of the program, if I want to leave it, I can just call a procedure.
	while True:
		newValue = int(input("What would you like to set the population of seniles to? "))
		if newValue <= 0:
			print("It must be greater than 0.")
		else:
			population["senile"] = newValue
			os.system("cls")
			set()
			
def set_sr():
	newValue = float(input("\nWhat would you like to set the survival rate of juveniles to? (0 - 1) "))
	if newValue < 0 or newValue > 1:
		print("It must be between 0 and 1.")
		set_sr()
	else:
		survivalRate["juvenile"] = newValue
		
		x = True
	while x == True:
		newValue = float(input("What would you like to set the survival rate of adults to? "))
		if newValue < 0 or newValue > 1:
			print("It must be between 0 and 1.")
		else:
			survivalRate["adult"] = newValue
			x = False
		
	while True:
		newValue = float(input("What would you like to set the survival rate of seniles to? "))
		if newValue < 0 or newValue > 1:
			print("It must be between 0 and 1.")
		else:
			survivalRate["senile"] = newValue
			os.system("cls")
			set()

def set_br():
	newValue = float(input("What would you like the birth rate of each greenfly to be? "))
	if newValue < 0:
		print("It must be greater than 0.")
		set_br()
	else:
		other["birth rate"] = newValue
		os.system("cls")
		set()
	
def set_gen():
	newValue = int(input("How many generations would you like to run through? "))
	if newValue < 5 or newValue > 25:
		print("It must be between 5 and 25.")
		set_gen()
	else:
		other["generations"] = newValue
		os.system("cls")
		set()
	
def set_disease():
	newValue = int(input("What would you like the population trigger for the disease to be? "))
	if newValue <= 0:
		print("It must be greater than 0.")
	else:
		other["disease"] = newValue
	
	while True:
		newValue = float(input("How much will the disease affect survival rates? (0 - 1) "))
		if newValue < 0 or newValue > 1:
			print("It must be between 0 and 1.")
		else:
			other["dis mod"] = newValue
			os.system("cls")
			set()

### Displaying
def display():
	print("Current values|")
	print("---------------")
	#%s is a command in python if placed inside a string, which allows you to enter information after the string
	#you use it like this: "blah blah blah %s blah blah blah %s" % (information, information2)
	#%s changes it's meaning based on which one it is.
	print("Populations: Juveniles = %s, Adults = %s, Seniles = %s." % (population["juvenile"], population["adult"], population["senile"]))
	#putting the decimals as percentages mean that it is more readable by the user.
	print("Survival Rates: Juveniles = %s percent, Adults = %s percent, Seniles = %s percent." % (survivalRate["juvenile"] * 100, survivalRate["adult"] * 100, survivalRate["senile"] * 100))
	print("Each Adult Produces: %s juveniles." % (other["birth rate"]))
	print("It runs through: %s generations." % (other["generations"]))
	print("When the population reaches %s greenfly, a disease occurs, lowering the survival rates by %s percent.\n" % (other["disease"], other["dis mod"] * 100))
	#sends back to the main menu.
	main()

### Running
#taking the parameters as easier to type variables, that I can mess around with.
def run(juvenileAmount, adultAmount, senileAmount, juvenileRate, adultRate, senileRate):
	#sets the list into a global so I can use it in the export procedure.
	global finalList
	#initialises the list so I can append items to it.
	finalList = []
	#for loop between generation 0 and the maximum amount of generations ran.
	for i in range(0, other["generations"] + 1):
		#when it is at gen 0
		if i == 0:
			#create a new variable
			#this checks to see in the export procedure if the run procedure has been ran.
			global programRan
			#since it is 'False' initially
			#the opposite is to set it to 'True'
			programRan = True
			#append to the list the original settings set by the user.
			finalList.append("Generation 0, Original Settings: Juveniles = %s, Adults = %s, Seniles = %s, Total Population = %s.\n" % (juvenileAmount, adultAmount, senileAmount, juvenileAmount + adultAmount + senileAmount))
			#also prints the same thing so that the user can see the results.
			print("Generation 0, Original Settings: Juveniles = %s, Adults = %s, Seniles = %s, Total Population = %s.\n" % (juvenileAmount, adultAmount, senileAmount, juvenileAmount + adultAmount + senileAmount))
		else:
			#then it runs through the rest of the generations
			#each generation is labelled at the top of it for more visual
			print("----- Generation %s -----" % (i))
			#this checks if the population is too high and kickstarts the disease factor.
			if (juvenileAmount + adultAmount + senileAmount) >= other["disease"]:
				#if the population is equal to or greater than the disease trigger
				#affect all of the survival rates by the disease modifier.
				juvenileRate *= other["dis mod"]
				if juvenileRate < 0:
					juvenileRate = 0
				adultRate *= other["dis mod"]
				if adultRate < 0:
					adultRate = 0
				senileRate *= other["dis mod"]
				if senileRate < 0:
					senileRate = 0
			#kills any possible juveniles.
			juvenileAmount *= juvenileRate
			#kills any adults
			adultAmount *= adultRate
			#kills any seniles
			senileAmount *= senileRate
			#the adults become the seniles
			senileAmount += adultAmount
			#the juveniles become the adults
			adultAmount = juvenileAmount
			#the new juveniles are worked out by the current adults multiplied by the birth rate.
			juvenileAmount = adultAmount * other["birth rate"]
			#set all of the values to be an integer, because you can't have 0.2 of a living green fly.
			juvenileAmount = math.floor(juvenileAmount)
			adultAmount = math.floor(adultAmount)
			senileAmount = math.floor(senileAmount)
			#appends the new content to the file, with which generation it is.
			finalList.append("Generation %s: Juveniles = %s, Adults = %s, Seniles = %s, Total Population = %s.\n" % (i, juvenileAmount, adultAmount, senileAmount, juvenileAmount + adultAmount + senileAmount))
			#for readablility, I have the population of each type and the total population on different lines.
			print("Juveniles = %s\nAdults = %s\nSeniles = %s\nTotal Population = %s.\n" % (juvenileAmount, adultAmount, senileAmount, juvenileAmount + adultAmount + senileAmount))
	#reads for a button press by the user, so that the console doesn't clear before the user has completely read the display.
	wait = input("PRESS <ENTER> TO CONTINUE")
	os.system("cls")
	#sends back to the menu.
	main()
	
### Export
def export():
	#if the user hasn't gone through the run procedure
	if programRan == False:
		#tell them the error and send them back to the main menu.
		print("Please run the program once before trying to export.\n")
		main()
	else:
		#ask for the file name to save it under.
		fileName = input("What would you like to name your file? ")
		#sets it to being a .txt file and also opens it as a writable file, keeping it under the easier name of 'file'
		with open(fileName + ".txt", "w") as file:
			#loop through each of generations
			#len(listName) returns the amount of items in the list.
			for i in range(0, len(finalList)):
				#write them separately to the files.
				#you cannot write a list into a file.
				file.write(finalList[i])
		#tell them the name of the newly created file for reference.
		print("File %s.txt created.\n" % (fileName))
		#sends back to the main menu.
		main()
		
### Loop
#starts up the program.
main()
