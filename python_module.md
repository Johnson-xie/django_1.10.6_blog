# python module  

## python bisect
```  
def binary_search_recursion(lst, value, low, high):
    if high < low:
        return None
    mid = int((low + high) / 2)
    if lst[mid] > value:
        return binary_search_recursion(lst, value, low, mid-1)
    elif lst[mid] < value:
        return binary_search_recursion(lst, value, mid+1, high)
    return mid

def binary_search_loop(lst, value):
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if lst[mid] < value:
            low = mid + 1
        elif lst[mid] > value:
            high = mid - 1
        else:
            return mid
    return None

if __name__ == "__main__":
    import random
    lst = [random.randint(0, 10000) for _ in range(100000)]
    lst.sort()

    def test_recursion():
        binary_search_recursion(lst, 999, 0, len(lst)-1)

    def test_loop():
        binary_search_loop(lst, 999)

    import timeit
    t1 = timeit.Timer("test_recursion()", setup="from __main__ import test_recursion")
    t2 = timeit.Timer("test_loop()", setup="from __main__ import test_loop")

    print("Recursion:", t1.timeit())
    print("Loop:", t2.timeit())

```
