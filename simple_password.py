"""
Have the function SimplePassword(str) take the str parameter being passed and determine 
if it passes as a valid password that follows the list of constraints: 

1. It must have a capital letter.
2. It must contain at least one number.
3. It must contain a punctuation mark.
4. It cannot have the word "password" in the string.
5. It must be longer than 7 characters and shorter than 31 characters.

If all the above constraints are met within the string, the your program should return the string true, 
otherwise your program should return the string false. For example: if str is "apple!M7" then your program should return "true". 

Use the Parameter Testing feature in the box below to test your code with different arguments.
"""
import re

def SimplePassword(str): 
    upper = False
    number = False
    mark = False
    
    if 'password' in str.lower():
        return "false"
    if len(str) < 7 or len(str) > 31:
        return "false"

    for char in str:
        upper = upper if not char.isupper() else True
        number = number if not char.isdigit() else True
        mark = mark if not re.match(r'\W', char) else True
        
    return "true" if (upper and number and mark) else "false"


# keep this function call here  
print (SimplePassword(raw_input()))
