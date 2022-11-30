#!/usr/bin/python3
def compute(ip,L,fname) :
	print('called compute function in compute_metrics.py')

	
	return(compute_metric(ip,L,fname))

#grabs a number from a string
def get_num(string):
	

    return int(''.join(num for num in string if num.isdigit()))

def compute_metric(ip,L,fname):
	avg_reply_delay=0
	request_throughput=0
	request_goodput=0
	org_hop=129
	request_sent_count=0
	request_rcvd_count=0
	bytes_sent=0
	bytes_rcvd=0
	data_sent=0
	data_rcvd=0
	count_1=0
	reply_sent_count=0
	total_time_1=0
	count_2=0
	reply_rcvd_count=0
	total_time_2=0
	avg_rtt=0
	
	hop_count=0
	request_count=0
	
        

	for i in L :
		if i[8] == "reply" :
			if i[2] == ip :
				reply_sent_count += 1 

		
			elif i[3] == ip :
				reply_rcvd_count += 1 

		if i[8] == "request" :
			if i[2] == ip :
				request_sent_count += 1 
				bytes_sent += int(i[5]) 
				data_sent += int(i[5]) - 42 
		
			elif i[3] == ip :
				request_rcvd_count += 1 
				bytes_rcvd += int(i[5]) 
				data_rcvd += int(i[5]) - 42 


	
	for i in range(0,len(L)):
		if L[i][8] == "request" :
			if L[i][2] == ip :
				count_1 += 1
				total_time_1 += (float(L[i+1][1]))-(float(L[i][1]))

	
	for i in range(0,len(L)):
		if L[i][8] == "request" :
			if L[i][3] == ip :
				count_2 += 1
				total_time_2 += (float(L[i+1][1]))-(float(L[i][1]))			
	
	
	for i in range(0,len(L)):
		if L[i][8] == "reply" :
			if L[i][3] == ip :
				hop_count += (org_hop - get_num(L[i][11]))
				

	
	avg_rtt = (total_time_1 / count_1)*1000 
	request_throughput = (bytes_sent / total_time_1)/1000 
	request_goodput = (data_sent / total_time_1)/1000 
	avg_reply_delay = (total_time_2/count_2) * 1000000 
	avg_hop = float(hop_count)/float(request_sent_count) 

	
	return(request_sent_count,request_rcvd_count,reply_sent_count,reply_rcvd_count,round(bytes_sent,2),round(data_sent,2),round(bytes_rcvd,2),round(data_rcvd,2),round(avg_rtt,2),\
		round(request_throughput,2),round(request_goodput,2),round(avg_reply_delay,2,),round(avg_hop,2))
