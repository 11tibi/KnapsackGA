import numpy as np


def solve(d, r, SCj, Dk, Cjk):
    out = np.zeros((d, r), dtype=int)
    i, j = 0, 0
    while i < len(SCj) and j < len(Dk):
        if SCj[i] > Dk[j]:
            out[i][j] += Dk[j] * Cjk[i][j]
            SCj[i] -= Dk[j]
            Dk[j] = 0
            j += 1
        elif SCj[i] < Dk[j]:
            out[i][j] += SCj[i] * Cjk[i][j]
            Dk[j] -= SCj[i]
            SCj[i] = 0
            i += 1
        else:
            out[i][j] += SCj[i] * Cjk[i][j]
            SCj[i], Dk[j] = 0, 0
            i += 1
            j += 1
    print(out)
    print(out.sum())


if __name__ == '__main__':
    # d = 2
    # r = 3
    #
    # SCj = [89, 82]  # sup
    # Dk = [52, 28, 62]  # dest
    #
    # Cjk = [[68, 59, 55],
    #        [55, 34, 35]]
    d = 3
    r = 3

    SCj = [50, 40, 60]  # sup
    Dk = [20, 95, 35]  # dest

    Cjk = [[5, 8, 4],
           [6, 6, 3],
           [3, 9, 6]]
    solve(d, r, SCj, Dk, Cjk)
