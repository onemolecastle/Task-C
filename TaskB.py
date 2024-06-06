"""
Components:
    Trigger: Slurm job scheduler
    Data Transfer Script: Python script using paramiko library
    Source Data: Located on the cluster’s storage
    Destination: Sheffield storage (assuming accessible via SCP)

Steps:
    Job Submission: When a job is submitted to Slurm, it includes information about the required data files.
    Trigger Script Execution: Slurm can trigger a post-submission script (e.g., using sbatch flags) that initiates the data transfer process.
    Data Transfer Script:
    Parses the Slurm job submission data to identify required files.
    Establishes an SCP connection to the Sheffield storage using the paramiko library.
    Iterates through the required files:
    Uploads each file to the designated location on Sheffield storage using SCP commands.
    Closes the SCP connection.
Benefits:
    Secure transfer: SCP uses SSH for secure authentication and data encryption.
    Script-based automation: Integrates seamlessly with Slurm for automatic data transfer.
    Scalability: The script can handle transferring multiple files for each job submission

"""


#pip install paramiko
import paramiko

source_file = "/path/to/data/file.txt"
destination_path = "/sheffield/storage/data/file.txt"
hostname = "sheffield_storage.example.com"
username = "storage_user"
password = "storage_password"

def transfer_data(source_file, destination_path, hostname, username, password):
  
  # Create SSH transport
  transport = paramiko.Transport((hostname, 22)) 
  transport.connect(username=username, password=password)
  
  # Create SFTP client
  sftp = paramiko.SFTPClient.from_transport(transport)
  
  # Upload the file
  sftp.put(source_file, destination_path)
  
  # Close connections
  sftp.close()
  transport.close()

transfer_data



