import subprocess
import os
import getpass

def hadoop():
	print("\t\t 1)to setup namenode \n\t\t 2) to setup datanode \n\t\t3) to setup client")
	choice=int(input("Enter ur choice: "))
	if choice==1:
		print("\t\t 1) remote  \n\t\t 2) local")
		choice1=int(input("Enter ur choice: "))
		subprocess.getoutput("mkdir /temp")
		os.system("cp /root/core-site.xml /root/temp/core-site.xml")
		os.system("cp /root/hdfs-site.xml /root/temp/hdfs-site.xml")
		with open("/root/temp/hdfs-site.xml","a") as f:
			f.write(f"<configuration> \n<property> \n<name>dfs.name.dir</name> \n<value>/NN</value> \n</property> \n</configuration>")
			f.close()
		with open("/root/temp/core-site.xml","a") as f:
			f.write(f"<configuration> \n<property> \n<name>fs.default.name</name> \n<value>hdfs://0.0.0.0:9001</value> \n</property> \n</configuration>")
			f.close()
		if choice1==1:
			nameIP=input("Enter the IP: ")
			pss=getpass.getpass(f"Enter {nameIP}'s password: ")
			os.system(f"sshpass -p {pss} ssh {nameIP} systemctl stop firewalld")
			subprocess.getoutput(f"sshpass -p {pss} scp /root/hadoop-1.2.1-1.x86_64.rpm /root/jdk-8u171-linux-x64.rpm  {nameIP}:/root") 
			subprocess.getoutput(f'sshpass -p {pss} ssh {nameIP} "rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force; rpm -ivh jdk-8u171-linux-x64.rpm"')
			os.system(f"sshpass -p {pss} scp /root/temp/hdfs-site.xml {nameIP}:/etc/hadoop/hdfs-site.xml ; scp /temp/core-site.xml {nameIP}:/etc/hadoop/core-site.xml ")
			subprocess.getoutput(f"sshpass -p {pss} ssh {nameIP} mkdir /NN")
			os.system(f"sshpass -p {pss} ssh {nameIP} hadoop namenode -format")
			os.system(f"sshpass -p {pss} ssh {nameIP} hadoop-daemon.sh start namenode ")
		elif choice1==2:
			subprocess.getoutput("rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force; rpm -ivh jdk-8u171-linux-x64.rpm")
			subprocess.getoutput("mkdir /NN")
			os.system("systemctl stop firewalld")
			os.system("cp /root/hdfs-site.xml /etc/hadoop/hdfs-site.xml ; cp /root/core-site.xml /etc/hadoop/core-site.xml ")
			os.system(" hadoop namenode -format")
			os.system("hadoop-daemon.sh start namenode ")
	elif choice==2:
		ipN=input("Enter the namenode IP: ")
		n=int(input("Enter the number of datanodes: "))
		dataIP=[]
		dataPass=[]
		for i in range(n):
			choice2=input("Enter the datanode IP:")
			pas=getpass.getpass(f"Enter {choice2}'s password: ")
			dataIP.append(choice2)
			dataPass.append(pas)
		
		os.system("cp /root/core-site.xml /root/temp/core-site.xml")
		os.system("cp /root/hdfs-site.xml /root/temp/hdfs-site.xml")
		with open("/root/temp/core-site.xml","a") as f:
			f.write(f"<configuration> \n<property> \n<name>fs.default.name</name> \n<value>hdfs://{ipN}:9001</value> \n</property> \n</configuration>")
			f.close()
		with open("/root/temp/hdfs-site.xml","a") as f:
			f.write(f"<configuration>\n<property>\n<name>dfs.data.dir</name>\n<value>/data</value>\n</property>\n</configuration>")
			f.close()
		for i in range(n):
			ip=dataIP[i]
			p=dataPass[i]
			os.system(f"sshpass -p {p} ssh {ip} systemctl stop firewalld")
			subprocess.getouput(f"sshpass -p {p} /root/hadoop-1.2.1-1.x86_64.rpm /root/jdk-8u171-linux-x64.rpm  {ip}:/root") 
			subprocess.getouput(f'sshpass -p {p} ssh {ip} "rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force; rpm -ivh jdk-8u171-linux-x64.rpm"')
			os.system(f"sshpass -p {p} scp /root/temp/core-site.xml  {ip}:/etc/hadoop/core-site.xml")
			os.system(f"sshpass -p {p} scp /root/temp/hdfs-site.xml  {ip}:/etc/hadoop/hdfs-site.xml")
			subprocess.getoutput(f"sshpass -p {p} ssh {ip} mkdir /data")
			os.system(f"sshpass -p {p} ssh {ip} hadoop-daemon.sh start datanode ")
			os.system(f"sshpass -p {p} ssh {ip} jps")
	elif choice==3:
		ipN=input("Enter the namenode IP: ")
		n=int(input("Enter the number of clients: "))
		clientIP=[]
		clientPass=[]
		for i in range(n):
			choice2=input("Enter the client IP:")
			pas=getpass.getpass(f"Enter {choice2}'s password: ")
			clientIP.append(choice2)
			clientPass.append(pas)
		
		os.system("cp /root/core-site.xml /root/temp/core-site.xml")
		os.system("cp /root/hdfs-site.xml /root/temp/hdfs-site.xml")
		with open("/root/temp/core-site.xml","a") as f:
			f.write(f" <configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{ipN}:9001</value>\n</property>\n</configuration>")
			f.close()
		with open("/root/temp/hdfs-site.xml","a") as f:
			f.write(f"<configuration>\n<property>\n<name>dfs.replication</name>\n<value>2</value>\n</property>\n<property>\n<name>dfs.block.size</name>\n<value>1024</value>\n</property>\n</configuration>")
			f.close()
		for i in range(n):
			ip=dataIP[i]
			p=dataPass[i]
			subprocess.getouput(f"sshpass -p {p} /root/hadoop-1.2.1-1.x86_64.rpm /root/jdk-8u171-linux-x64.rpm  {ip}:/root") 
			subprocess.getouput(f'sshpass -p {p} ssh {ip} "rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force; rpm -ivh jdk-8u171-linux-x64.rpm"')
			os.system(f"sshpass -p {p} scp /root/temp/core-site.xml  {ip}:/etc/hadoop/core-site.xml")
			os.system(f"sshpass -p {p} scp /root/temp/hdfs-site.xml  {ip}:/etc/hadoop/hdfs-site.xml")
			
