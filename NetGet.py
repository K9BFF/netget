#   Copyright 2017 masoncodes
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
	os.system("title NetGet")

# get proxies
print("You are connected to the following proxies:", urllib.request.getproxies())

def getinfo():
    while 1 > 0:  # loop
        # url input
        print("Please input a URL. (ex. \"google.com.\" Please do not include \"http(s)://\" in the URL.)")
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
            print("Trying", url, "on port", purl.port, "using", purl.scheme+"...")
            global r1

        except urllib.error.HTTPError as e:  # http error exception (404, 500, etc)
            print("Error:", url+"'s error code was", e.code)
            errcode = str(e.code)
            print("If you would like to know what this code means, click here: https://httpstatuses.com/"+errcode)

        except urllib.error.URLError as e:  # dns/connection refused error
            print('Error: Connection refused. Make sure you didn\'t mistype the URL, and that you are not connecting to'
                  ' localhost.')

        else:  # connction successful
            print(url+"'s status code was", conn.getcode())
            good_code = str(conn.getcode())
            print("If you would like to know what this code means, click here: https://httpstatuses.com/"+good_code)
            print("Would you like to see the header from", a+"? (y/n)")
            getHeader = input(">> ").lower()
            if getHeader == 'y':
                print(conn.info())  # print header
            else:
                pass

getinfo()

print("Get info on another URL? (y/n)")  # continue or break loop
another = input(">> ")
if another == 'y':
    pass
else:
    exit()
