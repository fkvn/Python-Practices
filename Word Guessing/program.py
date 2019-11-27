import random, os

# import call method from subprocess module 
from subprocess import call 

# define clear function 
def clear(): 
    # check and make call for specific operating system 
    _ = call('clear' if os.name =='posix' else 'cls')

def printPlaceHolder(s):
  print(' '.join([ s for s in s]))

def play():

  while True:
    fruits  = str(open("words.txt","r").read()).split(",")
    fruits = [s.strip() for s in fruits]

    isWinner = False
    numOfWrongGuess = 0
    numOfHint = 2
    prevGuess = []
    hintWord = ''

    randomWord = fruits[random.randrange(len(fruits))]
    placeHolder = ''.join([ "_" for s in randomWord])
    message = ''

    while(not isWinner):
      clear()
      print("Total hints: ", numOfHint)
      print("Number of wrong guesses: ", numOfWrongGuess)
      if message:
        print("\n-----> : ", message)
        message = ''

      if hintWord:
        print("\n-----> Your hint: \"", hintWord, "\". Try it!")
        hintWord = ''

      print("\nGuessing Word: ", end ='') 
      printPlaceHolder(placeHolder)

      print("\nOptions: \n 1) Guesses a letter \n 2) Asks for a hint \n 3) Views previously guessed letters")

      while True:
        option = input("Please enter your choice: ")
        if option.isdigit() and int(option) == 1:
          if int(option) == 1:
            while True:
              guess = input("Please enter your guess letter: ")
              if guess.isalpha() and len(guess) == 1 :
                try:
                  if randomWord.index(guess) > -1:
                    letterIndices = [i for i in range(len(randomWord)) if randomWord.startswith(guess, i)]
                    for i in letterIndices:
                      if placeHolder[i] == guess:
                        message = "You already got it. Try another one!"
                        break
                      placeHolder = placeHolder[:i] + guess + placeHolder[i+1:]    
                except:
                  numOfWrongGuess += 1
                  message = "Opps! It was the wrong one. Please try another one or ask for a hint (if applicable)!"      

                prevGuess.append(guess)  
                if placeHolder == randomWord:
                  isWinner = True
                break
              # end if
            # end while 
          # end if
          break

        elif option.isdigit() and int(option) == 2:
          if numOfHint == 0:
            message = "No more hints! You've used all available hints"
            break

          availableGuesses = [i for i in range(len(placeHolder)) if placeHolder.startswith("_", i)]  

          if numOfHint > 0 and len(availableGuesses) >= 2:
            dashIndices = [i for i in range(len(placeHolder)) if placeHolder.startswith("_", i)]
            availableHints = []

            for i in dashIndices:
              letterIndices = [j for j in range(len(randomWord)) if randomWord.startswith(randomWord[i], j)]

              if len(letterIndices) == 1:
                availableHints.append(letterIndices[0])

            hintWord = randomWord[availableHints[0]]
            numOfHint -= 1  
          else:
            message = "There is only 1 letter left. Hints can't be used here. Good luck!"
          break


        elif option.isdigit() and int(option) == 3:
          print("Your previous guesses: ", prevGuess)
        else:
          break  
      # end while

      if numOfWrongGuess >= 4:
        print("\nOpps! You have guessed incorrectly 4 times. ")
        break
    # end while  

    if isWinner:
      print("\nCongrats! You are the winner")
    else:
      print("\nSorry! You are not winning this time. Try again!!!")
    
    newGame = input("\nYou want to start a new game (y/n)?  -> ")
    if newGame == 'n':
      return
    else:
      isWinner = False

play()