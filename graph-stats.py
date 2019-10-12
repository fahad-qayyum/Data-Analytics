import argparse
import sys; 
from string import punctuation
from operator import itemgetter
import parser
import copy
import collections


def main():

    # contains the list of all the id's
    id_list = []

    # counts the edges
    edge_counter = 0
    counter = 0
    node_degree = 0

    # opening the file in read mode
    file = open(sys.argv[1] , "r")
    for line in file:
        for id in line.strip().split(" "):
            id_list.append(id)
        edge_counter += 1
    number_nodes = len(set(id_list))
    
    # part A print #nodes:|N|#edges:|E|    
    print("#nodes:", number_nodes, "#edges:", edge_counter)

    # for frequency distribution
    counter = collections.Counter(id_list)
    
    # part C print
    for item in sorted(counter, key=counter.get, reverse=True):
        node_degree += counter[item]
        print(item ,":", counter[item])
    avg = node_degree/number_nodes

    # part 4 print
    print("avgNodeDegree:", "%.2f" %avg)




if __name__ == "__main__":
    main()