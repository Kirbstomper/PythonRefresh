from random import randint
"""Project # 1, The name generator
 This project fist anc foremost is meant to generate a random name each time it is run
 The bonus for this is not only generating a name, but also random credentials such as a...
 Phone number, email, birth date, and address.
 Shouldn't be too hard
   -Christopher Smith, 12/24/2015
"""

# So to generate all this stuff I am going to use a txt file full of first names, and randomly select from it
# Its gonna be the same for last. Cause who wants to actually type a ton of names?

#some code created by Stackoverflow user SilentGhost, I figure, why reinvent the wheel?
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
# Code use ends

def random_name(list):
    nameList = open(list,'r' ).readlines()
    listlen = file_len(list)
    return nameList[randint(0,listlen)].split(' ', 1)[0]

def get_first():
    print random_name('first.txt')

def get_last():
    print random_name('last.txt')


print "First Name:",get_first()
print "Lasst Name:",get_last()