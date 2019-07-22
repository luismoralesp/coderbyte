"""
Have the function MatrixSpiral(strArr) read the array of strings stored in strArr which will represent a 2D N matrix, and your program should return the elements after printing them in a clockwise, spiral order. 
You should return the newly formed list of elements as a string with the numbers separated by commas. For example: if strArr is "[1, 2, 3]", "[4, 5, 6]", "[7, 8, 9]" then this looks like the following 2D matrix: 

1 2 3
4 5 6
7 8 9 

So your program should return the elements of this matrix in a clockwise, spiral order which is: 1,2,3,6,9,8,7,4,5 

Use the Parameter Testing feature in the box below to test your code with different arguments.
"""
import json

def MatrixSpiral(strArr):
    matrix = []
    result = ""

    for elm in strArr: 
        matrix.append(json.loads(elm))
    
    height = len(matrix)
    width = len(matrix[0])

    top = 0
    bottom = 0
    left = 0
    right = 0
    size = 0

    def append(result, size, elm):
        return result + ",%d" % elm if result != "" else str(elm), size + 1
    index = 1
    while size < width*height:
        if index == 1:
            for i in range(left, width - right):
                result, size = append(result, size, matrix[top][i])
            top += 1
        if index == 2:
            for i in range(top, height - bottom):
                result, size = append(result, size, matrix[i][-(bottom + 1)])
            right += 1
        if index == 3:  
            for i in range(left, width - right):
                result, size = append(result, size, matrix[-(bottom + 1)][-(i + right + 1) + left])
            bottom += 1
        if index == 4:
            for i in range(top, height - bottom):
                result, size = append(result, size, matrix[-(i + bottom + 1) + top][left])
            left += 1
        index = index + 1 if index < 4 else 1
    return result


# keep this function call here  
print (MatrixSpiral(raw_input()))