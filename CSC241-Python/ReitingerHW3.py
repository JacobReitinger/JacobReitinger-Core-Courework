# CSC 241-401
# Assignment 3 template

# Jacob Reitinger

# List your collaborator(s) here (no more than two other people)

# Add a comment describing each person's contribution

# I worked alone

# Files without this information will earn a 0

# Include doc strings for full credit

# Question 1
#Input
#The user puts in two variables n and m
#Output
#The user generated variables n and m shows the multiples of n up untill m
#Algorithm
#The program first checks to see that both n and m are postives. it then
# assigns new varaibles to match n and m. Then prints the new variable then
#does the mutiplication. Which it adds a to n untill it has met m
def printMultiples(n, m):
    if n < 0 & m < 0:
        print()
    else:
        a= n
        b = m - 1
        list = [a]
        for clock in range(0,b):
            n = a + n
            list.append(n)
        print(*list)

# Question 2
#Input
# the user puts in a name an ammount and a email address
#Output
# a paragraph plugging in the name, ammount, and email address given eariler by the user
#Algorithm
# I made it so that the program finds the first space in name and then gives it the variable a.  I then make a variable c which is 2 more then a.
#I created name which makes the  string capital but only using the first character I then add the rest. I then assign variable b, the same thing as the
# variable name but use a and c to correctly make the first character capital and the rest lowercase. finally I make the amount given all uppercase, and
# change it so that ever single time there is no space, there is now. Finally i put it all together in a print statment that is static except for the
# name amount and address. 
def customSpam(name, amount, address):
    a = name.find(" ")
    c = a + 2

    b = name[a:c].upper()+name[c:]
    d = amount.upper()
    e = d.replace("", " ")[1:-1]
    name = name[:1].upper()+name[1:a]
    print('Dear '+ name + " " + b)
    print('We would like to let you know about a great opportunity.')
    print('You can make '+ e + ' dollars in just a few short weeks!')
    print('This is a limited-time offer.')
    print('Please contact us at ' + address +' for more information')
    
        
# Question 3
#Input
#The user puts in a string
#Output
# if the string ends in "ion" replace it with e
#Algorithm
#The progam frst looks to see if it ends with "ion". if it does, the program
#takes off the last three chracters and replaces it with the letter "e"
# it then prints s
def ion2e(s):
    if 'ion' in s[-3:]:
        s = s[0:-3]+ "e"
        print(s)
    else:
        print()

# Question 4
#Input
#a user puts in a string and a number
#Output
#The user recieves a printed number of words in the sentence whos character length equals the input number. 
#Algorithm
#the program first sets a variable clock to 0 then the string gets split, and for each part of it it is assigned to a varaible word. then it checks
# to see if the words length equals the n given by the user. if so it adds one to clock. when it is done it returns the total number of clock. 
def numLen(s, n):
    clock = 0
    for word in s.split():
        if len(word) == n:
            clock += 1
    return clock

# Question 5
#input
#a list the user decides as well as a number
#Output
#the lsit gets print again but digit in the list at the palce the number specified is changed to a negative.
#algorithm
#the program first checks to see if the length of the lsit is shroter then the num, if so it prints a statment sying it can't do that.
# otherwise it goes to the list where the num specified and makes it negative, then prints the list again. 
def makeNeg(lst, num):
    if len(lst) < num:
       print("The index is invalid")
    else:
        lst[num] =-lst[num]
        print(lst)
