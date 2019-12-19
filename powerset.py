def printPowerSet(set, set_size):

    # set_size of power set of a set
    # with set_size n is (2**n -1)
    pow_set_size = (int)(pow(2, set_size))
    counter = 0
    j = 0
    l = list()
    # Run from counter 000..0 to 111..1
    for counter in range(0, pow_set_size):
        m = list()
        for j in range(0, set_size):
            # Check if jth bit in the
            # counter is set If set then
            # print jth element from set
            if((counter & (1 << j)) > 0):
                m.append(set[j])
                #print(set[j], end="")
        # print("")
        l.append(m)
    return l
    # print(l)


# Driver program to test printPowerSet
set = list(range(1, 3))
printPowerSet(set, 2)
