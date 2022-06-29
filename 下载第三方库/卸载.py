import os,sys
while True:
	search=input("卸载第三方库：")
	os.system("pip uninstall " + search)