import random

def findGreen(ans,guess):
	greenPos = []
	for i in range(5):
		if guess[i] == ans[i]:
			greenPos.append(i)
	return greenPos

def findYellow(ans,guess,greenPositions):
	positions = [0,1,2,3,4]
	yellowPos = []
	letters = []
	for i in range(len(greenPositions)):
		positions.remove(greenPositions[i])
	for position in positions:
		letters.append(ans[position])
	for position in positions:
		if guess[position] in letters:
			letters.remove(guess[position])
			yellowPos.append(position)
	return yellowPos

def wordCheck(ans,guess):
	wordResults = ["0","0","0","0","0"]
	greenPos = findGreen(guess,ans)
	yellowPos = findYellow(guess,ans,greenPos)
	for position in greenPos:
		wordResults[position] = "2"
	for position in yellowPos:
		wordResults[position] = "1"
	wordResults = "".join(wordResults)
	return wordResults

def convertToSymbols(greySymbol,yellowSymbol,greenSymbol,wordResults):
    symbols = []
    for i in range(len(wordResults)):
        if wordResults[i] == "0":
            symbols.append(greySymbol)
        elif wordResults[i] == "1":
            symbols.append(yellowSymbol)
        elif wordResults[i] == "2":
            symbols.append(greenSymbol)
    symbols = ("".join(symbols))
    return symbols

def guessDisplay(previousGuesses,previousResults):
    for i in range(len(previousGuesses)):
        print("    " + previousGuesses[i] + " | " + previousResults[i])
    for i in range(8 - len(previousGuesses)):
        print("    ▢▢▢▢▢ | ▢▢▢▢▢")

def removeLetters(word,unusedLetters):
    for letter in word:
        if letter in unusedLetters:
            unusedLetters.remove(letter)
    return unusedLetters

def main():
    with open("possibAnswers.txt", 'r') as f:
        ansList = [line.strip() for line in f]
    with open("possibGuesses.txt", 'r') as f:
        guessList = [line.strip() for line in f]

    symbolList = ["♥","♠","♣","♦","∞","∫","≈","π","ζ","λ","η","φ","θ","Ω","Π","Σ","Δ"]
    greySymbol = random.choice(symbolList)
    symbolList.remove(greySymbol)
    yellowSymbol = random.choice(symbolList)
    symbolList.remove(yellowSymbol)
    greenSymbol = random.choice(symbolList)
    symbolList.remove(greenSymbol)

    ans = random.choice(ansList)
    solved = False
    numGuesses = 0
    previousGuesses = []
    previousResults = []
    unusedLetters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    while not solved and numGuesses<8:
        guessed = False
        while not guessed:
            guess = input("Enter your guess: ")
            if guess in guessList:
                guessed = True
            else:
                print("Invalid guess. Please try again.")
        previousGuesses.append(guess)
        numGuesses += 1
        unusedLetters = removeLetters(guess,unusedLetters)
        wordResults = wordCheck(ans,guess)
        wordSymbols = convertToSymbols(greySymbol,yellowSymbol,greenSymbol,wordResults)
        previousResults.append(wordSymbols)
        print()
        guessDisplay(previousGuesses,previousResults)
        for letter in unusedLetters:
            print(letter,end=" ")
        print("\n")
        if guess == ans:
            solved = True
            print("You win! the answer was: " + ans)
        if numGuesses == 8 and not solved:
            print("You lose! the answer was: " + ans)

# play again
playAgain = True
while playAgain:
    main()
    playAgain = input("Play again? (y/n) ")
    print()
    if playAgain == "n":
        playAgain = False
    else:
        playAgain = True

