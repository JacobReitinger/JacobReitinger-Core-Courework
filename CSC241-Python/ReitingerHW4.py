# CSC 241-401
# Assignment 4 template

# Jacob Reitinger

# Patrick

# Talked out problem 1 to help me better solve it.
#Helped work out problem 4

# If you worked alone, add a comment indicating that

# Files without this information will earn a 0

# Include doc strings for full credit

# Question 1
#INPUT
#The user puts in a lst of names and a letter
#OUTPUT
#The program returns the list taking out all names that started alphabetacly before letter
#ALGORITHM
#The program takes the letter the user puts in and makes it lower case then assigns it to a new value
# then for each element of the list the program chances the element to lowercase and assigns it a new variable
#finally the two programs come together and if new variable 2 is higher then new variable 2 it prints the orginal word
def partition(lst, c):
    a = c.lower()
    for b in lst:
        d = b.lower()
        if d > a:
            print(b)

# Question 2
#DOC
#INPUT
#The user puts in a list of names as well as a name
#OUTPUT
#The list is printed but any variation of the name given is taken out of the list
#ALGORITHM
#First the program checks to make sure there is stuff inside the list
#then it assigns the name the name given by the user to a variable all lower case
#Then it turns each variable in the list to all lower case, if the lowercase
#name variant doesnt equals the lower case variable in the lsit it prints the variable in the list
#otherwise it prints a blank line
def excludeName(nlst, name):
    if len(nlst) < 1:
        pass
    d = name.lower()
    for b in nlst:
        c = b.lower()
        if c != d:
            print(b)
        else:
            print()


# Question 3
#Input
#User inputs a file name
#Output
# The user recieves the number of lines, words, and characters in the file
#Algorithm
#First the program opens the file and then sets some variables that will be needed later
# Then it goes line by line, and adding a varable for each line to account for enters. But it lowers one count to take away from characters while also adding
#one to show each lines. Then for each character it adds to a variable mentioned before to account for characters
# then looks to see if there is a space in the character spot and adds it to a variable.
# finally it prints all of all of the variables together and prints them 
def stats(fname):
    infile = open(fname, "r")
    count = 0
    counter = 0
    b = 0
    c = 0
    d = 0
    for a in infile:
        d = d + 1
        counter = counter -1
        for b in a:
            if " " in b:
                d = d + 1
            counter = counter + 1
        count = count+ 1
    
    print("line count: " + str(count))
    print("Word Count: " + str(d))
    print("character count: " + str(counter))
# Question 4
#INPUT
#The user puts in the name of a file. 
#OUTPUT
#It prints the variables in the file that are positive.
#ALGORITHM
#first the program opens up the file. It then goes through the file and for each line it assigns it to a new variable making it a float. It then check to
#see if its above 0 and prints it if that is true. 
def printPositive(fname):
    infile = open(fname, "r") 
    for a in infile:
        b = float(a)
        if b > 0:
            print(b)
       

# Question 5
#INPUT
#The user puts in a file name and another one
#OUTPUT
#Prints out the number of hours timed pay per hour. 
#ALGORITHM
# it frist opens up the file.  then it looks through each line assigning
#each part of the line to a variable. Then the variables were mutiplied and pritned.
def payroll(infname, outfname):
    infile = open(infname, "r")
    for a in infile:
        b = a[0:2]
        z = a[3:]
        c = float(b)
        y = float(z)
        d = c * y
        print(d)
    
