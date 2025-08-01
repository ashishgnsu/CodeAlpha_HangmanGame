import random
import Hangman_stages
import words

print("===================================")
print("🎉 Welcome to the Hangman Game! 🎉")
print("===================================")
print("Rules:")
print("- A secret word will be selected.")
print("- You have to guess one letter at a time.")
print("- You are allowed only 6 wrong attempts.")
print("- Each wrong guess brings the hangman closer to danger!")
print("- You win if you guess the word before all 6 chances are used.")
print("Let's begin! Good luck!\n")


choosen_word=random.choice(words.fruits + words.general+words.lst+words.places+words.technology)
blank=[]
for i in range(len(choosen_word)):
    blank.append('_')
print("guess the word: ",blank)

lives=6
game_over= False
while not game_over:
    guessed_word=input("enter gussed letter: ").lower()
    for i in range(len(choosen_word)):
        if choosen_word[i]== guessed_word:
            blank[i]=guessed_word
            if "".join(str(x) for x in blank)==choosen_word:
                game_over = True
                break
    
    if guessed_word not in choosen_word:
        lives=lives - 1
        print("\nYou loose a live\n")
        print(Hangman_stages.stages[lives])
        if lives == 0:
            game_over = True

    else:
        print(f'{blank}')
     
    
if "_" not in blank:
    print("\n🎉 You won! The word was:", choosen_word)
else:
    print("\n💀 Game Over! The word was:", choosen_word)



