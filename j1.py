# // Constant
REGULAR_BOX_SIZE:   int = 8
SMALL_BOX_SIZE:     int = 3
STUDENTS:           int = 28

# // Get box amount inputs
regular_boxes: int = int(input())
small_boxes: int = int(input())

# // Calculate the amount of cupcakes in boxes
cupcakes: int = \
    (SMALL_BOX_SIZE * small_boxes) + (REGULAR_BOX_SIZE * regular_boxes)

# // Print result
print(cupcakes-STUDENTS)