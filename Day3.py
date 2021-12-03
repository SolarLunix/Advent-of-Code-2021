import numpy as np

def reduce_list_o2(list, i):
    unique, count = np.unique(list[:,i], return_counts=True)
    if len(count) > 1:
        if count[0] > count [1]:
            new_list = list[np.where(list[:,i] == unique[0])]
        elif count[0] == count[1]:
            new_list = list[np.where(list[:,i] == '1')]
        else:
            new_list = list[np.where(list[:,i] == unique[1])]
        return new_list
    return list[:]

def reduce_list_co2(list, i):
    unique, count = np.unique(list[:,i], return_counts=True)
    if len(count) > 1:
        if count[0] > count [1]:
            new_list = list[np.where(list[:,i] == unique[1])]
        elif count[0] == count[1]:
            new_list = list[np.where(list[:,i] == '0')]
        else:
            new_list = list[np.where(list[:,i] == unique[0])]
        return new_list
    return list[:]

data = []

with open("data\d3e2.txt") as file:
    for line in file:
        cropped = line.replace('\n', '')
        data.append(list(cropped))

data = np.array(data)
m_gamma = ''
m_epsilon = ''

o2 = np.copy(data)
co2 = np.copy(data)


for i in range(0, data.shape[1]):
    unique, count = np.unique(data[:,i], return_counts=True)
    print(unique, count)
    if(count[0] > count[1]):
        m_gamma += unique[0]
        m_epsilon += unique[1]
    else:
        m_gamma += unique[1]
        m_epsilon += unique[0]

    o2 = reduce_list_o2(o2, i)
    co2 = reduce_list_co2(co2, i)

d_gamma = int(m_gamma, 2)
d_epsilon = int(m_epsilon, 2)
power = d_gamma * d_epsilon

s_o2 = ''.join(o2[0])
s_co2 = ''.join(co2[0])

d_o2 = int(s_o2, 2)
d_co2 = int(s_co2, 2)
life_support = d_o2 * d_co2

print("~~~~~~~ Part 1 ~~~~~~~")
print("Gamma: ", d_gamma)
print("Epsilon: ", d_epsilon)
print("Power: ", power)

print("~~~~~~~ Part 2 ~~~~~~~")
print("O2: ", d_o2)
print("CO2: ", d_co2)
print("Life support: ", life_support)