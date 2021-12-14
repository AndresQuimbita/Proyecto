def count_paths(A):
    n = len(A)
    dic = {}
    dic_prev = {}

    for ind, val in enumerate(A):
        for j in range(ind):
            prev_val = A[j]
            dif = val - prev_val
            cur = (ind,dif)
            prev = (j,dif)

            if cur not in dic:
                dic[cur] = 0

            if cur not in dic_prev:
                dic_prev[cur] = 1

            else:
                dic_prev[cur] +=1

            if prev in dic_prev:
                dic[cur] += dic[prev]
            if prev in dic:
                dic[cur] += dic_prev[prev]
    return sum(dic.values())


