from sorting.objectypes import ListObject
from sorting.utils import register_algorythm


@register_algorythm('bubble')
def bubble(app, ls, speed):
    delay = int(speed//3)
    n = len(ls)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):
            key = ls[j]
            key.color("green")
            app.after(delay)
            other = ls[j+1]
            other.color("red")
            app.after(delay)
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if key > other:
                ls[j], ls[j + 1] = other, key
            ls.refresh_indexes()
            ls.render_sorted()
            other.color("blue")
            app.after(delay)
            key.color("blue")


@register_algorythm('selection')
def selection(app, ls, speed):
    delay = int(speed//3)
    n = len(ls)
    for i in range(n):

        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, n):
            key = ls[j]
            key.color("red")
            app.after(delay)
            if ls[min_idx] > ls[j]:
                min_idx = j
            key.color("blue")

        # Swap the found minimum element with
        # the first element
        min = ls[min_idx]
        min.color("green")
        first = ls[i]
        first.color("red")
        ls[i], ls[min_idx] = min, first
        app.after(delay*2)
        ls.refresh_indexes()
        ls.render_sorted()
        app.after(delay*2)
        min.color("blue")
        first.color("blue")


@register_algorythm('insertion')
def insertion(app, ls, speed):
    delay = int(speed // 3)
    for i in range(1, len(ls)):
        key = ls[i]
        key.color("green")
        app.after(delay)
        j = i - 1
        while j>= 0 and key < ls[j]:
            ls[j].color("red")
            app.after(delay//2)
            ls[j].color("blue")
            ls[j + 1] = ls[j]
            j -= 1
        ls[j + 1] = key
        ls.refresh_indexes()
        ls.render_sorted()
        app.after(delay)
        key.color("blue")


@register_algorythm('merge')
def merge(app, ls, speed):
    delay = int(speed // 4)
    # Python program for implementation of MergeSort
    # ls.strict=False

    def merge_sort(arr):
        if len(arr) > 1:
            # arr.strict=False
            mid = len(arr) // 2  # Finding the mid of the array
            left_array = ListObject(arr[:mid], strict=False)  # Dividing the array elements
            right_array = ListObject(arr[mid:], strict=False)  # into 2
            arr[mid].color("orange")
            app.after(delay)
            arr[mid].color("blue")

            merge_sort(left_array)  # Sorting the first half
            merge_sort(right_array)  # Sorting the second half

            # arr.refresh_indexes()

            i = j = k = 0

            # Copy data to temp arrays L[] and R[]
            while i < len(left_array) and j < len(right_array):
                left = left_array[i]
                right = right_array[j]
                left.color("red")
                right.color("red")
                app.after(delay)
                if left_array[i] < right_array[j]:
                    # key = left_array[i]
                    # key.color("green")
                    # app.after(delay)
                    arr[k] = left_array[i]
                    i += 1
                    # arr.refresh_indexes()
                    # ls.render_sorted()
                else:
                    # key = right_array[j]
                    # key.color("green")
                    # app.after(delay)
                    arr[k] = right_array[j]
                    j += 1
                    # arr.refresh_indexes()
                    # ls.render_sorted()
                # arr.refresh_indexes()
                # ls.render_sorted()
                app.after(delay)
                left.color("blue")
                right.color("blue")
                k += 1
            # arr.refresh_indexes()
            # Checking if any element was left
            while i < len(left_array):
                key = left_array[i]
                key.color("green")
                arr[k] = left_array[i]
                i += 1
                k += 1
                app.after(delay)
                arr.refresh_indexes()
                # ls.render_sorted()
                app.after(delay)
                key.color("blue")

            while j < len(right_array):
                key = right_array[j]
                key.color("green")
                arr[k] = right_array[j]
                j += 1
                k += 1
                app.after(delay)
                arr.refresh_indexes()
                app.after(delay)
                key.color("blue")

            ls.render_sorted()

    merge_sort(ls)
