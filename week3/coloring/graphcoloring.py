#!/usr/bin/python
# -*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pyplot as plt


input_data = "4 3 \n 0 1 \n 1 2 \n 1 3"
print(input_data)

def CreateGraph():
    """takes input from the file and creates a undirected graph"""

    # parse the input
    lines = input_data.split('\n')

    first_line = lines[0].split()
    node_count = int(first_line[0])
    edge_count = int(first_line[1])

    # Initialize an empty graph
	G = nx.Graph()
    for i in range(1, edge_count + 1):
        line = lines[i]
        parts = line.split()
	    G.add_edge(int(parts[0]), int(parts[1]))
	    return G



#implementation of welsh_powell algorithm
def welsh_powell(G):
	#sorting the nodes based on it's valency
	node_list = sorted(G.nodes(), key =lambda x: list(G.neighbors(x)))
	col_val = {} #dictionary to store the colors assigned to each node
	col_val[node_list[0]] = 0 #assign the first color to the first node
	# Assign colors to remaining N-1 nodes
	for node in node_list[1:]:
		available = [True] * len(G.nodes()) #boolean list[i] contains false if the node color 'i' is not available

		#iterates through all the adjacent nodes and marks it's color as unavailable, if it's color has been set already
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
	return col_val




#draws the graph and displays the weights on the edges
def DrawGraph(G,col_val):
	pos = nx.spring_layout(G)
	values = [col_val.get(node, 'blue') for node in G.nodes()]
	nx.draw(G,
            pos,
            with_labels = True,
            node_color = values,
            edge_color = 'black' ,
            width = 1,
            alpha = 0.7)  #with_labels=true is to show the node number in the output graph




#main function
if __name__ == "__main__":
	G = CreateGraph()
	col_val = welsh_powell(G)
	DrawGraph(G,col_val)
	plt.show()