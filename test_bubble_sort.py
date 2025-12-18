from bubble_sort import bubble_sort

def test_empty():
    assert bubble_sort([]) == []

def test_sorted():
    assert bubble_sort([1, 2, 3]) == [1, 2, 3]

def test_reverse():
    assert bubble_sort([3, 2, 1]) == [1, 2, 3]

def test_duplicates():
    assert bubble_sort([3, 1, 2, 1]) == [1, 1, 2, 3]

def test_negative_numbers():
    assert bubble_sort([0, -2, 5, -1]) == [-2, -1, 0, 5]
