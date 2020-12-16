
import sys
import socket

from nmap import PortScanner

MESSAGE_CHRISTMAS = b"""
\r
                              ..... ..\r
                          ..::XXX XXXXX:...\r
                        XXXXXXXXXXXXXXXXXXXXX::\r
                     XXXXX:XXXXXXX:XXXXXXX:XXXXX::\r
                    ..:IXX::XXXXXX:XXXX::.:':XXXX::\r
                  ..::::XX:XXXXXX:XXXX:'::':XXXXX::\r
                  ...:X'.'XXXXXXXXX.XXXXXXXXXXXX'XXX:\r
                 ....:X.:XXXXXXXXXXXXXXXXXXXXXX:'XXXX\r
                 ....'X.XXXXXXXXXXXXXXXXX''''' :XXXXXX\r
                 ...:::....'''''''''''''       :XXXXXXX\r
                 :..::.....                    :'XXXXX\r
                  .:::....                     .:XXXXX\r
                   ::''''                      .:XXXXX\r
                   .      ....,,      ......    :XXXXX\r
                    .::'   XXX   ::'   ''':  .XXXX:\r
                 :.:   :::'MM'''X    .:'MM '.    'X''.\r
                 ::'     I:..:.:X     .'''.'     .::'\r
                 ::XI          XI                :::\r
                  :XX         XI                .::''\r
                  :X' .:.     /X.              .:::\r
                  '''....    /XXX.:XX.         ...:\r
                   ':....    '::''            ...:\r
                    ':...                      ...\r
                     :....  :..:II:II:..:     ...\r
                     ':....  ::.              ..:::\r
                      ':...   '''''''         .::::\r
                       .:...               . ..::::\r
                   ....:::.:...         .:::::'.XXXX::::....\r
          .....:::XXXXXXXX::::::......:::::'   .XXXXXXXIMMM::\r
     .::XXXXXXXXXXXXXXXXXX:::::::::::::::'    .XXXXXXXXXMMMMMMM:\r
   .XXXXXXXXXXXXXXXXXXXXXX'::::::::::::'   .'.:XXXXXXXX:XXXXXXXXXX\r
  .XXXXXXXXXXXXXXXXXXXXXXX '::::::::::'  .' .XXXXXXXXXX:MMMMMMMMMMM\r
 .XXXXXXXXXXXXXXXXXXXXXXXX  ':::::::' .'   .XXXXXXXXXXX:MMMMMMMMMMM\r
.XXXXXXXXXXXXXXXXXXXXXXXXX   ':::::'.'    .XXXXXXXXXXXX:MMMMMMMMMMM\r
XXXXXXXXXXXXXXXXXXXXXXXXXX   .'WWWW.     .XXXXXXXXXXXXXX'MMMMMMMMMM\r
XXXXXXXXXXXXXXXXXXXXXXXXX.  .:WWWWWW    .XXXXXXXXXXXXXXX:MMMMMMMMMM\r
XXXXXXXXXXXXXXXXXXXXXXXXX.  .:WWWW' '   .XXXXXXXXXXXXXXX:MMMMMMMMMM\r
XXXXXXXXXXXXXXXXXXXXXXXXX  : 'WW'    '  XXXXXXXXXXXXXXXXX.MMMMMMMMM\r
XXXXXXXXXXXXXXXXXXXXXXXX' :.WWWW'     .XXXXXXXXXXXXXXXXX'MMMMMMMMMM\r
XXXXXXXXXXXXXXXXXXXXXXXX...WWWWWW....XXXXXXXXXXXXXXXXXXXXMMMMMMMMMM\r
\r
"""

                                                                                                                          
def sendData(printers=[], message=''):
	
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	for printer in printers:
		print(f'connecting to printer {printer}...')
		sock.connect((printer, 9100))
		print('done.')
		print('sending message...')
		sock.sendall(message)
		print('done.')
		print('closing connection...')
		sock.close()
		print('done.')

def findPrinters(IP='192.168.0.0', r='/24'):
	printers = []
	nmap = PortScanner()
	scan = nmap.scan(f'{IP}{r}', '9100')['scan']
	for ip in scan.values():

		if ip['tcp'][9100]['state'] == 'open':
			print(f'9100 OPEN AT {ip["addresses"]["ipv4"]}')
			printers.append(ip["addresses"]["ipv4"])
		else:
			print(f'9100 closed at {ip["addresses"]["ipv4"]}')

	return printers





sendData(['192.168.0.36'], MESSAGE_CHRISTMAS)
