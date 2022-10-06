# // Constant
REGULAR_BOX_SIZE:   int = 8
SMALL_BOX_SIZE:     int = 3
STUDENTS:           int = 28

# // Get box amount inputs
regular_boxes: int = int(input())
small_boxes: int = int(input())

# // Calculate the amount of cupcakes in boxes
cupcakes: int = (3 * small_boxes) + (8 * regular_boxes)

# // Print result
print(cupcakes - STUDENTS)
