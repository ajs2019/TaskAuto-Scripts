#!/usr/bin/python3
import sys
import os
import hashlib


def main():
    if len(sys.argv) < 3:
        print("Required arguments: <New MD5 File> <Old MD5 File>")
        exit(0)

    md5newer = sys.argv[1]
    md5orig = sys.argv[2]

    md5origlist = []
    with open(md5orig) as f:
            for l in f:
			line = l.strip().split(" ")
			md5origlist.append(line)

    md5new = []
    with open(md5newer) as f:
		for l in f:
			line = l.strip().split(" ")
			md5new.append(line)

    for ele in md5origlist:
        for md5 in md5new:
			if ele[0] == md5[0]:
				if ele[1] == md5[1]:
					continue
				else:
					print(str(ele[0]) + ": MD5 original = " + md5[1] + ", new MD5 = " + ele[1])
				break

				

if __name__ == "__main__":
    main()
