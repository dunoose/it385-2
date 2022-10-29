#!/usr/bin/env python3
import paramiko
import time
# getpass modeule hides password as you type in
from getpass import getpass

# Get Remote node's login info
n_username = 'justincase' #input('Username: ')
n_password = getpass("Enter Password: ")
web1_ip = '192.168.0.111'
db1_ip = '192.168.0.121'
# the command(s) to run on the remote host
command = 'hostname; ls -lrt'

#Open Connection to login
conn = paramiko.SSHClient()

#Add SSH host key automatically
# NOTE: has security implications
conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#Connect to web1:
conn.connect(web1_ip, username = n_username,
            password = n_password)

# run the command to get the hostname and dir of web1
# using the variable above
mystdin, mystdout, mystderr = conn.exec_command(command)

#capture output stream
output = mystdout.readlines()
for line in output:
    print(line.strip())

#capture any error messages
error = mystderr.read().decode().strip()
print(error)
'''
# Alternately, create a list to clean the output string
stdoutList = []
for line in output:
    stdoutList.append(line.strip())

for item in stdoutList:
    print(item)
'''
# close the connection & clean up
conn.close()
del conn, mystdin, mystdout, mystderr #, stdoutList
