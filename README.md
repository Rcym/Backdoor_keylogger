# Backdoor_keylogger
 
The project is backdoor that lets the attacker execute commands on the victim's computer when it is active,
the main files to look at are:
- **not_a_backdoor.py** : that should run on the victims pc (should change the destination ip address to the attacker's)
- **hkrServ.py** : which is the script that allows the attacker to get the victim's data

## The backdoor part
it starts by trying to connect to the attacker's server, if the server is not up it will make another atempt every 5s untils it connects, once it successfully connect to the server, it will wait for its command and send the apropriate response.
while this is running the keylogger would have already started to record what the victim is typing and writing it in **recorded.txt**.

## The attacker's part
the attacker script starts by oppening a port and listening for the backdoor connection,
once it connects, it will prompt the attacker to enter one of its command

- **get-commands** : returns all the possible commands
- **get-file** : returns the location of the backdoor script in the victim's machine
- **get-info** : returns the os name, username, hostname, local ip and public ip of the victim
- **get-keylog** : returns what is recorded in the recorded.txt file
- **send-command** : opens a promt to enter the command that will be executed on the victim's machine (exe: dir)
- **deconnecter** : disconnects the attacker and the victims and stop the backdoor script