# 
#         builder.py
# Copyright (c) 2022 Hawk2811
#
#

#importing libraries
import os
import sys
import time



#usage message
def usage():
    print("usage: python builder.py new proj_name")

def main(): #Main of Program
    if len(sys.argv) < 2: #check argv
        usage() ##print usage
        sys.exit()
    elif sys.argv[1] == "new": #else check the argv 1
        if sys.argv[2] == "":
            usage()
            sys.exit()
        else:#If true create a new project
            if os.name == "nt": # If Program running on Windows Platforms
                os.mkdir(sys.argv[2]) 
                os.mkdir(sys.argv[2] + "/src")
                os.system("python -m venv " + sys.argv[2] + "/env")
                os.system("echo. >" + sys.argv[2] + "/src/main.py")               
            else: # on UNIX-Based Platforms(macOS, linux, BSDs, etc)
                os.mkdir(sys.argv[2])
                os.mkdir(sys.argv[2] + "/src")
                os.system("python3 -m venv " + sys.argv[2] + "/env")
                os.system("touch " + sys.argv[2] + "/src/main.py")

main()
            
