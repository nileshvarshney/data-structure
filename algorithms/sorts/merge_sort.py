def mergeSort(arr=[]):
    n = len(arr)
    if n > 1:
        mid = n//2
        L = arr[:min]
        R = arr[mid:]

        # sorting the first half
        mergeSort(L)

        # sorting the second half
        mergeSort(R)

        print(len(L), len(R))


if __name__ == "__main__":
    my_array = [12, 11, 13, 5, 6, 7]
    mergeSort(my_array)
