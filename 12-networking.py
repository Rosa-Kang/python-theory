from multiprocessing import log_to_stderr
import numbers
from syslog import LOG_INFO
from xmlrpc.client import Server


# Transport Control Protocol(TCP)
# . Built on top of IP(Internet Protocol)
# . Assume IP might lose some data ; stores and retransmits data if it seems to be lost
# . Handles "flow control" using a transmit window
# . Provides a nice reliable pipe

# TCP Connections / Sockets
# "In computer networking, an internet socket or network socket is an endpoint of a bidirectional inter-process communication flow across an Internet Protocol-based computer network, such as the Internet"

# TCP Port numbers
# .A port is an application-specific or process-specific software communications endpoint.
# .It allows multiple networkded applications to coexist on the same server
# .There is a list of well-known TCP port numbers (like; extensions on the phone)

# Common TCP Ports
# .Telnet(23) - login
# .SSH(22) - Secure Login
# .HTTP(80) - Web Server
# .HTTPS(443) Secure
# .SMTP(25) - Mail
# .IMAP(143/220/993) - Mail Retrieval
# .POP(109/110) -Mail Retrieval
# .DNS(53) - DOmain Name
# .FTP(21) - File Transfer

# Let's Write a Web Browser !
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')
mysock.close()