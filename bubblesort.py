# Bubble sort com python

def bubblesort(arr_list):

    cont = True

    while cont:

        swapped = False

        for i in range(len(arr_list)-1):

            if arr_list[i] > arr_list[i+1]:
                swapped = True
                a_1 = arr_list[i]
                a_2 = arr_list[i+1]
                arr_list[i+1] = a_1
                arr_list[i] = a_2

        if swapped is False:
            cont = False

    return arr_list


if __name__ == '__main__':

    import unittest
    from test_bubblesort import TestBubblesort

    unittest.main()
