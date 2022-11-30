#!/usr/bin/python3

def parse(file_name, L) :
    print('called parse function in packet_parser.py')
    file_parsing(file_name, L)

def file_parsing(fname, L):
    f = open(fname, 'r')
    lines = f.readlines()

    for line in lines:
        L.append(line.strip().split())
    
    f.close()
	
