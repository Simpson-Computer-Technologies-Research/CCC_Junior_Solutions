# // Define Variables
violations: int = 0
must_be_same_group: list[str] = []
must_not_be_same_group: list[str] = []

# // Append the students that must be in the same group
x: int = int(input())
for _ in range(x):
    must_be_same_group.append(input())

# // Append the students that must not be in a same group
y: int = int(input())
for _ in range(y):
    must_not_be_same_group.append(input())


# // Must be same group array check
def must_be_same_group_check(p: list[str], group: str):
    return (p[0] in group and p[1] not in group) or \
        (p[1] in group and p[0] not in group)

# // Number of groups
g: int = int(input())
for _ in range(g):
    group: str = input()

    # // Check if the must be in same group students
    # // are in the provided group
    for i, s in enumerate(must_be_same_group):
        p = s.split(" ")

        # // If, increase violations and remove
        # // the students from their corresponding array
        if must_be_same_group_check(p, group):
            must_be_same_group.pop(i)
            violations+=1
            
    # // Check if the must not be in same group
    # // students are in the provided group
    for i, s in enumerate(must_not_be_same_group):
        p = s.split(" ")

        if p[0] in group and p[1] in group:
            must_not_be_same_group.pop(i)
            violations += 1

# // Print the amount of violations
print(violations)
