def kWeakestRows(mat, k: int):

    num_soldiers = []

    for i in range(len(mat)):
        num_soldiers.append(sum(mat[i]))

    weakest_rows = []

    for i in range(k):
        min_index = num_soldiers.index(min(num_soldiers))
        num_soldiers[min_index] = 10**9
        weakest_rows.append(min_index)

    return weakest_rows


kWeakestRows(mat = [[1,1,0,0,0],
                    [1,1,1,1,0],
                    [1,0,0,0,0],
                    [1,1,0,0,0],
                    [1,1,1,1,1]], k = 3)