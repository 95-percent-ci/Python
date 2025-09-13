import time
import multiprocessing

start = time.perf_counter()


def do_something(seconds):
    print(f"Sleeping {seconds} seconds..")
    time.sleep(seconds)
    print("Done sleeping..")


if __name__ == "__main__":

    # do_something()  # Sequential processing
    # do_something()

    # p1 = multiprocessing.Process(target=do_something) # Processing Object 1
    # p2 = multiprocessing.Process(target=do_something) # Process Object 2

    # p1.start() # Starting P1
    # p2.start() # Starting P2

    # p1.join() # This ensures rest of script is executed after the process starts
    # p2.join()

    processes = []
    for _ in range(10):
        p = multiprocessing.Process(target=do_something, args=[1.5])
        p.start()
        processes.append(p)
        ## p.join should not be used, as it will start executing process, and it will same as sequential process
    
    for process in processes:
        process.join()  # join ensures waiting of script

    finish = time.perf_counter()

    print(f"Finished in {round(finish - start,2)} seconds")
