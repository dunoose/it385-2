#!/usr/bin/env python3
#
# THIS FILE SHOWS HOW TO USE PARAMIKO'S exec_command()
#  TO RUN COMMANDS ON REMOTE CISCO DEVICE
#
import paramiko
# getpass modeule hides password as you type in
from getpass import getpass

# Get Remote node's login info
csr_ip = '192.168.0.11'
n_username   = 'cisco' #input('Username: ')
n_password = 'cisco' #input('Password: ')
command = 'show ip int brief' #input('Enter command: ')

#Open Connection to login
conn = paramiko.SSHClient()

#Add SSH host key automatically 
conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())

conn.connect(csr_ip, username=n_username, 
            password=n_password)

# run a command
mystdin, mystdout, mystderr = conn.exec_command(command)

#capture output stream
output = mystdout.readlines()

'''
#create a list to clean the output string
# method 1:
stdoutList = []
for line in output:
    stdoutList.append(line.strip())

for item in stdoutList:
    print(item)
'''
# method 2:
for line in output:
	print(line.strip())
	
# close the connection & clean up
conn.close()
del conn, mystdin, mystdout, mystderr
