from ftplib import FTP
class Client:
	def __init__(self, ip, usr = 'rcp', psw = 'rcp'):
		self.ip = ip
		self.usr = usr
		self.psw = psw

	def getfile(self, source, destination):
		with open(f'{destination}', 'wb') as f:
			ftp = FTP(f'{self.ip}', f'{self.usr}', f'{self.psw}')
			ftp.retrbinary(f'RETR {source}', f.write)
			ftp.quit()

	def putfile(self, source, destination):
		with open(f'{source}', 'rb') as f:
			ftp = FTP(f'{self.ip}', f'{self.usr}', f'{self.psw}')
			ftp.storbinary(f'STOR {destination}', f)
			ftp.quit()