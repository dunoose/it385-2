#pip3 install paramiko
#
# THIS FILE SHOWS HOW TO USE PARAMIKO'S exec_command()
#  TO RUN COMMANDS ON REMOTE CISCO DEVICE, MODIFIED
#  TO RUN IN A LOOP TO RUN MULTIPLE COMMANDS
#
import paramiko

hostname = '192.68.0.11'
port = 22
user = 'cisco'
passwd = 'cisco'

try:
	client = paramiko.SSHClient()
	client.load_system_host_keys()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(hostname, port=port, username=user, password=passwd)

	#interactive shell
	while True:
		try:
			cmd = input("$> ")
			if cmd == "exit": break
			stdin, stdout, stderr = client.exec_command(cmd)
			print(stdout.read().decode())
		except KeyboardInterrupt:
			break

	client.close()
	
except Exception as err:
	print(str(err))