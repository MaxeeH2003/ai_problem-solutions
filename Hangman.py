#Importing 
import random
from hangman_art import stages,logo
from Hangmancountrywords import words

#chossing word at random
chosen_word = random.choice(words)


limit = len(stages)

#Giving number of chances
lives = len(chosen_word)


#Displaying LOGO
print(logo)
print(f'psst,the solution is {chosen_word}.')

disp = []
a = []
b = []


for i in range(len(chosen_word)):
    disp.append("_")


#Displaying Dashes
while "_" in disp:
    
    guess = input("Guess a letter:").lower()
    
    for i in range(len(chosen_word)):
        letter = chosen_word[i]

        if letter == guess:
            disp[i] = letter

        

    if guess == 'ans':
        print(f'psst,the solution is {chosen_word}.')
        lives = lives+1        

    if guess not in chosen_word and guess not in a:
        lives = lives-1
        a.append(guess)
        print("𝐇𝐈𝐍𝐓:𝐈𝐓 𝐈𝐒 𝐀 𝐂𝐎𝐔𝐍𝐓𝐑𝐘")
    
        
        if lives == 0:
            print("𝖄𝕺𝖀 𝕷𝕺𝕾𝕰")
            
            exit(1)
        if lives == 1:
            print("You are about to lose")
            print("For answer type **ans**")
            
            

    print(f"{' '.join(disp)}")

    print(stages[lives])


else:
    print("𝖄𝕺𝖀 𝖂𝕴𝕹")
        
