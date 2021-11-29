import math


def path(A, order):
    '''
    From a python list create sublists to separate the level order of a Tree
    '''
    if len(A) == 0:
        return []
    paths = [[A[0]]]
    i = 1
    n = 1
    while i < len(A):
        a = A[i:i+2**n]
        i += 2**n
        n += 1
        paths.append(a)
    return vertical_order(paths, order)


def vertical_order(paths, order):
    '''
    Use Newton's binomial to traversed in a vertical order a Tree give it in the level order in a python list
    '''
    vertical = [[] for i in range((2*order)-1)]
    count = order-1
    for k in range(order):
        vertical[k].append(paths[count][0])
        count -= 1
    count = order-1
    for k in range(2*order-2, order-1, -1):
        vertical[k].append(paths[count][-1])
        count -= 1
    if order == 2:
        return remove_None(vertical)
    if order == 3:
        vertical[order-1].append(paths[-1][len(paths[-1])-3])
        vertical[order-1].append(paths[-1][len(paths[-1])-2])
        return remove_None(vertical)
    b = 2
    count_1 = len(vertical[0:-1])-2
    for i in range(order, 1, -1):
        j = len(paths[i-1])-1
        c = 1
        min_count = 1
        for k in range(b, count_1+1, 2):
            for h in range(c, c+math.comb(i-1, min_count)):
                vertical[k].append(paths[i-1][h])
            c += math.comb(i-1, min_count)
            min_count += 1
        b += 1
        count_1 -= 1
    return remove_None(vertical)


def remove_None(vertical):
    '''
    Remove the None elements from the python list of the vertical order of a Tree.
    '''
    vertical_1 = []
    aux = []
    aux_1 = []
    for i in vertical:
        for j in i:
            if j != None:
                aux.append(j)
        aux_1.append(aux)
        aux = []
    vertical_1 = [x for x in aux_1 if x != []]
    return vertical_1
