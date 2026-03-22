from mergesort import mergesort
from heapsort import heap_sort
from quicksort import quick_sort
from countingsort import counting_sort
from bucketsort import bucket_sort
from radixsort import radix_sort_int, radix_sort_str, radix_sort_bit

from random import randint, uniform

def gen_str(l):
    res = ""
    for i in range(l):
        res += chr(randint(65, 122))
    return res

def gen_str_fixed_table(n):
    l = randint(1, 5)
    c = 65, 122
    return [gen_str(l) for _ in range(n)]


def main() -> None:

    arr = [randint(0, 20) for _ in range(100)]
    words = gen_str_fixed_table(10)
    arr01 = [uniform(0, 1) for _ in range(20)]

    print(f"Random array: {arr}")
    print(f"Random Words: {words}")
    print(f"Random (0,1): {arr01}")

    print("SORTOWANIA (<, logarytmiczne) ==================\n\n")

    print("Merge sort: -------------")
    print(mergesort(arr))
    print()
    print("Heap sort: --------------")
    print(heap_sort(arr))
    print()
    print("quick sort : --------------")
    print(quick_sort(arr))
    print("\n\nSORTOWANIA (liniowe) ==================\n\n")
    print("counting sort : --------------")
    m_max = max(arr) + 1
    print(counting_sort(arr, m_max))
    print()
    print("radix sort (int) : --------------")
    print(radix_sort_int(arr))
    print()
    print("radix sort (str) : --------------")
    print(radix_sort_str(words))
    print()
    print("radix sort (bit) : --------------")
    print(radix_sort_bit(arr))
    print()
    print("bucket sort : --------------")
    print(bucket_sort(arr01))



    return None

if __name__ == "__main__":
    main()