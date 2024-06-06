
#The scripts Task1A.py and Task1Aa.sh will be scheduled to run as cronjobs everday at 00:00 and 8:30 respectively
#This script uses ssh to remotely login into the pdu, then use SCP to copy the data.txt file to the local machine
#!/usr/bin/bash


sudo apt install sshpass -y
sudo apt install scp -y
sshpass -p password ssh apc@hostname/I.P address

scp apc@hostname/I.p address: data.txt 
exit