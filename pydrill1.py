from time import sleep
import sys
if __name__=="__main__":
	num=int(sys.argv[1])
	for i in range(num):
		print(i, i**3)
		sleep(1)
