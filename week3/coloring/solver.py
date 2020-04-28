#!/usr/bin/python
# -*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pyplot as plt
import collections


def solve_it(input_data):
    # parse the input
    lines = input_data.split('\n')

    first_line = lines[0].split()
    node_count = int(first_line[0])
    edge_count = int(first_line[1])

    # Initialize an empty graph
    G = nx.Graph()
    # Fill the graph
    for i in range(1, edge_count + 1):
        line = lines[i]
        parts = line.split()
        G.add_edge(int(parts[0]), int(parts[1]))

    # Coloring the graph

    d = nx.coloring.greedy_color(G, strategy='saturation_largest_first')

    # build a trivial solution
    # every node has its own color
    od = collections.OrderedDict(sorted(d.items()))
    solution = list(od.values())
    distinct_colors = len(set(d.values()))

    # prepare the solution in the specified output format
    output_data = str(distinct_colors) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, solution))

    return output_data


import sys

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/gc_4_1)')

