import numpy as np

#     0:      1:      2:      3:      4:
#    aaaa    ....    aaaa    aaaa    ....
#   b    c  .    c  .    c  .    c  b    c
#   b    c  .    c  .    c  .    c  b    c
#    ....    ....    dddd    dddd    dddd
#   e    f  .    f  e    .  .    f  .    f
#   e    f  .    f  e    .  .    f  .    f
#    gggg    ....    gggg    gggg    ....

#     5:      6:      7:      8:      9:
#    aaaa    aaaa    aaaa    aaaa    aaaa
#   b    .  b    .  .    c  b    c  b    c
#   b    .  b    .  .    c  b    c  b    c
#    dddd    dddd    ....    dddd    dddd
#   .    f  e    f  .    f  e    f  .    f
#   .    f  e    f  .    f  e    f  .    f
#    gggg    gggg    ....    gggg    gggg

def decode(ft):
    ft.sort(key=len)
    zero = ""
    one = ft[0]
    two = ""
    three = ""
    four = ft[2]
    five = ""
    six = ""
    seven = ft[1]
    eight = ft[9]
    nine = ""

    t1 = set(eight) - set(four) - set(ft[3])
    t2 = set(eight) - set(four) - set(ft[4])
    t3 = set(eight) - set(ft[3]) - set(ft[4])
    t4 = set(eight) - set(ft[4]) - set(ft[5])
    
    if len(t1) == 0:
        two = ft[3]
        if len(t3) == 0:
            three = ft[5]
            five = ft[4]
        else:
            three = ft[4]
            five = ft[5]
    elif len(t2) == 0:
        two = ft[4]
        if len(t3) == 0:
            three = ft[5]
            five = ft[3]
        else:
            three = ft[3]
            five = ft[5]
    else:
        two = ft[5]
        if len(t4) == 0:
            three = ft[3]
            five = ft[4]
        else:
            three = ft[4]
            five = ft[3]

    t1 = set(eight) - set(one) - set(ft[6])
    if len(t1) == 0:
        six = ft[6]
        t1 = set(eight) - set(four) - set(ft[7])
        if len(t1) == 0:
            zero = ft[7]
            nine = ft[8]
        else:
            zero = ft[8]
            nine = ft[7]
    else:
        t1 -= set(four)
        if len(t1) == 0:
            zero = ft[6]
            t1 = set(eight) - set(one) - set(ft[7])
            if len(t1) == 0:
                six = ft[7]
                nine = ft[8]
            else:
                six = ft[8]
                nine = ft[7]
        else:
            nine = ft[6]
            t1 = set(eight) - set(one) - set(ft[7])
            if len(t1) == 0:
                six = ft[7]
                zero = ft[8]
            else:
                six = ft[8]
                zero = ft[7]
        
    #[1, 7, 4, (2,3,5), (2,3,5), (2,3,5), (0,6,9), (0,6,9), (0,6,9), 8]
    nums = [set(zero), set(one), set(two), set(three), set(four), 
        set(five), set(six), set(seven), set(eight), set(nine)]
    #print(nums)
    return nums

tries = []
outputs = []
with open("data\d8e2.txt") as file:
    for i, line in enumerate(file):
        split_line = line.replace("\n", "").split(" | ")
        tries.append(split_line[0].split(" "))
        outputs.append(split_line[1].split(" "))

#print(tries, outputs)

numbers = []
for out in outputs:
    display = ""
    for num in out:
        if len(num) == 2:
            display += "1"
        elif len(num) == 4:
            display += "4"
        elif len(num) == 3:
            display += "7"
        elif len(num) == 7:
            display += "8"
    numbers.append(display)

final = []
for test, out in zip(tries, outputs):
    code = decode(test)
    number = ""
    for o in out:
        num = code.index(set(o))
        number += "{}".format(num)
    #print(number)
    final.append((int)(number))

print("~~~~~~~ Part 1 ~~~~~~~")
print(len("".join(numbers)))

print("~~~~~~~ Part 2 ~~~~~~~")
print(np.sum(final))