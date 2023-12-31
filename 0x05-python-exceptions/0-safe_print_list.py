#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printed = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            printed += 1
    # handling trying to access an index beyond the list len
    except IndexError:
        pass
    finally:
        print()
    return (printed)
