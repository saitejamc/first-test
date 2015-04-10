import datetime

def gettime():
	curtime = datetime.datetime.now().strftime("%F %T")
	return curtime

def writetolog(towrite):
	f = open('/tmp/file.txt','a')
	f.write(towrite)
	f.close()

def logger():
	con = "[" + gettime() + "]" + " hello world \n"
	writetolog(con)
	

if __name__ == '__main__':
	logger()