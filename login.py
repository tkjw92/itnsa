import requests
import json
import getpass
import os

os.system("mkdir -p /home/siswa/.smkw92 > /dev/null")

username = input("Username: ")
password = getpass.getpass(prompt="Password: ")

url = "http://10.10.10.1/auth.php"
payload = {
	"method" : "log",
	"username" : username,
	"password" : password
}

try:
	req = requests.post(url, data=payload)
	res = json.loads(req.text)

	if (res['status'] == 'success'):
		file = open("/home/siswa/.smkw92/.user", "w")
		file.write(username + "|" + password)
		print("Berhasil login...")
	else:
		print("Gagal login...")
except:
	print("Connection timed out...")
