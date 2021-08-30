secret_word = "mk"
guessCount = 0
guessLimit= 3
no_ofGuesses = False
guess = ""

while guess != secret_word and not no_ofGuesses :
   if  guessCount < guessLimit :
    guess = input("Enter another word")
    guessCount += 1

   else :
       no_ofGuesses = True

if no_ofGuesses:
    print("Grind your ass as dumb  potato")
else :
    print("asshole monster Win")