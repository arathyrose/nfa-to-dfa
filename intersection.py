def final_set_generator(set1, set2):
    # find all those elements in set1 which conrtains all elements in set2
    finale = list()
    for i in set1:
        if([value for value in i if value in set2] == set2):
            finale.append(i)
    print(finale)
    return finale


final_set_generator([[1, 2], [2, 3], [3, 1]], [2, 3])
