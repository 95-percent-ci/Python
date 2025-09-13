import time
import threading


def do_something(second):
    print(f'Sleeping for {second} second')
    time.sleep(second)
    print(f"DONE Sleeping {second}")

if __name__ == "__main__":
    start = time.perf_counter()

    t1 = threading.Thread(target=do_something) # thread initialation
    t2 = threading.Thread(target=do_something)

    t1.start()
    t2.start()

    t1.join()
    t2.join() # blocks later script execution threads finishes

    threads = []

    sleeps = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    
    for idx in range(10):
        t = threading.Thread(target=do_something, args=[sleeps[idx]])
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

    # do_something() # sequential
    # do_something()

    finish = time.perf_counter()

    print(f"Finished Processing in {finish - start}")
