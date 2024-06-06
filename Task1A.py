#The scripts Task1A.py and Task1Aa.sh will be scheduled to run as cronjobs everday at 00:00 and 8:30 respectively
#This script makes use of the data.txt file that was copied to the local machine, converts it to a csv file, attach it to a e-mail and send

import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import schedule
import time

#This function converts a space delimited file to a csv file
def space_delimited_to_csv(input_file, output_file):
    with open(input_file, 'r') as file:
        # Read lines from the input file
        lines = file.readlines()

    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)

        # Write lines to the CSV file
        for line in lines:
            # Split each line by spaces and strip whitespace
            row = [item.strip() for item in line.split()]
            writer.writerow(row)

input_file = 'data.txt'
output_file = 'data.csv'
space_delimited_to_csv(input_file, output_file)

def send_email(sender_email, sender_password, recipient_email, subject, message):
    # Set up the SMTP server
    smtp_server = 'smtp.example.com'
    smtp_port = 587  # or 465 for SSL/TLS

    # Create a message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the message body
    msg.attach(MIMEText(message, 'plain'))

    # Start the SMTP session
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        # Start TLS for security
        server.starttls()

        # Login to the SMTP server
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, recipient_email, msg.as_string())

#This function sends the convertedd csv file as email at a specified time(08:30)
def send_email_at_specified_time():
    sender_email = 'XXXXXXXX@mail.com'
    sender_password = 'YYYYYYYYYY'
    recipient_email = 'ZZZZZZZZZ@mail.com'
    subject = 'PDUs Power Usage'
    message = 'Please find attached the power usgae of the PDUs.'

    send_email(sender_email, sender_password, recipient_email, subject, message)

# Schedule the email to be sent at a specified time
schedule.every().day.at("08:30").do(send_email_at_specified_time)

# Run the schedule continuously
while True:
    schedule.run_pending()
    time.sleep(1)
