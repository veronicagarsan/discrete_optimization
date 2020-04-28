
import networkx as nx
import matplotlib.pyplot as plt
import collections


input_data = '20 63\n0 4\n0 13\n1 2\n1 3\n1 6\n1 18\n1 19\n2 3\n2 5\n2 8\n2 10\n2 11\n2 15\n2 16\n2 18\n3 7\n3 8\n3 13\n3 15\n3 19\n4 6\n4 9\n4 10\n4 11\n4 12\n4 14\n4 15\n4 18\n5 6\n5 7\n5 9\n5 10\n5 11\n6 11\n6 13\n6 14\n6 16\n6 17\n7 9\n8 11\n8 13\n8 18\n9 10\n9 11\n9 12\n9 13\n9 14\n9 17\n10 11\n10 12\n10 14\n10 15\n10 17\n10 19\n11 13\n11 19\n12 18\n13 15\n13 18\n15 18\n15 19\n16 19\n18 19\n'

print(input_data)


lines = input_data.split('\n')

first_line = lines[0].split()
node_count = int(first_line[0])
edge_count = int(first_line[1])

# Initialize an empty graph
G = nx.Graph()
# Fill the graph
for i in range(1,edge_count+1):
    line = lines[i]
    parts = line.split()
    G.add_edge(int(parts[0]), int(parts[1]))

for i in range(node_count):
    print(str(i),len(list(G.neighbors(i))))

# Coloring the graph
# sorting the nodes based on it's valency
node_list = sorted(G.nodes(),key= lambda x: len(list(G.neighbors(x))),reverse=True)
col_val = {}  # dictionary to store the colors assigned to each node
col_val[node_list[0]] = 0  # assign the first color to the first node
# Assign colors to remaining N-1 nodes
for node in node_list[1:]:
    available = [True] * len(G.nodes())  # boolean list[i] contains false if the node color 'i' is not available

    # iterates through all the adjacent nodes and marks it's color as unavailable, if it's color has been set already
    for adj_node in G.neighbors(node):
        if adj_node in col_val.keys():
            col = col_val[adj_node]
            available[col] = False
    clr = 0
    for clr in range(len(available)):
        if available[clr] == True:
            break
    col_val[node] = clr
print(col_val)


pos = nx.spring_layout(G)
values = [col_val.get(node, 'blue') for node in G.nodes()]
nx.draw(G,
        pos,
        with_labels = True,
        node_color = values,
        edge_color = 'black' ,
        width = 1,
        alpha = 0.7)  #with_labels=true is to show the node number in the output graph
plt.show()

# build a trivial solution
# every node has its own color
od = collections.OrderedDict(sorted(col_val.items()))
solution = list(od.values())
distinct_colors = len(set(col_val.values()))

# prepare the solution in the specified output format
output_data = str(distinct_colors) + ' ' + str(1) + '\n'
output_data += ' '.join(map(str, solution))

print(output_data)

