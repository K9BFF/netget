#   Copyright 2017-2023 masoncodes
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0


import urllib.request  # to get connection information
import urllib.error  # error exceptions
import os  # for renaming the command prompt in windows
from urllib.parse import urlparse  # parsing urls

if os.name == 'nt':
	os.system("title NetGet") # Renaming CMD window (windows only)

# get proxies
print("You are connected to the following proxies:", urllib.request.getproxies())

#asks user if they want to retry
def retry():
    print ("Get info on another URL? (Y/n)")
    another = input(">> ")
    if another == 'n':
        exit()

    if another == "":
        getinfo()

    if another == "y":
        getinfo()
    else:
            print("Huh?")

def getinfo(): #the actual meat of the program
    while 1 > 0:  # loop
        # url input
        print("Please input a URL. (ex. \"google.com.\" Do not include \"http(s)://\" in the URL.)")
        a = input(">> ")

        # http/https selection
        print("(HTTP) or (HTTPS)?")
        s = input(">> ").lower()
        if s == "http":
            url = ('http://' + a + ':80')  # where to connect (80, http/not secure)
            url = str(url)

        if s == "https":
            url = ('https://' + a + ':443')  # where to connect (443, https/secure)
            url = str(url)

        try:  # open connection
            conn = urllib.request.urlopen(url)
            purl = urlparse(url)
            print("Trying", a, "on port", purl.port, "using", purl.scheme+"...")
            global r1

        #catch http error
        except urllib.error.HTTPError as e:  # http error exception (404, 500, etc)
            print("Error:", url+"'s error code was", e.code)
            errcode = str(e.code)
            print("If you would like to know what this code means, click here: https://httpstatuses.com/"+errcode)
            break

        #connection refused
        except urllib.error.URLError as e:  # dns/connection refused error (FUCKED UP FUCKED UP FUCKED UP FUCKED UP YOU DONE FUCKED UP -XXXTentacion, Take a step back)
            print('Error: Connection refused. Make sure you didn\'t mistype the URL, and that you are not connecting to'
                  ' localhost.')
            break

        else:  # connction successful
            print(s+"://"+a+"'s status code was", conn.getcode())
            good_code = str(conn.getcode())
            print("If you would like to know what this code means, click here: https://httpstatuses.com/"+good_code)
            print("Would you like to see the header from", a+"? (y/N)")
            getHeader = input(">> ").lower()
            if getHeader == 'y':
                print(conn.info())  # print header
                retry()
            else:
                retry()

getinfo()
retry()
