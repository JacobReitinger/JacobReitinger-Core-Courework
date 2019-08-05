# CSC 241-401
# Assignment 2 template

# Jacob Reitinger


# I worked by myself

# Files without this information will earn a 0

# Include doc strings for full credit

# For each problem
#
#  
#  INPUT
#  variable name, source (user? passed in? file?), data type
#   
#
#  OUTPUT
#  variable name or input string, destination (screen? return? file?), data type 
#
#  PROCESSING (Algorithm or pseudocode)
#  Put your algorithm here for getting from the INPUT to the OUTPUT
#  
#
#  

# Question 1
#put in by the computer as integers
# prints i on the screen
# for the first one it starts at 26, so it displays
#26 and shows each number untill 37 where it stops
#the second one starts at 21 displays 21 and shows every seven numbers
# till it stops at 77
# the third and final one starts at 35, goind down isntead of up by two
# ending at 1. 
def sequences():
    list = []
    for i in range(26,37,1):
        list.append(i)
    print(*list)
    list = []
    for i in range(21, 77, 7):
        list.append(i)
    print(*list)
    list = []
    for i in range(35, 1, -2):
       list.append(i)
    print(*list)
# Question 2
#input the user puts in the string
#output if it has three or more letters it returns the first three letters
# if it has less then three it returns nothing.
# the program first checks to see how many letters are in the string
# if there are more then 3 it only prints the first three
# if there are less then three it prings nothing. 
def returnThree(s):
    if len(s)>=3:
        print(s[0:3])
    else:
        print("' '")
# Question 3
#input the user puts in the string as well as teh integer n
#output if n is greater then strings letter number print the string with n
# deciding how far it goes
# the program checks to see how many letters are in the string, if the
# umber of letters is greater then n it prints the string, n deep. if n
# is greater then the number of letters in the string it prints nothing
def returnN(s, n):
    if len(s)> n:
        print(s[0:n])
    else:
        print("' '")

# Question 4
#input the user puts in an arry of strings
# output The first letter of the user's inputted words
# the code checks to see first if the list is empty, if so it prints nothing
# if it has at least one in the list the code assigns word to each part in list
# for each part it looks for the first letter and then prints it, moving
#on to the next one
def firstChars(l):
    if len(l) < 1:
        print("The list provided as a parameter was empty.")
    else:
        for word in l:
            print(word[0:1])
            
# Question 5
#input the user generates
#output any nums that the user put in that is bigger then the value use put in
#the code first checks to see if there is anything in the nums list
#then it assigns i to each nums in the list, then it checks to see if any
#part of the list is greater then value and it prints what is done. 
def printGreater(nums, value):
    for i in nums:
        if i > value:
            print(i,end=' ')

