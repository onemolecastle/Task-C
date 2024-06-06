#This script uses the request module to acces an api endpoint, stores the result as a json file and the parses the file to extract values which are used to print a table

import request
pip install prettytable
from prettytable import PrettyTable

#use request module to access an api endpoint and save it inti the Output variable
Output = request.get('https://access.redhat.com/hydra/rest/securitydata/cve').json()

#print(Output)
#

#open the Output variable and write its content inti anothe variable FullList
with open('Output.json' , 'r') as file:
   FullList = file.read('Output')

#use a for loop and an a conditional statement to iterate over the FullList variable and write the output to another variable MainList if the condition is met
MainList = []
for X in FullList:
    if (X['severity'])=='important':
        MainList.append('result')

#This captures the CVE ID by using a for loop to iterate over the MainList variable and write the output to another variable cveidist
cveidList= []
for X in MainList:
    cveidList.append(X['CVE'])
#This captures the CVE public date by using a for loop to iterate over the MainList variable and write the output to another variable cve_publicDate
cve_publicDate = []
for X in MainList:
    cve_publicDate.append(X['public_date'])

#This captures the RHSAa by using a for loop and a conditional statement to iterate over the MainList variable and write the output to another variable RHSAs if the condition is met
RHSAs = []
for X in MainList:
    if (X['advisories'])=='null':
        RHSAs.append('no associated RHSAs')
    else: RHSAs.append(X['advisories'])

#This uses the PrettTable module to print the result in a table format
Result_table = PrettyTable(['CVE ID', 'CVE Public Date' , 'RHSAs'])
Result_table.addrow(['cveidList', 'cve_publicDate' , 'RHSAs'])
print(Result_table)