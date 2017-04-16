# Arukas-Docker-Port-Look-Up
This script will update IP address and port number for SSR Windows clinet, by one click
Problem solved: due to some unknown reason the Arukas restart itself in every couple days, each restart changes the IP address and port number. You have to reopen the seriver webpage and lookup and re-enter the parameters to the SSR clinet over and over again. That is a pain, especially if you are sharing the same seriver with several people. This script does everything for you.

## Get ready
Install Python 2.7 first. Make sure it works.

Run cmd

cd C:\Python27\Scripts(the place you installed Python)

pip install requests

## Before Starting
IMPORTANT: YOU NEED TO KNOW HOW TO OPERATE SSR MANUALLY.

The JSON file "gui-config.json" will be saved as "gui-config.json.temp". Orders of the keys will be re-sorted(not sure why, happens even when removed the "sort_keys").

Make sure the server is running, no checking/ debugging print avaliabled at this version

Make sure you know how to use the SSR Windows clinet, downloaded form here： https://github.com/shadowsocksr/shadowsocksr-csharp

Make sure all the parameters on SSR Windows clinet matches your setups in the seriver, this script only modify the SSR Windows clinet's IP address and port number at this version.

Make sure you modify this part in the script. If you don't know the parameters, ask your seriver "master"

user = '(your API keys "Token")'

passw = '(your API keys "Secret")'

contid = '(Container ID)'

port = '(SSR Port)'


## Enjoy
If all set up correctly, you will see "Parameter loaded, hit close(x) to exit" in the CMD window. Otherwise, go back and re-check all the steps above.

Manually open the SSR clinet(the JASON files seems like is blocked by the script... so any changes in SSR clinet will not actually changes...not sure whats going on, need time looking into it)

Feel free to trim the bottom part for "IP address and port number" lookup only.

First time writing python. If you find and bugs or have any suggestions, let me know. Thanks for reading!

