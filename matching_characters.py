"""
Have the function MatchingCharacters(str) take the str parameter being passed 
and determine the largest number of unique characters that exists between a pair of matching 
letters anywhere in the string. For example: if str is "ahyjakh" then there are only two pairs of matching letters, 
the two a's and the two h's. Between the pair of a's there are 3 unique characters: h, y, and j. Between the h's there are 4 unique characters: 
y, j, a, and k. So for this example your program should return 4. 

Another example: if str is "ghececgkaem" then your program should return 5 because the most unique characters exists within the farthest pair of e characters. 
The input string may not contain any character pairs, and in that case your program should just return 0. The input will only consist of lowercase alphabetic characters. 

Use the Parameter Testing feature in the box below to test your code with different arguments.
"""

import re
from collections import Counter

def MatchingCharacters(str):
    def get_max_match(str, max_match=0):
        if len(str) == 0:
            return max_match
        for char in str:
            exp = re.search(r"%s(\w*)%s" % (char, char), str)
            if exp:
                match = exp.group(1)
                new_max_match = len(Counter(match).keys())
                if new_max_match > max_match:
                    return get_max_match(str[1:], new_max_match)
        return max_match
    return get_max_match(str)


# keep this function call here  
print (MatchingCharacters(raw_input()))