__all__ = ['selection', 'bubble', 'insertion']


def bubble(app, ls, speed):
    delay = int(speed/3)
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


def selection(app, ls, speed):
    delay = int(speed/3)
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
        first= ls[i]
        first.color("red")
        ls[i], ls[min_idx] = min, first
        app.after(delay*2)
        ls.refresh_indexes()
        ls.render_sorted()
        app.after(delay*2)
        min.color("blue")
        first.color("blue")


def insertion(app, ls, speed):
    delay = int(speed / 3)
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