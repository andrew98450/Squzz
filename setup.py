# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
import shutil
def main():
    print "[*] Start Squzz Operating environment Install...."
    print "[*] Downloading Backdoor-Factory....."
    print os.system("git clone https://github.com/secretsquirrel/the-backdoor-factory.git")
    print "[*] Download Done...." 
    print "[*] Downloading pyinstaller......"
    print os.system("pip install pyinstaller")
    print "[*] Download Done...." 
    print "[*] Changeme Dir...."
    os.chdir(os.getcwd()+"/"+"the-backdoor-factory")
    print "[*] Changeme Dir Done...."
    print "[*] conver to execute file....."
    print os.system("pyinstaller -F backdoor.py")
    print "[*] Conver Done....."
    os.chdir(os.getcwd()+"/"+"dist")
    print "[*] Move backdoor file to /usr/bin Dir"
    shutil.move("backdoor","/usr/bin/backdoor")
    print "[*] Done......"
main()