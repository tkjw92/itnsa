from err import err_msg
import os
import netifaces
import requests as req
import json
import sys

status = ""

print("\n[$] Checking ALL Tasks...", end="\n\n")


int1 = os.popen("ip link show | grep enp0s3").read()
int2 = os.popen("ip link show | grep enp0s8").read()
print("[ case 1 ] -> ", end="")
if int1 != "" and int2 != "":
	print("berhasil")
else:
	err_msg("Nama pada interface tidak sesuai dengan ketentuan", "case 1", "lab-01")



dhcp = os.popen("cat /etc/network/interfaces | grep dhcp").read()
ip_dhcp = os.popen("ip a | grep enp0s3 | grep inet").read()
print("[ case 2 ] -> ", end="")
if dhcp != "" and ip_dhcp != "":
	print("berhasil")
else:
	err_msg("Konfigurasi pada enp0s3 salah", "case 2", "lab-01")


try:
	print("[ case 3 ] -> ", end="")
	static = os.popen("cat /etc/network/interfaces | grep static").read()
	ip_static = os.popen("ip a | grep enp0s8 | grep inet").read()
	ip = netifaces.ifaddresses('enp0s8')[netifaces.AF_INET][0]['addr']
	ping = False
	if os.system("ping -c 1 10.10.10.1 > /dev/null") == 0:
		ping = True
	if static != "" and ip_static != "" and ip == "10.10.10.2" and ping:
		print("berhasil")
		status = "lolos"
	else:
		err_msg("Konfigurasi pada enp0s8 salah", "case 3", "lab-01")
except:
		err_msg("Konfigurasi pada enp0s8 salah", "case 3", "lab-01")


if status == "lolos":
	try:
		url = "http://10.10.10.1/auth.php"
		file = open("/home/siswa/.smkw92/.user")
		file = file.readlines()[0].split("|")
	except:
		print("Silahkan Login Terlebih dahulu... {smkw92 login}\nAtau cek koneksi internet")
		sys.exit()
	payload = {
		"method" : "grade",
		"username" : file[0].replace(" ", ""),
		"password" : file[1].replace(" ", ""),
		"id" : "lab-01"
	}
	res = req.post(url, data=payload).text

	res = json.loads(res)

	if res["status"] == "success":
		print("\nBerhasil, menyelesaikan {}".format(payload['id']))
	else:
		print("\nGagal, {}".format(res["msg"]))


print("\n")
