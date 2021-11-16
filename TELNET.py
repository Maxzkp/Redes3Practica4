from telnetlib import Telnet

class Client:
	def __init__(self, ip, usr = 'rcp', psw = 'rcp'):
		self.ip = ip
		self.usr = usr
		self.psw = psw

	def updateconffile(self):
		tn = Telnet(f'{self.ip}')
		tn.read_until(b'User: ')
		tn.write(self.usr.encode('ascii') + b'\n')
		tn.read_until(b'Password: ')
		tn.write(self.psw.encode('ascii') + b'\n')
		tn.write(b'enable\n')
		tn.write(b'conf\n')
		tn.write(b'copy run start\n')
		tn.write(b'exit\n')
		tn.write(b'exit\n')
		tn.read_all()
		tn.close()