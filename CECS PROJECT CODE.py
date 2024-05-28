#import English dictionary
import nltk
nltk.download('words')
from nltk.corpus import words
secret_word = 0
is_word = 0
N = 0
player_true = 0
attempts=1
letter_in_the_right_spot = 0

player_word = 0


#start of the program
print('Welcome to Wordle - CECS 174 edition!')
secret_word = input('Enter the secret 5-letter word: ')

while(len(secret_word)!=5):
    print('Not a valid word, try again!')
    secret_word = input('Enter the secret 5-letter word: ')
   
if (secret_word in words.words()):
    is_word= True

else:
    is_word = False
   
while not is_word:
    print( 'Not a valid word, try again!')
    secret_word = input('Enter the secret 5-letter word: ')
    if (secret_word in words.words()):
        is_word= True

    else:
        is_word = False
N= int(input('Input allowed number of attempts: '))

while (attempts <=N):
    letter_in_the_right_spot = 0
    player_word = input(f'Enter your attempt #{attempts} \n')
    if (player_word in words.words()):
        player_true= True

    else:
        player_true = False
   
    while not player_true:
        print('Not a valid word, try again')
        player_word = input(f'Enter your attempt #{attempts} \n')
        if (player_word in words.words()):
            player_true= True
        else:
            player_true = False

    while (len(player_word)!=5):
        print(f'You entered a {len(player_word)}-letter word, but a 5-letter word is needed. Try again')
        player_word = input(f'Enter your attempt #{attempts} \n')                    

    if (len(player_word) ==5):
        print('You entered a 5-letter word')
        
    for x in range(len(secret_word)):
        for y in range(len(secret_word)):
            if secret_word[y] == player_word[x]:
                if x==y:
                    letter_in_the_right_spot +=1
                    print(f'{player_word[x]} is in the secret_word and in the correct spot #{x+1}')
                    print(f'Correct letters in the correct spot: {letter_in_the_right_spot}')
                else:
                    print(f'{player_word[x]} is in the secret_word but not in the correct spot')
    attempts+=1                
    if(secret_word == player_word):
        print(f'Congrats you won using {attempts-1} attempt(s)')#the message for correct word
        break
    if (N==attempts-1 and player_word != secret_word):
        print(f'You already used #{N} attempts. Better luck tomorrow!')#You lost message  
