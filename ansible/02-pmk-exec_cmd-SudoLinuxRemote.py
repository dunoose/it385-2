#!/usr/bin/env python3
#
# THIS FILE SHOWS HOW TO USE PARAMIKO'S exec_command()
#  TO RUN SUDO COMMANDS ON REMOTE LINUX HOSTS
#  SHOWS HOW TO SEND IN SUDO'S PASSWORD 
#
import paramiko
import time
# getpass modeule hides password as you type in
from getpass import getpass

# Get Remote node's login info
n_username = 'justincase' #input('Username: ')
n_password = 'Password01' # or use getpass()
web1_ip = '192.168.0.111'
db1_ip = '192.168.0.121'

# when using sudo commands, use sudo -S
# causes sudo to read the password from standard input 
# instead of the terminal device.

# EX-1: Create a user Krish and make him a wheel member (sudoers)
command = 'sudo -S useradd "stranger" -c "Stranger Danger" -G "root" -m -p "Password01"'

command = 'hostname; cat /etc/passwd | grep 'stranger''
# EX-2: Delete a user
#userToDelete = input('Enter login name of user to delete: ')
#command = 'sudo -S userdel -r userToDelete'

#Open Connection to login
conn = paramiko.SSHClient()

#Add SSH host key automatically 
conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())

conn.connect(web1_ip, username=n_username, 
            password=n_password)

# for sudo commands w/o -S, add the get_pty=True at the end or
#    use sudo -S and leave the get_pty option out
#mystdin, mystdout, mystderr = conn.exec_command(command, get_pty=True)

# sudo command with -S option, w/o get_pty option
mystdin, mystdout, mystderr = conn.exec_command(command)

# sending in sudo's password. Note the '\n' at the end
mystdin.write('Password01\n')
mystdin.flush()

#getting the output
output = mystdout.readlines()
for line in output:
    print(line.strip())

# error output if any
error = mystderr.read().decode().strip()
print(error)

# Cleanup
conn.close()

# Add this line below to handle the NoneType object is not callable error
del conn, mystdin, mystdout, mystderr, output, error
