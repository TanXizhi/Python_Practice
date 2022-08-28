#!/usr/bin/env python3
#finally clause used to do housekeeping after a possible exception

try:
    1/0
except NameError:
    print('Unknown variable')
else:
    print('That went well')
finally:
    print('Cleaning up')