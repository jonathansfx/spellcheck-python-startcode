import re  # Needed for splitting text with a regular expression
import time

# Linear search function
def linearSearch(word, word_list):
    for i in range(len(word_list)):
        if word_list[i] == word:
            return i
    return -1

# Binary search function
def binarySearch(word, word_list):
    low = 0
    high = len(word_list) - 1

    while low <= high:
        mid = (low + high) // 2
        if word_list[mid] == word:
            return mid
        elif word_list[mid] < word:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Load words from file
def loadWordsFromFile(fileName):
    with open(fileName, "r") as file:
        textData = file.read()
    return re.findall(r'\b\w+\b', textData.lower())


def spellCheckWord():
    word = input("Please enter a word: ").lower()
    selection = input("Which search algorithm to use (1: Linear Search, 2: Binary Search): ")

    if selection == "1":
        print("\nLinear Search starting...")
        start_time = time.time()
        index = linearSearch(word, dictionary)
        end_time = time.time()
        if index != -1:
            print(f"{word} is IN the dictionary at position {index}.")
        else:
            print(f"{word} is NOT IN the dictionary.")
        print(f"Time taken: {end_time - start_time} seconds")
    elif selection == "2":
        print("\nBinary Search starting...")
        start_time = time.time()
        index = binarySearch(word, dictionary)
        end_time = time.time()
        if index != -1:
            print(f"{word} is IN the dictionary at position {index}.")
        else:
            print(f"{word} is NOT IN the dictionary.")
        print(f"Time taken: {end_time - start_time} seconds")
    else:
        print("Invalid selection.")

def spellCheckAlice():
    selection = input("Which search algorithm to use (1: Linear Search, 2: Binary Search): ")

    not_found_count = 0
    start_time = time.time()

    if selection == "1":
        print("\nLinear Search starting for Alice in Wonderland words...")
        for word in aliceWords:
            if linearSearch(word, dictionary) == -1:
                not_found_count += 1
    elif selection == "2":
        print("\nBinary Search starting for Alice in Wonderland words...")
        for word in aliceWords:
            if binarySearch(word, dictionary) == -1:
                not_found_count += 1
    else:
        print("Invalid selection.")

    end_time = time.time()
    print(f"Number of words not found in dictionary: {not_found_count} "
          f"({end_time - start_time} seconds)\n")


def main():
    # global variables 
    global dictionary, aliceWords
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")

    # Print first 50 values of each list to verify contents
    print(dictionary[0:50])
    print(aliceWords[0:50])

    while True:
        print("\nMain Menu")
        print("1: Spell Check a Word (Linear Search)")
        print("2: Spell Check a Word (Binary Search)")
        print("3: Spell Check Alice In Wonderland (Linear Search)")
        print("4: Spell Check Alice In Wonderland (Binary Search)")
        print("5: Exit")

        selection = input("Enter menu selection (1-5): ")

        if selection == "1":
            spellCheckWord()
        elif selection == "2":
            spellCheckWord()
        elif selection == "3":
            spellCheckAlice()
        elif selection == "4":
            spellCheckAlice()
        elif selection == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid selection.")

# Call main() to begin program
main()
