import random


def resolver2D(array): 
    """
    """
    return_string = ""   
    for i in array:
        print("We are looking at {} which is type {}".format(i, type(i)))
    # print("printing return_string {}".format(return_string))
    for i in array:  
        # print("printing return_string {}".format(return_string))
        #print("loop looking at {}".format(i)) 
        if type(i) is list:
            #print("making a choice and adding {} to the return string.".format(i))
            # return_string += random.choice(i)
            #return(resolver2D(i))
            return_string = return_string + str(random.choice(i) )
        elif type(i) is str:  # type(i) is str:
            #print("adding {} to the return_string.".format(i))
            return_string += i 
            # pass
        
    return(return_string)


def resolverND():
    return_string = ""   
    for i in array:
        print("We are looking at {} which is type {}".format(i, type(i)))
    # print("printing return_string {}".format(return_string))
    for i in array:  
        # print("printing return_string {}".format(return_string))
        #print("loop looking at {}".format(i)) 
        if type(i) is list:
            #print("making a choice and adding {} to the return string.".format(i))
            # return_string += random.choice(i)
            #return(resolver2D(i))
            return_string = return_string + str(random.choice(i) )
        elif type(i) is str:  # type(i) is str:
            #print("adding {} to the return_string.".format(i))
            return_string += i 
            # pass
        
    return(return_string)


def bootstrap():
    choices = [
        'import os\n',
        [
            'import math\n',
            'import staticmethod\n',
            'import random\n'
        ]
    ]
    return(resolver2D(choices))


def payload():
    choices = [
        'print(os.system("cat /etc/shadow"))\n',
        [
            "c1\n",
            "c2\n",
            "cFuckyou\n",
            [
                "d1\n",
                "d2\n"
            ]
        ],
        'print("Doing the bad thing!!")\n',
        'print("installing the rootkit!!")\n'
    ]
    return(resolver2D(choices))


def compiled_code():
    return("{}{}".format(bootstrap(), payload()) )


if __name__ == "__main__":
    """Writing test code here 
    """
    print("############################################################")
    print("### Running tests                                        ###")
    print("############################################################")
    x = compiled_code()
    array = [111, 222, 333, 444, 555, 666, 777]
    
    # n_dimensional array test 
    n_dimensional = [
        "a",
        "b",
        [   
            "c1",
            "c2",
            [
                "c3_inner_1",
                "c3_inner_2"
            ],
            [
                "c4_inner_1"
                "c4_inner_2"
                "c4_inner_3"
            ]
        ],
        "d",
        [
            "e1"
        ],
        "f"
    ]

    # print(resolver(n_dimensional))
    for i in n_dimensional:
        #print(i)
        print(random.choice(i))
    print("############################################################")
    print("### actual output program                                ###")
    print("############################################################")
    print(x)
    print("############################################################")
    print("### end string                                           ###")
    print("############################################################")