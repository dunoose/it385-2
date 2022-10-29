#
# Script slightly modified to keep the commands in 
#  loop instead of logging in every time.
#  CANNOT RUN commands with sudo
#

import paramiko
import time

# Get Remote node's login info
n_username = 'justincase' #input('Username: ')
n_password = 'Password01' #input('Password: ')
hostnode = '192.168.0.111'

try:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostnode, 
        username = n_username,
        password=n_password)
    
    # pseudo interactive shell
	# NOTE: cannot run sudo commands
    while True:
        try:
            # provide a nice prompt to user for
            # getting commands to run
            command = input("$> ")
            
            # if user types 'exit', get out
            if command == "exit": break    

            # collect output from remote host
            mstdin, mstdout, mstderr = client.exec_command(command)            
            
            # print output
            print(mstdout.read().decode())
            
            # print errors if any
            print(mstderr.read().decode())
        except KeyboardInterrupt:
            # if user types Ctrl-C, exit as well
            break
   
except Exception as err:
    print(str(err))

finally:
    client.close()