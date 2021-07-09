def mergeSort(arr=[]):
    n = len(arr)
    if n > 1:
        mid = n//2
        L = arr[:mid]
        R = arr[mid:]

        # sorting the first half
        mergeSort(L)

        # sorting the second half
        mergeSort(R)

        #print(L, R)

        # Copy data to temp arrays L[] and R[]
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        # print(1, arr)
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        # print(2, arr)
        # Checking if any element was right
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

        # print(3, arr)


if __name__ == "__main__":
    my_array = [12, 11, 13, 5, 6, 7, 9, 14]
    mergeSort(my_array)
