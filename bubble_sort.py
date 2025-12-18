def bubble_sort(arr):
    """Повертає новий відсортований список (bubble sort)."""
    a = list(arr)
    n = len(a)

    for i in range(n):
        swapped = False
        for j in range(0, n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break

    return a


if __name__ == "__main__":
    data = [5, 2, 9, 1, 5, 6]
    print("Before:", data)
    print("After: ", bubble_sort(data))
