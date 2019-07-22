"""
Have the function CharlietheDog(strArr) read the array of strings stored in strArr which 
will be a 4x4 matrix of the characters 'C', 'H', 'F', 'O', where C represents Charlie the dog,
 H represents its home, F represents dog food, and O represents and empty space in the grid. 
 Your goal is to figure out the least amount of moves required to get Charlie to grab each piece of food in the grid by moving
  up, down, left, or right, and then make it home right after. 
  Charlie cannot move onto the home before all pieces of food have been collected. 
  For example: if strArr is ["FOOF", "OCOO", "OOOH", "FOOO"], then this looks like the following grid: 
   
    F O O F
    O C O O
    O O O H
    F O O O 

For the input above, the least amount of steps where the dog can reach each piece of food, 
and then return home is 11 steps, so your program should return the number 11. 
The grid will always contain between 1 and 8 pieces of food. 

Use the Parameter Testing feature in the box below to test your code with different arguments.
"""

from itertools import permutations 

def CharlietheDog(strArr):
    def walk(food_home, dog, matriz, steps=0):

        food_home_dx = food_home[0][0] - dog[0]
        food_home_dy = food_home[0][1] - dog[1]

        walk_x = food_home_dx/(abs(food_home_dx) if food_home_dx != 0 else 1)
        walk_y = food_home_dy/(abs(food_home_dy) if food_home_dy != 0 else 1)

        steps += abs(walk_x) + abs(walk_y)

        dog = (dog[0] + walk_x, dog[1] + walk_y)

        if food_home[0] == dog:
            food_home = food_home[1:]

        food_home_size = len(food_home)
        if food_home_size <= 0:
            return steps
        
        return walk(food_home, dog, matriz, steps)

    food = []
    home = None
    dog  = None

    for i in range(len(strArr)):
        for j in range(len(strArr[i])):
            if strArr[i][j] == 'F':
                food.append((i, j))
            if strArr[i][j] == 'H':
                home = (i, j)
            if strArr[i][j] == 'C':
                dog = (i, j)

    foods = permutations(food)

    min_steps = None
    for food in foods:
        food_home = food + (home, )
        steps = walk(food_home, dog, strArr)
        if min_steps == None or steps < min_steps:
            min_steps = steps

    return int(min_steps)


# keep this function call here  
print (CharlietheDog(raw_input()))  
