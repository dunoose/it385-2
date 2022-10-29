#!/usr/bin/env python3
#
# THIS FILE SHOWS HOW TO USE PARAMIKO'S invoke_shell()
#  TO RUN COMMANDS ON REMOTE CISCO DEVICE. THIS COMMAND
#  PERSISTS THE CONNECTION TO RUN AS THOUGH YOU ARE 
#  REMOTED IN TO THE DEVICE
#
import paramiko
# getpass modeule hides password as you type in
from getpass import getpass
import time

# Get Remote node's login info
csr_ip = '192.168.0.11'
user   = 'cisco' #input('Username: ')
passwd = 'cisco' #input('Password: ') or = getpass()

#Open Connection to login
conn = paramiko.SSHClient()

#Add SSH host key automatically 
conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())

conn.connect(csr_ip, username=user, 
            password=passwd)

# run a command using invoke_shell
# persist the connection
session = conn.invoke_shell()
session.send('terminal length 0\n')

# run another command
session.send('sho ip int brief\n')
# Notice the '\n' to indicate pressing <enter>

# wait for cisco to run and return output to Ansible vm
time.sleep(3)

#capture output stream, decode for clarity
output = session.recv(10000).decode()
time.sleep(1)

# print blank lines
print("\n\n")

# send another command to run 
session.send('conf t\n')

#wait for device to run cmd and respond
time.sleep(0.5)
output = session.recv(5000).decode()
print(output)

print(str(output) + '\n')
time.sleep(0.5)
session.send('end\n')
'''
#create a list to clean the output string
stdoutList = []
for line in output:
    stdoutList.append(line.strip())

for item in stdoutList:
    print(item)
'''
# close the connection & clean up
conn.close()
