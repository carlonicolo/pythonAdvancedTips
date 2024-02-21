from time import time
from threading import Thread


def func1():
    # execute the statement
    data = [i*i for i in range(100000000)]
    #print(len(data))


def func2():
    # execute the statement
    data = [i*i for i in range(100000000)]
    #print(len(data))


if __name__ == '__main__':
    # record start time
    time_start = time()
    func1()
    func2()
    # record end time
    time_end = time()
    # calculate the duration
    time_duration = time_end - time_start
    # report the duration
    print(f'Simple func1 func2 execution Took {time_duration} seconds')

    # record start time
    time_start_threads = time()
    t1 = Thread(target=func1)
    t1.start()
    t2 = Thread(target=func2)
    t2.start()
    # record end time
    time_end_threads = time()
    # calculate the duration
    time_duration_threads = time_end_threads - time_start_threads
    # report the duration
    print(f'Thread func1 func2 execution Took {time_duration_threads} seconds')