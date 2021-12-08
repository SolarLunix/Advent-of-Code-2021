import numpy as np

positions = []

with open("data\d7e2.txt") as file:
    for i, line in enumerate(file):
        split_line = line.replace("\n", "").split(',')
        for item in split_line:
            if len(item) > 0:
                try:
                    positions.append((int)(item))
                except Exception as e:
                    print(e)

positions = np.array(positions)
pos_max = np.max(positions)

movement = np.zeros(pos_max+1)
movement_2 = np.zeros(pos_max+1)

for i in range(pos_max+1):
    movement[i] = np.sum(np.abs(positions - i))

    distance = np.abs(positions - i)
    move = np.multiply(distance, (distance + 1)) /2
    movement_2[i] = np.sum(move)



print(movement)
print(np.min(movement))

print(movement_2)
print(np.min(movement_2))