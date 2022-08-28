#!/usr/bin/env python3
#Try the first run of nesting blocks

name=input('what is your name?')
if name.endswith('Tan'):
    if name.startswith('Mrs.'):
        print('Hello, Mrs. Tan')
    elif name.startswith('Miss.'):
        print('Hello, Miss. Tan')
    else:
        print('Hello, Tan')
else:
    print('Hello, stranger')
    
