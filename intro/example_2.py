import os
import threading



def hello() -> None:
    # sleep(3)
    print(f'Hello from {threading.current_thread()}')

t1 = threading.Thread(target=hello)
t1.start()


print(f'Python process running with id: {os.getpid()}')



total_threads = threading.active_count()
thread_name = threading.current_thread().name

print(f'Total threads : {total_threads}')
print(f'Current thread name: {thread_name}')

t1.join()