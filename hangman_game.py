import random
print("WELCOME TO HANGMAN GAME")
print("GUESS A FRUIT ONE WORD AT A TIME")
list = ["mango","banana",'cherry',"orange","grapes","watermelon","litchi","guava"]
word = random.choice(list)
guess_word = ["_"] * len(word)
guess_letters = []
attempts=6

while(attempts>0 and "_" in guess_word ):
      print("word:", " ".join(guess_word))
      print("guessed letters" ," ".join(guess_letters))
      print(f"remaining attempts {attempts}")
      x = input("enter a letter\n").lower() 
      if(len(x))!= 1:
           print("enter a single alphabet")

      if(not x.isalpha ):
           print('Enter only alphabet')
           continue
      if(x in guess_letters):
           print("You have already guesses this letter")        
           continue
      guess_letters.append(x)
            

      
      if x in word:
        for i in range(len(word)):
            if x ==word[i]:
                 guess_word[i] = x
        print()
        print('!!!Right!!!')
        print()
      else :
                attempts-=1
                print()
                print("!!!wrong!!!")
                print()

if "_" not in guess_word:
     
   print(" Congrulations you guessed the word ",word)            

else:
     print("Game over , the word was:",word)