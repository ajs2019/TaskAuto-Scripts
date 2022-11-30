#! /usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np


def process_lvl_metrics():
	time_apm=[]
	apm1 = []
	cpu_apm1 = []
	mem_apm1 = []
	read_data("APM1_metrics.csv",apm1,cpu_apm1,mem_apm1)
	
	for data in apm1:
		time_apm.append(int(data[0]))

	
	apm2 = []
	cpu_apm2 = []
	mem_apm2 = []
	read_data("APM2_metrics.csv",apm2,cpu_apm2,mem_apm2)
	

	apm3 = []
	cpu_apm3 = []
	mem_apm3 = []
	read_data("APM3_metrics.csv",apm3,cpu_apm3,mem_apm3)

	cpu_apm4 = []
	mem_apm4 = []
	apm4 = []
	read_data("APM4_metrics.csv",apm4,cpu_apm4,mem_apm4)

	cpu_apm5 = []
	mem_apm5 = []
	apm5 = []
	read_data("APM5_metrics.csv",apm5,cpu_apm5,mem_apm5)

	apm6 = []
	cpu_apm6 = []
	mem_apm6 = []
	read_data("APM6_metrics.csv",apm6,cpu_apm6,mem_apm6)

	plot(time_apm,cpu_apm1,cpu_apm2,cpu_apm3,cpu_apm4,cpu_apm5,cpu_apm6,"CPU(%)")
	plot(time_apm,mem_apm1,mem_apm2,mem_apm3,mem_apm4,mem_apm5,mem_apm6,"MEM(%)")




def read_data(filename, L,cpu,mem):
	file = open(filename,"r")
	
	lines = file.readlines()


	for line in lines:

		L.append(line.strip().split(","))

	file.close()
	
	for data in L:
		cpu.append(float(data[1]))
		mem.append(float(data[2]))

def plot(x,y1,y2,y3,y4,y5,y6,y_label):
	plt.plot(x,y1,color='blue',label='APM1')
	plt.plot(x,y2,color='black',label='APM2')
	plt.plot(x,y3,color='red',label='APM3')
	plt.plot(x,y4,color='green',label='APM4')
	plt.plot(x,y5,color='yellow',label='APM5')
	plt.plot(x,y6,color='cyan',label='APM6')
	plt.ylim(ymax = 100, ymin = -1)
	plt.xlim(xmax = 900, xmin = 0)
	plt.legend(loc='upper right')
	plt.ylabel(y_label)
	plt.xlabel('Time (seconds)')

	if y_label == "CPU(%)":
		plt.title('CPU Utilization over time')
		plt.savefig('cpu.png')
		plt.close()
	elif y_label == "MEM(%)":

		plt.title('Memory Utilization over time')
		plt.savefig('memory.png')
		plt.close()



def system_lvl_metrics() :
	time=[]
	rx=[]
	tx=[]
	writes=[]
	capacity=[]
	read_system_data("system_metrics.csv",time,rx,tx,writes,capacity)
		
	plot_2(time,rx,tx,"Data Rate (kB/sec)")
	plot_1(time,writes,"Disk Writes (kB/s)","Disk Writes")
	plot_1(time,capacity,"Disk Capacity (MB)","Disk Capacity")

def read_system_data (filename,s,r,t,w,c) :
	L =[]
	file = open(filename,"r")
	
	lines = file.readlines()

	for line in lines:

		L.append(line.strip().split(","))

	file.close()

	for data in L:
		s.append(int(data[0]))
		r.append(int(data[1]))
		t.append(int(data[2]))
		w.append(float(data[3]))
		c.append(int(data[4]))

def plot_1(x,y,y_label,l) :
	plt.plot(x,y,color = 'blue',label=l)
	plt.ylabel(y_label)
	plt.xlabel('Time (seconds)')
	plt.xlim(xmax = 900, xmin = 0)
	plt.legend(loc='lower center')

	if y_label == "Disk Writes (kB/s)":

		plt.title('Hard Disk Access Rates over Time')
		plt.ylim(ymax = 13000, ymin = 5000)
		plt.savefig('disk_access.png')
		plt.close()

	elif y_label == "Disk Capacity (MB)":

		plt.title('Hard Disk Utilization over Time')
		plt.ylim(ymax = 50000, ymin = 0)
		plt.savefig('disk_util.png')
		plt.close()	



def plot_2(x,y1,y2,y_label) :
	plt.plot(x,y1,color='blue',label='RX Data Rate')
	plt.plot(x,y2,color='red',label='TX Data Rate')
	plt.ylim(ymax = 100, ymin = 0)
	plt.xlim(xmax = 900, xmin = 0)
	plt.legend(loc='upper right')
	plt.ylabel(y_label)
	plt.xlabel('Time (seconds)')
	plt.title('Network Bandwidth Utilization over Time')
	plt.savefig('bandwidth.png')
	plt.close()	


def main():
	process_lvl_metrics()
	system_lvl_metrics()



main()	
