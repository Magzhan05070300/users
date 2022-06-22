import subprocess
cmd = 'python users.py'
p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
cmd2 = 'python admins.py'
p2 = subprocess.Popen(cmd2, stdout=subprocess.PIPE, shell=True)
