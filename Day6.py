import numpy as np

def run_cycle(today, days):
    #print(today)
    birthed_today = 0
    for i in range(1, days+1):
        birthed_today = today[0]
        today = np.roll(today, -1)
        today[6] += birthed_today
    print("Day", days, '-', (np.sum(today)), "fish")


fish = np.zeros(9)

with open("data\d6e2.txt") as file:
    for i, line in enumerate(file):
        split_line = line.replace("\n", "").split(',')
        for item in split_line:
            if len(item) > 0:
                try:
                    fish[(int)(item)] += 1
                except Exception as e:
                    print(e)

run_cycle(fish, 80)
run_cycle(fish, 256)
