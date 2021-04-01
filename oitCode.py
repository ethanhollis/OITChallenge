
##Time Spent developing = 2 hours and 16 minutes

## convert to roman numerals. Recieves an int, will convert to roman and print output
def toRoman(num):
    #each digit can be converted seperately, then concat together at the end so let's do that
    
    #get our array of digits to go through
    digits = []
    for digit in num:
        digits.append(int(digit))
    
    #here are the possible digit options 
    thousandOptions = ['', 'm', 'mm', 'mmm',]
    hundredOptions = ['', 'c', 'cc', 'ccc', 'cd', 'd', 'dc', 'dcc', 'dcc', 'cm']
    tenOptions = ['', 'x', 'xx', 'xxx', 'xl', 'l', 'lx', 'lxx', 'lxxx', 'xc']
    oneOptions = ['', 'i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix']

#Now we just have do decide how big of a number it is and do that!
    if int(num) >= 1000:
        thousands = thousandOptions[digits[0]]
        hundreds = hundredOptions[digits[1]]
        tens = tenOptions[digits[2]]
        ones = oneOptions[digits[3]]

    elif int(num) >= 100:
        thousands = thousandOptions[0]
        hundreds = hundredOptions[digits[0]]
        tens = tenOptions[digits[1]]
        ones = oneOptions[digits[2]]
    
    elif int(num) >= 10:
        thousands = thousandOptions[0]
        hundreds = hundredOptions[0]
        tens = tenOptions[digits[0]]
        ones = oneOptions[digits[1]]

    else:
        thousands = thousandOptions[0]
        hundreds = hundredOptions[0]
        tens = tenOptions[0]
        ones = oneOptions[digits[0]]       

    output = (thousands + hundreds + tens + ones)
        

    

    
    
    return print(output)


def toModern(num):
    # ok so all digits must be either I, V, X, L, C, D, or M. if digit0 is greater than or equal to digit1,
    #we can add it to the output. If it's less than, you subtract it from digit1 and then add that to output, since you can only have 1 subtractor. 
   
   #function to get the value of a digit.
    def getValue(n):
        if (n=="i"):
            return 1
        if (n=="v"):
            return 5
        if (n=="x"):
            return 10
        if (n=="l"):
            return 50
        if (n=="c"):
            return 100
        if (n=="d"):
            return 500
        if (n=="m"):
            return 1000
    ###### End Function #########

#set variables
    output = 0
    d=0

#goes through the string and checks digits
    while d < len(num):
        
        #gets the first digits value
        d1 = getValue(num[d])
        
        # checks to see if there is another digit after if so it checks to see if addition or subtraction is needed
        if d+1 < len(num):
            #if next number is equal to or smaller, we add the current number
            if d1 >= getValue(num[d+1]):
                output += d1
                d += 1
           #if next number is bigger, we do subtraction, taking the current number from the next, adding it to output
            else:
                d1 = getValue(num[d+1]) - d1
                output += d1
               #skip the next digit since its already accounted for in the subtraction
                d += 2
        #if no more digits after current, just add current
        else:
            output += d1
            d += 1
    
    
  
    return(print(str(output)) )


##Program to run the functions. Asks to know which you need, modern to roman or vice versa. 
method = int(input("Enter 1 or 2: \n 1: Roman to Modern \n 2: Modern to Roman\n"))
if(method == 1):
   #begins the conversion and makes all letters be uniform lowercase
    toModern(input("What is the number: ").lower())

#to convert to roman. Only accepts values between 0 and 3999 because I don't know syntax to make a bigger roman numeral than that...
elif(method == 2):
    number = 0
    while number <= 0 or 3999 < number:
        number = int(input("What is the number (0-3999): "))
    
    toRoman(str(number))


