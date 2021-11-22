import random
# The import random will generate the random sentences
# the user will be asked to input their name and a message will appear

user_name = input("What is your name?\n")
print(f"Hello {user_name}, you won't believe what i've just seen")

# The following will be used to generate the random sentence

sports = ["tennis", "badminton", "football", "cricket", "rugby", "hockey"]
places = [" on a ship", " in the supermarket", " in space", " in a field"]
people = ["jugglers", "firemen", "shoemakers", "sailors", "magicians"]
animals = ["mice", "hippos", "chickens", "cows", "giraffs", "cats", "dogs"]
time = ["One day", "One night", "One afternoon", "One evening", "One morning"]
action = ["playing a game of ", "complaining about playing "]

randomsports = random.choice(sports)
randomplaces = random.choice(places)
randompeople = random.choice(people)
randomanimals = random.choice(animals)
randomtime = random.choice(time)
randomaction = random.choice(action)

# The code below will print out the sentence


def rando_sentence():
    print(randomtime + " there were some " + randompeople + randomplaces)
    print(randomaction + randomsports + " against " + randomanimals)
rando_sentence()


print(f"Can you believe it {user_name}!")

# ask the user if they would like another sentence
# If yes another is generated if no the code says bye

sec_senten = input(f"Can i tell you something else {user_name}, yes or no?\n")
if sec_senten == "yes":
    print("Great!")
    rando_sentence()
    print(f"That surprised me, thanks for chatting {user_name} bye!")
elif sec_senten == "no":
    print(f"ok {user_name} i'll catch you later ")
else:
    print("Please enter yes or no")
    print("Hit run programme to go back to the start")
