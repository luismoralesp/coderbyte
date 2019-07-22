"""
Have the function PlusMinus(num) read the num parameter being passed which will be a combination of 1 or more single digits,
 and determine if it's possible to separate the digits with either a plus or minus sign to get the final expression to equal zero. 
 For example: if num is 35132 then it's possible to separate the digits the following way, 3 - 5 + 1 + 3 - 2, and this expression equals zero. 
 Your program should return a string of the signs you used, so for this example your program should return -++-. If it's not possible to get the digit expression to equal zero, 
 return the string not possible. 

Use the Parameter Testing feature in the box below to test your code with different arguments.
"""
def PlusMinus(num): 
    str_num = str(num)
    def iter(str_num, sign = 1, sum = 0, signs=""):
        
        digit = int(str_num[0])
        sum = sum + digit*sign
        
        if len(str_num[1:]) == 0:
            print (signs)
            return signs if sum == 0 else False

        re2 = iter(str_num[1:], -1, sum, signs + '-')
        if re2:
            return re2

        re1 = iter(str_num[1:], 1, sum, signs + '+')
        if re1:
            return re1

            
    return iter(str_num) or "not possible"


# keep this function call here  
print (PlusMinus(raw_input()))  
