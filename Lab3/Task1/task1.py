#!/usr/bin/python3

import sys

def read_data(filepath, l):
    sepal_length = []
    sepal_width = []
    petal_length = []
    petal_width = []
    rose_class = []
    with open(filepath, 'r') as f:
        for line in f:
            if '@DATA' in line:
                for line in f:  # now you are at the lines you want
                    string = line.strip().split(",")
                    sepal_length.append(float(string[0]))
                    sepal_width.append(float(string[1]))
                    petal_length.append(float(string[2]))
                    petal_width.append(float(string[3]))
                    rose_class.append(string[4])
    l.append(sepal_length)
    l.append(sepal_width)
    l.append(petal_length)
    l.append(petal_width)
    l.append(rose_class)

    f.close()

    return l


def process_numeric_field(process_list, x):
    min_value = 0
    max_value = 0
    x = x - 1

    min_value = min(process_list[x])

    max_value = max(process_list[x])

    average = sum(process_list[x]) / len(process_list[x])

    answer = str(round(average, 2))
    return (min_value,max_value,answer)


def count_iris_types(input):
    Iris_setosa = 0
    Iris_versicolor = 0
    Iris_virginica = 0

    for inp in input:
    	if inp == "Iris-setosa":
    		Iris_setosa+= 1
    	elif inp == "Iris-virginica":
    		Iris_virginica+= 1
    	elif inp == "Iris-versicolor":
    		Iris_versicolor+= 1
    return (Iris_setosa,Iris_versicolor,Iris_virginica)		

if len(sys.argv) < 2:
    print('usage: <filename>')
    exit()

filename = sys.argv[1]
a_list = []

my_list = read_data(filename, a_list)

r = 1
while r < 5:
    mini, maxi, avrg = process_numeric_field(my_list, r)
    print("Sepal Length: min={0}, max={1}, average={2}".format(str(mini), str(maxi), str(avrg)))
    r += 1

setosa ,versicolor ,virginica = count_iris_types(my_list[-1])
print("Iris Types: Iris Setosa=" + str(setosa) + ", Iris Versicolor=" + str(versicolor) + ", Iris Virginica=" + str(virginica))
