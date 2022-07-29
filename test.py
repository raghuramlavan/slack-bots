import subprocess

#subprocess.Popen("ssh {user}@{host} {cmd}".format(user="root", host="54.91.8.133", cmd='ls -l'), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
x=subprocess.Popen("ping -c 4 google.com", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
print(x)