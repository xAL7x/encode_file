from tqdm import *
import base64,pyfiglet,time,os
os.system("clear")
print("\033[0;31m")
pyfiglet.print_figlet("base64")
print("\033[0;37m")
print("#"*50)
print("")
file1=input("\033[0;31m[\033[0;34m~\033[0;31m]\033[0;36m File: ")
file=open(file1,"r")
a=file.read()
base=a.encode('utf-8')
time.sleep(0.5)
print("\033[0;37m \n")
print("#"*40)
print("\033[0;36m \n")
time.sleep(0.3)
print("encode [1] | decode [2] \n")
ask=input("options >> ")
print("\033[0;37m \n")
print("#"*50)
print("\033[0;31m")
if ask=="1":
	for i in tqdm(range(10),
		desc="encoding File: ",
		ascii=False):
		time.sleep(0.2)
	base64=base64.b64encode(base)
	file=open(file1,'w')
	file.write(base64.decode('utf-8'))
	file.close()
	print("\033[0;37m \n")
	print("#"*40)
	print("\033[0;34m \n")
	print(" >>>> Encoding is successfully <<<< \n")
elif ask=="2":
	for i in tqdm(range(10),
		desc="decode File: ",
		ascii=False):
		time.sleep(0.2)
	base64_decode=base64.decodebytes(base)
	file=open(file1,'w')
	file.write(base64_decode.decode('utf-8'))
	file.close()
	print("\033[0;37m \n")
	print("#"*40)
	print("\033[0;34m \n")
	print(" >>>> Decode is successfully <<<< \n")
