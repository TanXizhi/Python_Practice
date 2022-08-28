#!/usr/bin/env python3
#A simple database

#A dictionary with person names as keys. Each person is represented as another
#dictionary with keys 'phone' and 'addr' referring to their phone number and
#address, respectively.

people={'Alice':{'phone':'3423',
                'addr':'Foo drive 23'},
        'Berh':{'phone':'9320',
                'addr':'Bar street 42'},
        'Xizhi':{'phone':'2308',
                'addr':'Heng Avenue 70'}}

#Descriptive labels for the phone number and address. These will be used
#when printing the output.

labels={'phone':'phone number','addr':'address'}

name=input('Name:')

#Are we looking for a phone number or an address?
request=input('Phone number (p) or address (a)?')

#Use the correct key:
if request=='p':key='phone'
if request=='a':key='addr'

#Only try to print information if the name is a valid key in our dictionary:
if name in people:print("{}'s {} is {}.".format(name,labels[key],people[name][key]))

                                                               
