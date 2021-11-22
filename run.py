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

print(randomtime + " there were some " + randompeople + randomplaces)
print(randomaction + randomsports + " against " + randomanimals)
print(f"Can you believe it {user_name}!")
