

from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight','value_weight'])

input_data="4 11 \n 8 4 \n 10 5 \n 15 8 \n 4 3"


# parse the input
lines = input_data.split('\n')
firstLine = lines[0].split()
item_count = int(firstLine[0])
capacity = int(firstLine[1])


items = []

for i in range(1, item_count+1):
    line = lines[i]
    parts = line.split()
    items.append(Item(i - 1, int(parts[0]), int(parts[1]),float(int(parts[0])/int(parts[1]))))

items.sort(key=lambda x: x[3], reverse=True)
print(items)

# a trivial algorithm for filling the knapsack
# it takes items in-order until the knapsack is full
value = 0
weight = 0
taken = [0] * len(items)


for item in items:
    if weight + item.weight <= capacity:
        taken[item.index] = 1
        value += item.value
        weight += item.weight

# prepare the solution in the specified output format


output_data = str(value) + ' ' + str(0) + '\n'
output_data += ' '.join(map(str, taken))

print(output_data)