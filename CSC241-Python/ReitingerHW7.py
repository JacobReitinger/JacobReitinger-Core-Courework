# CSC 241-404
# Assignment 7 template
#Jacob Reitigner
#Worked by myself
#Honestly This was the hardest homework every assigned I didn't even know how to attempt number 4 and most of these aren't completed. I will be coming in on
#Tuesday after this is due to talk so I can uncerstand this. 

# Include doc strings for full credit
# Question 1
#INPUT
#The user puts in a string
#OUTPUT
# The user recieves a number of out of order characters in the string
#Algorithm
# the program first has a while loop to make sure it keeps goinging even when teh loop is over. First the program checks through the first letter of the firstlist
# and the characters in the second list if any are out of order it keeps track.While this is happening it passes over already completed characters in teh first loop
#It then goes to the second character of the first loop and goes through it again, moving down the line of the first list to keep it from giving false positives. 
def inversions(s):
    a = list(s)
    done = False
    e = 0
    while (not done):
        for b in range(len(a)):
            for c in a[e]:
                for d in a:
                    if d > c:
                        e = e + 1
                        print(d)
        done = True
        
            

# Question 2
#INPUT
#User puts in numbers untill it 0 or a negative number is put in
#OUTPUT
# the highest and the second highest numbers are suppose to come out.
#ALGORITHM
#Fir the computre creats two while loops the first one keep the code from ending all together, the second is suppose to end when a 0 or negative number is entered
#While entering numbers it adds them all to a list. Once a 0 or negative number is added it breaks out of that loop deletes the last entry to the lsit and starts
#on the next part. Here if goes through the list looking for the biggest number, when it is found it gets stored away for later use, but also is deleated from
#the list. The same loop happens again with the moditfied loop and it is suppose to print the final loop. 
def printTwoLargest():
    done=False
    lst1 = []
    a = 0
    c = 0
    e = 0
    f = 0
    z = 0
    while a ==0:
        while (not done):
            x = input("Please Enter A Number: ")
            lst1.append(x)
            if x <="0":
                done=True
        lst1.pop()
        for d in range(len(lst1)):
                if lst1[d] < lst1[d-1]:
                    c = lst1[d]
                    f = d
        z = lst1.pop(f)
        for b in range(len(z)):
            if lst1[b] < lst1[b-1]:
                e = lst1[b]
            
            
        print("The Largest number is " + c)
        print("The Second Largest number is " +e)
        a = 1
# Question 3
#INPUT
#User puts in a letter grade.
#OUTPUT
#The user recieves the GPA equivelent
#ALGORITHM
#First the program boots up a list with the letter value assigned to there place in the list
#Then it makes the users input all capiatal for simplicitys sake. Then makes a loop that assins the variable to number describing the current length.
#then it checks if the user inputted number matches the current variable. If so it checks to see if there are any extra parts to grade given.
#If so it does the propr extra work and if not, simply leave it as it is. 
def letter2Number(grade):
    lst1 = ["F", "D", "C", "B", "A"]
    b = grade.upper()
    for a in range(len(lst1)):
        if b == lst1[a]:
            print(a)
        elif b[0] == lst1[a]:
            if b[1] == "-":
                print(a- .3)
            elif b[1] == "+":
                print(a + .3)
 
# Question 4
#INPUT
#The user words
#OUTPUT
#The user recieved the translation, if they aren't in the dicionary they return underscores however long the word was instead of a translation
#ALGORITHM
# first the user puts in the word. If its not in the dictionary it takes the length of the word added and puts that many underscores, and returns the word put
# with the underscores. If it is in the program searches through the lsit, then once found prints the word the user entered, with the translation.
def translate(word_dict):
    print("Welcome to the WordsRUs translation service."
    x = input("Please enter a word")
          

