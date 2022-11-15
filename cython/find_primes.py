import time
from main import find_primes_cythonically

def find_primes_pythonically(n: int) -> list[int]:
    primes = []
    found = 0
    number = 2
    while found < n:
        for x in primes:
            if number % x == 0:
                break
        else:
            primes.append(number)
            found += 1
        number += 1
    
    return primes

print("How many prime numbers do you want?")
n = int(input())
start_python = time.time()
find_primes_pythonically(n)
end_python = time.time()
python_time = end_python - start_python
print("python took %.10f seconds %d primes" % (python_time, n))

start_cython = time.time()
find_primes_cythonically(n)
end_cython = time.time()
cython_time = end_cython - start_cython
print("cython took:  %.10f seconds for %d primes" % (cython_time, n))
print("Cython is %2.10f times faster than python in that case" % (python_time / cython_time))