import os
import lvm
import hadoop
os.system("tput setaf 3")
print(\t"************************************************")
print(" \t\tPress 1: To setup hadoop \n\t\t Press 2: To setup lvm")
try:
  ch=int(input("Enter ur choice :"))
  if ch==1:
    while True:
      hadoop.hadoop()
  elif ch==2:
     print("\t\tPress 1:For remotr setup \n\t\tPress 2: For local setup
     ch1=int(input("Enter ur choice :"))
     if ch1==1:
       lvm.lvmremote()
     elif ch1==2:
       lvm.lvmlocal()
     else:
       print("Doesn't support")
  else:
     print("Doesn't support")
except ValueError:
  print("Please enter correct input")
  os.system("tput setaf 7")
   
