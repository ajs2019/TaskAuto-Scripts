#!/bin/bash

#starts each executable with IP argument
spawn () {
	ip=$(ifconfig ens192 | grep "inet" | head -1 | awk '{print $2}')
	./APM1 $ip &
	./APM2 $ip &
	./APM3 $ip &
	./APM4 $ip &
	./APM5 $ip &
	./APM6 $ip &
	
	

}
#kills each process
cleanup() {
	pkill APM1
	pkill APM2
	pkill APM3
	pkill APM4
	pkill APM5
	pkill APM6

}

collect_process_metrics () {
	#stores (CPU, MEM) using ps   
	procmetric=$(ps -C $1 -o %cpu,%mem | tail -1 | awk 'OFS="," {print $1,$2}')
	
	if [ $(( $duration % 5 )) -eq 0 ];
	then
		echo "$duration,$procmetric" >> $1_metrics.csv
	fi

}
collect_system_metrics () {
	#stores ifstat (RX Data Rate, TX Data Rate) 
	# rxtx=$(ifstat | grep ens192 | awk '{print $6,$8}' | sed 's/K//g')

	# in class now he said 7 and 9 for the rx and tx data rates
	rx=$(ifstat | grep ens192 | awk '{print $7}' | sed 's/K//g')
	tx=$(ifstat | grep ens192 | awk '{print $9}' | sed 's/K//g')

	# spereate network file made for data 

	echo "$duration,$rx,$tx" >> network_metrics.csv
	
	#stores iostat disk writes
	 hddwrite=$(iostat | grep sda | awk '{print $4}')
	
	#stores disk capacity using df
	disk_utilization=$(df -h -m /dev/mapper/centos-root | awk '{print $4}' | tail -1)

	if [ $(( $duration % 5 )) -eq 0 ];
	then
		echo "$duration,$hddwrite,$disk_utilization" >> system_metrics.csv
	fi
 
}

spawn
duration=0

while true ; do

	if [ $duration -ge 901 ]; then
		cleanup
		break
	fi
	
	collect_process_metrics APM1
	collect_process_metrics APM2
	collect_process_metrics APM3
	collect_process_metrics APM4
	collect_process_metrics APM5
	collect_process_metrics APM6
	collect_system_metrics
	
	echo $duration

	# going to change file writes based on timing for the intervals
	# going to collect every second but only write every 5 for the specifc ones
	sleep 1;
	duration=$(($duration + 1))
	

done
trap cleanup EXIT

