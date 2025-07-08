
print("             _____   ")      
print("             (   |")
print("             O   |")
print("            /|\  | ")
print("            / \  | ")
print("Hangman   ---------")
import random
import time
check = []
print("Welcome to hangman!")
time.sleep(0.5)
def enter():
    print("Press enter when ready")
    input(">>>")
test = ("""   _____   
   (   |
   O   |
  /|\  | 
  / \  | 
---------""")
print(test)

def dot():
    time.sleep(0.5)
    print(".", end='')
    time.sleep(0.5)
    print(".", end='')
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)

enter()
words = [

    "push", "pull", "mountain", "apple", "guitar", "ocean", 
    "bicycle", "rainbow", "garden", "elephant", "chocolate", "universe", "piano", "jungle", 
    "sunflower", "astronaut", "vacation", "puzzle", "whale", "paradise", "adventure", 
    "candle", "dolphin", "pizza", "caramel", "snowflake", "volcano", "treasure", "zebra", 
    "butterfly", "horizon", "clouds", "island", "rocket", "galaxy", "mountain", "puzzle", 
    "harmony", "moonlight", "pyramid", "tiger", "kangaroo", "tulip", "diamond", "squirrel", 
    "waterfall", "lighthouse", "cactus", "oasis", "mermaid", "wizard", "fairy", "tornado"
]
zero = ("""   _____
   (   |
       |
       |
       |
---------""")
one = ("""   _____       
   (   |
   O   |
       |
       |
---------""")
two = ("""   _____       
   (   |
   O   |
   |   |
       |
---------""")
three = ("""   _____      
   (   |
   O   |
  /|   |
       |
---------""")
four = ("""   _____      
   (   |
   O   |
  /|\  |
       |
---------""")

five = ("""   _____      
   (   |
   O   |
  /|\  |
  /    |
---------""")
six = ("""   _____      
   (   |
   O   |
  /|\  |
  / \  |
---------""")

word = random.choice(words)
strike = 0
test = ("-"*len(word))
tword = list("-" * len(word))

while strike != 6:
    if strike == 0:
        print(zero)
    
    elif strike == 1:
        print(one)
    elif strike == 2:
        print(two)
    elif strike == 3:
        print(three)
    elif strike == 4:
        print(four)
    elif strike == 5:
        print(five)
    elif strike == 6:
        print(six)
    print("")
    print("")
    tword = "".join(tword)
    print(tword)
    tword = list(tword)

    
    letg = input("What letter is in the word? : ")
    letg = letg.lower()
    if letg in check:
        print("You have already guessed this word!")
        continue
    if letg.isnumeric() == True:
        print("No numbers please")
        continue
    check.append(letg)
    
    if len(letg) > 1:
        if letg == word:
            break
        else:
            print(f"{letg} is not the word")
            strike += 1
            continue
    wordm = word
    q = word.find(letg) 
    if q == -1:
        print(f"{letg} is not found in this word")
        strike += 1
    elif q > -1:
        print(f"YEA! {letg} is in this word")
    test = ""
    linew = word
    while wordm.find(letg) > -1:
        e = wordm.find(letg)
        linew = list(linew)
        linew[e]= "-"
        linew = "".join(linew)
        wordm = linew

    
        tword[e] =  letg
        
    tword = "".join(tword)
    
    if tword.find("-") == -1:
        break
    tword = list(tword)
    
if strike == 6:
    print(six)
    print("you have failed!")
    print(f"the word was {word}")
    print("Your score is: 0/6")
else:
    print("You have guessed the word!")
    print(f"the word was {word}")
    score = strike
    score = score - 6
    score = score * -1
    
    print(f"Your score is {score}/6", end = '')
    if score == 6:
        print("!")
        print("Well done! :D")
    else:
        print("")
    

