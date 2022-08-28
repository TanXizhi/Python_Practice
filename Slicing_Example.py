#!/usr/bin/env python3
#split up a URL of the form http://www.something.com

url=input('please enter the URL:')
domain=url[11:-4]

print('Domain name:' +domain)

