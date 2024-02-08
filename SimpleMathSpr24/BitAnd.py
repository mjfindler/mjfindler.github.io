# Input: Number
number_string = input("Please enter a string: ")
print(number_string)

# algorithm 2 last character is binary 0 (bit &)
last_char = number_string[-1]
print(last_char)

last_int = int(last_char)
print(format(1, '08b'))
print(format(last_int, '08b'))
print(format(last_int & 1, '08b'))
print(format(last_int | 1, '08b'))
print(format(not(last_int & 1), '08b'))
print(format(last_int | 1, '08b'))
print(hex(last_int))
print(bin(last_int))

# bbb0 & 0001 --> 0001 (T) if odd and 0000 (F) if even 
#   so we "flip" the result 
#    (not(bbb0 & 0001)) 
#      --> 0001 (T) if odd     and     0000 (F) if even
#      --> not(0001) --> 0000 (F)  not(0000) --> 0001 (T)
if(not(int(last_char) & 1)):  
    print("evenly divisible by 2")
else:
    print("NOT divisible by 2")
