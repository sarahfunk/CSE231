###########################################################
#  Project 6
#   Create functions using lists and tuples
#       create function to open a file
#       create function to read the journal file
#       create function to read the category file
#       create function to display a table of data
#       create function to sort data
#       create function to prepare the data to be plotted
#       create function to plot results
#       create main function to incorporate all functions
#
###########################################################

from operator import itemgetter
import csv
import pylab as py

def open_file():
    
    #defined function to open a open an entered file
    
    
    fp = ""
    while fp == "":
        try:
            file_name = input("Please enter a valid filename: ")
            fp = open(file_name, "r")
        except FileNotFoundError:
            print("Error opening the file. ")
    return fp
    

def read_journal_file(fp):
   
    #defined function to read file and section lines into a list of tuples
    
    
    reader = csv.reader(fp) # create csv reader
    header1 = next(reader,None) # read one line (useful for skip) 
    header2  = next(reader,None) # read one line (useful for skip) 
    tuple_list = []
    for line_list in reader: #line_list is a list of the line
        name = line_list[0][:30]
        try:
            cites = int(line_list[1].replace(",",""))
        except ValueError:
             continue
        try: 
            impact_factor = float(line_list[2])
        except ValueError:
            continue
        line_tuple = (name, cites, impact_factor)
        tuple_list.append(line_tuple)
    
    # sort list of tuples and return it    
    tuple_list.sort(key = itemgetter(2), reverse = True)
    return tuple_list
        
def read_category_file(fp):
    
    #defined function to read file and section lines into a list of tuples
    
    reader = csv.reader(fp) # create csv reader
    header1 = next(reader,None) # read one line (useful for skip) 
    header2  = next(reader,None) # read one line (useful for skip) 
    tuple_list = []
    for line_list in reader: #line_list is a list of the line
        category = line_list[0][:30]
        try:
            num_of_journals = int(line_list[2]) 
        except ValueError:
            continue
        try:
            total_cites = int(line_list[3].replace(",",""))
        except ValueError:
            continue
        average_citation = total_cites / num_of_journals
        line_tuple = (category, num_of_journals, total_cites, average_citation)
        tuple_list.append(line_tuple)
    
    # sort list of tuples and return it  
    tuple_list.sort()
    return tuple_list
        

def display_table(data):
    
    #defined a function to display a correctly formatted table of the data inputted
    
    
    TITLE = "Citation Data of the Top 20 Categories"
    HEADINGS = ['Category', 'Journals', 'Total Citations', 'Citation per Journal']
    journals_sum = 0
    total_citations_sum = 0
    sum_average_citations = 0
    print("\n{:^85s}".format(TITLE))
    print("{:30s}{:>12s}{:>18s}{:>25s}".format(*HEADINGS))
    for tuple in data:
        print("{:30s}{:>10,d}{:>18,d}{:>25,.3f}".format(*tuple))
        journals_sum += tuple[1]
        total_citations_sum += tuple[2]
        sum_average_citations += tuple[3]
    print("-"*85)
    print("{:30s}{:>10,d}{:>18,d}{:>25,.3f}".format("TOTAL",journals_sum,total_citations_sum, sum_average_citations))
    
      
    
def sort_data(data, column):
    
    #defined a function to sort data inputted by an inputted column number
     

    if column == 0:
        data.sort()
    else:
        data.sort(key = itemgetter(column), reverse = True)
        
    return data

def prepare_plot_data(data):
   
    #defined a function that prepares data for plotting by returning an updated list
    
    
    names_list = []
    impact_factor_list = []
    
    data = data[:10]
    for tuple in data:
        names_list.append(tuple[0])
        impact_factor_list.append(tuple[2])
    final_tuple = (names_list, impact_factor_list)
    return final_tuple
    

def plot_data(name,impact_factor):
    '''
        Plots the bar chart of the Journal Impact Factor
        
        Input:
            data (list) -> List of journals and their impact factor
            
        Returns:
            None
    '''
    
    
    py.barh(name,impact_factor)

    py.title("Journal Impact Factor")
    py.xlabel('Impact Factor')
    py.ylabel('Journal Name')
    
    # To pass the Mimir plot test you must uncomment the 'savefig' line and comment out the 'show' line
    py.savefig("plot.png")
    #py.show()
    

def main():
    
    #defined a main function that combines all previously defnied functions
    
    
    fp1 = open_file()   # define all variables
    fp2 = open_file()
    category_list = read_category_file(fp1)
    journal_list = read_journal_file(fp2)
    
    
    #prompt for column number, convert it to an integer or prompt for correct number
    
    column = input("""Column number to sort data (1-category, 2-journals, 3-citations, 4-average citations): """)
    while column != "":
        if column == "1" or "2" or "3" or "4":
            column = int(column)
            column = column - 1
            break
        else:
            print("Incorrect column number. Try Again!")
            column = input("""
            Column number to sort data (1-category, 2-journals, 3-citations, 4-average citations): """)

    #sort data, display the table of data and prompt to plot

    category_list = sort_data(category_list, column)
    display_table(category_list[:20])
    answer_to_plot = input("Do you want to plot the journal data (yes/no)? ")
    
    #loop to either plot, quit if answer is no, or re-prompt for valid answer to prompt
    
    while answer_to_plot != "":
        if answer_to_plot.lower() == "yes":
            journal_list = prepare_plot_data(journal_list)
            plot_data(journal_list[0],journal_list[1])
        elif answer_to_plot.lower() == "no":
            break
        else:
            print("Incorrect answer! Enter yes/no")
            answer_to_plot = input("Do you want to plot the journal data (yes/no)? ")
    quit


#call the main function
    
if __name__ == "__main__":
    main()
