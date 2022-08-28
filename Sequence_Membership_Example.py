#!/usr/bin/env python3
#Check a user name and PIN code

database=[['amber','1991'],['joanna','19911'],['kayla','199112'],['cici','1989']]

username=input('User name:')
pin=input('Pin code:')

if [username,pin] in database:print('Access granted')
