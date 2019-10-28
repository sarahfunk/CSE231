###########################################################
#  Project 3
#
#  Algorithm
#    prompt for a level
#    if easy is chosen:
#        conduct typing game for easy
#    if medium is chosen:
#        conduct typing game for medium
#    if hard is chosen:
#        conduct typing game for hard
#    error message if level is not chosen
#    quit if q is chosen
#    print final scores
###########################################################

# import
import string, time
from cse231_random import randint

# define variables
ALPHABET_EASY = string.ascii_letters 
ALPHABET = string.ascii_letters + string.punctuation
reward = 0
total_count = 0
games = 0
total_time = 0
total_score = 0

LEVEL_PROMPT = '''
Please choose the difficulty level:
    E(e) for Easy;
    M(m) for Medium;
    H(h) for Hard;
    Hit "Enter" for Default;
    Q(q) to quit;

Level: '''

# prompt for a level (before your while loop)    
Level = input(LEVEL_PROMPT)
Level = Level.upper()
    
# main while loop starts here
while True:
    
    # if user choses to quit
    if Level == "Q" or Level == "q":
        break
    
    # if user choses easy
    elif Level == "E" or Level == "":
        total_score = 0
        games += 1
        i = 0
        str = ""
        t = 10
        
        # loop to conduct 10 games
        for n in range(0, 10):
            length = randint(3, 5)
            
            # loop to generate random string
            for i in range (length):
                Index = randint(0, len(ALPHABET_EASY)-1)
                char = ALPHABET_EASY[Index]
                str += char
            print("Level [{}], game [{}]/[10]\n".format(Level, games))
            t1 = time.time()
            print("Enter this string: {}".format(str))
            str_input = input(" ")
            str_input = str_input.replace(" ", "")
            t2 = time.time()
            
            # if there are spaces or it entered string is the wrong case
            if str_input == str.upper() or str_input == str.lower():
                str_input = str
                
            # if the string is correct
            if str_input == str:
                total_time += t2-t1
                
                # if the time limit was passed
                if t2 - t1 > t:
                    print("Oops! Too much time.")
                    reward = reward+0
                    print("You spent {:4.1f} of {} seconds entering string [{}][{}]".format(t2-t1,t,str,str_input))
               
                # if the time limit was not passed
                else:
                    print("Good job! You spent {:4.1f} of {} seconds entering string [{}][{}]\n".format(t2-t1,t,str,str_input))
                    reward += 1*length
                    total_count += 1
                    total_score = total_count
                    
            # if the string entered was incorrect
            elif str_input != str:
                games += 1
                print("Incorrect.")
                str = ""
                break
            str = ""
            games +=1
            
        # reset variables, print results, and reprompt user
        str = ""
        print("Result of this game is {}/{}.".format(total_count, 10))
        print("Total time for this game:{:4.1f}".format(total_time))
        games = 0
        total_count = 0
        Level = input(LEVEL_PROMPT)
        Level = Level.upper()
        
    # if user choses medium    
    elif Level == "M":
        total_score = 0
        games += 1
        i = 0
        str = ""
        t = 9
        
        # loop to conduct 10 games
        for n in range(0, 10):
            length = randint(6, 10)
            
            # loop to generate random string
            for i in range (length):
                Index = randint(0, len(ALPHABET)-1)
                char = ALPHABET[Index]
                str += char
            print("Level [{}], game [{}]/[10]\n".format(Level, games))
            t1 = time.time()
            print("Enter this string:", str)
            str_input = input(" ")
            str_input = str_input.replace(" ", "")
            t2 = time.time()
            
            # if the string is correct
            if str_input == str:
                total_time += t2-t1
                
                # if the time limit was passed
                if t2 - t1 > t:
                    print("Oops! Too much time.")
                    reward = reward+0
                    print("You spent {:4.1f} of {} seconds entering string [{}][{}]".format(t2-t1,t,str,str_input))
                    
                # if the time limit was not passed   
                else:
                    print("Good job! You spent {:4.1f} of {} seconds entering string [{}][{}]\n".format(t2-t1,t,str,str_input))
                    reward += 2*length
                    total_count += 1
                    total_score = total_count
                    
            # if the string entered was incorrect        
            elif str_input != str:
                games += 1
                print("Incorrect.")
                str = ""
                break
            str = ""
            games +=1
            
        # reset variables, print results, and reprompt user    
        str = ""
        print("Result of this game is {}/{}.".format(total_count, 10))
        print("Total time for this game:{:4.1f}".format(total_time))
        games = 0
        total_count = 0
        Level = input(LEVEL_PROMPT)
        Level = Level.upper()
        
    # if user choses medium      
    elif Level == "H":
        total_score = 0
        games += 1
        i = 0
        str = ""
        t = 8
        
        # loop to conduct 10 games
        for n in range(0, 10):
            length = randint(11, 15)
            
            # loop to generate random string
            for i in range (length):
                Index = randint(0, len(ALPHABET)-1)
                char = ALPHABET[Index]
                str += char
            print("Level [{}], game [{}]/[10]\n".format(Level, games))
            t1 = time.time()
            print("Enter this string:", str)
            str_input = input(" ")
            str_input = str_input.replace(" ", "")
            t2 = time.time()
            
            # if the string is correct
            if str_input == str:
                total_time += t2-t1
                
                # if the time limit was passed
                if t2 - t1 > t:
                    print("Oops! Too much time.")
                    reward = reward+0
                    print("You spent {:4.1f} of {} seconds entering string [{}][{}]".format(t2-t1,t,str,str_input))
                
                # if the time limit was not passed 
                else:
                    print("Good job! You spent {:4.1f} of {} seconds entering string [{}][{}]\n".format(t2-t1,t,str,str_input))
                    reward += 3*length
                    total_count += 1
                    total_score = total_count
                    
            # if the string entered was incorrect        
            elif str_input != str:
                games += 1
                print("Incorrect.")
                str = ""
                break
            str = ""
            games +=1
            
        # reset variables, print results, and reprompt user
        str = ""
        print("Result of this game is {}/{}.".format(total_count, 10))
        print("Total time for this game:{:4.1f}".format(total_time))
        games = 0
        total_count = 0
        Level = input(LEVEL_PROMPT)
        Level = Level.upper()
        
    # error message if difficulty input not recognized    
    else:
        print("Difficulty level not recognized.")
        Level = input(LEVEL_PROMPT)
        Level = Level.upper()
        
# output final results
print("Your final total: {:d}/{:<d}".format(total_score,10))
print("Your total reward: {:d}".format(reward))  
quit
    
    