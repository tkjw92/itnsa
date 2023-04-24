def err_msg(pesan, case, lab):
	print("gagal")
	print("\tketerangan lebih lanjut dapat dilihat di /var/log/smkw92/{}.log".format(lab))
	file = open("/var/log/smkw92/{}.log".format(lab), "a")
	file.write("[ {} ] -> Gagal:\n".format(case))
	file.write("\t{}\n".format(pesan))
	file.close()
