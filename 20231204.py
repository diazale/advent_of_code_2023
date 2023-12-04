f = open("input/20231204.txt", "r")
in_data = f.read()
f.close()

winners = list()
numbers = list()

for i in in_data.split("\n"):
    winners.append([int(j) for j in i.split("|")[0].split(":")[1].split()])
    numbers.append([int(j) for j in i.split("|")[1].split()])
    #print(winners)
    #print(i)
    #print(winners[-1])
    #print(numbers[-1])

# Part one:
# Check how many of the numbers are winners
# For every number that is a winner, we have 2^(winners-1) as our score
# Take the length of the intersection and that's the winners per card

score = 0

for card in range(len(numbers)):
    #print(winners[card], numbers[card])
    #print(set(winners[card]).intersection(set(numbers[card])))

    matches = len(set(winners[card]).intersection(set(numbers[card])))

    if matches > 0:
        score+=2**(matches - 1)

    #print(score)

# Part two:
# Each winning number grants an incremented scratch card
# e.g. four winners in card 1 grants a copy of cards 2,3,4,5
# Copies of cards can win as well
# Including the originals, how many total scratch cards do we have?

# Store the number of each card
# Originally planned to do a stack but went another way
card_stack = dict()
for card in range(len(numbers)):
    card_stack[card] = 1

card_counter = 0

for card in card_stack.keys():
    print("Card", card+1)
    print("Copies:", card_stack[card])
    card_counter+=card_stack[card]
    print("Card counter:", card_counter)

    # Number of matches for this card
    matches = len(set(winners[card]).intersection(set(numbers[card])))

    # Multiple the number of matches by the number of cards
    # Increment the next cards by this much
    for inc in range(0,matches):
        card_stack[card+inc+1]+=card_stack[card]

    print("Matches:", matches)
    print()

# 1185 too low
print(card_counter)