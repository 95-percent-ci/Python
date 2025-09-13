import concurrent.futures
import time


start = time.perf_counter()


def do_something(seconds):
    print(f"Sleeping {seconds} seconds..")
    time.sleep(seconds)
    return f"Done sleeping for {seconds}"


if __name__ == "__main__":
    start = time.perf_counter()

    with concurrent.futures.ThreadPoolExecutor() as executor: # context manager

        ## ex-1
        # f1 = executor.submit(do_something, 1)
        # f2 = executor.submit(do_something, 1)
        # print(f1.result()) # this waits around function is completes
        # print(f2.result())

        seconds = [5, 4, 3, 2, 1]

        ## ex-2

        # results = [executor.submit(do_something, sec) for sec in seconds]

        # for f in concurrent.futures.as_completed(results):
        #     print(f.result()) # get result for thread as they completed

        ## ex-3
        results = executor.map(do_something, seconds) # order is preserved

        for result in results:
            print(result)



    finish = time.perf_counter()

    print(f"Finished Processing in {finish - start}")