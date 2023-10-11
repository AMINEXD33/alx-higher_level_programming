#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dict_ = {}
    list_ = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    list_2 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    char_ = ''
    for x in list_:
        dict_[x] = []
    for x in a_dictionary:#O(n)
        for y in range(len(list_)):#O(26)
            if (x[0] == list_[y]):
                char_ = list_[y]
            elif (x[0] == list_2[y]):
                char_ = list_[y]
        dict_[char_].append([x,a_dictionary[x]])
    
    for x in dict_:#O(26)
        for y in dict_[x]:#O(l) where l is the lenght of the list inside dict_[x]
            print("{}: {}".format(y[0],y[1]))