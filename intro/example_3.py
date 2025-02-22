import multiprocessing
import os


def hello() -> None:
    print(f'Hello from {os.getpid()}')

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=hello)
    p1.start()
    print(f'Hello from {os.getpid()}')
    p1.join()




