import numpy as np

WINDOW = 3
values = []

with open("data\d1e1.txt") as file:
    for i, line in enumerate(file):
        try:
            current_val = (int)(line)
        except Exception as e:
            print(e)
        values.append(current_val)


increased = 0
sum_increased = 0

prev_val = values[0]
prev_sum_value = np.sum(values[0:WINDOW])
#print(prev_sum_value)
for i, val in enumerate(values):
    if i != 0:
        if val > prev_val:
            increased += 1
        prev_val = val
    
    w=i+1
    if i >= WINDOW:
        current = np.sum(values[w-WINDOW:w])
        #print(current)
        if current > prev_sum_value:
            sum_increased += 1
        prev_sum_value = current

print("Normal increased: {0}".format(increased))
print("Sum increased: {0}".format(sum_increased))