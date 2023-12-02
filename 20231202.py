import numpy as np

f = open("input/20231202.txt", "r")
in_data = f.read()
f.close()

games = [l for l in in_data.split("\n")]

# Input:
# Game [ID]: Subset 1; Subset 2; ...; Subset S
# Subset format: [N] [colour]

# Part one:
# Which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?
# We can eliminate the impossible ones: those where any subset has more than 12R, 13G, or 14B at once

impossible_games = []

max_red = 12
max_green = 13
max_blue = 14

colour_max = {
    "red":12,
    "green":13,
    "blue":14
}

# Go through each game and split by semi-colon, then check the numbers of bags
for game in games:
    game_id, subsets = game.split(":")
    #print(game_id)

    for subset in subsets.split(";"):
        #print(subset.strip())

        for colour in colour_max.keys():
            if colour in subset:
                #print("Checking", colour)

                if int(subset.split(colour)[0].split(",")[-1]) > colour_max[colour]:
                    #print("too much", colour, "!!!")
                    impossible_games.append(int(game_id.split()[1].strip()))

# I added up the wrong value, just gonna take the complement using gauss' childhood nonsense
game_id_sum = (100*101)/2 - np.sum(list(set(impossible_games)))
#print(game_id_sum)


# Part two:
# In each game you played, what is the fewest number of cubes of each color that could have been in the bag to
# make the game possible?
# So, find the minimum number of cubes in each bag? i.e. find the max of each colour in each game?

power_sum = 0

# Go through each game and split by semi-colon, then check the numbers of bags
for game in games:
    colour_max = {
        "red":0,
        "green":0,
        "blue":0
    }
    game_id, subsets = game.split(":")
    #print(game_id, subsets)

    for subset in subsets.split(";"):

        for colour in colour_max.keys():
            if colour in subset:
                if int(subset.split(colour)[0].split(",")[-1]) > colour_max[colour]:
                    colour_max[colour] = int(subset.split(colour)[0].split(",")[-1])

    power = colour_max["red"] * colour_max["green"] * colour_max["blue"]
    power_sum+=power

print(power_sum)