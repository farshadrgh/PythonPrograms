import time

def SumOf_n_Numbers(n):
    start_time = time.time()
    s = 0
    for i in range(1, n+1):
        s = s + i
    end_time = time.time()
    return s, end_time-start_time

n = int(input("What is yout number? "))
print("\nTime to sum of 1 to ", n ," and required time to calculate is :", SumOf_n_Numbers(n))
