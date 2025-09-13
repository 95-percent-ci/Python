import time
import multiprocessing
import concurrent.futures

start = time.perf_counter()


def do_something(seconds):
    print(f"Sleeping {seconds} seconds..")
    time.sleep(seconds)
    return f"Done sleeping for {seconds}"


if __name__ == "__main__":

    # do_something()  # Sequential processing
    # do_something()

    with concurrent.futures.ProcessPoolExecutor() as executor: # context manager automatically makes sure this code block finishes first
        secs = [5,4,3,2,1]
        # results = [executor.submit(do_something, sec) for sec in secs]

        # for f in concurrent.futures.as_completed(results): # as completed gives a iterator that we can yield over
        #     print(f.result())
        results = executor.map(do_something, secs) # map respects order of input payloads to function, even it a process completes before.

        for result in results:
            print(result)

    finish = time.perf_counter()

    print(f"Finished in {round(finish - start,2)} seconds")
