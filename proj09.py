# =============================================================================
# Project 9
#     Algorithm
#         Define open file function
#         Define check_characters function
#         Define password_entropy_function
#         Define build_password_dictionary function
#         Define cracking function
#         Define create_set function
#         Define common_patterns function
#         Define main function with use of all other functions
# =============================================================================

from math import log2
from operator import itemgetter
from hashlib import md5
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


def open_file(message):
    '''This function takes in a message and prompts a user using this message
    to enter a specific file name. It then attempts to open it, returns
    an error message if it is invalid, then returns a file pointer.'''

    fp = ""
    while fp == "":
        file_name = input(message)
        try:
            if file_name == "":
                fp = open("pass.txt", "r")
            else:
                fp = open(file_name, "r")
        except:
            print('File not found. Try again.')
    return fp

            
def check_characters(password, characters):
    '''Check characters function takes in a password
    and a type of characters then returns true if any
    of the character types are in the password'''

    counter = 0
    for ch in password:
        if ch in characters:
            return True
        else:
            counter +=1
    if counter == len(password):
        return False


def password_entropy_calculator(password):
    '''Password entropy calculator assigns a length then a certain N value
    to an entered password by using the check_characters function
    and many nested if-then statements. It then uses a formula to calculate
    the entropy of a password and returns it'''
    
    L = len(password)
    
    if password == "":
        return 0
    elif check_characters(password, ascii_lowercase ) == False:
        if check_characters(password, ascii_uppercase ) == False:
            if check_characters(password, punctuation ) == False:
                N = 10
            else:
                if check_characters(password, digits ) == False:
                    N = 32
                else:
                    N = 42
        else:
            if check_characters(password, punctuation ) == False:
                if check_characters(password, digits ) == False:
                    N = 26
                else:
                    N = 36
            else:
                if check_characters(password, digits ) == False:
                    N = 58
                else:
                    N = 68             
    else:
        if check_characters(password, ascii_uppercase ) == False:
            if check_characters(password, punctuation ) == False:
                if check_characters(password, digits ) == False:
                    N = 26
                else:
                    N = 36
            else:
                if check_characters(password, digits ) == False:
                    N = 58
                else:
                    N = 68
        else:
            if check_characters(password, punctuation ) == False:
                if check_characters(password, digits ) == False:
                    N = 52
                else:
                    N = 62
            else:
                if check_characters(password, digits ) == False:
                    N = 84
                else:
                    N = 94         
    entropy = L * log2(N)
    entropy = round(entropy, 2)
    return entropy

def build_password_dictionary(fp):
    '''Build password dictionary function takes in a file pointer
    then goes line by line, adding new entries to a dictionary with
    the password's hash as a key, then it, its rank, and its entropy as 
    a group of tuples as the value. It then returns the dictionary'''
    rank = 0
    password_dict = {}
    for line in fp:
        password = line.strip()
        hash_of_pass = md5(password.encode()).hexdigest()
        rank +=1
        entropy = password_entropy_calculator(password)
        tuple_values = (password, rank, entropy)
        password_dict[hash_of_pass] = tuple_values
    return password_dict
        

def cracking(fp,hash_D):
    '''Cracking function takes a file pointer and a dictionary of passwords
    created by build_password_dictionary as its parameters. It
    then loops through the file pointer to define the hash and checks
    if the hash is in the dictionary. If it is, it appends a sorted tuple of the 
    password, its entropy, and its hash to a larger list. This function returns
    a tuple of the list of tuples, a counter of cracked hashes and a counter of
    uncracked hashes.'''
    cracked_count = 0
    uncracked = 0
    list_of_cracked = []
    list_of_cracked2 = []
    for line in fp:
        line_list = line.split(":")
        hash_ = line_list[0] 
        if hash_ in hash_D:
            cracked_count += 1
            password = hash_D[hash_][0]
            entropy = hash_D[hash_][2]
            rank = hash_D[hash_][1]
            tuple_vals = [hash_,password,entropy, rank]
            list_of_cracked.append(tuple_vals)
        else:
            uncracked += 1
    list_of_cracked = sorted(list_of_cracked, key = itemgetter(1))   
    for l in list_of_cracked:
        l.pop()
        l = tuple(l)
        list_of_cracked2.append(l)
    final_tuple = (list_of_cracked2, cracked_count, uncracked)
    return final_tuple
            

def create_set(fp):  
    '''This function iterates through a file pointer to create a set
    of each line in the file. It then returns the set. '''
    set_of_words = {""}
    for line in fp:
        line = line.strip()
        set_of_words.add(line)
    set_of_words.remove("")
    return set_of_words   

def common_patterns(D,common,names,phrases):
    '''This function loops through a union of three sets and a dictionary
    to create a new dictionary with passwords as keys and lists of words from 
    the set that are found inside the password as values. It then sorts the lists 
    and returns the dictionary. '''

    dict_of_patterns = {}
    main_set = common | names | phrases
    for key, value in D.items():
        password = value[0]
        dict_of_patterns[password] = []
        for word in main_set:
            word = word.lower()
            if word.lower() in password:
                if password in dict_of_patterns:
                    if word.lower() in dict_of_patterns[password]:
                        continue
                    else:
                        dict_of_patterns[password].append(word)
                else:
                    dict_of_patterns[password].append(word)
    for key, value in dict_of_patterns.items():
        dict_of_patterns[key].sort()
    return dict_of_patterns
               
        
                
def main():
    '''The main function provides a loop that allows the user to choose between
    four options. Option one prompts for two files and displays a table of
    cracked passwords using the cracking function and the build_password_dictionary
    function. The second option locates common patterns within passwords created by
    a file pointer entered by the user. It uses the build_password_dictionary,
    create_set and common_patterns functions to build dictionaries and display the
    final dictionary. The third option prompts for a password then uses the 
    password_entropy_calculator function to find the entropy then display it.
    The fourth option is to quit.'''
    
    BANNER = """
       -Password Analysis-

          ____
         , =, ( _________
         | ='  (VvvVvV--'
         |____(


    https://security.cse.msu.edu/
    """

    MENU = '''
    [ 1 ] Crack MD5 password hashes
    [ 2 ] Locate common patterns
    [ 3 ] Calculate entropy of a password
    [ 4 ] Exit

    [ ? ] Enter choice: '''

    choice = ""
    print(BANNER)
    while choice != "4":        # begin while loop while the user does not choose to quit
        print(MENU)             # print menu and prompt for choice
        choice = input("")
        
        if choice == "1":       # run through functions and displays table for choice 1
            MESSAGE1 = "Common passwords file [enter for default]: "
            MESSAGE2 = "Hashes file: "
            fp = open_file(MESSAGE1) 
            fp2 = open_file(MESSAGE2)
            hash_D = build_password_dictionary(fp)
            cracking_tuple = cracking(fp2, hash_D)
            print("\nCracked Passwords:")
            for tup in cracking_tuple[0]:
                print('[ + ] {:<12s} {:<34s} {:<14s} {:.2f}'.format("crack3d!", tup[0], tup[1], tup[2]))
            print('[ i ] stats: cracked {:,d}; uncracked {:,d}'.format(cracking_tuple[1],cracking_tuple[2]))
            
        if choice == "2":       # run through functions and displays table for choice 2
            MESSAGE1 = "Common passwords file [enter for default]: "
            MESSAGE2 = 'Common English Words file: '
            MESSAGE3 ='First names file: '
            MESSAGE4 = 'Phrases file: '
            fp = open_file(MESSAGE1)
            pass_D = build_password_dictionary(fp)
            fp2 = open_file(MESSAGE2)
            fp3 = open_file(MESSAGE3)
            fp4 = open_file(MESSAGE4)
            names = create_set(fp3)
            common = create_set(fp2)
            phrases = create_set(fp4)
            D_patterns = common_patterns(pass_D,common,names,phrases)
            print("{:21s}{}".format("Password", "Patterns"))
            for k,v in D_patterns.items():
                print("{:20s} [".format(k),end='')# print password 
                print(', '.join(v),end=']\n') # print comma separated list
                
        if choice == "3":       # utilizes functions and displays string for choice 3
            password = input('Enter the password: ')
            entropy = password_entropy_calculator(password)
            print('The entropy of {} is {}'.format(password, entropy))
            
                
if __name__ == '__main__':
    main()






