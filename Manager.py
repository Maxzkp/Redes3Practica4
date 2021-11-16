import FTP
import TELNET

host = '30.30.30.1'

ftp = FTP.Client(host)
tel = TELNET.Client(host)

def getconffile(name):
	tel.updateconffile()
	ftp.getfile('startup-config', f'{name}')

def putconffile(name):
	ftp.putfile(f'{name}', 'startup-config')

if __name__ == '__main__':
	putconffile('R2-Conf')