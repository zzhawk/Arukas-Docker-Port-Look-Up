# Arukas-Docker-Port-Look-Up
This script will update IP address and port number for SSR clinet

## Get ready
Install Python 2.7 first. Make sure it works.

Run cmd

cd C:\Python27\Scripts(the place you installed Python)

pip install requests

## Before Starting
The JSON file "gui-config.json" will be saved as "gui-config.json.temp". Orders of the keys will be re-sorted(not sure why, happens even when removed the "sort_keys").

Make sure the server is running, no checking/ debugging print avaliabled at this version

Make sure you know how to use the SSR windows clinet, downloaded form here： https://github.com/shadowsocksr/shadowsocksr-csharp

Make sure all the parameters matches, this script only modify the IP address and port number at this version

## Enjoy
If all set up correctly, you will see "Parameter loaded, hit close(x) to exit" in the CMD window. Otherwise, go back and re-check all the steps above.

Manually open the SSR clinet(the JASON files seems like is blocked by the script... so any changes in SSR clinet will not actually changes...not sure whats going on, need time looking into it)

Feel free to trim the bottom part for "IP address and port number" lookup only.

First time writing python. If you find and bugs or have any suggestions, let me know. Thanks for reading!

