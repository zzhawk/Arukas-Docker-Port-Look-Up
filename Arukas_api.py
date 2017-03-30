import requests
import json
import subprocess

###################################################################
# load_cmd = 1
user = '(your API keys "Token")'
passw = '(your API keys "Secret")'

contid = '(Container ID)'
port = '(SSR Port)'
ssr = 'ShadowsocksR-dotnet4.0.exe'
###################################################################


url = "https://app.arukas.io/api/containers/"
header = {'content-type': 'application/json'}

response = requests.get(url + contid, auth=(user, passw), headers = header)

json_data = json.loads(response.content)

sub_json_data = json_data["data"]["attributes"];
# print json.dumps(sub_json_data, indent=4, sort_keys=True)

cmd = sub_json_data['cmd']

for x in sub_json_data["port_mappings"][0]:
    if x['container_port'] == port:
        output_port = x['service_port']
        output_host = x['host']

print output_port

if output_host.startswith("seaof-"):
    output_host = output_host[6:]
output_host = output_host.split(".")[0]
output_host = output_host.replace("-",".")

print output_host
###################################################################

in_file = open('gui-config.json')
indata = in_file.read()
out_file = open('gui-config.json.temp', 'w')
out_file.write(indata)

json_data_local = json.loads(indata)
# json_data_local['configs']['server'] = output_host;
# json_data_local['configs']['server_port'] = output_port;

for x in json_data_local["configs"]:
        x['server_port'] = output_port
        x['server'] = output_host

with open('gui-config.json', 'w') as outfile:
    json.dump(json_data_local, outfile, indent=4, sort_keys=True)

###################################################################
subprocess.call([ssr])
print "Parameter loaded, hit close(x) to exit"
