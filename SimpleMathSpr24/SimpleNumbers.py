"""
Description: Tests whether a number is evenly divisible by single digits 
             using multiple algorithms

Input: String with only numbers

Output: Reports whether a number is evenly divisible by single digits

Author: Michael J. Findler
Date: 7 Feb 24
"""

# Input: Number
number_string = input("Please enter a string: ")
print(number_string)

####################################################
# Divisible by 2
# algorithm 1 last character is 0, 2, 4, 6, 8
last_char = number_string[-1]
print(last_char)
if(last_char in ("0", "2", "4", "6", "8")):
    print("evenly divisible by 2")
    div2 = True
else:
    print("NOT divisible by 2")
    div2 = False
    
# algorithm 2 last character is binary 0 (bit &)
last_int = int(last_char)
print(format(1, '08b'))
print(format(last_int, '08b'))

# bbb0 & 0001 --> 0001 (T) if odd and 0000 (F) if even 
#   so we "flip" the result 
#    (not(bbb0 & 0001)) --> 0001 (T) if odd and 0000 (F) if even
if(not(int(last_char) & 1)):  
    print("evenly divisible by 2")
else:
    print("NOT divisible by 2")
   

####################################################
# Divisible by 3
# algorithm 1 numbers sum to 0, 3, 6 or 9 
# -- Optimize by throwing away 0, 3, 6 and 9
#    123456789 --> 124578 
temp = number_string
while len(temp) != 1:
    sum = 0
    for char in temp:
        if(char in ("0", "3", "6", "9")):
            pass
        else:
            sum += int(char)
            print(char + " " + str(sum))
    
    temp = str(sum)
    print(temp)
    
if(sum in ( 0, 3, 6, 9 ) ):
    print("evenly divisible by 3")
    div3 = True
else:
    print("NOT divisible by 3")
    div3 = False
        

####################################################
# Divisible by 4
# algorithm 1 last character is 0, 2, 4, 6, 8; divide by 2; repeat
if(div2):
    temp_int = int(number_string) // 2   # integer division
    temp = str(temp_int)
    last_char = temp[-1]
    if(last_char in ("0", "2", "4", "6", "8")):
        print("evenly divisible by 4")
    else:
        print("NOT divisible by 4")


# algorithm 2 last character is binary 0 (bit &); bit shift by 1 (>>); last character is binary 0 (bit &)
if( div2 ):
    temp_int = int(number_string) >> 2
    temp = str(temp_int)
    last_char = temp[-1]
    if(int(last_char) & 14):
        print("evenly divisible by 4")
    else:
        print("NOT divisible by 4")

# algorithm 3 last TWO characters are binary 00 (bit &)
# not(number_string & 1100)

####################################################
# Divisible by 5
# algorithm 1 last character is "5" or "0"

####################################################
# Divisible by 6
# algorithm 1 last digit is even AND divides by 3 -- can we use existing code?
if (div2 and div3):
    print("evenly divisible by 6")
else:
    print("NOT divisible by 6")

####################################################
# Divisible by 8
# algorithm 1 last character is 0, 2, 4, 6, 8; divide by 2; repeat; divide by 2; repeat

# algorithm 2 last character is binary 0 (bit &); bit shift by 1 (>>); 
#             last character is binary 0 (bit &); bit shift by 1 (>>); 
#             last character is binary 0 (bit &)

# algorithm 3 last THREE characters are binary 000 (bit &)


####################################################
# Divisible by 9
# algorithm 1 Divisble by 3; divide by 3; repeat

# algorithm 2 numbers sum to 0 or 9 -- Optimize by throwing away 0 or 9
