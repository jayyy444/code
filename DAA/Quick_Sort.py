import random
import time

def quick(arr):
    if len(arr) <= 1:
        return arr
    
    piv = arr[len(arr) // 2]
    left = [x for x in arr if x < piv]
    mid = [x for x in arr if x == piv]
    right = [x for x in arr if x > piv]

    return quick(left) + mid + quick(right)

def calc_time(n, arr):
    #Average Case Time
    start = time.time()
    quick(arr)
    avg_time = time.time() - start

    #Best Case Time
    start = time.time()
    quick(sorted(arr))
    best_time = time.time() - start

    #Worst Case time
    start = time.time()
    quick(sorted(arr, reverse=True))
    worst_time = time.time() - start

    return n, best_time, avg_time, worst_time  # Ensure return values

user_ip = [random.randint(1,10000) for _ in range (10)]
print("n\tbest_time\t avg_time\t worst_time")
for n in user_ip:
    arr = [random.randint(1,10000) for _ in range (n)]
    n, best_time, avg_time, worst_time = calc_time(n, arr)
    print(f"{n}\t{best_time:.8f}\t{avg_time:.8f}\t{worst_time:.8f}")
