#!/usr/bin/python
from filter_packets import *
from packet_parser import *
from compute_metrics import *
def write_data(ip,L,fname,node):
	(a,b,c,d,e,f,g,h,i,j,k,l,m) = compute(ip,L,fname)
	file.write(node)
	file.write(x)
	file.write("Echo Requests Sent,Echo Requests Received,Echo Replies Sent,Echo Replies Received" + x)
	file.write(str(a) + ',' + str(b) + ',' + str(c) + ',' + str(d) + x)
	file.write("Echo Request Bytes sent (bytes)" + "," + "Echo Request Data Sent (bytes)"+ x)
	file.write(str(e)+","+str(f)+x)
	file.write("Echo Request Bytes Recieved (bytes)" + "," + "Echo Request Data Recieved (bytes)"+x)
	file.write(str(g)+","+str(h)+x)
	file.write(x)
	file.write("Average RTT (miliseconds)" + "," + str(i) + x)
	file.write("Echo Request Throughput (kB/sec)" + "," + str(j) + x)
	file.write("Echo Request Goodput (kB/sec)" + "," + str(k) + x)
	file.write("Average Reply Delay (microseconds)" + "," + str(l) + x)
	file.write("Average Echo Request Hop Count" + "," + str(m) + x)
	file.write(x)
	

	
L1 = []
L2 = []
L3 = []
L4 = []
x ='\n'



filename = "project2_output.csv"
file = open(filename, 'a')
file.truncate(0)

filter_packets()


parse("Node1_filtered.txt",L1)
parse("Node2_filtered.txt",L2)
parse("Node3_filtered.txt",L3)
parse("Node4_filtered.txt",L4)




write_data("192.168.100.1",L1,"Node1_filtered.txt","Node1")
write_data("192.168.100.2",L2,"Node2_filtered.txt","Node2")
write_data("192.168.200.1",L3,"Node3_filtered.txt","Node3")
write_data("192.168.200.2",L4,"Node4_filtered.txt","Node4")

file.close()
