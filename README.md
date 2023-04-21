# Linux_mac_changer
<h1>Description: </h1>
Uses linux commands to change the users mac address to a random one or a specified one. The mac address is generated in a clever way by taking advantage of hexidecimal to convert
random integers into an alphanumeric string. This script provides a quick and efficient solution for users who need to change their MAC address for privacy or security reasons.

<h1>Requirements: </h1>
This script requires Python 3.X.X to be installed in the system. It is worth noting that optparse module, which was used in previous versions of Python, has been replaced by argparse in Python3 and later versions.<br>
**Additionally, it is important to note that this script uses Linux commands and therefore cannot be run on a Windows machine.

<h1>Usage: </h1>
Usage:<br>
  python mac_changer.py [OPTIONS]

Options:<br>
  -r, --random         Generates a random MAC address to be used<br>
  -m, --mac            Gives the option for a user entered MAC  <br>
 -i, --interface      Used to enter the interface you want to change your mac on. 
