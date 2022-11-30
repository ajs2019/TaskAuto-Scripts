#!/usr/bin/python3

#Adam Stout
#4/5/2022


import os
import re

os.system('clear')
f = open("linux_users.csv", "r")
next(f)

print ("Adding new users to the system.\n" + 
       "Please note: the default password for new users is 'password'\n" +
       "For testing purposes. Change the password to '1$pizz@'.\n\n"
	 
)
for i in f:
    line = i.split(",")

    eid = line[0]
    last = line[1]
    first = line[2]
    office = line[3]
    phone = line[4]
    department = line[5]
    group = line[6]

    
#checks for empty fields in each record 
    if (
        len(eid) == 0
        or len(last) == 0
        or len(first) == 0
        or len(office) == 0
        or len(phone) == 0
        or len(department) == 0
        or len(group) == 0
    ):
        if group == 'pubsaftey' or group == 'office':
            print("Cannot process employee ID " + eid, end="\t")
            print("Insufficient data\n")
        else:
            print("Cannot process employee ID " + eid, end = '\t')
            print("Not a valid group\n")

            

    else:
        
        print("Processing employee ID " + eid, end="\t\t")

        # creates the uid and deletes special chars
        firstinit = first[0]
        uid = firstinit.lower() + last.lower()
        newuid = re.sub(r"[^a-zA-Z0-9]", "", uid)

	#check for duplicate users and appends a number 
        occurences = int(os.popen('grep -c ' + newuid + ' /etc/passwd').read())
        if occurences >= 1:
            newuid = newuid + str(occurences)
      
        # assigns a login shell based on group
        if group == "office":
            shell = "/bin/csh"
        else:
            shell = "/bin/bash"

        # adds the group if it doesnt already exist
        if (os.system('grep -q -E "^' + group + ':" /etc/group')) == 256:
            os.system("sudo groupadd " + group)

        # specifies the home directory and adds the parent directory
        homedir = "/home/" + department + "/" + newuid
        os.system("sudo mkdir -p /home/" + department)

        # adds the user, sets the password to 'password' and expires the password
        os.system(
            "sudo useradd -m -d " + homedir + " " + newuid + " -g " + group + " -s " + shell
        )
        os.system('sudo echo "' + newuid + ':password" |sudo chpasswd')
        os.system('sudo passwd -e ' + newuid + ' > /dev/null')
        print(newuid + " added to the system\n")
