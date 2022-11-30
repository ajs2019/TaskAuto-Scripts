#!/usr/bin/python3

def filter(file , num):
    print('called filter function in filter_packets.py')
    filtered = "Node" + str(num) + "_filtered.txt"
    inputfile = open(file, 'r')
    filteredfile = open( filtered, 'w')
    data = inputfile.readlines()
	
    for line in data:
        if 'ICMP' in line:
            filteredfile.write(line)
    inputfile.close()
    filteredfile.close()


def filter_packets():
    filter("Node1.txt" , 1)
    filter("Node2.txt" , 2)
    filter("Node3.txt" , 3)
    filter("Node4.txt" , 4)
	

