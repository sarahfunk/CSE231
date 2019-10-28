###########################################################
#  Project 5
#   Create functions
#       create function to open a file
#       create function to check gender
#       create function to check if a man is named "mike"
#       create function to determine political party
#       create function to print the result
#       create function to plot results
#       create main function to incorporate all functions
#
###########################################################

#Retain these import statements which serve the plot function. 
import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

# define function to open a file
def open_file():
    fp = ""
    while fp == "":
        try:
            file_name = input("Input a file name: ")
            fp = open(file_name, "r")
        except FileNotFoundError:
            print("File not found.")
    return fp
    pass    

# define function to return gender
def get_gender(data_line):
    gender = data_line[39:].strip()
    return gender
        
    pass

# define function that checks if name is mike or michael
def is_mike(data_line):
    name = data_line[:30].lower()
    if "mike" in name or "michael" in name:
        return True
    else:
        return False
    pass 

# define function that returns political party
def get_party(data_line):
    party = data_line[30:39].strip()
    party = party.lower()
    if party == "r":
        return "Republican"
    else:
        return "Democrat"
    pass

# define function that prints the results in a correct format
def print_result(c_rm, c_rf, c_dm, c_df, c_m):
    print("{:<10s}{:>14s}{:>14s}".format("Party","Republican","Democrat"))
    print("{:<10s}{:>14d}{:>14d}".format("Male",c_rm,c_dm))
    print("{:<10s}{:>14d}{:>14d}".format("Female",c_rf,c_df))
    print("\nDudes named Mike: ",c_m)
    pass

# define function that plots the results
def plot_data(c_rm, c_rf, c_dm, c_df, c_m):
    '''
    Plot a figure with provided data. This function is completed and only for fun :)
    Input: 
    c_rm, c_rf, c_dm, c_df, c_m: integers indicate number of Repub_male, 
    Repub_female, Demo_male, Demo_female and dudes named 'Mike'.
    Return: No Return.
    '''
    ylabels = ("Dudes named Mike","Republican_Female", "Republican_Male", "Democratic_Female", "Democratic_Male")
#    ylabels = ("Republican_Male", "Republican_Female", "Democratic_Male", "Democratic_Female", "Dudes named Mike")
    ypos = np.arange(len(ylabels))
    count = np.array([c_m, c_rf, c_rm, c_df, c_dm,])
#    count = np.array([c_rm, c_rf, c_dm, c_df, c_m])
    plt.barh(ypos, count, align = 'center', alpha = 0.4)
    plt.yticks(ypos, ylabels)
    plt.xlabel('Count')
    plt.title("How many female representatives in congress this year?")
    plt.show()

#create function that uses all other functions to run a file
def main():
    
    # define variables
    c_df = 0
    c_dm = 0
    c_rf = 0
    c_rm = 0
    c_m = 0
    
    # call function to open file
    fp = open_file()
    
    # iterates each line to determine gender, party, and mike count
    for line in fp:
        gender = get_gender(line)
        if gender == "female":
            party = get_party(line)
            if party == "Democrat":
                c_df += 1
            elif party == "Republican":
                c_rf += 1
        elif gender == "male":
            mike = is_mike(line)
            if mike is True:
                c_m += 1
            party = get_party(line)
            if party == "Democrat":
                c_dm += 1
            elif party == "Republican":
                c_rm += 1
                
    # print the result
    print_result(c_rm, c_rf, c_dm, c_df, c_m)
    
    # prompt to plot
    ask = input("Do you want to plot? ")
    ask = ask.lower()
    if ask == "yes":
        plot_data(c_rm, c_rf, c_dm, c_df, c_m)
    pass
    
            
# call the main function
if __name__ == '__main__':
     main()
