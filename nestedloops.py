#character occurence
#Take input of a word
string = input("Please enter your own word:" )
#take input of a character
char = input("Please enter your own character: ")
i = 0
count = 0
#loop will to find the occurence of character
while(i<len(string)): #string operation
    if(string[i] == char): #condition 1
        count = count+1
    i = i+1
    
#Display the result
print("The total Number of Times", char, "has occured=", count)

#FInding prime numbers
#take two input from user
lower = int(input("enter a lower range: "))
upper = int(input("enter a upper range: "))

print("prime numbers between", lower, "and", upper, "are:")
#iterate loop from lower limit to upper limit
for num in range(lower, upper + 1):
    #all prime numbers are greater than 1
    if num > 1:
        for i in range(2, num):
            if (num%i) == 0:
                break
        else:
            print(num)
            
#Finding middle number
#input a number
num1 = int(input("ENter a numebr: "))
t = num1
numLen = 0
#iterate the loop
while t>0:
    numLen = numLen + 1
    t = int(t/10)
    
if numLen>4: #condition 1
    numLen = int(numLen/2)
    chk = 0
    while num1>0: #iterate loop
        rem = num1%10
        if chk==numLen: #nested condition 1
            midOne = rem
        elif chk==(numLen-1):
            midTwo = rem
        num = int(num/10)
        chk = chk+1
    prod = midOne*midTwo #product of middle digits
    #display the result
    print("\nProduct of Mid Digits (" +str(midOne)+ "*" +str(midTwo)+ ") = ", prod)
else: 
    print("\nIt's not a 4 or more than 4-digit number!")