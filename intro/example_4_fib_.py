import threading
import time

def print_fib(number: int) -> None:
    def fib(n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)

    print(f'fib({number}) = {fib(number)}')

def fibs_no_threading() -> None:
    print_fib(40)
    print_fib(41)

def fibs_with_threading() -> None:
    t1 = threading.Thread(target=print_fib, args=(40,))
    t2 = threading.Thread(target=print_fib, args=(41,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


start = time.time()
fibs_with_threading()
# fibs_no_threading()
end = time.time()

print(f'Completed in {end - start} seconds')