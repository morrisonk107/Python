import random

lists_word = ["rarely",
"universe",
"notice",
"sugar",
"interference",
"constitution",
"we",
"minus",
"breath",
"clarify",
"take",
"recording",
"amendment",
"hut",
"tip",
"logical",
"cast",
"title",
"brief",
"none",
"relative",
"recently",
"detail",
"port",
"such",
"complex",
"bath",
"soul",
"holder",
"pleasant",
"buy",
"federal",
"lay",
"currently",
"saint",
"for",
"simple",
"deliberately",
"means",
"peace",
"prove",
"sexual",
"chief",
"department",
"bear",
"injection",
"off",
"son",
"reflect",
"fast",
"ago",
"education",
"prison",
"birthday",
"variation",
"exactly",
"expect",
"engine",
"difficulty",
"apply",
"hero",
"contemporary",
"that",
"surprised",
"fear",
"convert",
"daily",
"yours",
"pace",
"shot",
"income",
"democracy",
"albeit",
"genuinely",
"commit",
"caution",
"try",
"membership",
"elderly",
"enjoy",
"pet",
"detective",
"powerful",
"argue",
"escape",
"timetable",
"proceeding",
"sector",
"cattle",
"dissolve",
"suddenly",
"teach",
"spring",
"negotiation",
"solid"
"seek",
"enough",
"surface",
"small",
"search"]

# TODO 1.Random the name from the list of words
print("Welcome to the game of 'Hangman'. \nHere is your word to guess:")
number = random.randint(0,2)
word = lists_word[number]
length = len(word)
#print(length)
display = ["*"]* length
print(display)
letter_list = list(word)
#print(letter_list)
life = 6


#TODO 2. if player still has lifes, is the letter correct?
#print(letter_guess)
while life > 0 or display == letter_list:
    result = "False"
    letter_guess = input("Please, guess a letter? ").lower()
    for letter in letter_list:
        if letter_guess == letter:
            
            result = "True"
            for item in range (0,length):
                character = letter_list[item]
                if character == letter_guess:
                    display[item] = letter_guess
                    
#TODO 3. if player guess right or wrong? Take life or add letter to the word.           
    if result == "False":
        life -= 1 
        print(f"This is not a letter in the word! You have lost a life. You have {life} lifes left.")
        #print(result)
        #print(life)
        print(display)
    elif result == "True":
        #print(result)
        #print(life)
        print(display)  
        print(f"This is a in the word! You have {life} lifes left.")
        

    if life == 0:
        print ("Game Over! Your are out of lives!")
    elif display == letter_list:
        print ("You Win and correctly got the word!")
        
        
        
        
