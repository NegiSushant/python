import time
import threading

def square_numbers():
    for _ in range(5000):
        result = 0
        for i in range(100):
            result += i*i
# Example 1: Running threads concurrently without GIL consideration.
start_time = time.time()
t1 = threading.Thread(target=square_numbers)
t2 = threading.Thread(target=square_numbers)

t1.start()
t2.start()

t1.join()
t2.join()

end_time = time.time()
print(f"Example 1 Execution time without GIL: {end_time - start_time} seconds.")

# Example 2: Running threads with GIL consideration.
start_time = time.time()
t1 = threading.Thread(target=square_numbers)
t2 = threading.Thread(target=square_numbers)

t1.start()
t1.join() # waiting for the first thread to finish before starting the second one.

t2.start()
t2.join()

end_time = time.time()
print(f"Example 2 Execution time with GIL: {end_time - start_time} seconds.")