"""
Card Validator Program (Luhan's algorithm)
    After getting the user input : 
    # 1. Remove any '-' or ' '
    # 2. Add all the digits in the odd places from right to left
    # 3. Double every even places digits from right to left
                {if the 2 * digit == two-digit number then add the 2 digits to get a single digit}
    # 4. sum the totals of steps 2 & 3
    # 5. if the total sum % 10 == 0 then a valid card else notValid 
"""



sum_odd_digits = 0
sum_even_digits = 0
total = 0

# Step 1 : 
card_number = input("Enter Your card number #:")
# print(card_number[4 : 8])
card_number = card_number.replace("-", "")
card_number = card_number.replace(" ", "")
card_number = card_number[::-1]

# Step 2 :
for x in card_number[::2]:
    sum_odd_digits += int(x)
    
#  Step 3 : 
for x in card_number[1::2]:
    x = int(x) * 2
    if(x >= 10) :
        # 9 is the biggest single digit number so the biggest two-digit we get 18 so, 18 % 10 = 8 + 1 
        sum_even_digits += (1 + (x % 10))
    else :
        sum_even_digits += x    
        

#  Step 4 : 
total = sum_even_digits + sum_odd_digits

if(total % 10 == 0) :
    print("valid")
else :
    print("invalid")    
   
