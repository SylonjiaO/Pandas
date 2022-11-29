#IP Addresses Arithmetic

import ipaddress
try:
   
  pp=ipaddress.ip_address(input("Enter Valid IP Address : "))
  
  print("IP Address Obtained : " + str(pp))
  col=str(pp).split(".")
  print("List of Octats Are")
  for x in col:
    print(x)
except ValueError:
  print("Invalid IP Address")
