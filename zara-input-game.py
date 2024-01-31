print ("Welcome to MyStory! A game where we personalise a story for you! We will start by asking you some simple questions.Please just reply with a word and try not to use a or the.")
print(' ')
gender = input("Firstly, what is your character a boy, girl, man ,or woman? ")
name = input("Brilliant! Now, what's your character's name? ")
friendname = input("Thank you! Now of course, your character needs a friend. What is their friend's name? ")
House = input("Nearly done! What type of house do they live in? ")
pet = input("Fabulous! Finally, what pet do they have? ")

ready = input("Are you ready to hear your story? yes/no: ")
if ready == "yes":
	print ("Okay! Here it is!")
if ready == "no":
	print ("Well I'm sorry but you'll have to listen to it anyway. Lol!")
	
	
	
print("Once upon a time there lived a"+ ' ' +  gender + ' '+ "called " + name + ". " + name +" lived in a "+House +" On top of a large hill with their best friend "+friendname+"." )
print(" ")

print ("They also had a beautiful pet "+pet+" who they loved a lot. One day, on a bright and sunny day, something awful happened! "+pet+" escaped!! "+name+" and "+friendname+" searched for hours and hours but they still couldn't find their "+pet+" .Feeling more and more stressed, "+friendname+" had a great idea! They would make posters and put them up everywhere! "+name+" was so pleased with this idea and they game each other a big high five.")
print(" ")
print("The next day, they both woke up bright and early and put posters everywhere. Even on their own windows! But days and days passed and their "+pet+" unfortunately never came back.")
print ("Years and years later, they had almost forgotten about the beloved pet "+pet+".  The next day, "+name+" was going for A walk in the park when they heard screaming behind her! She quickly span around as the screaming began to get louder and louder. ")
