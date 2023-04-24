import sys
from os import system as st

try:
	if sys.argv[1] == "start":
		if sys.argv[2] == "lab-01":
			st("sudo python3 /smkw92/lab-01/start.py")
		else:
			print("Sepertinya lab yang anda masukkan tidak tersedia...")

	elif sys.argv[1] == "grade":
		st("python3 /smkw92/{}/grade.py".format(sys.argv[2]))

	elif sys.argv[1] == "finish":
		pass

	elif sys.argv[1] == "login":
		st("python3 /smkw92/login.py")

	else:
		print("Invalid syntax...")
		print("Example: smkw92 {start, grade, finish} [name-of-labs]")
except:
		print("Invalid syntax...")
		print("Example: smkw92 {start, grade, finish} [name-of-labs]")


