
p1_horizontal = 0
p1_depth = 0

aim = 0
p2_horizontal = 0
p2_depth = 0

val = 0
with open("data\d2e2.txt") as file:
    for i, line in enumerate(file):
        input = line.split(" ")
        try:
            val = (int)(input[1])
        except Exception as e:
            print(e)
        
        if input[0].__contains__("forward"):
            p1_horizontal += val
            p2_horizontal += val
            p2_depth += (aim * val)
        elif input[0].__contains__("up"):
            p1_depth -= val
            aim -= val
        elif input[0].__contains__("down"):
            p1_depth += val
            aim += val

print("~~~~~~~ Part 1 ~~~~~~~")
print("Horizontal: {0}".format(p1_horizontal))
print("Depth: {0}".format(p1_depth))
print("Multiplied: {0}".format((p1_horizontal * p1_depth)))

print("\n~~~~~~~ Part 2 ~~~~~~~")
print("Horizontal: {0}".format(p2_horizontal))
print("Depth: {0}".format(p2_depth))
print("Multiplied: {0}".format((p2_horizontal * p2_depth)))