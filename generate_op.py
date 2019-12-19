def op_for(a, total, input):
    # finds the union of the outputs of each element in a
    ans = list()
    for i in total:
        print(i)
        if(i[1] == input):
            if(i[0] in a):
                ans = list(set(ans) | set(i[2]))
    return ans


a = [1]
total = [0, "a", [0, 1]], [0, "b", [1]], [1, "b", [0, 1]]
print(op_for(a, total, "b"))
