import paramiko
import time

# Function to execute commands from a file and save the response
def execute_commands(ssh_client, commands_file, output_file):
    cli = ssh_client.invoke_shell()
    with open(commands_file, 'r') as file:
        commands = file.readlines()

    # Execute each command
    output = ''
    for command in commands:
        cli.send(command)
        time.sleep(5)  # Adjust this as needed for waiting output
        output += cli.recv(999999).decode()

    # Write the output to a file
    with open(output_file, 'w') as file:
        file.write(output)

# Initialize the SSH client
username = 'administrator'
password = 'Changeme_123'
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Read the IP addresses from the file
with open("iplist.txt", "r") as ipfile:
    ip_list = ipfile.readlines()

# Iterate through each IP address and connect
for ip in ip_list:
    ip = ip.strip()  # Remove any leading/trailing whitespace characters
    try:
        ssh_client.connect(hostname=ip, port=22, username=username, password=password)
        print(f"Successfully connected to {ip}")
        
        # Perform your tasks here
        # Execute commands and save the response
        output_filename = f"{ip}_output.txt" ## file_name of output
        execute_commands(ssh_client, "configfile.txt", output_filename)
        print(f"Output saved to {output_filename}")

        ssh_client.close()
        
    except Exception as e:
        print(f"Failed to connect to {ip}: {e}")

# Close the SSH client
ssh_client.close()

