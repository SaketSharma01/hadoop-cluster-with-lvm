import os
import getpass
def lvmremote():
    ip=input("Enter the required ip address: ")
    ps=getpass.getpass(f"Enter {ip}'s password: ")
    while True:
	print(''' \tpress 1: to show hard disks
	press 2: to create physical volume
	press 3: to display physical volume
	press 4: to create volume group
	press 5: to display volume group
	press 6: to create logical volume
	press 7: to display logical volume
	press 8: format the partition
	press 9: mount the partion
	press 10: Extend the logical volume
	press 11: Extend the volume group
	press 12: Reduce the logical volume
	press 13: Show the logical volumes
	press 14: exit''')
	ch=int(input("Enter ur choice: "))
	if ch==1:
		os.system(f"sshpass -p {ps} ssh {ip} fdisk -l")
	elif ch==2:
		diskname=input("Enter the disk name: ")
		os.system(f"sshpass -p {ps} ssh {ip} pvcreate {diskname}")
	elif ch==3:
		diskname=input("Enter the disk name: ")
		os.system(f"sshpass -p {ps} ssh {ip} pvdisplay {diskname}")
	elif ch==4:
		vgname=input("Enter the volume group name: ")
		disknames=input("Enter the diskname separated by a space").split(' ')
		new=' '.join(str(x) for x in disknames)
		os.system(f"sshpass -p {ps} ssh {ip} vgcreate {vgname} {new}")
	elif ch==5:
		vgname=input("Enter the volume group name: ")
		os.system(f"sshpass -p {ps} ssh {ip} vgdisplay {vgname}")
	elif ch==6:
		lvname=input("Enter the logical volume name: ")
		vgname=input("Enter the volume group name: ")
		size=input("Enter the logical volume size: ")
		os.system(f"sshpass -p {ps} ssh {ip} lvcreate --size {size} --name {lvname}  {vgname}")
	elif ch==7:
		lvname=input("Enter the logical volume name: ")
		vgname=input("Enter the volume group name: ")
		os.system(f"sshpass -p {ps} ssh {ip} lvdisplay {vgname}/{lvname} ")
	elif ch==8:
		lvname=input("Enter the logical volume name: ")
		vgname=input("Enter the volume group name: ")
		os.system(f"sshpass -p {ps} ssh {ip} mkfs.ext4 /dev/{vgname}/{lvname} ")
	elif ch==9:
		folder=input("Enter the folder name: ")
		lvname=input("Enter the logical volume name: ")
		vgname=input("Enter the volume group name: ")
		os.system(f"sshpass -p {ps} ssh {ip} mkdir /{folder} ; mount /dev/{vgname}/{lvname} /{folder} ; df -hT")
	elif ch==10:
		lvname=input("Enter the logical volume name: ")
		vgname=input("Enter the volume group name: ")
		esize=input("Enter the extending size: ")
		os.system(f"sshpass -p {ps} ssh {ip} lvextend --size +{esize}  /dev/{vgname}/{lvname} ; resize2fs /dev/{vgname}/{lvname} ")
	elif ch==11:
		vgname=input("Enter the volume group name: ")
		pvname=input("Enter the new physical volume nme: ")
		os.system(f"sshpass -p {ps} ssh {ip} vgextend {vgname}  {pvname} ")
	elif ch==12:
		rsize=input("Enter the reduced size here: ")
		folder=input("Enter the folder name: ")
		lvname=input("Enter the logical volume name: ")
		vgname=input("Enter the volume group name: ")
		os.system(f"sshpass -p {ps} ssh {ip} umount /{folder} ; e2fsck -f /dev/{vgname}/{lvname} ; resize2fs /dev/{vgname}/{lvname} {rsize} ")
		os.system(f"sshpass -p {ps} ssh {ip} lvreduce --size {rsize} /dev/{vgname}/{lvname} ; mount /dev/{vgname}/{lvname}  /{folder} ")
	elif ch==13:
		os.system(f"sshpass -p {ps} ssh {ip} lvs")
	elif ch==14:
		break
  	else:
    		print('doesn't support")
def lvmlocal():
    while True:	    
   
	print(''' press 1: to show hard disks
	press 2: to create physical volume
	press 3: to display physical volume
	press 4: to create volume group
	press 5: to display volume group
	press 6: to create logical volume
	press 7: to display logical volume
	press 8: format the partition
	press 9: mount the partion
	press 10: Extend the logical volume
	press 11: Extend the volume group
	press 12: Reduce the logical volume
	press 13: Show the logical volumes
	press 14: exit''')
	ch=int(input("Enter ur choice: "))
	if ch==1:
		os.system("fdisk -l")
	elif ch==2:
		diskname=input("Enter the disk name: ")
		os.system(f"pvcreate {diskname}")
	elif ch==3:
		diskname=input("Enter the disk name: ")
		os.system(f"pvdisplay {diskname}")
	elif ch==4:
		vgname=input("Enter the volume group name: ")
		disknames=input("Enter the diskname separated by a space").split(' ')
		new=' '.join(str(x) for x in disknames)
		os.system(f"vgcreate {vgname} {new}")
	elif ch==5:
		vgname=input("Enter the volume group name: ")
		os.system(f"vgdisplay {vgname}")
	elif ch==6:
		lvname=input("Enter the logical volume name: ")
		vgname=input("Enter the volume group name: ")
		size=input("Enter the logical volume size: ")
		os.system(f"lvcreate --size {size} --name {lvname}  {vgname}")
	elif ch==7:
		lvname=input("Enter the logical volume name: ")
		vgname=input("Enter the volume group name: ")
		os.system(f"lvdisplay {vgname}/{lvname} ")
	elif ch==8:
		lvname=input("Enter the logical volume name: ")
		vgname=input("Enter the volume group name: ")
		os.system(f"mkfs.ext4 /dev/{vgname}/{lvname} ")
	elif ch==9:
		folder=input("Enter the folder name: ")
		lvname=input("Enter the logical volume name: ")
		vgname=input("Enter the volume group name: ")
		os.system(f"mkdir /{folder} ; mount /dev/{vgname}/{lvname} /{folder} ; df -hT")
	elif ch==10:
		lvname=input("Enter the logical volume name: ")
		vgname=input("Enter the volume group name: ")
		esize=input("Enter the extending size: ")
		os.system(f"lvextend --size +{esize}  /dev/{vgname}/{lvname} ; resize2fs /dev/{vgname}/{lvname} ")
	elif ch==11:
		vgname=input("Enter the volume group name: ")
		pvname=input("Enter the new physical volume nme: ")
		os.system(f"vgextend {vgname}  {pvname} ")
	elif ch==12:
		rsize=input("Enter the reduced size here: ")
		folder=input("Enter the folder name: ")
		lvname=input("Enter the logical volume name: ")
		vgname=input("Enter the volume group name: ")
		os.system(f"umount /{folder} ; e2fsck -f /dev/{vgname}/{lvname} ; resize2fs /dev/{vgname}/{lvname} {rsize} ")
		os.system(f"lvreduce --size {rsize} /dev/{vgname}/{lvname} ; mount /dev/{vgname}/{lvname}  /{folder} ")
	elif ch==13:
		os.system("lvs")
	elif ch==14:
		break
  	else:
    		print('doesn't support")
