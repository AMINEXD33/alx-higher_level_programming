#!/usr/bin/python3
"""find_peak
    @pram list_of_integers: a list of integers
"""


def find_peak(list_of_integers):
    """
        find all preaks in a list of integers
    """
    # to store the results
    result = []
    # ints to the right and left of an element
    left   = None
    right  = None
    # of the len of the list is smaller then 3
    # it doesn't qualify to have a peak
    if (len(list_of_integers) < 3): return (result)
    # the tracker
    element = 1
    # this variable allow to set the left and right element
    # the default way
    do_set  = True
    # while we're in the range of the list
    while element < len(list_of_integers)-1:
        if do_set:
            left  = element-1
            right = element+1
        # if the right is out of range , return
        if (right > len(list_of_integers)-1):
            return (result)

        # if element > right and element > left , then it's a peak
        if (list_of_integers[element] > list_of_integers[left]\
            and list_of_integers[element] > list_of_integers[right]):
            
            # append to the result list
            result.append(list_of_integers[element])
            # if the right doesn't have at least two right neighbors
            # then we're done , no peaks left
            if (right+1 > len(list_of_integers)-1\
                and right+2 > len(list_of_integers)-1):
                return (result)
            # set do_set to false in the next loop
            do_set  = False
            # right of the next element is the current_right + 2
            right   = right+2
            # left of the next element is the current_right
            left    = right
            # the next element is the current_right + 1
            element = right+1
        # of the element is not a peak
        else:
            do_set = True
            element += 1
    return(result)
