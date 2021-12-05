import numpy as np

def get_coordinates(line):
    line = line.replace(" -> ", ',').replace("\n", '')
    x1, y1, x2, y2 = line.split(',')
    try:
        x1 = (int)(x1)
        x2 = (int)(x2)
        y1 = (int)(y1)
        y2 = (int)(y2)
    except Exception as e:
        print(e)

    coordinates = []
    point = [x1, y1]
    coordinates.append(point)
    point = [x2, y2]
    coordinates.append(point)

    return coordinates

coordinates_set = []

with open("data\d5e2.txt") as file:
    for i, line in enumerate(file):
        coordinates_set.append(get_coordinates(line))

max_coor = np.max(coordinates_set)
grid_1 = np.zeros([max_coor+1, max_coor+1])
grid_2 = np.zeros([max_coor+1, max_coor+1])

#print(grid)

for [x1, y1], [x2, y2] in coordinates_set:
    if x1 == x2:
        y1, y2 = np.sort([y1, y2])
        grid_1[y1:y2+1, x1:x2+1] += 1
        grid_2[y1:y2+1, x1:x2+1] += 1
    elif y1 == y2:
        x1, x2 = np.sort([x1, x2])
        grid_1[y1:y2+1, x1:x2+1] += 1
        grid_2[y1:y2+1, x1:x2+1] += 1
    else:
        x_list = list(range(x1, x2, 1 if x1<x2 else -1))
        y_list = list(range(y1, y2, 1 if y1<y2 else -1))
        for x, y in zip(x_list, y_list):
            grid_2[y, x] += 1
        grid_2[y2, x2] += 1

        


#print(grid_2)

grid_1[np.where(grid_1 == 1 )] = 0
grid_2[np.where(grid_2 == 1 )] = 0

print(np.count_nonzero(grid_1))
print(np.count_nonzero(grid_2))
