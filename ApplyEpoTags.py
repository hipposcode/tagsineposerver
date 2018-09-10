import requests

hosts=open("hosts.txt", "r")
for line in hosts:
	eposerver=requests.get("https://<SERVER>:<PORT>/remote/system.applyTag?names=" + line.strip() + "&tagName=<TAGTOAPPLY>", auth=("<USERNAME>", "<PASSWORD>"), verify=False)
	print(eposerver.text)
