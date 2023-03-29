import random as rand
import time as time

# Define a function to randomly choose a box and pick two coins from it
def pickTwoCoins():
    # Define the three possible boxes
    listBoxes = [["G","G"], ["G", "S"], ["S","S"]]
    # Randomly choose a box
    intChosenBox = rand.randint(0, 2)
    # Randomly choose a coin from the box
    intChosenCoin = rand.randint(0, 1)
    listTwoCoins = []
    
    # Append the two coins to a list in the order they were picked
    if intChosenCoin == 0:
        listTwoCoins.append(listBoxes[intChosenBox][0])
        listTwoCoins.append(listBoxes[intChosenBox][1])
    else:
        listTwoCoins.append(listBoxes[intChosenBox][1])
        listTwoCoins.append(listBoxes[intChosenBox][0])
    
    # Return the list of two coins
    return listTwoCoins

# Keep track of the starting time
start = time.time()

# Set the number of times we want to pick two coins and record the results
intTotalAttempts = 100000

# Initialize counters to keep track of the number of times each outcome occurs
intFirstCoinSilver = 0
intFirstCoinGold = 0
intOneGoldOneSilver = 0
intOneGoldOneGold = 0

# Loop through the specified number of attempts
for i in range(intTotalAttempts):
    # Call the pickTwoCoins function to randomly pick two coins from a box
    listTwoCoins = pickTwoCoins()
    # Check what the first coin is and update the counters accordingly
    if listTwoCoins[0] == "G":
        intFirstCoinGold += 1
        # If the first coin is gold, check what the second coin is and update the counters accordingly
        if listTwoCoins[1] == "G":
            intOneGoldOneGold += 1
        else:
            intOneGoldOneSilver += 1
    else:
        intFirstCoinSilver += 1

# Calculate the percentage of times the first coin was gold and round to two decimal places
floatFirstGoldPercentage = round(100 * intFirstCoinGold/intTotalAttempts, 2)

# Calculate the percentage of times the second coin was gold given that the first coin was gold, and round to two decimal places
floatSecondGoldPercentage = round(100 * intOneGoldOneGold/intFirstCoinGold, 2)

# Calculate how long the script took to run
elapsedTime = time.time() - start

# Print the results and some explanatory text
print("Total Number of Attempts:", intTotalAttempts)
print("First coin gold:", intFirstCoinGold)
print("First coin silver:", intFirstCoinSilver)
print("Expected chance of first coin being Gold: 50%")
print("Actual chance of first coin being Gold:", str(floatFirstGoldPercentage) + "%")
print()
print("After first coin Gold:")
print("Second coin Gold:", intOneGoldOneGold)
print("Second coin Silver:", intOneGoldOneSilver)
print("Expected chance of second coin being Gold: 66.66%")
print("Actual chance of second coin being Gold:", str(floatSecondGoldPercentage) + "%")
print()
print("Computed in", round(elapsedTime, 4), "seconds")


