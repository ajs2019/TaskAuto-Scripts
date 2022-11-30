#! /bin/bash

num_writer() {
	if [ $# -eq 0 ]; then
		echo "No argument(s): <num_rands> <min> <max>"
	elif [ $# -eq 1 ]; then
		shuf -i 1-32767 -n $num_rands > rands_$num_rands.txt
		smallNum=$(cat rands_$num_rands.txt | sort -n | head -n 1)
		largeNum=$(cat rands_$num_rands.txt | sort -n | tail -n 1)
		echo "You requested $num_rands number(s)"
		echo "The smallest value generated was $smallNum"
		echo "The largest value generated was $largeNum"
		total=0;
		while read line; do
			total=$(($total + $line))
		done < rands_$num_rands.txt
		average=$(($total / $num_rands))
		echo "The average value generated was $average"
	elif [ $# -eq 2 ]; then
		echo "You must have a minimum AND maximum in your range" 

	elif [ $# -eq 3 ]; then
		shuf -i $min-$max -n $num_rands > rands_$num_rands.txt
		smallNum=$(cat rands_$num_rands.txt | sort -n | head -n 1)
		largeNum=$(cat rands_$num_rands.txt | sort -n | tail -n 1)
		echo "You requested $num_rands numbers between $min and $max"
		echo "The smallest value generated was $smallNum"
		echo "The largest value generated was $largeNum"
		total=0;
		while read line; do
			total=$(($total + $line))
		done < rands_$num_rands.txt
		average=$(($total / $num_rands))
		echo "The average value generated was $average"
	fi
}	



num_rands=$1
min=$2
max=$3

num_writer $num_rands $min $max
